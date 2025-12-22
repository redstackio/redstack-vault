---
id: 0184868e-c2dc-4568-8901-cba61d7864c1
name: decode-base64-encoded-string
type: command
executor: bash
data: base64 -d <<< $_STRING
output: |-
  root@kali:~# base64 -d <<< c3VwZXJ0b3BzZWNyZXQhISEhCg==
  supertopsecret!!!!
created_at: '2020-03-26T03:48:55.520527+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - decode
  - base64
verified: true
validated: true
---

# decode-base64-encoded-string

## Command

```bash
base64 -d <<< $_STRING
```

## Description

Decodes a Base64 string to plaintext using stdin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_STRING | Base64 encoded input | Yes |
| -d | Decode mode | Built-in |

## Examples

### Basic Usage

```bash
base64 -d <<< SGVsbG8=
```

### Advanced Usage

```bash
base64 -d encoded.txt > decoded.txt
```

## Expected Output

Plaintext decoded string.

## Related

- [[commands/decode-base64-encoded-string]]
