---
id: 5e9ea4d2-911d-40c4-95ab-c13e9f472f2c
name: Hibernate-Query-Language-Injection-with-Dollar-Quoted-Strings
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.350777+00:00'
updated_at: '2023-04-10T20:22:28.068938+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/User Execution|T1204 - User Execution]]'
sub_techniques: []
tags:
  - '[[tags/Dollar-Quoted-Strings]]'
  - '[[tags/Hibernate-Query-Language-Injection]]'
  - injection
  - hql
  - web
commands:
  - '[[commands/curl-hql-injection-test]]'
platforms:
  - Web
  - Java
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
validated: true
---

# Hibernate-Query-Language-Injection-with-Dollar-Quoted-Strings

## Summary

Hibernate Query Language (HQL) Injection with $-quoted strings is a procedure to exploit vulnerabilities in web applications using Hibernate ORM by injecting malicious HQL statements via user inputs. This technique leverages PostgreSQL-style $-quoted strings (e.g., $$) to craft payloads that bypass string escaping, enabling unauthorized data access, privilege escalation, or remote code execution on the backend server.

## Description

Hibernate Query Language (HQL) Injection targets web applications built with Hibernate ORM, where user inputs are improperly concatenated into HQL queries without parameterization. $-quoted strings, a feature borrowed from PostgreSQL, allow delimiters like $$ to enclose multi-line or complex strings without needing to escape single quotes, making it ideal for injecting arbitrary HQL. This can lead to dumping sensitive data (e.g., user credentials), modifying records, or executing system commands if the application has elevated privileges. The attack assumes a public-facing web app with an injectable endpoint like a search or login form. Success depends on the application's query construction and database backend (typically PostgreSQL with Hibernate).

## Requirements

1. Access to a vulnerable web application using Hibernate ORM and a database supporting $-quoted strings (e.g., PostgreSQL).
2. Knowledge of HQL syntax and basic web interception tools.
3. Ability to manipulate HTTP requests (e.g., via proxy or direct API calls).
4. Target endpoint that accepts user input reflected in HQL queries.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to strip or escape special characters like $ and quotes.
- Use parameterized HQL queries or Hibernate's Criteria API to avoid dynamic string building.
- Limit database user privileges to read-only where possible and enable query logging for anomaly detection.
- Deploy Web Application Firewalls (WAFs) tuned for HQL injection patterns, monitoring for unusual query lengths or $ delimiters.

## Objectives

1. Confirm HQL injection vulnerability in the target application.
2. Inject $-quoted strings to bypass filters and execute arbitrary HQL.
3. Extract sensitive data or achieve code execution on the server.
4. Escalate privileges using the injected access.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate an input field (e.g., search box or login form) where user data is directly inserted into HQL queries. Use a proxy to inspect requests and responses for database error messages indicating HQL usage.

**Tool**: [[tools/Burp-Suite]]

Intercept traffic to the target endpoint and submit a test input like "test" to observe if responses leak HQL errors (e.g., "org.hibernate.hql.internal.ast.QuerySyntaxException").

### Step 2: Test for Basic Injection

**Context**: Probe for injection by closing the expected string in the HQL query with a single quote, causing a syntax error if vulnerable. This confirms the input is unescaped.

**Command** ([[commands/curl-hql-injection-test]]):
```bash
curl -X POST -d "search='" http://target.example.com/search -H "Content-Type: application/x-www-form-urlencoded"
```

> This sends a single quote payload to trigger an HQL syntax error. Look for stack traces mentioning Hibernate or HQL in the response, indicating vulnerability.

### Step 3: Inject $-Quoted String Payload

**Context**: Once confirmed, craft a payload using $$ to delimit an injected HQL query. For example, close the original string and append a union-like select to dump data, bypassing quote escaping.

**Command** ([[commands/curl-hql-injection-test]]):
```bash
curl -X POST -d "search=\' || $$select username, password from users$$ --" http://target.example.com/search -H "Content-Type: application/x-www-form-urlencoded"
```

> The payload \' closes the original string, then $$select username, password from users$$ injects a query to exfiltrate data. Adjust based on the exact HQL structure (e.g., from Entity classes). Expected output includes leaked data in the response or error.

### Step 4: Escalate to Code Execution

**Context**: If data access succeeds, extend the injection to execute system commands via HQL functions or if the app allows (e.g., injecting into a query that runs OS commands through JDBC). Verify success by checking for command output in responses.

Use Burp Suite to iterate payloads, such as injecting $$exec('whoami')$$ if supported, and monitor for privilege escalation indicators like admin data access.
