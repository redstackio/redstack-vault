---
id: cmd-setup-chain
data: ./setup_chain
tags:
  - chain-setup
  - testnet
type: command
output: Local chain started and running
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:46.752Z'
verified: false
validated: true
submitted: true
---
---

# setup-chain

## Command

```bash
./setup_chain
```

## Description

Initializes and starts a local Cosmos testnet using built SDK binaries, enabling lockup module for vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Script handles genesis and node start | No |

## Examples

### Basic Usage

```bash
chmod +x setup_chain
./setup_chain
```

### Advanced Usage

```bash
./setup_chain --reset-on-start
```

## Expected Output

Genesis initialized; nodes started with block production logs.

## Related

- [[Related Procedure: Start-Local-Cosmos-Chain]]
