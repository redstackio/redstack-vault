---
id: 2b7c1743-e410-48ec-b606-4c3fbeb72106
name: submit-signup-form
type: command
executor: bash
data: curl -X POST "$_TARGET_URL/submit-signup" -d '$_FORM_DATA' -L -v
output: null
created_at: '2023-04-06T03:56:31.693253+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - web
verified: true
validated: true
---

# submit-signup-form

## Command

```bash
curl -X POST "$_TARGET_URL/submit-signup" -d '$_FORM_DATA' -L -v
```

## Description

Submits the signup form data and follows any redirects to test the open redirection exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Submit endpoint | Yes |
| $_FORM_DATA | Form data including redirect (e.g., username=test&redirectUrl=evil) | Yes |
| -L | Follow redirects | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://famous-website.tld/submit-signup" -d 'username=test&redirectUrl=https://evil-website.tld' -L -v
```

## Expected Output

Redirect to malicious URL upon successful submission.

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/fill-in-signup-form]]
