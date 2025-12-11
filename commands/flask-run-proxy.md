---
id: 70514091-cc25-410b-bf68-8669e692b413
type: command
executor: bash
data: FLASK_APP=api flask run
output: null
created_at: '2025-12-11T03:48:05.891Z'
updated_at: '2025-12-11T03:48:05.891Z'
platforms:
  - Linux
tags:
  - proxy
  - flask
verified: false
validated: true
submitted: true
---

# flask-run-proxy

## Command

```bash
FLASK_APP=api flask run
```

## Description

Run the Flask proxy server from api.py, launching a proxy to replace uploads.tar.gz with the malicious version during import.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `FLASK_APP=api` | Specify the app file | Yes |
| `flask run` | Run the Flask development server | Yes |

## Examples

### Basic Usage

```bash
FLASK_APP=api flask run
```

## Expected Output

Server startup message indicating it's running on port 5000.

## Related

- [[procedures/Setup-Proxy-Server-with-Flask-and-Ngrok]]
- [[commands/ngrok-expose-server]]
