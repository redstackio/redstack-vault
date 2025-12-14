---
id: cmd-ondragend-ui
data: >-
  ondragend=function(){ btn1.innerHTML=""; setTimeout(function(){
  btn1.innerHTML=""; btn2.innerHTML="copy the red text and paste here after
  that, press enter!"; },1100) }
tags:
  - dragend
  - ui-update
type: command
output: UI buttons updated after timeout
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.026Z'
verified: false
validated: true
submitted: true
---
# Ondragend Handle UI Update

## Command

```javascript
ondragend=function(){ btn1.innerHTML=""; setTimeout(function(){ btn1.innerHTML=""; btn2.innerHTML="copy the red text and paste here after that, press enter!"; },1100) }
```

## Description

Handles drag end, updates buttons after delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| btn1 | First button | Yes |
| btn2 | Second button | Yes |

## Examples

### Basic Usage

```javascript
// Attach to drag element
```

## Expected Output

Buttons clear; prompt appears after 1.1s.

## Related

- [[Related Procedure: Trick User into Dragging]]
