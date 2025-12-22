---
id: cmd-uuid-2
data: 'node attack.js --target localhost:3000 --connections 100'
tags:
  - connections
  - dos
type: command
output: |-
  Connection 1 established
  Connection 2 established
  ...
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.662Z'
verified: false
validated: true
submitted: true
---
# node-attack-connections

## Command

```bash
node attack.js --target localhost:3000 --connections 100
```

## Description

Runs a Node.js attack script to open multiple HTTP/2 connections to the target server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--target` | Target host:port | Yes |
| `--connections` | Number of connections to open | Yes |

## Examples

### Basic Usage

```bash
node attack.js --target localhost:3000 --connections 100
```

### Advanced Usage

```bash
node attack.js --target example.com:443 --connections 500 --timeout 30
```

## Expected Output

Logs for each successful connection establishment.

## Related

- [[procedures/Establish-Multiple-HTTP2-Connections]]
