---
type: procedure
description: >-
  Perform boolean-based SQL injection on a SQLite database to determine the
  number of user tables by querying sqlite_master and using threshold
  comparisons.
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sqli
  - sqlite
  - boolean-based
  - database-enumeration
commands:
  - '[[commands/curl-boolean-sqli-injection]]'
tools:
  - '[[tools/sqlmap]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Count-Tables-in-SQLite-Database-via-Boolean-Injection

## Summary

This procedure outlines a boolean-based SQL injection technique to count the number of user tables in a SQLite database. By injecting a crafted SQL payload into a vulnerable web application parameter, an attacker can query the sqlite_master table to compare the table count against a threshold value, enabling a binary search to determine the exact number of tables. This is useful for database reconnaissance in web applications using SQLite as the backend.

## Description

SQLite databases store metadata about their structure in the sqlite_master table, including user-created tables (excluding system tables like those starting with 'sqlite_'). Boolean-based SQL injection exploits unsanitized user input in web applications to force conditional responses (e.g., true/false based on page content or timing). The payload checks if the count of user tables is less than a specified number, returning a boolean result via the application's response.

To count tables, perform a binary search: start with a high threshold (e.g., 1000), inject the payload, and observe if the condition is true (count < threshold). Halve the threshold iteratively until the exact count is isolated. This technique assumes a blind injection point where direct query results are not visible, but boolean outcomes are distinguishable (e.g., login success vs. failure, or page content differences). It maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under tactics TA0001 (Initial Access) and TA0007 (Discovery). Use this in controlled environments like penetration testing; unauthorized use is illegal.

## Requirements

1. Access to a web application with a vulnerable SQL injection point (e.g., GET/POST parameter in login, search, or ID fields) connected to a SQLite database.
2. Ability to distinguish boolean responses (e.g., via different HTTP responses, page content, or timing).
3. Tools for crafting and sending requests, such as curl for manual injection or Burp Suite/sqlmap for automation.
4. Knowledge of the injection syntax for the target (e.g., appending to a WHERE clause like ' OR [payload] --).

## Defense

- Implement prepared statements or parameterized queries to separate SQL code from user input.
- Use input validation and sanitization to reject or escape special characters (e.g., quotes, operators).
- Employ web application firewalls (WAFs) to detect and block injection patterns.
- Regularly audit database logs for anomalous queries and enable query logging in SQLite.
- Limit database privileges to least necessary and avoid exposing error messages that leak schema info.

## Objectives

1. Determine the exact number of user tables in the SQLite database.
2. Confirm the presence of a boolean-based SQL injection vulnerability.
3. Gather intelligence for further enumeration (e.g., table names via similar injections).
4. Assess the database structure without direct query access.

## Instructions

### Step 1: Identify and Confirm the Injection Point

**Context**: Locate a parameter vulnerable to SQL injection and confirm it accepts boolean conditions. This step ensures the payload can be injected without breaking the query syntax.

Test basic injection by appending a tautology like ' OR 1=1 -- to the parameter and observe if the response changes (e.g., bypasses authentication or alters output).

Use [[commands/curl-boolean-sqli-injection]] for testing:

```bash
curl "http://target.com/vulnerable?param=' OR 1=1 --" -v
```

> This command sends a request with a basic tautology. A successful injection typically results in an altered response, such as successful login or full result set, confirming the vulnerability.

### Step 2: Inject the Boolean Payload for Table Count

**Context**: Append the boolean payload to query the table count. Replace 'number_of_table' in the payload with your test threshold (start high, e.g., 1024, for binary search).

Reference the payload [[codes/SQLite-Count-Tables-Boolean-Payload]] and inject it into the vulnerable parameter, e.g., param=' OR [payload] --.

Use [[commands/curl-boolean-sqli-injection]] to send the request:

```bash
curl "http://target.com/vulnerable?param=' OR and (SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ) < 100 --" -v
```

> If the count is less than 100, the boolean condition is true, and the response should match the 'true' case (e.g., login success). If false, the count is 100 or higher. Adjust the threshold and repeat.

### Step 3: Perform Binary Search to Find Exact Count

**Context**: Iteratively refine the threshold to pinpoint the exact number of tables. This step leverages the boolean responses from previous injections.

Start with low=0, high=1024. Calculate mid=(low+high)/2, inject with < mid, and adjust: if true, high=mid; if false, low=mid+1. Repeat until low == high.

For each iteration, use [[commands/curl-boolean-sqli-injection]] with the updated threshold:

```bash
curl "http://target.com/vulnerable?param=' OR and (SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ) < 50 --" -v
```

> Success is indicated when the search converges (e.g., after ~10 iterations for <1024 tables). The final low value is the count. Log responses to track flips in boolean outcomes.

### Step 4: Automate with sqlmap (Optional)

**Context**: For efficiency, use sqlmap to automate detection and enumeration if manual injection is tedious.

Install and run sqlmap with SQLite-specific options to count tables directly.

> Sqlmap will fingerprint the DBMS, confirm injection, and output the table count without manual binary search. Expected: 'available databases [1] [*] sqlite_master' followed by table count.
