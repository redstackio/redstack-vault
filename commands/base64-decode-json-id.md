---
id: cmd-uuid-2
data: echo 'eyJpZCI6MX0=' | base64 -d
tags:
  - decoding
type: command
output: '{"id":1}'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.493Z'
verified: false
validated: true
submitted: true
---
# Base64 Decode Json Id

## Command

```bash
echo 'eyJpZCI6MX0=' | base64 -d
```

## Description

Decodes base64-encoded JSON parameter to reveal ID structure for modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Input | Base64 string | Yes |

## Examples

### Basic Usage

```bash
echo 'encoded' | base64 -d
```

## Expected Output

Decoded JSON object.

## Related

- [[procedures/Exploit-IDOR-in-People-Rater-via-Base64-Decoding]]
