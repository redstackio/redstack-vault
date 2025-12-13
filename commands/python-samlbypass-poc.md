---
data: python3 samlbypasspoc.py <URL_encoded_SAMLResponse>
tags:
  - python
  - saml
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 7ccaf5d8-9340-4c82-a242-4504ed947210
created_at: '2025-12-13T09:01:26.299Z'
updated_at: '2025-12-13T09:01:26.299Z'
verified: false
validated: true
submitted: true
---
# python-samlbypass-poc

## Command

```bash
python3 samlbypasspoc.py <URL_encoded_SAMLResponse>
```

## Description

Runs the POC script to generate a modified SAMLResponse by injecting a malicious Response element before the signed one, enabling authentication bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<URL_encoded_SAMLResponse>` | The original URL-encoded SAMLResponse from the intercepted request | Yes |

## Examples

### Basic Usage

```bash
python3 samlbypasspoc.py %3Coriginal_encoded_response%3E
```

### Advanced Usage

Modify the script first, then run:

```bash
python3 samlbypasspoc.py %3Coriginal_encoded_response%3E
```

## Expected Output

A new modified SAMLResponse value to use in the request, printed to stdout.

## Related

- [[procedures/Generate-Modified-SAML-Response-with-POC-Script]]
- [[tools/samlbypasspoc-py]]
