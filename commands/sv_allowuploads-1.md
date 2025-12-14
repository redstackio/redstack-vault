---
id: cmd-sv-allowuploads
data: sv_allowuploads 1
tags:
  - server-config
  - csgo
type: command
output: 'Console confirmation: "sv_allowuploads changed to 1"'
executor: csgo-server
platforms:
  - Windows
  - Gaming
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.895Z'
verified: false
validated: true
submitted: true
---
# sv_allowuploads-1

## Command

```bash
sv_allowuploads 1
```

## Description

This CS:GO server console command enables file uploads from clients to the server, necessary for receiving leaked files like _leak.txt containing the client.dll base address during exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sv_allowuploads | Sets upload allowance (0=disable, 1=enable) | Yes |

## Examples

### Basic Usage

```bash
sv_allowuploads 1
```

### Disable Usage

```bash
sv_allowuploads 0
```

## Expected Output

Console confirmation; allows server to receive leaked base address file from client.

## Related

- [[commands/connect-to-malicious-server]]
