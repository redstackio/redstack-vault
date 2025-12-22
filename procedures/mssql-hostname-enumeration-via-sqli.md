---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - mssql
  - sql-injection
  - hostname-enumeration
  - discovery
commands:
  - '[[commands/mssql-select-host-name]]'
  - '[[commands/mssql-select-server-hostname]]'
platforms:
  - Windows
  - MSSQL
tools: []
verified: true
validated: true
---

# mssql-hostname-enumeration-via-sqli

## Summary

This procedure demonstrates how to enumerate the hostname of a Microsoft SQL Server (MSSQL) instance using SQL injection vulnerabilities. By injecting specially crafted SQL payloads into a vulnerable web application or input field that interacts with an MSSQL backend, an attacker can extract server hostname information, aiding in further reconnaissance, mapping the internal network, or planning lateral movement.

## Description

MSSQL hostname enumeration via SQL injection targets applications with unsanitized inputs that reach the database layer, allowing arbitrary SQL execution. The technique exploits functions like HOST_NAME() or the @@hostname variable to retrieve the server's network hostname. This is particularly useful in blind SQL injection scenarios where direct query results are not visible, but inference techniques (e.g., time-based or boolean-based) can confirm the output. The target environment typically involves a web application fronting an MSSQL database, often on Windows servers. Success provides critical system details for pivoting attacks, such as identifying domain-joined servers or crafting targeted exploits. This procedure assumes basic knowledge of SQL injection identification and assumes the vulnerability allows stacked queries or UNION-based injection.

## Requirements

1. Access to a web application or input field vulnerable to SQL injection targeting an MSSQL backend.
2. Knowledge of SQL injection techniques, including payload crafting for MSSQL syntax.
3. Tools for testing injections, such as a proxy (e.g., Burp Suite) or SQL injection framework (e.g., sqlmap).
4. Network connectivity to the target application, potentially requiring bypassing WAFs if present.

## Defense

- Implement strict input validation, sanitization, and prepared statements/parameterized queries to prevent SQL injection.
- Use web application firewalls (WAFs) tuned to detect SQL injection patterns, including anomalous SELECT queries on system functions.
- Enable database logging (e.g., SQL Server Audit) to monitor execution of sensitive functions like HOST_NAME() or @@hostname.
- Apply least privilege to database accounts, restricting access to system variables and functions.

## Objectives

1. Identify and confirm a SQL injection vulnerability in an MSSQL-backed application.
2. Inject payloads to extract the server's hostname without direct access to the database console.
3. Use the enumerated hostname for further attack planning, such as network mapping or privilege escalation.

## Instructions

### Step 1: Identify the SQL Injection Vulnerability

**Context**: Begin by probing the target application for SQL injection points, such as login forms, search fields, or URL parameters. Use classic payloads to confirm error-based or blind injection. This step ensures the vulnerability exists before attempting enumeration.

**Command** ([[commands/mssql-test-basic-injection]]):

```sql
' OR 1=1 --
```

> Inject this into a parameter (e.g., username field). If successful, it may return all records or trigger a database error revealing MSSQL specifics (e.g., "Microsoft OLE DB Provider for SQL Server"). For blind injection, observe response differences (true/false conditions).

### Step 2: Craft and Inject Hostname Enumeration Payload

**Context**: Once injection is confirmed, use UNION-based or stacked query payloads to append the hostname retrieval. This step executes the enumeration query alongside the original, extracting the hostname from the response or inferred behavior.

**Code** ([[codes/mssql-hostname-enumeration-sql-payload]]):

```sql
SELECT HOST_NAME(); SELECT @@hostname;
```

> Embed this code in a UNION SELECT payload, e.g., `' UNION SELECT HOST_NAME(), @@hostname FROM dual --`. For stacked injections, terminate the original query and append. Expected output in error-based SQLi: Hostname displayed in error messages or response data, e.g., "SERVER01". In blind SQLi, extract character-by-character using conditional payloads like `IF(ASCII(SUBSTRING(HOST_NAME(),1,1))>64, SLEEP(5), 0)`.

### Step 3: Verify and Extract the Hostname

**Context**: Analyze the response for the hostname. If using tools like sqlmap, automate extraction; otherwise, manually decode. This confirms success and provides the data for next steps.

**Command** ([[commands/mssql-select-host-name]]):

```sql
SELECT HOST_NAME()
```

> Use this as the core of your injection payload. Expected output: A single column with the hostname, e.g., "DBSERVER-01". Cross-verify with the alternative command if needed.

**Command** ([[commands/mssql-select-server-hostname]]):

```sql
SELECT @@hostname;
```

> Alternative query for the same information. Expected output: Identical to HOST_NAME(), confirming consistency. If the first fails due to permissions, this may succeed as it's a global variable.

### Step 4: Document and Pivot

**Context**: Record the hostname and use it to inform further actions, such as querying additional system properties (e.g., @@servername for instance name) or attempting lateral movement.

> No specific command here; manually note the output. Success is indicated by consistent hostname retrieval across multiple injections, with no blocks from defenses.
