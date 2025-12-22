---
data: GET /ok HTTP/1.0
tags:
  - ssrf
  - http
  - get
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 4516053a-9b8f-4856-ada9-ec1e7f0e1af5
created_at: '2025-12-13T09:00:27.200Z'
updated_at: '2025-12-13T09:00:27.200Z'
verified: false
validated: true
submitted: true
---
# SSRF GET Request

## Command

```bash
GET /ok HTTP/1.0
```

## Description

This is an observed HTTP GET request in server logs, confirming SSRF induced by XXE exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/ok` | The path requested on the external server | Yes |

## Examples

### Basic Usage

```bash
GET /ok HTTP/1.0
```

### Advanced Usage

N/A - This is a log observation, not an executable command.

## Expected Output

Log entry like '200 227' indicating successful request processing.

## Related

- [[commands/xxe-post-request]]
- [[procedures/Verify-SSRF-via-Access-Logs]]
