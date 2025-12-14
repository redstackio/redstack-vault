---
data: heroku create $1
tags:
  - heroku
  - create
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.919Z'
id: 8c964598-7baa-4ff8-b46a-27391f03780e
verified: false
validated: true
submitted: true
---
# heroku-create-app

## Command

```bash
heroku create tim-exclusive
```

## Description

Creates a new Heroku app with a specified name, claiming it if unclaimed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `appname` | Name for the app | Yes |

## Examples

### Basic Usage

```bash
heroku create tim-exclusive
```

### Advanced Usage

```bash
heroku create tim-exclusive --region eu
```

## Expected Output

"Created https://tim-exclusive.herokuapp.com/".

## Related

- [[Related Procedure: Claim-and-Takeover-Heroku-App]]
