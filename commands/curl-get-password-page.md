---
data: 'curl -X GET https://shoppers.instacart.com/password -c cookies.txt'
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.561Z'
id: 7c698de6-f418-4bc0-8b78-62322d06ca06
verified: false
validated: true
submitted: true
---
# curl-get-password-page

## Command

```bash
curl -X GET https://shoppers.instacart.com/password -c cookies.txt
```

## Description

Retrieves the password reset page from Instacart's shopper app, saving session cookies for subsequent requests. Used to inspect the form and extract authenticity_token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `https://shoppers.instacart.com/password` | Target reset endpoint | Yes |
| `-c cookies.txt` | Saves cookies to file | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://shoppers.instacart.com/password -c cookies.txt
```

### Advanced Usage

```bash
curl -X GET https://shoppers.instacart.com/password -c cookies.txt | grep authenticity_token
```

## Expected Output

HTML response containing the reset form, including <meta name="csrf-token" content="..."> for authenticity_token, and session cookies saved.

## Related

- [[commands/curl-post-password-reset]]
