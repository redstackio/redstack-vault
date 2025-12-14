---
id: cmd-monitor-frames-interval
data: >-
  setInterval(function(){ if(i==2){ console.log("stop counter..."); } if(x!=1){
  if(ifr.contentWindow.frames.length==1){ console.log("page change!");
  btn1.innerHTML="drag the image to here!"; x=1; } } },1000)
tags:
  - interval
  - frame-monitor
type: command
output: Console logs for detection; UI update
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.031Z'
verified: false
validated: true
submitted: true
---
# SetInterval Monitor Frames

## Command

```javascript
setInterval(function(){ if(i==2){ console.log("stop counter..."); } if(x!=1){ if(ifr.contentWindow.frames.length==1){ console.log("page change!"); btn1.innerHTML="drag the image to here!"; x=1; } } },1000)
```

## Description

Polls frame count every second to detect upload page and update UI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| i | Counter | Yes |
| x | Flag | Yes |
| ifr | Iframe | Yes |
| btn1 | Button element | Yes |

## Examples

### Basic Usage

```javascript
// As above
```

## Expected Output

"page change!" log; button text changes.

## Related

- [[Related Procedure: Monitor Iframe Frames]]
