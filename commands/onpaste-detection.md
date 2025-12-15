---
id: cmd-onpaste-detect
data: 'onpaste=function(){console.log("ONPASTE!");}'
tags:
  - paste
  - event
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.824Z'
verified: false
validated: true
submitted: true
---
# onpaste-detection

## Command

```javascript
onpaste=function(){console.log("ONPASTE!");}
```

## Description

Logs when paste event occurs to detect user pasting the payload.

## Parameters

None

## Examples

### Basic Usage

```javascript
onpaste=function(){console.log("ONPASTE!");}
```

## Expected Output

Console log 'ONPASTE!'.

## Related

- [[procedures/Guide-User-Interaction-for-Payload-Delivery]]
