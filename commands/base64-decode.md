---
id: cmd-uuid-1
data: echo "$KEY==" | base64 -d
tags:
  - decoding
  - base64
type: command
output: '4815'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.636Z'
verified: false
validated: true
submitted: true
---
# base64-decode

## Command

```bash
echo "$KEY==" | base64 -d
```

## Description

Decodes a Base64-encoded string, with optional padding (`==`) for unpadded keys from URLs. Used to extract integer product IDs from public keys in web vulnerability exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$KEY` | The Base64 string to decode (env var or replace inline) | Yes |
| `==` | Padding for valid Base64 (add if length % 4 != 0) | No |

## Examples

### Basic Usage

```bash
echo "NDgxNQ==" | base64 -d
```

### Advanced Usage

```bash
echo -n "NDgxNQ" | base64 -d 2>/dev/null || echo "Invalid Base64"
```

## Expected Output

A decoded string, e.g., `4815` for product ID extraction. Errors if invalid Base64.

## Related

- [[Related Command: base64-encode]]
- [[procedures/Decode-Base64-Public-Key-to-Integer]]
