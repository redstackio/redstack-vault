---
type: procedure
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - extended-stored-procedure
  - mssql-server
  - dll-injection
commands:
  - '[[commands/sp-addextendedproc-load-dll]]'
  - '[[commands/exec-extended-proc]]'
  - '[[commands/sp-dropextendedproc-drop-proc]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Load-DLL-Using-sp_addextendedproc

## Summary

This procedure enables an attacker with administrative access to SQL Server to load a custom DLL as an extended stored procedure, execute its functions within the SQL Server process context, and then remove it. It facilitates arbitrary code execution, persistence, or privilege escalation by injecting malicious code disguised as legitimate database functionality, often evading detection through obfuscation of the DLL path or content.

## Description

In Microsoft SQL Server, extended stored procedures allow loading external DLLs that run in the server's address space, providing a vector for code execution. An attacker can use the built-in sp_addextendedproc system procedure to register a malicious DLL, invoke it via the xp_ prefix, and clean up with sp_dropextendedproc. This technique is particularly effective in environments where SQL Server runs with high privileges, allowing the DLL to perform system-level actions like file access, network communication, or further exploitation. The DLL can be hosted locally, on a UNC share, or even WebDAV for remote delivery. Detection is challenging if the DLL is obfuscated or loaded from trusted paths. This maps to defense evasion by hiding malicious payloads and execution within legitimate server processes.

## Requirements

1. Administrative (sysadmin) privileges on the SQL Server instance.
2. Access to place the DLL on the target system (local path like C:\mydll\xp_calc.dll) or a network share (UNC path).
3. SQL Server client access (e.g., via sqlcmd, SSMS, or integrated tools) to execute T-SQL commands.
4. The DLL must export a function compatible with extended procedures (e.g., named xp_calc).

## Defense

- Limit sysadmin roles to trusted administrators only and use principle of least privilege.
- Monitor SQL Server logs for sp_addextendedproc and sp_dropextendedproc executions, as well as unusual xp_ invocations.
- Enable SQL Server auditing for extended procedures and DLL loads; use tools like SQL Server Audit or Extended Events.
- Scan for and block suspicious DLLs on file systems and network shares; implement application whitelisting for SQL Server directories.
- Regularly review and disable unnecessary extended procedures; consider disabling xp_cmdshell and similar features.

## Objectives

1. Register and load a custom DLL as an extended stored procedure in SQL Server memory.
2. Execute the DLL's functions to run arbitrary code in the SQL Server process context.
3. Remove the extended procedure to erase traces and maintain stealth.

## Instructions

### Step 1: Add the Extended Stored Procedure

**Context**: Use sp_addextendedproc to load the malicious DLL into SQL Server. Specify the procedure name (e.g., xp_calc) and the full path to the DLL. This registers the DLL's entry point for execution. The path can be local, UNC, or WebDAV to avoid direct file transfer.

**Command** ([[commands/sp-addextendedproc-load-dll]]):
```sql
sp_addextendedproc 'xp_calc', 'C:\mydll\xp_calc.dll'
```

> This command returns a success message if the procedure is added without errors. Verify by querying sys.extended_procedures or executing sp_helpextendedproc 'xp_calc'. If the DLL path is invalid or inaccessible, it will error with a file not found message.

### Step 2: Execute the Extended Stored Procedure

**Context**: Once loaded, invoke the procedure using the EXEC statement to run the DLL's code. This executes the malicious payload in the context of the SQL Server service, potentially allowing system compromise depending on the DLL's functionality (e.g., reverse shell, data exfil).

**Command** ([[commands/exec-extended-proc]]):
```sql
EXEC xp_calc
```

> Expected output depends on the DLL; a simple calc DLL might return a computation result, while a malicious one could produce no visible output but establish persistence or connections. Check SQL Server error logs or network traffic for side effects. Success is indicated by no execution errors and any intended payload behavior (e.g., new process spawned).

### Step 3: Drop the Extended Stored Procedure

**Context**: After execution, remove the procedure to avoid detection during audits. This unloads the DLL from memory and cleans up the registry entry, reducing forensic footprints.

**Command** ([[commands/sp-dropextendedproc-drop-proc]]):
```sql
sp_dropextendedproc 'xp_calc'
```

> The command succeeds silently if the procedure exists, or errors if it doesn't. Verify removal by querying sys.extended_procedures; the entry should be gone. This step ensures the attack leaves minimal traces in the database metadata.
