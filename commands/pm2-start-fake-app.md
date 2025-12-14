---
data: 'pm2.start({script:''app.js''}, (err, apps)=> { /* handle */ })'
tags:
  - api
  - start
type: command
output: App started or error thrown
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.430Z'
id: 51a68736-0c5d-4090-ae46-0c8fc824f571
verified: false
validated: true
submitted: true
---
# pm2-start-fake-app

## Command

```javascript
pm2.start({script:'app.js'}, (err, apps)=> { /* handle */ })
```

## Description

Starts a fake application in PM2 to suppress 'No script path' errors during scripted exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `script` | Fake script path ('app.js') | Yes |
| `err, apps` | Callback with error and apps array | Yes |

## Examples

### Basic Usage

```javascript
pm2.start({script: 'app.js'}, (err, apps) => {});
```

### Advanced Usage

```javascript
pm2.start({script: 'fake.js', name: 'dummy'}, (err, apps) => {});
```

## Expected Output

App ID or name in callback on success; error if daemon issues.

## Related

- [[commands/pm2-install-payload]]
- [[procedures/Exploit-PM2-API-Command-Injection]]
