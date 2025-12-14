---
id: cmd-uuid-5
data: start = time()
tags:
  - timing
  - benchmark
type: command
output: null
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:02.926Z'
verified: false
validated: true
submitted: true
---
---

# start-timing

## Command

```python
start = time()
```

## Description

Records the current timestamp in seconds to mark the start of a timed operation, like urlize execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Calls time() | Yes |

## Examples

### Basic Usage

```python
start = time()
```

## Expected Output

No output; start variable set to float timestamp.

## Related

- [[Related Procedure|procedures/Demonstrate-DoS-in-Django-urlize-with-Repeated-Payloads]]
