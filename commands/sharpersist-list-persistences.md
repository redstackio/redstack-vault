---
type: command
executor: powershell
data: >-
  SharPersist -t schtaskbackdoor -m list; SharPersist -t startupfolder -m list;
  SharPersist -t schtask -m list; SharPersist -t service -m list
tags:
  - persistence
  - enumeration
platforms:
  - Windows
verified: true
validated: true
---

# sharpersist-list-persistences

## Command

```powershell
SharPersist -t schtaskbackdoor -m list; SharPersist -t startupfolder -m list; SharPersist -t schtask -m list; SharPersist -t service -m list
```

## Description

This command queries existing persistence entries created by SharPersist across multiple types in a Cobalt Strike beacon session, helping operators assess the current state without external tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t <type>` | Persistence type (schtaskbackdoor, startupfolder, schtask, service) | Yes |
| `-m list` | Mode to list entries | Yes |

## Examples

### Basic Usage

```powershell
SharPersist -t schtask -m list
```

### Advanced Usage

```powershell
SharPersist -t service -m list | findstr /i suspicious
```

## Expected Output

If entries exist:
```
Persistence: Something Cool
Type: schtaskbackdoor
Command: C:\Windows\System32\cmd.exe /c calc.exe
Path: HKCU:\Software\Microsoft\Windows\CurrentVersion\Run
```

If none:
```
No persistences found.
```

## Related

- [[procedures/Establish-Persistence-Using-SharPersist-in-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
