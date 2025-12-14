---
data: 'curl http://gameday.websummit.net'
tags:
  - http
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 3fad9778-af96-494f-9fb3-3adeb65d6815
created_at: '2025-12-14T05:32:24.263Z'
updated_at: '2025-12-14T05:32:24.263Z'
verified: false
validated: true
submitted: true
---
# curl-verify-subdomain

## Command

```bash
curl http://gameday.websummit.net
```

## Description

Retrieves content from the subdomain to confirm it serves the uploaded S3 content post-takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://gameday.websummit.net` | Target subdomain URL | Yes |

## Examples

### Basic Usage

```bash
curl http://gameday.websummit.net
```

### Advanced Usage

```bash
curl -L http://gameday.websummit.net
```

## Expected Output

HTML content from the POC file, e.g., "<h1>Subdomain Taken Over</h1>".

## Related

- [[Related Procedure]]
