---
data: heroku info --app $1
tags:
  - heroku
  - info
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.926Z'
id: 6c509cc0-7671-4e79-87c8-91e6a9c6d64f
verified: false
validated: true
submitted: true
---
# heroku-app-info

## Command

```bash
heroku info --app tim-exclusive
```

## Description

Retrieves detailed information about a specific Heroku app, used to check ownership and status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--app` | Specifies the app name | Yes |

## Examples

### Basic Usage

```bash
heroku info --app tim-exclusive
```

### Advanced Usage

```bash
heroku info --app tim-exclusive --json
```

## Expected Output

App details or error if not found, e.g., "App not found" for unclaimed.

## Related

- [[Related Procedure: Verify-Unclaimed-Heroku-Instance]]
