---
id: cmd-flask-run-001
data: FLASK_ENV=development FLASK_APP=poc1 flask run
tags:
  - flask
  - server
type: command
output: '* Running on http://127.0.0.1:8067'
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.685Z'
verified: false
validated: true
submitted: true
---
# run-flask-redirect-server

## Command

```bash
FLASK_ENV=development FLASK_APP=poc1 flask run
```

## Description

Launches Flask app in development mode; code sets port 8067 for handling webhook redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `FLASK_ENV` | Environment (development for debug) | Yes |
| `FLASK_APP` | App module/file | Yes |

## Examples

### Basic Usage

```bash
FLASK_ENV=development FLASK_APP=poc1 flask run
```

### Advanced Usage

```bash
FLASK_ENV=development FLASK_APP=poc1 flask run --port=8067 --host=0.0.0.0
```

## Expected Output

Server startup message with URL.

## Related

- [[commands/install-flask]]
- [[procedures/Setup-Attacker-Controlled-Redirect-Server]]
