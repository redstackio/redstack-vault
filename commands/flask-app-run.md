---
id: 5a08237d-7c92-4309-b1a9-352e171e522f
name: flask-app-run
type: command
executor: python
data: app.run(host='0.0.0.0')
output: null
created_at: '2025-12-11T06:10:15.587Z'
updated_at: '2025-12-11T06:10:15.587Z'
platforms:
  - Linux
  - Web
tags:
  - flask
  - server
verified: false
validated: true
submitted: true
---

# flask-app-run

## Command

```python
app.run(host='0.0.0.0')
```

## Description

Starts the Flask web server listening on all available network interfaces, used to run the timing and logging server for DNS rebinding attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `host` | Specifies the host to bind to, '0.0.0.0' means all interfaces | Yes |

## Examples

### Basic Usage

```python
app.run(host='0.0.0.0')
```

### Advanced Usage

```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

## Expected Output

The Flask app starts running and listening for requests on port 5000 (default).

## Related

- [[commands/flask-sleep]]
- [[procedures/Set-Up-Timing-and-Logging-Server]]
