---
id: cmd-onmessage-handle
data: 'onmessage=function(event){ console.log(event); i++; }'
tags:
  - postmessage
  - event-handling
type: command
output: Console log of message event
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.028Z'
verified: false
validated: true
submitted: true
---
# Onmessage Handle Event

## Command

```javascript
onmessage=function(event){ console.log(event); i++; }
```

## Description

Handles postMessage events from iframe, logging and incrementing counter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| event | Message event | Yes |
| i | Counter | Yes |

## Examples

### Basic Usage

```javascript
// Attach to window
```

## Expected Output

Event data logged; counter increments.

## Related

- [[Related Procedure: Setup ClickJacking]]
