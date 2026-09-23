---
name: query-cardano-api
description: Query Cardano on-chain data through the blockchain-applied MCP connector and BCA API. Use when a request asks to inspect Cardano addresses, transactions, blocks, epochs, staking, pools, native assets, scripts, datums, metadata, UTxOs, balances, or related on-chain activity.
---

# Query Cardano API

Use the `blockchain-applied` MCP connector as the only API access path. Never request, print, copy, infer, or expose connector credentials, tokens, cookies, signatures, headers, or environment values. Do not construct a direct HTTP request that bypasses the MCP connector.

## Workflow

1. **Parse the request.** Identify the Cardano entities, network assumptions, time range, pagination requirements, desired output, and whether the user wants raw JSON, a table, a chart, or an exploratory follow-up file.
2. **Choose the narrowest MCP tool set.** Consult [references/endpoints.md](references/endpoints.md). If an exact tool is unclear, inspect the connector tool schema with `tool.get` before calling it. Do not guess parameter names or formats.
3. **Check service health when useful.** For a new analysis or an error, call `ada_check_api_health` first. Treat Bitcoin tools as out of scope for this skill.
4. **Plan dependent queries.** Resolve identifiers in stages, for example pool identifier to pool hash, asset policy and name to fingerprint, or latest block to block details. Keep a short query plan in the response.
5. **Run independent calls in parallel.** The connector credentials permit up to 10 concurrent queries. Batch only independent calls, keep each batch at 10 or fewer, and avoid parallel calls when one result supplies a required parameter for another.
6. **Preserve raw results.** Create a temporary directory such as `/tmp/query-cardano-api/<UTC timestamp>/`. Save each MCP JSON result as a separate file named with the tool and a sequence number. Keep raw results unchanged so the user can inspect them or run follow-up queries. Do not store credentials with the results.
7. **Validate and interpret.** Check for connector errors, missing records, pagination metadata, default time windows, and units. Distinguish lovelace from ADA and state conversions explicitly. Do not present an absent record as proof that an entity never existed.
8. **Render the requested view.** Use a concise Markdown table for scalar or row-like results. Use a chart only when it answers a defined comparison or time-series question. Use `scripts/json_to_markdown.py` for a quick inspection of saved JSON, then use a suitable analysis tool for more involved transformations.
9. **Report reproducibly.** State the tools called, key parameters excluding secrets, time windows, pagination, the raw-result directory, and any interpretation or data-quality limitations. Offer concrete next queries when useful.

## Query rules

- Prefer explicit `after` and `before` timestamps for historical listings. Address, staking, and reward listings default to a recent window when `after` is omitted, so never imply full history without an explicit range.
- Use zero-indexed `page` and a `pagesize` no greater than 2000 for paginated endpoints. Fetch additional pages only when needed.
- Preserve hashes, addresses, policy IDs, fingerprints, asset names, and datum values exactly as returned.
- Treat timestamps and epoch or slot values as API data. Do not silently substitute local time or a different chain tip.
- For graphs, label axes, units, time range, source tool, and any aggregation. Prefer a chart over a graph visualization only when the data supports quantitative comparison; use Mermaid for relationship diagrams when appropriate.
- Never log raw connector request headers or authentication material. If an error message contains a secret, redact it before saving or displaying it.

## Endpoint reference

Read [references/endpoints.md](references/endpoints.md) for the connector's available tools and the corresponding BCA API concepts. Use the live MCP tool schema as authoritative if it differs from the reference.

## Common query patterns

- **Address activity:** `ada_get_address_summary`, then `ada_list_address_transactions` with explicit dates and pagination.
- **Transaction audit:** `ada_get_transaction_details`, followed by `ada_get_datum` or `ada_get_script_info` for referenced contract data.
- **Chain status:** `ada_check_api_health`, `ada_get_latest_block`, and `ada_get_current_epoch`; use `ada_get_block_info` or `ada_get_block_txs` for a selected block.
- **Staking analysis:** `ada_get_staking_info`, `ada_list_staking_transactions`, and `ada_list_staking_rewards` with an explicit historical range.
- **Asset analysis:** resolve with `ada_get_native_asset` or `ada_get_native_asset_by_policy_name`, inspect a policy with `ada_get_policy_assets`, and use the returned identifiers for further queries.
- **Pool analysis:** use `ada_get_pool_hash` when the input is not already a pool hash, then call `ada_get_pool_info`.

## Output template

Use this structure unless the user asks for another format:

```text
Query summary: [question and scope]
Source: blockchain-applied MCP connector, [tool names]
Parameters: [non-secret identifiers, time range, page settings]
Raw results: [temporary directory]

Findings
[table, chart, or concise interpretation]

Caveats
[defaults, missing data, pagination, unit conversions, or API limitations]

Follow-up queries
[optional concrete next steps]
```

Do not include credentials in any section.
