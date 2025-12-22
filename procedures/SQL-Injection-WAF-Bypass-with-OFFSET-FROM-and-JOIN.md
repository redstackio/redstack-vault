---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - sql-injection
  - waf-bypass
commands:
  - '[[commands/sql-limit-to-offset-bypass]]'
  - '[[commands/sql-substr-from-for-bypass]]'
  - '[[commands/sql-union-select-with-joins-bypass]]'
platforms:
  - Web
tools: []
verified: true
validated: true
---

# SQL-Injection-WAF-Bypass-with-OFFSET-FROM-and-JOIN

## Summary

This procedure outlines techniques to bypass Web Application Firewalls (WAFs) during SQL Injection (SQLi) attacks by rewriting common SQL clauses. Specifically, it replaces comma-separated LIMIT and SUBSTR syntax with OFFSET/FROM alternatives and simulates multi-column UNION SELECT using nested JOINs, evading signature-based detection while maintaining query functionality for data exfiltration.

## Description

SQL Injection exploits unsanitized user input to inject malicious SQL into database queries, potentially leading to data leakage or system compromise. WAFs often detect patterns like commas in functions (e.g., SUBSTR('x',1,1)) or standard UNION SELECT clauses. This procedure uses MySQL-compatible alternatives: 'LIMIT n OFFSET m' instead of 'LIMIT m,n'; 'SUBSTR(string FROM pos FOR len)' instead of comma-based; and 'UNION SELECT * FROM (subqueries) JOIN' to avoid direct column lists. Applicable in union-based SQLi scenarios on public-facing web apps. Success enables extraction of sensitive data like user credentials without triggering alerts. Target environments include PHP/MySQL applications with weak input validation.

## Requirements

1. Access to a web application with a confirmed SQLi vulnerability (e.g., via ' or 1=1-- payloads)
2. Knowledge of the database schema and query structure (e.g., number of columns in original SELECT)
3. Proxy tool like Burp Suite for intercepting and modifying requests
4. Basic SQL proficiency to adapt payloads to the injection point

## Defense

- Use prepared statements and parameterized queries in application code to neutralize injected SQL
- Deploy WAFs with machine learning-based anomaly detection, not just static signatures
- Enable comprehensive logging of database queries and web traffic for anomaly hunting
- Conduct regular code reviews and vulnerability scans for SQLi entry points

## Objectives

1. Construct WAF-evading SQLi payloads using alternative syntax
2. Maintain query functionality for data enumeration and exfiltration
3. Verify bypass success through successful data retrieval without blocks

## Instructions

### Step 1: Replace LIMIT Clause to Avoid Commas

**Context**: WAFs may flag comma-separated LIMIT offsets (e.g., LIMIT 0,1). Rewrite as LIMIT with OFFSET to fetch the first row without triggering rules. Use this in union-based payloads to control result sets.

**Command** ([[commands/sql-limit-to-offset-bypass]]):
```sql
LIMIT 1 OFFSET 0
```

> Append this to your base SQLi payload after matching the original query's column count. Why: OFFSET avoids comma detection while preserving pagination logic. Expected: Query returns the first result row; no WAF alert in proxy logs.

### Step 2: Rewrite SUBSTR Function with FROM and FOR

**Context**: Comma-based substring extraction (e.g., SUBSTR('x',1,1)) is a common WAF signature. Use the alternative FROM/FOR syntax to extract characters for blind SQLi or data encoding, bypassing comma filters.

**Command** ([[commands/sql-substr-from-for-bypass]]):
```sql
SUBSTR('SQL' FROM 1 FOR 1)
```

> Integrate into conditional payloads like IF(SUBSTR(password FROM 1 FOR 1)='a',1,0). Why: FROM/FOR clauses restructure the function call to evade pattern matching. Expected: Returns 'S' (first character); successful in time-based or boolean blind SQLi without blocking.

### Step 3: Simulate UNION SELECT with Nested JOINs

**Context**: Direct 'UNION SELECT 1,2,3,4' may be blocked due to column commas. Use subqueries joined together to create equivalent multi-column output, allowing data dumping from other tables.

**Command** ([[commands/sql-union-select-with-joins-bypass]]):
```sql
UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT 3)c JOIN (SELECT 4)d
```

> Match the number of JOINs to the required columns (e.g., 4 here). Why: JOINs nest selections without explicit comma-separated values, dodging UNION signatures. Expected: Returns a row with values 1,2,3,4; use in payloads like ' UNION SELECT username,password,null,null FROM users -- to exfiltrate data.

### Step 4: Test and Chain Bypasses in Full Payload

**Context**: Combine techniques in a complete injection. Start with a basic union payload and iteratively apply bypasses if blocked.

**Instructions**: Intercept a request in Burp, inject at the vulnerable parameter (e.g., id=1' [payload] --). If blocked, replace elements step-by-step. Verify by observing response changes.

> Example full payload: ' UNION SELECT * FROM (SELECT username)a JOIN (SELECT password)b -- LIMIT 1 OFFSET 0. Expected: Database dumps sensitive data in the app response; check for errors or truncated output indicating partial success.
