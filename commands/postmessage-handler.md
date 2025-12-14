---
id: cmd-postmessage-handle
data: 'onmessage=function(event){console.log(event);i++;}'
tags:
  - inter-frame
  - communication
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.828Z'
verified: false
validated: true
submitted: true
---
# postmessage-handler

## Command

```javascript
onmessage=function(event){console.log(event);i++;}
```

## Description

Handles postMessage events, logging and incrementing a counter for inter-frame communication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| event | Incoming message | Yes |

## Examples

### Basic Usage

```javascript
onmessage=function(event){console.log(event);i++;}
```

## Expected Output

Logs event data and increments i.

## Related

- [[procedures/Detect-Navigation-to-Vulnerable-Upload-Page]]
