---
data: FLASK_APP=fake_server3.py flask run
tags:
  - web-server
  - flask
type: command
executor: bash
platforms:
  - Linux
id: e8ae17cb-ecd3-445a-84d2-163b6e87261d
created_at: '2025-12-11T03:48:06.029Z'
updated_at: '2025-12-11T03:48:06.029Z'
verified: false
validated: true
submitted: true
---
# flask-run-fake-server

## Command

```bash
FLASK_APP=fake_server3.py flask run
```

## Description

Starts a Flask development server using the specified app file, used to run fake API servers for delivering malicious responses in exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `FLASK_APP` | Environment variable for app file | Yes |
| `flask run` | Command to start server | Yes |

## Examples

### Basic Usage

```bash
FLASK_APP=fake_server3.py flask run
```

### Advanced Usage

```bash
FLASK_APP=fake_server3.py flask run --port 5000
```

## Expected Output

Server running on http://127.0.0.1:5000.

## Related

- [[procedures/Setup-Fake-GitHub-API-Server-with-Ngrok]]
- [[tools/Flask]]
