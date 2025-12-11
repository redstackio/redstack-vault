---
data: FLASK_APP=api_project_ql.py flask run
tags:
  - proxy
type: command
executor: bash
platforms:
  - Linux
id: bb8afc4b-afbb-4fed-b30f-9b6741f72bfd
created_at: '2025-12-11T03:48:05.999Z'
updated_at: '2025-12-11T03:48:05.999Z'
verified: false
validated: true
submitted: true
---
# flask-run

## Command

```bash
FLASK_APP=api_project_ql.py flask run
```

## Description

Runs a Flask application for proxying requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `FLASK_APP` | App file | Yes |

## Examples

### Basic Usage

```bash
FLASK_APP=app.py flask run
```

## Expected Output

Flask server running

## Related

- [[tools/Flask]]
