---
id: 930f9e45-fa8c-4cc4-9d58-4b0bd2ed6d2b
name: flask-set-log-level
type: command
executor: python
data: log.setLevel(logging.ERROR)
output: null
created_at: '2025-12-11T06:10:15.560Z'
updated_at: '2025-12-11T06:10:15.560Z'
platforms:
  - Linux
  - Web
tags:
  - flask
  - logging
verified: false
validated: true
submitted: true
---

# flask-set-log-level

## Command

```python
log.setLevel(logging.ERROR)
```

## Description

Sets the logging level for Werkzeug in Flask to ERROR to minimize unnecessary output during server operation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `logging.ERROR` | The logging level to set | Yes |

## Examples

### Basic Usage

```python
log.setLevel(logging.ERROR)
```

### Advanced Usage

```python
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)  # For more output
```

## Expected Output

Logging is configured to only show errors.

## Related

- [[commands/flask-app-run]]
- [[procedures/Set-Up-Timing-and-Logging-Server]]
