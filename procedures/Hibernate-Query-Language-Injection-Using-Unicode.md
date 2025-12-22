---
id: 10d8f2b2-9076-4389-b2b0-8bfec3d84bde
name: Hibernate-Query-Language-Injection-Using-Unicode
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.408822+00:00'
updated_at: '2023-04-10T20:22:25.393338+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Public-Facing Application|T1190 - Exploitation
    of Public-Facing Application]]
sub_techniques: []
tags:
  - '[[tags/HQL Injection]]'
  - '[[tags/Unicode]]'
  - '[[tags/SQL Injection]]'
commands:
  - '[[commands/sql-len-subquery-length]]'
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Hibernate-Query-Language-Injection-Using-Unicode

## Summary

This procedure demonstrates how to exploit Hibernate Query Language (HQL) injection vulnerabilities in Java applications by using Unicode encoding to bypass input validation, allowing execution of arbitrary SQL commands through the underlying database, such as Microsoft SQL Server.

## Description

Hibernate is an Object-Relational Mapping (ORM) framework for Java that translates HQL queries into SQL. Vulnerabilities arise when user input is directly concatenated into HQL without proper sanitization, enabling injection attacks. This technique leverages Unicode characters, like the non-breaking space (U+00A0), to evade trimming or filtering mechanisms that might strip standard whitespace. Attackers can inject payloads to manipulate queries, extract data, or execute commands. The target is typically a web application exposing HQL-driven endpoints, such as search or login forms. Success depends on the application's query construction and database backend.

## Requirements

1. Access to a vulnerable HQL-based web application (e.g., via browser or proxy like Burp Suite).
2. Knowledge of the application's input points (e.g., search fields) that feed into HQL queries.
3. Familiarity with SQL syntax for the backend database (e.g., Microsoft SQL Server).
4. Tools for testing injections, such as a web proxy or SQL client.

## Defense

- Implement strict input validation and sanitization, rejecting or escaping special characters including Unicode.
- Use parameterized HQL queries or Hibernate's Criteria API to bind user input safely.
- Apply web application firewalls (WAFs) to detect injection patterns.
- Regularly audit and patch Hibernate and application code for known vulnerabilities.
- Enable database logging to monitor anomalous queries.

## Objectives

1. Identify injectable HQL parameters in the application.
2. Bypass validation using Unicode-encoded payloads to execute arbitrary SQL.
3. Extract sensitive data or manipulate database contents.
4. Achieve unauthorized access or data exfiltration.

## Instructions

### Step 1: Test Basic Subquery Length

**Context**: Begin by verifying the ability to execute a simple subquery within a length function to confirm injection feasibility. This helps gauge if the HQL layer allows nested SQL without immediate error.

**Command** ([[commands/sql-len-subquery-length]]):
```sql
SELECT LEN((SELECT(1)))
```

> This command executes a subquery returning 1 and measures its string length, expecting output of 1. If successful, it indicates the injection point allows SQL execution. Use this in the application's input field, e.g., appending to a WHERE clause like 'name' = 'test' AND (injected payload).

### Step 2: Inject Unicode to Bypass Trimming

**Context**: Use Unicode non-breaking spaces to prevent the database from trimming injected code, allowing malformed but executable queries. This step tests evasion of basic filters.

**Code** ([[codes/sql-unicode-len-select-statement]]):
```sql
SELECT LEN([U+00A0](select[U+00A0](1))
```

> Inject this into the HQL parameter. The U+00A0 characters act as invisible separators, bypassing whitespace filters. Expected output is the length of the subquery string (around 10 characters). Monitor for errors; success shows the query executes despite encoding.

### Step 3: Craft Malicious Injection Payload

**Context**: Build a full injection to extract data, such as user information, by combining conditions that always evaluate to true while appending data-retrieval logic. This exploits the HQL-to-SQL translation for lateral data access.

**Command** ([[commands/sql-len-subquery-length]]):
```sql
SELECT * FROM hqli.persistent.Post WHERE name = 'dummy' AND LEN((SELECT TOP 1 name FROM users)) > 1 AND '1'='1'
```

> Adapt this to the target: Replace 'hqli.persistent.Post' with the actual entity. The always-true condition ('1'='1') ensures results, while LEN probes user data length. Expected output includes posts plus leaked user names if vulnerable. Iterate to extract full data by adjusting subqueries (e.g., UNION SELECT for concatenation).
