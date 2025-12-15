---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
data: heroku create $APP_NAME
tags:
  - cloud
  - heroku
type: command
output: null
executor: bash
platforms:
  - Linux
  - Cloud
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:18.220Z'
verified: false
validated: true
submitted: true
---
# heroku-create-app

## Command

```bash
heroku create dangling-app
```

## Description

Creates a new Heroku application with a specified name, useful for claiming dangling app names in takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$APP_NAME` | Name for the new app | Yes |

## Examples

### Basic Usage

```bash
heroku create dangling-app
```

### Advanced Usage

```bash
heroku create dangling-app --region us
```

## Expected Output

'Creating dangling-app... done\nhttps://dangling-app.herokuapp.com/ | https://git.heroku.com/dangling-app.git'.

## Related

- [[commands/heroku-login]]
- [[procedures/Claim-Heroku-App-for-Takeover]]
