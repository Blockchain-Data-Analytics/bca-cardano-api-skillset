<a href="https://www.blockchain-applied.com"><img src="assets/logo.svg" alt="BCA - Blockchain Applied" width="64" height="64"></a>

# bca-cardano-api-skillset

Claude Code skill for querying Cardano on-chain data through the `blockchain-applied` MCP connector and the BCA API — addresses, transactions, blocks, epochs, staking, pools, native assets, scripts, datums, and metadata.

## Install

Clone (or add as a submodule) into your Claude Code skills directory:

```sh
git clone https://github.com/Blockchain-Data-Analytics/bca-cardano-api-skillset.git ~/.claude/skills/query-cardano-api
```

Requires the `blockchain-applied` MCP connector to be configured separately in your Claude Code environment.

## Contents

- `SKILL.md` — skill instructions and workflow.
- `references/endpoints.md` — MCP tool and BCA API endpoint reference.
- `scripts/json_to_markdown.py` — renders a saved query result JSON file as Markdown. No dependencies beyond the Python standard library (Python 3.9+).

`scripts/__pycache__/` is generated automatically the first time `json_to_markdown.py` runs and is git-ignored — nothing to set up.

## Usage

Once installed, ask Claude Code about Cardano addresses, transactions, blocks, staking, pools, or assets. The skill triggers automatically and follows the workflow defined in `SKILL.md`.

## License

Apache 2.0 — see [LICENSE](LICENSE).
