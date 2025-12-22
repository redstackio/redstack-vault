---
id: 4dae1d77-de7f-4b61-b134-0b14117f96b4
name: Retrieve-DB2PATH-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.179761+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/DB2 Cheatsheet]]'
  - '[[tags/DB2 Injection]]'
  - '[[tags/Location of DB Files]]'
  - sql-injection
  - database-enumeration
commands: []
platforms:
  - Linux
  - Windows
  - Database
tools: []
validated: true
---

# Retrieve-DB2PATH-via-SQL-Injection

## Summary

This procedure demonstrates how to use SQL injection in a vulnerable DB2 database to retrieve the DB2PATH environment variable, which specifies the installation path of DB2 files. This information can aid in further database enumeration or exploitation by revealing file locations for potential lateral movement or data access.

## Description

DB2 Injection exploits vulnerabilities in DB2 database applications where user input is not properly sanitized, allowing attackers to append malicious SQL code to legitimate queries. In this case, the goal is to query the system registry table sysibmadm.reg_variables to extract the DB2PATH value. This path is critical as it points to the DB2 instance directory, potentially exposing configuration files, logs, or other sensitive data. The technique assumes access to an injection point, such as a web form or API endpoint interacting with the DB2 backend. Success requires sufficient privileges to access the registry, typically available in default or misconfigured setups. This procedure maps to exploiting public-facing applications and can lead to unauthorized data collection or execution within the database environment.

## Requirements

1. Access to a web application or interface connected to a vulnerable DB2 database instance with an SQL injection vulnerability.
2. Knowledge of the injection point (e.g., login form, search field) and basic SQL syntax for DB2.
3. Tools for testing injections, such as a browser, proxy like Burp Suite, or sqlmap (though not required for manual execution).
4. Network connectivity to the target application and sufficient privileges to query system tables (e.g., non-restricted user context).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation, sanitization, and parameterization for all database queries to prevent injection attacks.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns in requests.
- Enable database auditing and logging to monitor queries against system tables like sysibmadm.reg_variables.
- Apply least privilege principles to database users, restricting access to administrative or registry tables.
- Regularly scan for vulnerabilities using tools like sqlmap or database-specific scanners.

## Objectives

1. Identify and exploit an SQL injection vulnerability in a DB2-connected application.
2. Query the system registry to retrieve the DB2PATH environment variable.
3. Use the retrieved path for further reconnaissance or exploitation of the database environment.

## Instructions

### Step 1: Identify the SQL Injection Point

**Context**: Locate a user-controllable input field in the application that interacts with the DB2 database, such as a search box or login form. Test for injection by appending a single quote (') to the input and observing if it causes a SQL error, indicating unsanitized input.

**Test Input**: Enter a payload like `test' OR '1'='1` in the field and submit. If the application returns unexpected results or errors mentioning SQL syntax, an injection point is confirmed.

> This step verifies the vulnerability without executing the full query, reducing detection risk.

### Step 2: Craft and Inject the DB2PATH Retrieval Query

**Context**: Once the injection point is confirmed, append the SQL query to extract DB2PATH from the registry. This leverages the comment syntax (--) to ignore any trailing query parts. The query targets the sysibmadm.reg_variables table, which stores environment variables like DB2PATH.

**Code** ([[codes/DB2-SQL-Query-Retrieve-DB2PATH]]):

```sql
select * from sysibmadm.reg_variables where reg_var_name='DB2PATH' -- requires priv
```

> Inject this by concatenating it to the legitimate input, e.g., if the original query is `SELECT * FROM users WHERE id = '<input>'`, make it `SELECT * FROM users WHERE id = '1' UNION select * from sysibmadm.reg_variables where reg_var_name='DB2PATH' --`. The expected output is the row containing the DB2PATH value, such as `/opt/ibm/db2/V11.5`. If privileges are insufficient, an error like "DB21034E The command was processed as an SQL statement" may appear—escalation or alternative tables may be needed.

### Step 3: Validate and Utilize the Retrieved Path

**Context**: Confirm the output reveals the DB2 installation path and assess its utility for next steps, such as attempting to read files at that location via further injections or file access techniques.

**Verification**: Check the response for the reg_var_value column containing a path like `C:\Program Files\IBM\SQLLIB` (Windows) or `/opt/ibm/db2/V11.5` (Linux). If successful, note the path for chaining with procedures like file enumeration.

> Success here enables deeper access; failure may indicate privilege issues—test with less sensitive queries first.
