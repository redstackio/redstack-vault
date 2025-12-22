---
id: 17cb6090-edaa-41bc-8f7e-78139aefd3af
name: MySQL-Union-Based-Column-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.235644+00:00'
updated_at: '2023-04-10T20:22:49.030437+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploitation of Remote
    Services]]
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques: []
tags:
  - '[[tags/Detect columns number]]'
  - '[[tags/MYSQL Injection]]'
  - '[[tags/MYSQL Union Based]]'
  - '[[tags/Using order by or group by]]'
commands: []
platforms:
  - Web
  - MySQL
tools: []
validated: true
---

# MySQL-Union-Based-Column-Enumeration

## Summary

MySQL Union Based Column Enumeration is a SQL injection technique used to determine the number of columns in a vulnerable database query. By injecting UNION SELECT statements with incremental column counts and using ORDER BY or GROUP BY clauses to probe for errors, attackers can map the query structure without direct access to schema information. This procedure is essential during database reconnaissance to prepare for data extraction or further exploitation.

## Description

This technique exploits a SQL injection vulnerability in a web application connected to a MySQL database. Attackers append payloads to user input fields (e.g., search boxes, login forms) that manipulate the original SELECT query. The ORDER BY clause tests column counts by sorting results; an error indicates exceeding the actual count. Similarly, GROUP BY groups results by column position, failing when columns are mismatched. Once the column count is confirmed, a UNION SELECT can inject custom data to verify compatibility and begin extracting information like database names or table structures. This is typically used in the reconnaissance phase to understand the backend database layout, enabling targeted attacks such as data exfiltration. The procedure assumes a blind or error-based SQLi vulnerability where error messages or response differences reveal success/failure.

## Requirements

1. A vulnerable web application with SQL injection in a GET or POST parameter connected to MySQL.
2. Basic knowledge of SQL syntax and injection payloads.
3. Tools for sending HTTP requests (e.g., browser, Burp Suite) to test payloads.
4. Ability to observe application responses for errors or behavioral changes.

## Defense

- Implement strict input validation and parameterized queries (e.g., using prepared statements in application code) to prevent injection.
- Use web application firewalls (WAFs) to detect and block common SQLi patterns like UNION SELECT or ORDER BY clauses.
- Limit database user privileges to read-only where possible and monitor query logs for anomalous GROUP BY or ORDER BY usage.
- Enable MySQL error logging and application-level logging to identify injection attempts.

## Objectives

1. Determine the exact number of columns in the vulnerable SQL query.
2. Confirm query compatibility for UNION-based data extraction.
3. Identify potential data types through error responses or null injections.

## Instructions

### Step 1: Probe Column Count Using ORDER BY

**Context**: Start by injecting an ORDER BY clause with incremental numbers to find the maximum sortable column. Success returns normal results; failure (error or no change) indicates the column limit. This step isolates the query's column count without altering results.

**Code** ([[codes/MySQL-ORDER-BY-Column-Enumeration-Payload]]):

```sql
1' ORDER BY 1--+    #True
1' ORDER BY 2--+    #True
1' ORDER BY 3--+    #True
1' ORDER BY 4--+    #False - Query is only using 3 columns
                    #-1' UNION SELECT 1,2,3--+    True
```

> Inject the payload into the vulnerable parameter (e.g., ?id=1' ORDER BY N--+). Increment N until an error occurs. The last successful N is the column count. Follow up with a UNION SELECT using that count to confirm (e.g., replace 1 with NULL or a string to test types). Expected output: Normal page for valid N, SQL error or blank response for invalid N.

### Step 2: Verify Column Count Using GROUP BY

**Context**: Use GROUP BY as an alternative probe if ORDER BY is filtered. It groups results by column position, failing similarly on excess columns. This provides a secondary confirmation and bypasses potential WAF rules targeting ORDER BY.

**Code** ([[codes/MySQL-GROUP-BY-Column-Enumeration-Payload]]):

```sql
1' GROUP BY 1--+    #True
1' GROUP BY 2--+    #True
1' GROUP BY 3--+    #True
1' GROUP BY 4--+    #False - Query is only using 3 columns
                    #-1' UNION SELECT 1,2,3--+    True
```

> Append the payload to the parameter (e.g., ?id=1' GROUP BY N--+). Test incrementally as with ORDER BY. The syntax allows grouping by multiple columns (e.g., GROUP BY 1,2), but single-column probes suffice for enumeration. Expected output: Aggregated or normal results for valid N, error for invalid. Use this to cross-verify the ORDER BY findings before proceeding to UNION injection.
