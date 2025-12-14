---
id: cmd-sqlmap-detect-001
data: sqlmap -r request.txt --batch --level=1 --risk=1
tags:
  - sqli
  - detection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.149Z'
verified: false
validated: true
submitted: true
---
# sqlmap-detect

## Command

```bash
sqlmap -r request.txt --batch --level=1 --risk=1
```

## Description

This command uses SQLMap to detect SQL injection vulnerabilities in a saved HTTP request file, focusing on low-level, low-risk tests suitable for initial scanning of login forms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r request.txt` | Load HTTP request from file | Yes |
| `--batch` | Non-interactive mode, auto-accept defaults | No |
| `--level=1` | Testing level (1-5, higher more thorough) | No |
| `--risk=1` | Risk level (1-3, higher more aggressive) | No |

## Examples

### Basic Usage

```bash
sqlmap -r request.txt --batch
```

### Advanced Usage

```bash
sqlmap -r request.txt --batch --level=3 --risk=2 --dbms=mysql
```

## Expected Output

SQLMap will output detection results, such as "Parameter: username (POST) is vulnerable. Type: error-based" along with DBMS identification and payload examples.

## Related

- [[Related Procedure: Detect-SQL-Injection-Vulnerability-with-SQLMap]]
