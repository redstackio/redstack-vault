---
id: cmd-001
data: >-
  curl -I -s
  http://mandrillapp.com/track/click/30956340/instagram-brand.com?p=<REDACTED> |
  grep Location
tags:
  - redirect-check
  - http-analysis
type: command
output: 'Location: http://instagram-brand.com/register/reset/<token>?email=<email>'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.430Z'
verified: false
validated: true
submitted: true
---
# Verify-HTTP-Redirect-in-Password-Reset-Link

## Command

```bash
curl -I -s http://mandrillapp.com/track/click/30956340/instagram-brand.com?p=<REDACTED> | grep Location
```

## Description

This command fetches the HTTP headers of the password reset tracking link from Mandrillapp and extracts the Location header to verify the redirect behavior, confirming if the target URL exposes the token over HTTP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only (HEAD request equivalent) | Yes |
| `-s` | Silent mode, suppress progress meter | Yes |
| `http://mandrillapp.com/track/click/30956340/instagram-brand.com?p=<REDACTED>` | The vulnerable HTTP link with redacted token | Yes |
| `| grep Location` | Pipe to grep for the redirect Location header | Yes |

## Examples

### Basic Usage

```bash
curl -I -s http://mandrillapp.com/track/click/30956340/instagram-brand.com?p=<REDACTED> | grep Location
```

### Advanced Usage

To save output for further analysis:

```bash
curl -I -s http://mandrillapp.com/track/click/30956340/instagram-brand.com?p=<REDACTED> | grep Location > redirect.txt
```

## Expected Output

`Location: http://instagram-brand.com/register/reset/<token>?email=<email>` indicating the insecure HTTP redirect with exposed token.

## Related

- [[Related Procedure: Intercept-Token-via-Network-Traffic-Capture]]
