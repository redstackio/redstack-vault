---
data: >-
  attack = attack.replace('Content-Length: '+content_length, 'Content-length:
  '+str(int(content_length)+len(chunk_size)-3))
tags:
  - scripting
  - http-smuggling
type: command
executor: python
platforms:
  - Web
id: 41b278d2-d584-4dd8-aee8-1b77be7d12f0
created_at: '2025-12-13T09:01:22.454Z'
updated_at: '2025-12-13T09:01:22.454Z'
verified: false
validated: true
submitted: true
---
# Adjust Content Length

## Command

```python
attack = attack.replace('Content-Length: '+content_length, 'Content-length: '+str(int(content_length)+len(chunk_size)-3))
```

## Description

Adjusts the Content-Length header to account for the added chunk size.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `replace` | Updates header | Yes |

## Examples

### Basic Usage

```python
attack = attack.replace('Content-Length: '+content_length, 'Content-length: '+str(int(content_length)+len(chunk_size)-3))
```

## Expected Output

Updated attack request.

## Related

- [[procedures/Prepare-Turbo-Intruder-Desync-Script]]
