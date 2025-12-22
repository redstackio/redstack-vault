---
id: d50f9e11-3f69-40f4-86ad-08d3e3318485
name: Enumerate-MSSQL-Version
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.557317+00:00'
updated_at: '2023-04-10T20:22:39.738059+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/MSSQL]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Database]]'
  - '[[tags/SQL-Injection]]'
commands:
  - '[[commands/mssql-select-version]]'
platforms:
  - Windows
  - Linux
tools: []
validated: true
---

# Enumerate-MSSQL-Version

## Summary

This procedure demonstrates how to enumerate the version of a Microsoft SQL Server (MSSQL) instance using a simple SQL query. This information can reveal potential vulnerabilities specific to the server's version, aiding in targeted exploitation during penetration testing or red team engagements.

## Description

Enumerating the MSSQL version is a reconnaissance technique often used in database-focused attacks, particularly when SQL injection vulnerabilities are present. By injecting or executing a query like SELECT @@version, an attacker can obtain details such as the exact version number, build, edition, and operating system information. This data helps identify exploitable weaknesses, such as unpatched CVEs in older versions (e.g., SQL Server 2008 vulnerabilities). The technique assumes access to the database via direct connection, SQL injection, or compromised credentials. It is typically performed in web applications vulnerable to SQLi or during lateral movement in Active Directory environments with exposed MSSQL instances.

## Requirements

1. Network access to the target MSSQL server (default port 1433/TCP).
2. Valid credentials or a SQL injection point in a web application.
3. A tool like sqlcmd, Impacket's mssqlclient.py, or a SQL client (e.g., [[tools/sqlmap]] for automated injection).
4. Basic knowledge of SQL syntax and injection techniques.

## Defense

- Keep MSSQL servers patched to the latest version and apply security updates promptly.
- Disable unnecessary information disclosure by configuring SQL Server to hide version details (e.g., via sp_configure 'show advanced options', 1; RECONFIGURE; sp_configure 'info msg', 0).
- Implement web application firewalls (WAFs) to detect and block SQL injection attempts.
- Enable query logging and monitor for anomalous queries containing @@version or similar reconnaissance patterns.
- Use least-privilege accounts for database connections and restrict direct access to MSSQL instances.

## Objectives

1. Retrieve the exact version and build information of the target MSSQL instance.
2. Identify edition-specific features or vulnerabilities for further exploitation.
3. Validate the presence of MSSQL as a service for chaining to other database attacks.

## Instructions

### Step 1: Establish Connection to MSSQL Instance

**Context**: Connect to the target MSSQL server using a SQL client tool. This step assumes you have credentials or an injection vector; if using SQLi, identify the vulnerable parameter first.

If using sqlcmd (built-in on Windows, installable on Linux):

**Command** ([[commands/mssql-select-version]]):
```sql
sqlcmd -S $_TARGET_SERVER -U $_USERNAME -P $_PASSWORD -Q "SELECT @@version"
```

> This command connects to the server and executes the version query. Replace placeholders with actual values. Expected output includes version details; if connection fails, check firewall rules or credentials.

Decision point: If no direct access, proceed to Step 2 for SQL injection delivery.

### Step 2: Inject Query via SQL Injection (If Applicable)

**Context**: If the target is a web app with SQLi, craft an injection payload to execute the query. Use tools like [[tools/sqlmap]] for automation, or manual injection with Burp Suite.

Manual example using a vulnerable login form:

**Command** ([[commands/mssql-select-version]]):
```sql
' UNION SELECT @@version --
```

> Append this to a vulnerable parameter (e.g., username field). The query extracts version info into the response. Expected output: Version string echoed in the app's output, such as error messages or data fields.

Verify success by checking if the response contains MSSQL-specific strings like "Microsoft SQL Server".

### Step 3: Parse and Analyze Output

**Context**: Review the retrieved version to map against known vulnerabilities (e.g., using NIST NVD or Exploit-DB).

No specific command needed; manually note the output from previous steps.

> For example, if output shows "SQL Server 2016 (13.x)", research CVEs like CVE-2017-0144 (if unpatched). Success criteria: Clear version identification without errors.
