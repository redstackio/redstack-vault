---
id: f991b8cc-3a32-4351-8d37-8a7ac698d2a2
type: command
executor: bash
data: >-
  curl -X POST "http://target.example.com/vulnerable" -d "input={% csrf_token
  %}" -H "Content-Type: application/x-www-form-urlencoded"
output: null
created_at: '2023-04-06T03:56:39.377324+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Web
tags:
  - ssti
  - engine-test
verified: true
validated: true
---

# ssti-jinja2-csrf-test

## Command

```bash
curl -X POST "http://target.example.com/vulnerable" -d "input={% csrf_token %}" -H "Content-Type: application/x-www-form-urlencoded"
```

## Description

This command tests template engine type by injecting a CSRF token tag. It helps differentiate Django (which supports it) from Jinja2 (which may error), guiding payload adaptation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://target.example.com/vulnerable` | Target endpoint | Yes |
| `input` | Parameter for injection | Yes |
| `{% csrf_token %}` | Django-specific tag payload | Yes |
| `-H "Content-Type: application/x-www-form-urlencoded"` | POST data type | Yes for POST |

## Examples

### Basic Usage

```bash
curl -X POST "http://target.example.com/form" -d "input={% csrf_token %}"
```

### GET Variant

```bash
curl -X GET "http://target.example.com/vulnerable?input={% csrf_token %}"
```

## Expected Output

In Django, expect a rendered token or no error; in Jinja2, a template syntax error:

```
Error: Invalid block tag: 'csrf_token'
```

Success in Django confirms engine and proceeds to exploitation.

## Related

- [[procedures/Exploit-SSTI-in-Django-Templates-using-Burp-Payloads]]
- [[commands/ssti-django-simple-math-test]]
