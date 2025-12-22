---
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:39Z'
updated_at: '2023-04-10T20:23:40Z'
platforms:
  - Web
  - Python
tags:
  - ssti
  - django
  - payload
validated: true
---

# Django-Template-SSTI-Leak-Signer-Key

## Code

```python
{{ messages.storages.0.signer.key }}
```

## Description

This Django template expression exploits SSTI to access and leak the signer key from the messages framework's storage. When injected into a vulnerable template-rendered input, it executes on the server and returns the key, enabling cookie forgery and session attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| messages | Django's messages context (assumed available in template) | Built-in |
| storages.0 | First storage in messages (default configuration) | Built-in |
| signer.key | The secret key used for signing | Built-in |

## Usage

Inject this payload into a vulnerable form field, URL parameter, or API input that gets rendered in a Django template. Use tools like Burp Suite or curl to deliver it. Once leaked, use the key with Django's signing utilities to manipulate signed data.

## Detection

- Monitor web application logs for template errors or access to internal objects like 'messages.storages'.
- WAF rules to block template expressions containing '{{' or object traversals.
- Anomaly detection in responses leaking base64-like strings (signer keys).

## Related

- [[procedures/Exploit-Django-Template-SSTI-to-Leak-Signer-Key]]
