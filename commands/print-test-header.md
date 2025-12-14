---
id: cmd-uuid-3
data: print('=== django.utils.html.urlize(".;" * n) ===')
tags:
  - logging
  - poc
type: command
output: '=== django.utils.html.urlize(".;" * n) ==='
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:02.938Z'
verified: false
validated: true
submitted: true
---
---

# print-test-header

## Command

```python
print('=== django.utils.html.urlize(".;" * n) ===')
```

## Description

Prints a header message to the console indicating the start of the urlize performance test with repeated '.;' payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Fixed string | Yes |

## Examples

### Basic Usage

```python
print('=== django.utils.html.urlize(".;" * n) ===')
```

## Expected Output

=== django.utils.html.urlize(".;" * n) ===

## Related

- [[Related Procedure|procedures/Demonstrate-DoS-in-Django-urlize-with-Repeated-Payloads]]
