---
type: command
executor: bash
data: cme mimikatz --server http --server-port 80
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - mimikatz
  - server
verified: true
validated: true
---

# cme-mimikatz-server

## Command

```bash
cme mimikatz --server http --server-port 80
```

## Description

Starts a Mimikatz HTTP server for remote dumping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --server http | Protocol | Yes |
| --server-port 80 | Port | Yes |

## Examples

### Basic Usage

```bash
cme mimikatz --server http --server-port 80
```

## Expected Output

Server listening: "Mimikatz server started on port 80".

## Related

- [[tools/CrackMapExec]]
