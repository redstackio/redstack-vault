---
id: cmd-flask-run-api-script
data: FLASK_APP=api_project_ql.py flask run
tags:
  - flask
  - server
  - mock
type: command
output: 'Server running on http://127.0.0.1:5000'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.583Z'
verified: false
validated: true
submitted: true
---
# flask-run-api-script

## Command

```bash
FLASK_APP=api_project_ql.py flask run
```

## Description

Starts a Flask development server using the specified app script for the mock GitLab API, binding to localhost:5000 by default.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| FLASK_APP | Environment var for app file | Yes |
| flask | CLI tool | Yes |
| run | Starts server | Yes |

## Examples

### Basic Usage

```bash
FLASK_APP=api_project_ql.py flask run
```

### Advanced Usage

With host/port: `FLASK_APP=api_project_ql.py flask run --host=0.0.0.0 --port=5000`.

## Expected Output

* Running on http://127.0.0.1:5000; access logs show requests.

## Related

- [[tools/Flask]]
