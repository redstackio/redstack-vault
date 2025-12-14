---
id: cmd-004
data: >-
  curl -s -X POST -H "Content-Type: application/json" -d
  '{"jsonrpc":"2.0","method":"web3_clientVersion", "params": {}, "id":1337}'
  https://bounty-node.rsk.co
tags:
  - rpc
  - version
type: command
output: '{"jsonrpc":"2.0","id":1337,"result":"RskJ/0.4.0/Linux/Java1.8/BAMBOO-1192882"}'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.630Z'
verified: false
validated: true
submitted: true
---
# RPC Web3 ClientVersion Query

## Command

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"web3_clientVersion", "params": {}, "id":1337}' https://bounty-node.rsk.co
```

## Description

Retrieves the client version string via JSON-RPC to test endpoint health and verify DoS impact through failures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent | Yes |
| -X POST | POST | Yes |
| -H "Content-Type: application/json" | JSON type | Yes |
| -d '{...}' | Version query payload | Yes |
| https://bounty-node.rsk.co | Endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"web3_clientVersion", "params": {}, "id":1337}' https://bounty-node.rsk.co
```

## Expected Output

Pre-DoS: Version JSON; post-DoS: 504 timeout.

## Related

- [[commands/rpc-eth-blocknumber-query]]
- [[procedures/Verify-Server-Responsiveness-Impact]]
