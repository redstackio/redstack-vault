---
id: cmd-uuid-8
data: 'print(len(PAYLOAD), "\t", time()- start)'
tags:
  - logging
  - results
  - benchmark
type: command
output: "e.g., 80000 \t 0.517104148864746"
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:02.910Z'
verified: false
validated: true
submitted: true
---
---

# print-timing-results

## Command

```python
print(len(PAYLOAD), "\t", time()- start)
```

## Description

Prints the length of the PAYLOAD and the elapsed time since start, tab-separated, to log performance metrics.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| len(PAYLOAD) | String length | Yes |
| time()-start | Elapsed seconds | Yes |

## Examples

### Basic Usage

```python
print(len(PAYLOAD), "\t", time()- start)
```

## Expected Output

e.g., 80000 	 0.517104148864746

## Related

- [[Related Procedure|procedures/Demonstrate-DoS-in-Django-urlize-with-Repeated-Payloads]]
