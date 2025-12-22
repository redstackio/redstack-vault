---
data: chunk_size = hex(len(prefix)).lstrip("0x")
tags:
  - scripting
  - http-smuggling
type: command
executor: python
platforms:
  - Web
id: a43c0209-4d35-4b05-ba18-ebdec152f08b
created_at: '2025-12-13T09:01:22.472Z'
updated_at: '2025-12-13T09:01:22.472Z'
verified: false
validated: true
submitted: true
---
# Calculate Chunk Size

## Command

```python
chunk_size = hex(len(prefix)).lstrip("0x")
```

## Description

Calculates the hexadecimal size of the smuggled prefix for chunked encoding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `len(prefix)` | Length of prefix | Yes |
| `hex()` | Convert to hex | Yes |
| `lstrip("0x")` | Remove '0x' | Yes |

## Examples

### Basic Usage

```python
chunk_size = hex(len(prefix)).lstrip("0x")
```

## Expected Output

Hex string, e.g., 'a2'.

## Related

- [[procedures/Prepare-Turbo-Intruder-Desync-Script]]
