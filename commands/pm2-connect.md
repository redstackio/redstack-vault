---
data: >-
  pm2.connect(function(err){ if (err) { console.error(err); process.exit(2); }
  /* proceed */ })
tags:
  - api
  - connect
type: command
output: Connection established or error logged and exit
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.436Z'
id: a528e0f6-f703-45d5-9dc4-8edaf5825d15
verified: false
validated: true
submitted: true
---
# pm2-connect

## Command

```javascript
pm2.connect(function(err){ if (err) { console.error(err); process.exit(2); } /* proceed */ })
```

## Description

Connects a Node.js script to the running PM2 daemon for API interactions, handling errors to ensure exploitation proceeds.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `err` | Callback error handler | Yes |

## Examples

### Basic Usage

```javascript
pm2.connect(function(err) { /* handle */ });
```

### Advanced Usage

```javascript
pm2.connect({ secret: 'key' }, function(err) { /* handle */ });
```

## Expected Output

No output on success (proceeds to next API calls); on error, logs the error and exits with code 2.

## Related

- [[commands/pm2-install-payload]]
- [[procedures/Exploit-PM2-API-Command-Injection]]
