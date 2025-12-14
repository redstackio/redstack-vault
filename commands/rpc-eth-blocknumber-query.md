---
id: cmd-001
data: >-
  curl -s -X POST -H "Content-Type: application/json" -d
  '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": [], "id":1337}'
  https://bounty-node.rsk.co
tags:
  - rpc
  - query
type: command
output: '{"jsonrpc":"2.0","id":1337,"result":"0x437ca"}'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.643Z'
verified: false
validated: true
submitted: true
---
# RPC Eth BlockNumber Query

## Command

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": [], "id":1337}' https://bounty-node.rsk.co
```

## Description

Queries the current Ethereum-compatible block number via JSON-RPC on a Rootstock node, used for baseline or confirmation in DoS assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent mode, suppresses progress meter | Yes |
| -X POST | Specifies HTTP POST method | Yes |
| -H "Content-Type: application/json" | Sets JSON header | Yes |
| -d '{...}' | JSON payload with method and id | Yes |
| https://bounty-node.rsk.co | Target RPC URL | Yes |

## Examples

### Basic Usage

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": [], "id":1337}' https://bounty-node.rsk.co
```

### Advanced Usage

Add timeout: ```bash
curl -s --max-time 10 -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": [], "id":1337}' https://bounty-node.rsk.co
```

## Expected Output

JSON response with hex block number, e.g., {"jsonrpc":"2.0","id":1337,"result":"0x437ca"} pre-DoS or "0x0" post-reset.

## Related

- [[commands/rpc-web3-clientversion-query]]
- [[procedures/Baseline-RPC-Block-Number-Check]]
