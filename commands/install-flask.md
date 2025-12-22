---
id: cmd-pip-install-flask-001
data: pip install Flask
tags:
  - python
  - install
type: command
output: Successfully installed Flask-2.0.1 ...
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.687Z'
verified: false
validated: true
submitted: true
---
# install-flask

## Command

```bash
pip install Flask
```

## Description

Installs the Flask web framework via pip for hosting the redirect server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Flask` | Package name | Yes |

## Examples

### Basic Usage

```bash
pip install Flask
```

### Advanced Usage

```bash
pip install Flask==1.1.2
```

## Expected Output

Installation success with version details.

## Related

- [[commands/run-flask-redirect-server]]
- [[procedures/Setup-Attacker-Controlled-Redirect-Server]]
