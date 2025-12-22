---
id: ffb03725-82af-4281-ba3a-c1aeb92d0314
name: mysql-time-based-blind-injection-using-sleep-subselect
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.694624+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/MySQL Injection]]'
  - '[[tags/Time-Based Blind SQLi]]'
  - '[[tags/Sleep Subselect]]'
commands:
  - '[[commands/mysql-confirm-time-delay-injection]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# mysql-time-based-blind-injection-using-sleep-subselect

## Summary

This procedure demonstrates a time-based blind SQL injection attack on a MySQL database using the SLEEP function within a subselect clause. It allows attackers to extract sensitive information, such as database names, table structures, and credentials, by inferring data through response delays rather than direct output, making it effective against applications that suppress error messages or visible results.

## Description

Time-based blind SQL injection exploits vulnerable input parameters in web applications that interact with a MySQL backend, where the application does not return database errors or data directly. By injecting a subselect containing SLEEP(10), the query execution is delayed by 10 seconds if the condition is true, allowing the attacker to deduce information bit by bit using boolean logic and pattern matching with LIKE operators. This technique is particularly useful in black-box scenarios where only timing differences (e.g., via proxy tools like Burp Suite) indicate success. The target environment is typically a web application with unsanitized user inputs passed to SQL queries, such as search fields or ID parameters. Prerequisites include identifying the injection point through error-based or boolean-based tests. Successful execution can lead to full database enumeration, credential dumping, or further lateral movement within the network.

## Requirements

1. Access to a vulnerable web endpoint with a MySQL backend (e.g., GET parameter like ?id=1).
2. A proxy tool like [[tools/Burp-Suite]] or browser developer tools to measure response times accurately.
3. Basic knowledge of SQL syntax and MySQL functions.
4. Patience for manual enumeration or automation tools like sqlmap for scaling.

## Defense

- Implement prepared statements or parameterized queries to separate code from user input.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns and timing delays.
- Enable database logging and monitor for unusual query execution times or SLEEP function usage.
- Conduct regular input validation, escaping, and code reviews for SQL injection vulnerabilities.

## Objectives

1. Confirm the presence of a time-based blind SQL injection vulnerability.
2. Extract database metadata, such as the current database name, character by character.
3. Identify tables and columns containing sensitive data, like passwords.
4. Dump credentials or other data for further exploitation.

## Instructions

### Step 1: Confirm Time-Based Blind Injection

**Context**: Test the vulnerable parameter to verify that a time delay can be induced, confirming the injection point supports subselects with SLEEP. This step establishes the baseline for boolean inference without visible output.

**Command** ([[commands/mysql-confirm-time-delay-injection]]):
```sql
1' AND (SELECT SLEEP(10)) --
```

> Inject this payload into the vulnerable parameter (e.g., ?id=1' AND (SELECT SLEEP(10)) --). Monitor the response time; a delay of approximately 10 seconds indicates successful injection and control over query execution. If no delay occurs, adjust the payload syntax for the specific application (e.g., use # for comment instead of --). This step is crucial to avoid false positives from network latency.

**Expected Output**: Server response delayed by ~10 seconds; no data returned, but timing confirms vulnerability.

### Step 2: Extract Database Name Using LIKE Patterns

**Context**: Use a series of payloads to guess the database name character by character via binary search with LIKE wildcards. Each true condition triggers the SLEEP delay, narrowing down possibilities (e.g., first character 'a' to 'z'). The payloads assume a 5-character database name starting with 's' (adjust based on initial guesses).

**Code** ([[codes/mysql-sleep-subselect-extraction-payloads]]):

> Reference the full set of payloads in the linked code for systematic enumeration. Start with broad patterns like database() like '%' to confirm, then refine with underscores (_) for unknown positions and specific letters. Inject each payload sequentially into the vulnerable parameter, timing responses to build the name (e.g., delay on 's____' confirms first letter 's'). Why this step? It reveals the schema context needed for further discovery without direct queries that might be logged or blocked.

**Expected Output**: Delays on true conditions (e.g., 10s delay for matching patterns), allowing reconstruction of the database name like 'swsomething'.

### Step 3: Enumerate Tables and Columns for Sensitive Data

**Context**: Once the database name is known, query information_schema to find tables and columns (e.g., those containing 'pass' for passwords). Use nested subselects with SLEEP to confirm existence via timing, enabling targeted data extraction.

**Command** ([[commands/mysql-confirm-time-delay-injection]]):
```sql
1' AND (SELECT SLEEP(10) FROM DUAL WHERE (SELECT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND COLUMN_NAME LIKE '%pass%' LIMIT 0,1) LIKE '%') --
```

> Build on the extraction payloads by nesting queries for table_name or column_name. Iterate with LIKE patterns to extract full names. If a delay occurs, the condition is true, confirming the presence of password-related columns. This step transitions from discovery to collection, focusing on high-value targets like user credentials.

**Expected Output**: Timing delays reveal matching tables/columns (e.g., 'users' table with 'password' column), setting up for data dumping in subsequent manual or automated steps.

### Step 4: Verify and Escalate

**Context**: Validate extracted information and prepare for data exfiltration or privilege escalation. If credentials are obtained, test them against the application or related services.

> Use the confirmed database details to craft union-based payloads if possible, or continue time-based extraction for full dumps. Decision point: If delays are inconsistent, switch to automated tools like sqlmap with --technique=T for time-based. Success here enables credential access or lateral movement.
