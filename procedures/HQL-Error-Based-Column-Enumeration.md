---
type: procedure
description: >-
  Enumerate database column names in a Hibernate-based application by inducing
  an SQL grammar exception through HQL injection.
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.286526+00:00'
updated_at: '2023-04-10T20:22:26.594989+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/HQL Injection]]'
  - '[[tags/Database Enumeration]]'
  - '[[tags/Error-Based Injection]]'
commands: []
platforms:
  - Web
  - Java
tools: []
validated: true
---

# HQL-Error-Based-Column-Enumeration

## Summary

HQL Error-Based Column Enumeration is a technique to extract database schema information from applications using Hibernate Query Language (HQL) by injecting payloads that trigger SQL grammar exceptions. This reveals the underlying column names in the SELECT clause of the generated SQL query, allowing attackers to map the database structure for further exploitation such as data extraction or privilege escalation.

## Description

This procedure targets web applications built with Java and Hibernate ORM where user inputs are concatenated into HQL queries without proper parameterization, leading to injection vulnerabilities. By injecting a reference to a non-existent column, an org.hibernate.exception.SQLGrammarException is triggered, and the error message often includes the full SQL statement executed by the database, leaking column names from the target table. This is particularly useful in black-box testing scenarios where direct database access is unavailable. The technique assumes the application exposes an input field (e.g., search or filter) that influences an HQL query like 'from BlogPosts where title like \'%search_term%\' and published = true'. Success depends on error messages being verbose and not sanitized.

## Requirements

1. Access to a web application endpoint vulnerable to HQL injection, such as a search form or list view parameter.
2. Knowledge of the base HQL query structure or table name (e.g., via error messages or source code leaks).
3. A proxy tool like Burp Suite to intercept and modify requests, though manual form submission may suffice.
4. Understanding of SQL/HQL syntax to craft payloads that cause syntax errors without breaking the query entirely.

## Defense

- Use parameterized HQL queries or Criteria API in Hibernate to bind user inputs safely, preventing injection.
- Implement input validation and sanitization to reject suspicious patterns like comments (-- ) or invalid identifiers.
- Configure Hibernate to suppress detailed SQL errors in production (e.g., set hibernate.show_sql=false and handle exceptions gracefully).
- Employ web application firewalls (WAFs) to detect and block injection attempts based on payload signatures.
- Regularly audit and update Hibernate and application dependencies to mitigate known vulnerabilities.

## Objectives

1. Identify and confirm an HQL injection point in the application.
2. Induce a database error to leak column names from the target table.
3. Map the database schema for subsequent attacks like data exfiltration or union-based injections.

## Instructions

### Step 1: Identify the Vulnerable Input Point

**Context**: Locate an application feature that accepts user input likely translated to an HQL WHERE clause, such as a search field for blog posts. Test for injection by appending a single quote (') to the input and observing if it causes a syntax error, indicating unparameterized queries.

Submit a test input like 'search_term' in the title search field and inspect the response for any database-related errors.

**Expected Output**: Normal results if no injection, or a partial syntax error if vulnerable.

### Step 2: Craft and Inject the Error-Inducing Payload

**Context**: Construct a payload that references a non-existent column to trigger a SQLGrammarException. This forces Hibernate to reveal the full SELECT statement in the error, listing all selected columns. Use the HQL injection payload to append to the existing query.

Inject the following payload into the vulnerable parameter (e.g., title search field):

**Code** ([[codes/HQL-Error-Inducing-Payload-for-Column-Enumeration]]):

```sql
and DOESNT_EXIST=1 and ''='%' -- 
```

The full injected query might appear as:

```sql
from BlogPosts
where title like '%search_term%'
  and DOESNT_EXIST=1 and ''='%' -- 
  and published = true
```

Submit the request via the application form or proxy.

**Expected Output**: An error page or response containing an org.hibernate.exception.SQLGrammarException with the expanded SQL statement, such as:

```
org.hibernate.exception.SQLGrammarException: Column "DOESNT_EXIST" not found; SQL statement:
      select blogposts0_.id as id21_, blogposts0_.author as author21_, blogposts0_.promoCode as promo3_21_, blogposts0_.title as title21_, blogposts0_.published as published21_ from BlogPosts blogposts0_ where blogposts0_.title like '%' or DOESNT_EXIST='%' and blogposts0_.published=1 [42122-159]
```

This leaks columns: id, author, promoCode, title, published.

### Step 3: Analyze the Error Output and Verify Columns

**Context**: Parse the error message to extract column names. Verify by crafting follow-up queries using the discovered columns to confirm the schema and test for further injections (e.g., union select).

Review the exception details for the SELECT clause and list the columns. If the error is suppressed, try variations like using 'or' instead of 'and' or different invalid references.

**Expected Output**: A documented list of column names (e.g., id, author, promoCode, title, published) that can be used in subsequent attacks.

**Success Indicators**:
- Error message includes the full SQL with column aliases (e.g., id21_, author21_).
- No application crash; query partially executes to reveal structure.
- Discovered columns match expected table schema upon verification.
