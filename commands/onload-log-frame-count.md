---
id: cmd-frame-count-log
data: 'ifr.onload=function(){ console.log(ifr.contentWindow.frames.length); }'
tags:
  - frame-count
  - detection
type: command
output: 'Console log of frame count (e.g., 4)'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.034Z'
verified: false
validated: true
submitted: true
---
# Onload Log Frame Count

## Command

```javascript
ifr.onload=function(){ console.log(ifr.contentWindow.frames.length); }
```

## Description

Logs the number of nested frames in the iframe upon load to baseline page structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ifr | Iframe element reference | Yes |

## Examples

### Basic Usage

```javascript
// Attach to iframe
```

## Expected Output

Console: Number like >3 for normal pages.

## Related

- [[Related Procedure: Monitor Iframe Frames]]
