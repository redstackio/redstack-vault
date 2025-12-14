---
id: cmd-ondragend-update
data: >-
  ondragend=function(){btn1.innerHTML="";setTimeout(function(){btn1.innerHTML="";btn2.innerHTML="copy
  the red text and paste here after that, press enter!";},1100)}
tags:
  - drag
  - ui-update
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.820Z'
verified: false
validated: true
submitted: true
---
# ondragend-ui-update

## Command

```javascript
ondragend=function(){btn1.innerHTML="";setTimeout(function(){btn1.innerHTML="";btn2.innerHTML="copy the red text and paste here after that, press enter!";},1100)}
```

## Description

On drag end, clears button text and after 1.1s updates to instruct copying and pasting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| timeout | 1100ms | Yes |

## Examples

### Basic Usage

```javascript
ondragend=function(){btn1.innerHTML="";setTimeout(function(){btn1.innerHTML="";btn2.innerHTML="copy the red text and paste here after that, press enter!";},1100)}
```

## Expected Output

UI update with paste instructions.

## Related

- [[procedures/Guide-User-Interaction-for-Payload-Delivery]]
