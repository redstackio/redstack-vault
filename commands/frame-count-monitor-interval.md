---
id: cmd-frame-monitor
data: >-
  setInterval(function(){if(i==2){console.log("stop
  counter...");}if(x!=1){if(ifr.contentWindow.frames.length==1){console.log("page
  change!");btn1.innerHTML="drag the image to here!";x=1;}}},1000)
tags:
  - monitoring
  - frames
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.831Z'
verified: false
validated: true
submitted: true
---
# frame-count-monitor-interval

## Command

```javascript
setInterval(function(){if(i==2){console.log("stop counter...");}if(x!=1){if(ifr.contentWindow.frames.length==1){console.log("page change!");btn1.innerHTML="drag the image to here!";x=1;}}},1000)
```

## Description

Monitors frame count every second; detects upload page (1 frame) and updates UI to instruct dragging image.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| interval | 1000ms | Yes |
| condition | frames.length==1 | Yes |

## Examples

### Basic Usage

```javascript
setInterval(function(){if(i==2){console.log("stop counter...");}if(x!=1){if(ifr.contentWindow.frames.length==1){console.log("page change!");btn1.innerHTML="drag the image to here!";x=1;}}},1000)
```

## Expected Output

Console log 'page change!' and UI update when on upload beta page.

## Related

- [[procedures/Detect-Navigation-to-Vulnerable-Upload-Page]]
