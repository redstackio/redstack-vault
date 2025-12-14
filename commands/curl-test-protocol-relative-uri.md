---
data: >-
  curl
  "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com"
tags:
  - oauth
  - http
  - malformed
  - error
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.126Z'
id: aef9e7c9-c013-4085-86bd-ced4f836be48
verified: false
validated: true
submitted: true
---
# curl-test-protocol-relative-uri

## Command

```bash
curl "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com"
```

## Description

Sends a GET request to the OAuth endpoint using a protocol-relative URI in the redirect parameter to trigger validation errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Endpoint with protocol-relative query | Yes |

## Examples

### Basic Usage

```bash
curl "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com"
```

### Advanced Usage

```bash
curl -v "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com" | grep error
```

## Expected Output

Error response from the server, such as 500 or authorization failure details.

## Related

- [[commands/curl-access-oauth-endpoint]]
