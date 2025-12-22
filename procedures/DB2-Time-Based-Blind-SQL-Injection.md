---
id: 1bbe4a87-4876-4915-85de-85aff964c649
name: DB2-Time-Based-Blind-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.094963+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - db2
  - sqli
  - blind-sqli
  - time-based
commands: []
platforms:
  - Web
  - Database
tools: []
validated: true
---

# DB2-Time-Based-Blind-SQL-Injection

## Summary

This procedure demonstrates how to perform time-based blind SQL injection on IBM DB2 databases to extract sensitive information, such as database user details, without relying on error messages or visible output. By injecting payloads that cause conditional delays through resource-intensive queries, attackers can infer data based on response times.

## Description

Time-based blind SQL injection exploits vulnerabilities in web applications connected to DB2 databases where user input is not properly sanitized, allowing arbitrary SQL execution. Unlike union-based or error-based SQLi, blind variants return no direct data; instead, this technique uses timing differences to deduce information. In DB2, since there is no built-in SLEEP function, delays are achieved via heavy computations, such as cross-joins on system tables like sysibm.columns, which consume CPU and slow responses when a condition is true. This procedure targets extraction of simple data like the current database user by testing ASCII values through boolean conditions. It assumes a reflected or time-measurable injection point, such as a search parameter in a web form. Success depends on consistent baseline response times and the ability to measure delays (e.g., >5 seconds for true conditions).

## Requirements

1. Access to a web application vulnerable to SQL injection with a DB2 backend (e.g., unparameterized queries in PHP/JSP).
2. Tools for intercepting and modifying HTTP requests, such as a proxy (Burp Suite or similar).
3. Ability to measure response times accurately (e.g., via scripting or manual timing).
4. Knowledge of the injection point (e.g., GET/POST parameter) and basic SQL syntax for DB2.
5. Network access to the target application without WAF blocking timing anomalies.

## Defense

- Use prepared statements and parameterized queries to separate code from user input.
- Implement web application firewalls (WAFs) with SQLi rules that detect anomalous query patterns or timing attacks.
- Enable database logging for long-running queries and monitor for resource-intensive operations like cross-joins on system tables.
- Apply input validation, escaping, and least-privilege database accounts to limit query impact.
- Use rate limiting on endpoints to disrupt timing-based inference.

## Objectives

1. Confirm the presence of a time-based blind SQL injection vulnerability in a DB2-backed application.
2. Extract sensitive database information, such as the current user or version, via conditional timing delays.
3. Bypass basic defenses relying on quick responses or error suppression.

## Instructions

### Step 1: Identify and Confirm Injection Point

**Context**: Locate a parameter vulnerable to SQL injection (e.g., a search field) and confirm it's a blind boolean-based point by testing simple conditions that alter response without errors. This step verifies DB2 as the backend via timing or subtle differences.

Navigate to the target application and input a basic payload like ' OR 1=1 -- to check for boolean logic. Then test a false condition like ' OR 1=2 --. Measure baseline response times (e.g., using browser dev tools or a proxy). If responses differ slightly but no data leaks, proceed to time-based tests.

**Expected Output**: Consistent fast responses for false conditions (~1-2 seconds) and potential delays for true ones when using heavy queries.

### Step 2: Test Time-Based Delay with Sample Payload

**Context**: Inject a payload that causes a delay only if a known true condition holds, using a resource-heavy query to simulate sleep. This confirms the vulnerability by observing extended response times.

Use a proxy to intercept the request and append the payload to the vulnerable parameter. Reference the delay-inducing code from [[codes/DB2-Time-Delay-Payload-for-Blind-SQL-Injection]] and inject it as:

```sql
' and (SELECT count(*) from sysibm.columns t1, sysibm.columns t2, sysibm.columns t3)>0 and 1=1 --
```

Submit the request and time the response. For a false condition, replace 1=1 with 1=2.

**Expected Output**: Delayed response (>5-10 seconds) for true conditions due to the cross-join computation; quick response for false.

### Step 3: Extract Data Using Conditional Timing

**Context**: Systematically extract information by varying the boolean condition to guess values (e.g., ASCII characters). Start with the current database user by testing the first character's ASCII value from 32 to 126.

Modify the payload to target specific data. For extracting the first character of the current user (e.g., if it's 'D' with ASCII 68):

Use the code from [[codes/DB2-Time-Delay-Payload-for-Blind-SQL-Injection]]:

```sql
' and (SELECT count(*) from sysibm.columns t1, sysibm.columns t2, sysibm.columns t3)>0 and (select ascii(substr(user,1,1)) from sysibm.sysdummy1)=68 --
```

Submit payloads incrementing the number (e.g., =65 for 'A', =66 for 'B', etc.). A delay indicates a match.

For subsequent characters, adjust substr(user,2,1), etc. Use binary search (e.g., test >64 vs. <64) to speed up guessing.

**Expected Output**: Delays on matching conditions, allowing reconstruction of the user string (e.g., 'DB2ADMIN').

### Step 4: Verify and Expand Extraction

**Context**: Once basic extraction works, validate the data and attempt broader queries (e.g., database version or table names) while monitoring for detection.

Test a known value like database version: (select ascii(substr(dbmsinfo('dbname'),1,1)) from sysibm.sysdummy1)=XX. If successful, chain to extract full strings or enumerate schema.

Automate with scripts if manual timing is tedious, but manually confirm to avoid noise.

**Expected Output**: Accurate data extraction without triggering alerts; full user or schema details inferred from multiple timed requests.
