---
data: pm2.disconnect()
tags:
  - api
  - cleanup
type: command
output: Connection closed
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.405Z'
id: c6446c0b-20f3-4f07-b89c-bfe7de7e870f
verified: false
validated: true
submitted: true
---
# pm2-disconnect

## Command

```javascript
pm2.disconnect()
```

## Description

Disconnects the Node.js script from the PM2 daemon after exploitation to clean up the session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```javascript
pm2.disconnect();
```

### Advanced Usage

```javascript
pm2.disconnect(function() { console.log('Disconnected'); });
```

## Expected Output

Silent closure on success; no output unless callback used.

## Related

- [[commands/pm2-connect]]
- [[procedures/Exploit-PM2-API-Command-Injection]]
