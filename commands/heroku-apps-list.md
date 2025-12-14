---
data: heroku apps
tags:
  - heroku
  - cloud
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.927Z'
id: a0eca3da-3e9a-43f0-9abd-e6d4ffb488e1
verified: false
validated: true
submitted: true
---
# heroku-apps-list

## Command

```bash
heroku apps
```

## Description

Lists all Heroku apps associated with the authenticated account, helpful for verifying app existence during takeover checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Lists all apps | No |

## Examples

### Basic Usage

```bash
heroku apps
```

### Advanced Usage

```bash
heroku apps --json
```

## Expected Output

Table or JSON of app names, e.g., "=== My Apps ... app1 ...".

## Related

- [[Related Procedure: Verify-Unclaimed-Heroku-Instance]]
