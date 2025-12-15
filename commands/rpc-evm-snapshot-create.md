---
id: cmd-002
data: >-
  curl -s -X POST -H "Content-Type: application/json" -d
  '{"jsonrpc":"2.0","method":"evm_snapshot", "params": {}, "id":666}'
  https://bounty-node.rsk.co
tags:
  - evm
  - snapshot
type: command
output: '{"jsonrpc":"2.0","id":666,"result":"0x1"}'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.640Z'
verified: false
validated: true
submitted: true
---
# RPC EVM Snapshot Create

## Command

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_snapshot", "params": {}, "id":666}' https://bounty-node.rsk.co
```

## Description

Creates an EVM state snapshot via JSON-RPC, testing for debugging method exposure on RPC nodes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent output | Yes |
| -X POST | POST request | Yes |
| -H "Content-Type: application/json" | JSON content type | Yes |
| -d '{...}' | Payload with evm_snapshot method | Yes |
| https://bounty-node.rsk.co | RPC endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_snapshot", "params": {}, "id":666}' https://bounty-node.rsk.co
```

### Repeated Usage

Run multiple times for incremental IDs.

## Expected Output

{"jsonrpc":"2.0","id":666,"result":"0x1"} or higher for repeats.

## Related

- [[commands/rpc-evm-reset-trigger]]
- [[procedures/Test-EVM-Snapshot-Methods]]
