---
id: bd0e9bdd-a2c6-4125-bb59-6a84e5772cca
name: flask-print-log
type: command
executor: python
data: 'print request.args[''msg'']'
output: null
created_at: '2025-12-11T06:10:15.563Z'
updated_at: '2025-12-11T06:10:15.563Z'
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

# flask-print-log

## Command

```python
print request.args['msg']
```

## Description

Prints the 'msg' parameter from a GET request to the console, used for logging exfiltrated data in the Flask app.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `request.args['msg']` | The message to log, passed via GET parameter | Yes |

## Examples

### Basic Usage

```python
print request.args['msg']
```

### Advanced Usage

```python
if 'msg' in request.args:
    print(request.args['msg'])
```

## Expected Output

The message is printed to the console.

## Related

- [[commands/flask-app-run]]
- [[procedures/Set-Up-Timing-and-Logging-Server]]
