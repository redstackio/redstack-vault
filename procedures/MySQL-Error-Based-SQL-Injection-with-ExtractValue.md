---
id: b929b08c-8245-4ae0-b3b3-9ac717f160f3
name: MySQL-Error-Based-SQL-Injection-with-ExtractValue
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.502228+00:00'
updated_at: '2023-04-10T20:22:51.610775+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
  - >-
    [[techniques/Data-from-Information-Repositories|T1213 - Data from
    Information Repositories]]
sub_techniques: []
tags:
  - '[[tags/MySQL-Injection]]'
  - '[[tags/Error-Based-SQLi]]'
  - '[[tags/Blind-SQL-Injection]]'
  - '[[tags/ExtractValue-Function]]'
commands:
  - '[[commands/mysql-check-version]]'
tools: []
platforms:
  - Web
  - MySQL
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# MySQL-Error-Based-SQL-Injection-with-ExtractValue

## Summary

This procedure demonstrates how to perform error-based blind SQL injection using MySQL's ExtractValue function to extract sensitive information such as database version, schema names, table names, column names, and actual data from a vulnerable web application. It exploits insufficient input sanitization in SQL queries to force database errors that reveal concatenated data, allowing attackers to bypass authentication and retrieve information without direct query results.

## Description

Error-based SQL injection with ExtractValue targets MySQL databases (version 5.1+) vulnerable to injection in parameters like 'id' in URL queries. The technique uses the ExtractValue function, which generates an XPATH error when provided invalid input, to leak data via the error message. By concatenating target data with delimiters (e.g., CHAR(126) for ~), the attacker infers information from error responses. This is 'blind' as it relies on error differences rather than direct output. Applicable in scenarios where the application echoes SQL errors, such as development or misconfigured production environments. Prerequisites include identifying a injectable parameter via manual testing or tools like sqlmap.

## Requirements

1. Access to a web application with a MySQL backend vulnerable to SQL injection (e.g., unparameterized query in a search or ID parameter).
2. Knowledge of basic SQL syntax and MySQL functions.
3. A proxy tool like Burp Suite for intercepting and modifying requests (optional but recommended for precision).
4. MySQL client installed locally if verifying against a test database.

## Defense

- Implement strict input validation and sanitization for all user inputs, especially in dynamic SQL queries.
- Use prepared statements and parameterized queries to separate code from data.
- Configure the application to suppress detailed SQL error messages in production (e.g., set display_errors=Off in PHP).
- Regularly scan for vulnerabilities using tools like sqlmap or OWASP ZAP, and apply database-level protections like WAF rules blocking common injection patterns.
- Keep MySQL and web server software updated to mitigate known exploits.

## Objectives

1. Verify MySQL version compatibility for the injection technique.
2. Extract database metadata (version, schemas, tables, columns) via error messages.
3. Retrieve sensitive data from target tables without direct query visibility.
4. Confirm successful data exfiltration through response analysis.

## Instructions

### Step 1: Verify MySQL Version

**Context**: Ensure the target MySQL instance supports the ExtractValue function (available since 5.1). This step confirms compatibility before attempting injections, preventing wasted effort on unsupported versions.

**Command** ([[commands/mysql-check-version]]):
```bash
mysql --version
```

> This command runs the MySQL client to display the installed version. If testing locally or with direct access, compare the output to confirm >= 5.1. For remote targets, infer from error messages during initial injection tests. Expected output includes the server version; if below 5.1, the technique may fail.

### Step 2: Inject Payloads to Extract Database Information

**Context**: Use the blind injection payloads to force errors that reveal data. Start with version extraction, then progress to schemas, tables, columns, and data. Replace 'data_offset' with incremental values (0,1,2...) to enumerate items one by one. Monitor application responses for error messages containing the delimited data (e.g., ~extracted_value~).

**Code** ([[codes/MySQL-ExtractValue-Blind-SQL-Injection-Payloads]]):
```sql
?id=1 AND extractvalue(rand(),concat(CHAR(126),version(),CHAR(126)))--
?id=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),schema_name,CHAR(126)) FROM information_schema.schemata LIMIT data_offset,1)))--
?id=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),TABLE_NAME,CHAR(126)) FROM information_schema.TABLES WHERE table_schema=data_column LIMIT data_offset,1)))--
?id=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),column_name,CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME=data_table LIMIT data_offset,1)))--
?id=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),data_info,CHAR(126)) FROM data_table.data_column LIMIT data_offset,1)))--
```

> Append these payloads to the vulnerable URL parameter (e.g., http://target.com/page?id=...). The first payload extracts the MySQL version. Subsequent ones require substituting 'data_column' with the discovered schema name, 'data_table' with the table name, and 'data_info'/'data_column' with actual column names for data extraction. Success is indicated by error messages like "XPATH syntax error: '~5.7.XX~'" where the version or data appears between tildes (~). Iterate offsets to dump full lists. If no error, the parameter may not be injectable—test with a simple ' AND 1=1--' first.
