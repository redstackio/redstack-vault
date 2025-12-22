---
id: ca24626f-c625-494c-a97f-76454d06f2f5
name: SQL-Injection-Admin-Password-Change-via-ON-DUPLICATE-KEY-UPDATE
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.652019+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Public-Facing Application|T1190 - Exploitation
    of Public-Facing Application]]
sub_techniques: []
tags:
  - '[[tags/SQL Injection]]'
  - '[[tags/MySQL]]'
  - '[[tags/ON DUPLICATE KEY UPDATE]]'
  - '[[tags/Password Change]]'
commands:
  - '[[commands/mysql-inject-admin-password-update]]'
platforms:
  - Web
  - MySQL
tools: []
validated: true
---

# SQL-Injection-Admin-Password-Change-via-ON-DUPLICATE-KEY-UPDATE

## Summary

This procedure exploits a SQL injection vulnerability in a web application's user registration or login form to change the administrator's password using MySQL's ON DUPLICATE KEY UPDATE clause. By injecting a crafted SQL payload, the attacker inserts a dummy user record and simultaneously updates the existing admin user's password hash, allowing subsequent authentication with the new password to gain unauthorized admin access.

## Description

SQL injection vulnerabilities occur when user input is not properly sanitized and is directly concatenated into SQL queries. In this scenario, the target web application uses a MySQL database with an INSERT statement for user registration that lacks parameterization. The attacker targets the email and password fields to inject additional SQL that leverages the ON DUPLICATE KEY UPDATE feature. This MySQL-specific syntax checks for duplicate keys (e.g., on the email field) and updates the record instead of inserting a new one. The payload creates a harmless dummy user while overwriting the admin's password with a known hash (e.g., bcrypt of 'qwerty'). This technique assumes the admin email is known or guessable and the database enforces unique emails. Successful execution grants full administrative control of the application, potentially leading to server compromise if the app has elevated privileges. This is commonly used against poorly secured PHP-based web apps with direct SQL queries.

## Requirements

1. Access to a vulnerable web form (e.g., registration or forgot password) that accepts email and password inputs vulnerable to SQL injection.
2. Knowledge of the admin's email address (e.g., 'admin@example.com') and the database structure (e.g., 'users' table with 'email' and 'password' columns).
3. A tool like Burp Suite or a browser to intercept and modify HTTP requests containing the form submission.
4. The password hash format used by the application (e.g., bcrypt) and ability to generate a hash for the desired new password.
5. Network access to the target web application.

## Defense

- Use prepared statements or parameterized queries in all database interactions to prevent injection.
- Implement strict input validation and sanitization, rejecting or escaping special characters like quotes and semicolons.
- Apply the principle of least privilege to database accounts used by the web application, restricting UPDATE operations on sensitive tables.
- Employ a web application firewall (WAF) to detect and block common SQL injection patterns.
- Regularly audit database logs for anomalous queries and enable query logging for monitoring.

## Objectives

1. Exploit SQL injection to modify the admin user's password without direct authentication.
2. Establish a new, known password for the admin account to enable login.
3. Gain administrative access to the web application for further exploitation or persistence.

## Instructions

### Step 1: Identify Vulnerable Input and Confirm Injection

**Context**: Locate the SQL injection point, typically in a user registration form where email and password are submitted via POST. Confirm the vulnerability by injecting a simple test payload like a single quote (') to cause a SQL error, verifying that input is unsanitized.

**Command** ([[commands/mysql-test-sql-injection]]):
```sql
' OR 1=1 --
```

> Submit the test payload in the email field (e.g., email=' OR 1=1 --, password=anything). If successful, the application may return an error or unexpected behavior like bypassing login. This confirms the injection point without altering data.

### Step 2: Generate Password Hash

**Context**: The application likely stores passwords as bcrypt hashes. Use an external tool to generate the hash for your desired new password (e.g., 'qwerty'). This step ensures the injected update uses a valid format.

> Manually compute the bcrypt hash offline using a library or online tool (in a safe environment). For example, bcrypt('qwerty') might produce '$2y$10$examplehashhere'. Replace placeholders in the payload with this hash.

### Step 3: Craft and Inject the Payload

**Context**: Construct the full payload to insert a dummy user and update the admin password. Use the ON DUPLICATE KEY UPDATE to target the admin email. Intercept the form submission with a proxy to modify the POST data.

**Command** ([[commands/mysql-inject-admin-password-update]]):
```sql
INSERT INTO users (email, password) VALUES ("attacker_dummy@example.com", "bcrypt_hash_of_qwerty"), ("admin@example.com", "bcrypt_hash_of_qwerty") ON DUPLICATE KEY UPDATE password="bcrypt_hash_of_qwerty" --
```

> Embed this SQL in the vulnerable input field, closing the original query properly. For a registration form, set email to: `attacker_dummy@example.com", "bcrypt_hash_of_qwerty"), ("admin@example.com", "bcrypt_hash_of_qwerty") ON DUPLICATE KEY UPDATE password="bcrypt_hash_of_qwerty" -- ` and password to a dummy value. Submit via the intercepted request. The dummy insert fails harmlessly due to duplicate key, but triggers the update on the admin record.

### Step 4: Verify Access

**Context**: After injection, attempt to log in with the admin email and new password to confirm the change.

> Navigate to the login page and authenticate as 'admin@example.com' with 'qwerty'. If successful, you have admin access. Check application logs or database (if accessible) to verify the password update.
