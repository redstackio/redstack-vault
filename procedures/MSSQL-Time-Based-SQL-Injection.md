---
id: 248b8059-759e-4266-8538-0c445d24e838
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.874406+00:00'
updated_at: '2023-04-10T20:22:45.303894+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059.001 - Command and
    Scripting Interpreter: SQL]]
sub_techniques: []
tags:
  - '[[tags/MSSQL Injection]]'
  - '[[tags/MSSQL Time based]]'
  - sql-injection
  - time-based
commands: []
platforms:
  - Web
  - Windows
tools: []
validated: true
---

# MSSQL-Time-Based-SQL-Injection

## Summary

MSSQL Time-Based SQL Injection exploits vulnerabilities in web applications backed by Microsoft SQL Server databases by injecting SQL payloads that introduce deliberate delays in query execution, allowing attackers to infer data presence or values based on response times without direct error messages.

## Description

This procedure targets web applications vulnerable to SQL injection where the backend uses MSSQL. By appending time-delay functions like WAITFOR DELAY to input fields, attackers can craft blind injections that don't rely on visible errors or boolean responses but instead on timing differences. For example, a longer response time indicates a true condition in a conditional statement, enabling gradual data extraction such as database schema, user credentials, or sensitive records. This is particularly effective against applications with strict error handling or WAFs that block error-based injections. The attack assumes the application processes user input directly in SQL queries without parameterization, and it can lead to full database compromise, data exfiltration, or even command execution if elevated privileges are obtained.

## Requirements

1. Access to a vulnerable web application endpoint that interacts with an MSSQL database (e.g., via GET/POST parameters like 'id' or 'search').
2. Knowledge of potential injection points, such as numeric or string fields in forms/URLs.
3. A tool for sending HTTP requests (e.g., browser, curl, or Burp Suite) to measure response times accurately.
4. Basic understanding of SQL syntax and the target application's query structure.

## Defense

- Use parameterized queries or prepared statements in application code to separate SQL logic from user input.
- Implement web application firewalls (WAFs) with rules to detect anomalous delays or SQL keywords like 'WAITFOR'.
- Enable database logging and monitor for unusual query patterns or long-running queries.
- Regularly audit and sanitize all user inputs, and apply least-privilege principles to database accounts.

## Objectives

1. Confirm the presence of a time-based SQL injection vulnerability by observing response delays.
2. Extract database information, such as table names, column data, or user credentials, through conditional timing inferences.
3. Escalate to data exfiltration or further exploitation like executing system commands if possible.

## Instructions

### Step 1: Identify and Test Injection Point

**Context**: Locate a parameter vulnerable to SQL injection and test basic concatenation to confirm the endpoint processes input as SQL. This step verifies the attack surface without triggering delays yet.

Use a simple payload like appending a comment to see if the query alters (e.g., response changes or errors appear). For example, in a URL parameter 'ProductID=1', test 'ProductID=1--'.

**Expected Output**: The application responds normally if injectable, or errors if not; no delay yet, but confirms input reaches the SQL layer.

### Step 2: Inject Time-Delay Payload to Confirm Vulnerability

**Context**: Introduce a WAITFOR DELAY statement to force a measurable response lag, confirming blind injection capability. This exploits MSSQL's time-based inference without needing output.

**Payload** ([[codes/MSSQL-Time-Based-Delay-Payloads]]):

```sql
ProductID=1;waitfor delay '0:0:10'--
ProductID=1);waitfor delay '0:0:10'--
ProductID=1';waitfor delay '0:0:10'--
ProductID=1');waitfor delay '0:0:10'--
ProductID=1));waitfor delay '0:0:10'--
```

Send these variations via the web form or URL, adjusting for the injection context (e.g., stacked queries with ';', or closing strings with '). Measure response time; a 10-second delay indicates success.

**Expected Output**: Response takes approximately 10 seconds longer than a normal query, confirming the payload executes.

### Step 3: Perform Data Inference Using Conditional Delays

**Context**: Build on the delay to extract data bit-by-bit. Use conditional logic (IF statements) to delay only if a condition is true, inferring database content from timing.

**Payload** ([[codes/MSSQL-Time-Based-Delay-Payloads]]):

```sql
IF([INFERENCE]) WAITFOR DELAY '0:0:[SLEEPTIME]' comment: --
```

Replace [INFERENCE] with conditions like 'ASCII(SUBSTRING((SELECT TOP 1 name FROM sys.databases),1,1))>64' to check character values, and [SLEEPTIME] with '0:0:5' for shorter tests. Iterate through possibilities (e.g., binary search on ASCII values) and send requests sequentially, noting delays for 'true' conditions.

**Expected Output**: Delayed responses (e.g., 5 seconds) when the condition evaluates to true, allowing reconstruction of data like database names or passwords.

### Step 4: Extract Sensitive Data and Verify

**Context**: Chain inferences to pull full data sets, such as user tables, and validate extracted information.

Expand conditions to query tables like 'SELECT username FROM users WHERE id=1', using SUBSTRING and ASCII to extract character-by-character. Automate with scripts if manual timing is tedious, but manually verify key extractions.

**Expected Output**: Reconstructed strings from delay patterns, e.g., a username 'admin' inferred over multiple requests.

**Success Indicators**:
- Consistent delays matching expected sleep times.
- Accurate data reconstruction without application crashes.
- No WAF blocks or IP bans during testing.
