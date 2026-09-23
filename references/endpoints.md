# Cardano MCP endpoint reference

The `blockchain-applied` connector exposes these Cardano tools. The live MCP schema is authoritative for parameters and return types. Call `tool.get` before using a tool when parameter details are needed.

| MCP tool | Purpose |
|---|---|
| `ada_get_address_summary` | Summarize an address, including total outputs, consumed UTxOs, ADA received, and ADA spent. |
| `ada_list_address_transactions` | List address transactions with pagination and a time range. The default window is recent, not full history. |
| `ada_get_transaction_details` | Return comprehensive transaction details, including inputs, outputs, metadata, minted assets, and scripts. |
| `ada_get_latest_block` | Return the current chain tip and its block metadata. |
| `ada_get_block_info` | Return details for a block hash, including epoch, slot, size, transaction count, and neighboring blocks. |
| `ada_get_block_txs` | List transaction hashes in a block. |
| `ada_get_block_by_slot` | Resolve a slot number to a block hash. |
| `ada_get_current_epoch` | Return statistics for the current epoch. |
| `ada_get_epoch_info` | Return statistics and time boundaries for a specified epoch. |
| `ada_get_staking_info` | Summarize a stake address, including delegation, rewards, withdrawals, and transaction summaries. |
| `ada_list_staking_transactions` | List transactions for a stake address with pagination and a time range. |
| `ada_list_staking_rewards` | List rewards and withdrawals for a stake address with pagination and a time range. Use an explicit historical start for full history. |
| `ada_get_pool_info` | Return stake-pool pledge, margin, fixed cost, registration data, and delegation count. |
| `ada_get_pool_hash` | Translate a pool identifier to its pool hash. |
| `ada_get_native_asset` | Look up a native asset or NFT by fingerprint, including policy, asset name, and metadata. |
| `ada_get_native_asset_by_policy_name` | Look up a native asset by policy ID and asset name. |
| `ada_get_policy_assets` | List or summarize assets under a policy ID. |
| `ada_get_script_info` | Return script type, size, JSON representation, and creation transaction for a script hash. |
| `ada_get_datum` | Return datum JSON, bytes, and the transaction that introduced a datum hash. |
| `ada_list_metadata_transactions` | List transactions containing metadata under a specified key, with pagination and time range. |
| `ada_check_api_health` | Check whether the Cardano API is healthy and responding. |

## BCA API route concepts

The OpenAPI document at <https://schemas.blockchain-applied.com/cardano/api/openapi.json> describes the corresponding REST concepts under `/api_ada/v1`, including address summaries, balances by stake address, asset UTxOs, blocks, epochs, latest block, address and staking listings, metadata listings, native assets, policy assets, pools, scripts, datums, transactions, and health. Use the MCP connector rather than calling these routes directly so connector credentials remain protected.

## Important parameter conventions

- Paginated routes use zero-indexed `page` and a bounded `pagesize`.
- Historical listing routes accept `after` and `before` timestamps. Omitted `after` values invoke endpoint-specific recent-history defaults.
- Native asset policy and asset-name lookups use the asset name's hex representation where required by the API.
- Asset UTxO units are policy ID concatenated with asset-name hex in the underlying API.
- Keep Cardano identifiers in their original representation. Do not normalize or truncate them in saved results.
