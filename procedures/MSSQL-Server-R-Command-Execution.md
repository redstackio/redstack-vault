---
id: 414bab68-d171-4fe2-9a92-4d2cb08c2537
name: MSSQL-Server-R-Command-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.630962+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/MSSQL-Server]]'
  - '[[tags/R]]'
commands:
  - '[[commands/invoke-sqloscmdr-execute]]'
  - '[[commands/mssql-execute-external-r-script]]'
platforms:
  - Windows
tools: []
validated: true
---

# MSSQL-Server-R-Command-Execution

## Summary

This procedure enables attackers with authenticated access to an MSSQL Server to execute arbitrary operating system commands via R scripts using the sp_execute_external_script stored procedure. By leveraging R's system or shell functions within external scripts, attackers can run commands like directory listings or PowerShell payloads, bypassing some database-level restrictions to achieve remote code execution on the underlying server.

## Description

MSSQL Server supports external script execution for languages like R through the 'SQL Server Machine Learning Services' feature, which allows running scripts outside the SQL engine. Attackers can abuse the sp_execute_external_script procedure to execute R code that invokes OS commands via functions such as system() or shell(). This technique is particularly effective if the MSSQL service account has sufficient privileges on the host OS, enabling actions like file access, network operations, or further payload execution. The target environment is typically a Windows server running MSSQL with R Services enabled. Prerequisites include valid SQL credentials with EXECUTE permission on sp_execute_external_script. Successful execution returns command output as a dataset, allowing attackers to confirm results and chain further actions like privilege escalation or data exfiltration.

## Requirements

1. Authenticated access to the MSSQL Server instance via SQL client (e.g., sqlcmd, SSMS).
2. User account with EXECUTE permission on the sp_execute_external_script stored procedure.
3. MSSQL Server with R Services (Machine Learning Services) enabled and configured.
4. Knowledge of R scripting basics for embedding OS commands.
5. Optional: Base64-encoded payloads for evasion in PowerShell invocations.

## Defense

- Restrict EXECUTE permissions on sp_execute_external_script to trusted users only; disable external script execution if not needed via sp_configure 'external scripts enabled', 0.
- Monitor SQL Server error logs and audit logs for invocations of sp_execute_external_script, especially with R language parameter.
- Implement least privilege for the MSSQL service account to limit OS command impact; use AppLocker or similar to block unauthorized script execution.
- Enable SQL Server auditing for stored procedure calls and review for anomalous R script usage.
- Segment the database server network to contain potential lateral movement from executed commands.

## Objectives

1. Execute arbitrary OS commands on the MSSQL host via R scripts to achieve remote code execution.
2. Bypass database-only restrictions by leveraging external scripting capabilities.
3. Retrieve command output as SQL result sets for verification and further exploitation.

## Instructions

### Step 1: Connect to MSSQL Instance and Prepare Credentials

**Context**: Establish a connection to the target MSSQL instance using provided credentials. This step ensures authenticated access required for external script execution. Use a SQL client like sqlcmd or PowerShell's Invoke-Sqlcmd if available.

**Command** ([[commands/invoke-sqloscmdr-execute]]):
```powershell
Invoke-SQLOSCmdR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell -e <base64encodedscript>" -Verbose
```

> This PowerShell-based command (assuming a custom or module-loaded cmdlet) authenticates and prepares for OS command injection. Replace placeholders with actual values. Expected output includes verbose connection logs confirming successful authentication to the instance.

### Step 2: Execute R Script for OS Command via System Function

**Context**: Use the sp_execute_external_script procedure to run an R script that executes an OS command (e.g., directory listing) using the system() function. This captures output and returns it as a SQL dataset, allowing verification within the database session.

**Command** ([[commands/mssql-execute-external-r-script]]):
```sql
EXEC sp_execute_external_script @language=N'R', @script=N'OutputDataSet <- data.frame(system("cmd.exe /c dir",intern=T))' WITH RESULT SETS (([cmd_out] text)); GO
```

> The command embeds the OS command within an R script, directing output to a data frame. The system() function runs cmd.exe synchronously. Expected output is a result set with columns containing the directory listing (e.g., file names, sizes). If the command fails due to permissions, SQL errors indicate insufficient privileges.

### Step 3: Alternative Execution Using Shell Function

**Context**: For variation or if system() is restricted, use R's shell() function to execute the command. This step provides a fallback and demonstrates flexibility in payload delivery. Verify output to confirm command success.

**Code** ([[codes/MSSQL-R-Command-Execution-Script]]):

> Embed the R script snippet using shell() for non-interactive command execution. Expected output mirrors Step 2, returning command results as text in the dataset. Success is indicated by populated rows without R runtime errors.
