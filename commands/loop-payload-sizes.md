---
id: cmd-uuid-4
data: 'for i in range(0,1000000,40000):'
tags:
  - loop
  - payload
  - poc
type: command
output: null
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:02.934Z'
verified: false
validated: true
submitted: true
---
---

# loop-payload-sizes

## Command

```python
for i in range(0,1000000,40000):
```

## Description

Starts a for loop iterating i from 0 to 1,000,000 in steps of 40,000, used to generate payloads of escalating sizes for testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| range(0,1000000,40000) | Start, stop, step for loop | Yes |

## Examples

### Basic Usage

```python
for i in range(0,1000000,40000):
    # body
```

## Expected Output

No direct output; controls iterations (25 total).

## Related

- [[Related Procedure|procedures/Demonstrate-DoS-in-Django-urlize-with-Repeated-Payloads]]
