---
id: e98960c3-c4e4-4c2c-aff1-a93cccbe76ba
name: MySQL-Column-Detection-via-Order-By-or-Group-By
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.268884+00:00'
updated_at: '2023-04-10T20:22:54.543285+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/detect-columns-number]]'
  - '[[tags/mysql-injection]]'
  - '[[tags/mysql-union-based]]'
  - '[[tags/using-order-by-or-group-by]]'
  - '[[tags/using-order-by-or-group-by-error-based]]'
commands:
  - '[[codes/mysql-group-by-column-detection]]'
  - '[[commands/mysql-union-select-column-test]]'
platforms:
  - Web
  - MySQL
tools: []
validated: true
---

# MySQL-Column-Detection-via-Order-By-or-Group-By

## Summary

This procedure exploits SQL injection vulnerabilities in MySQL databases to determine the number of columns in a target table using ORDER BY or GROUP BY clauses. By injecting these clauses and observing error messages, an attacker can identify the column count, enabling subsequent attacks like UNION-based data extraction.

## Description

In a typical SQL injection scenario, an attacker targets a vulnerable web application parameter that is concatenated into a backend MySQL query without proper sanitization. By appending ORDER BY or GROUP BY clauses followed by incremental column numbers, the attacker triggers errors when referencing non-existent columns. The point at which the error occurs reveals the exact number of columns. This information is crucial for crafting effective UNION SELECT payloads to exfiltrate data. The procedure assumes an authenticated or unauthenticated injection point, such as a search field or URL parameter, and works in error-based SQL injection contexts where database errors are reflected in responses.

## Requirements

1. Access to a web application with a confirmed SQL injection vulnerability in a MySQL backend.
2. Knowledge of the injection point (e.g., GET/POST parameter).
3. Tools for sending HTTP requests, such as a browser, curl, or Burp Suite.
4. Ability to observe error messages in HTTP responses.

## Defense

- Implement input validation and sanitization to strip or escape SQL keywords like ORDER BY and GROUP BY.
- Use parameterized queries or prepared statements to separate SQL code from user input.
- Configure the database to suppress detailed error messages, using generic error pages instead.
- Employ web application firewalls (WAFs) to detect and block anomalous SQL patterns.

## Objectives

1. Determine the number of columns in the vulnerable query's SELECT statement.
2. Validate the injection point supports error-based techniques.
3. Prepare for advanced exploitation, such as UNION-based data retrieval.

## Instructions

### Step 1: Test ORDER BY for Column Detection

**Context**: Append an ORDER BY clause with incrementally increasing column numbers to the injection point. MySQL will return an error like "Unknown column 'N' in 'order clause'" when the number exceeds the actual columns, indicating the column count is N-1.

**Code** ([[codes/mysql-order-by-column-detection]]):

Use the following SQL payload, adjusting the injection point (e.g., via URL parameter like ?id=1' ORDER BY ...).

**Command** ([[codes/mysql-order-by-column-detection]]):

Inject the payload into the vulnerable parameter and observe the response.

```sql
1' ORDER BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100--+
```

> Start with small numbers (e.g., ORDER BY 1) and increase until an error occurs. For example, if an error appears at column 4, the query has 3 columns. Expected output includes the error message confirming the unknown column.

### Step 2: Test GROUP BY for Column Detection

**Context**: Similar to ORDER BY, inject a GROUP BY clause with column numbers. MySQL errors on non-existent columns with messages like "Unknown column 'N' in 'group statement'", revealing the structure.

**Code** ([[codes/mysql-group-by-column-detection]]):

Inject this payload into the vulnerable parameter.

**Command** ([[codes/mysql-group-by-column-detection]]):

```sql
1' GROUP BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100--+
```

> Increment the column numbers until an error is triggered. The error message will specify the invalid column, allowing deduction of the total columns. This method works if the query context supports GROUP BY.

### Step 3: Verify with UNION SELECT

**Context**: Once the column count is known (e.g., 3), test a basic UNION SELECT to confirm exploitability and prepare for data extraction.

**Command** ([[commands/mysql-union-select-column-test]]):

```sql
1' UNION SELECT 1,2,3--+
```

> Inject this payload. If successful, the response should display the literal values 1,2,3 without errors, indicating the injection is viable for further exploitation like database name or table enumeration.
