---
id: 683fd927-6604-4f01-8559-3e9dca6e8184
name: flask-sleep
type: command
executor: python
data: sleep(3)
output: null
created_at: '2025-12-11T06:10:15.574Z'
updated_at: '2025-12-11T06:10:15.574Z'
platforms:
  - Linux
  - Web
tags:
  - flask
  - timing
verified: false
validated: true
submitted: true
---

# flask-sleep

## Command

```python
sleep(3)
```

## Description

Pauses execution for a specified number of seconds in a Flask route to create timing differences for DNS rebinding attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `3` | Duration in seconds to sleep | Yes |

## Examples

### Basic Usage

```python
sleep(3)
```

### Advanced Usage

```python
from time import sleep
sleep(5)  # Longer delay
```

## Expected Output

Delays the response from the route by 3 seconds.

## Related

- [[commands/flask-app-run]]
- [[procedures/Set-Up-Timing-and-Logging-Server]]
