---
type: code
language: php
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - web
tags:
  - vulnerable-code
  - sql-injection
validated: true
---

# vulnerable-php-md5-raw-auth-query

## Code

```php
"SELECT * FROM admin WHERE pass = '".md5($password,true)."'"
```

## Description

This PHP code snippet represents a vulnerable SQL query in a login script that inserts a raw (binary) MD5 hash of the user password directly into the query string without escaping or parameterization. This allows binary output to inject SQL code, enabling authentication bypass.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $password | User-supplied password input | ffifdyop |

## Usage

This is typically found in legacy PHP authentication scripts. Attackers exploit by providing a $password whose md5(true) binary equals bytes like 0x27204f5227323d3127 ("' OR '1'='1"). Submit via POST to the login endpoint to bypass.

## Detection

- Review source code for direct hash insertion in SQL.
- Monitor database logs for queries with binary data in WHERE clauses.
- WAF rules for SQLi in password fields; anomalous login successes.

## Related

- [[procedures/SQL-Injection-Authentication-Bypass-Using-Raw-MD5-and-SHA1-Hashes]]
- [[commands/calculate-md5-sha1-raw-hashes-php]]
