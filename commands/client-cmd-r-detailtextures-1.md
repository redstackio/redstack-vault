---
id: cmd-goldsrc-client-cmd
data: client_cmd "r_detailtextures 1"
tags:
  - remote-execution
  - client-command
type: command
output: >-
  Client executes the command remotely; enables detail textures without local
  input.
executor: amxx_script
platforms:
  - Windows
  - Game (GoldSrc Engine)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.574Z'
verified: false
validated: true
submitted: true
---
# client-cmd-r-detailtextures-1

## Command

```bash
client_cmd "r_detailtextures 1"
```

## Description

AMX Mod X command to remotely force a connected client to execute a console command string, here enabling the vulnerable detail textures feature to trigger file parsing and overflow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"r_detailtextures 1"` | Command string to run on the client (enables feature) | Yes |

## Examples

### Basic Usage

```bash
client_cmd "r_detailtextures 1"
```

### For Specific Client

In plugin: client_cmd(id, "say hello")

```bash
client_cmd "echo Test"
```

## Expected Output

Client-side: Feature enables silently; no server feedback, but client is now vulnerable to map load.

## Related

- [[commands/r-detailtextures-1]]
