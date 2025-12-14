---
id: cmd-uuid-1
data: python main.py
tags:
  - web-server
  - flask
type: command
output: '* Running on http://127.0.0.1:5000'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.737Z'
verified: false
validated: true
submitted: true
---
# python-flask-server

## Command

```bash
python main.py
```

## Description

This command starts a Flask development server to host malicious webpages (index.html and attack.html) for the double clickjacking PoC, serving on localhost:5000 by default.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No flags; runs default Flask app from main.py | No |

## Examples

### Basic Usage

```bash
python main.py
```

### Advanced Usage

For custom port: edit main.py to app.run(port=8080) then run.

```bash
python main.py
```

## Expected Output

Flask server startup message, e.g., * Running on http://127.0.0.1:5000 * Debug mode: on.

## Related

- [[Related Procedure: Setup-Malicious-Clickjacking-Server]]
