---
data: >-
  curl
  "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=https://hackerone.com"
tags:
  - oauth
  - http
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.129Z'
id: a9fdaf4e-3f01-4969-a476-e66a26af471b
verified: false
validated: true
submitted: true
---
# curl-access-oauth-endpoint

## Command

```bash
curl "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=https://hackerone.com"
```

## Description

This command uses curl to send a GET request to the Respondly Twitter OAuth endpoint with a full redirect URI, testing parameter acceptance without errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The OAuth endpoint with query parameter | Yes |

## Examples

### Basic Usage

```bash
curl "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=https://hackerone.com"
```

### Advanced Usage

```bash
curl -v "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=https://hackerone.com" > response.txt
```

## Expected Output

HTTP response with redirect or authorization HTML, no errors on valid input.

## Related

- [[commands/curl-test-protocol-relative-uri]]
