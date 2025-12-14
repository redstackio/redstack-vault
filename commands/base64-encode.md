---
id: cmd-uuid-2
data: echo "$STRING" | base64 | sed 's/==$//'
tags:
  - encoding
  - base64
type: command
output: QUEjNDgxNSNBQQ
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.629Z'
verified: false
validated: true
submitted: true
---
# base64-encode

## Command

```bash
echo "$STRING" | base64 | sed 's/==$//'
```

## Description

Encodes a string to Base64 and removes trailing padding (`==`) to match URL-friendly formats. Used for crafting manipulated product IDs in CSRF attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$STRING` | The input string to encode (e.g., `AA#4815#AA`) | Yes |
| `sed 's/==$//'` | Removes trailing `==` for compact output | No |

## Examples

### Basic Usage

```bash
echo "AA#4815#AA" | base64 | sed 's/==$//'
```

### Advanced Usage

```bash
echo -n "test" | base64
```

## Expected Output

Base64 string without padding, e.g., `QUEjNDgxNSNBQQ`.

## Related

- [[Related Command: base64-decode]]
- [[procedures/Craft-Malicious-Private-Product-ID]]
