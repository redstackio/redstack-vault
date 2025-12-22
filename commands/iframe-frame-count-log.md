---
id: cmd-iframe-frame-log
data: >-
  <iframe
  id="ifr"></iframe><script>ifr.onload=function(){console.log(ifr.contentWindow.frames.length);}</script>
tags:
  - frame-detection
  - javascript
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.851Z'
verified: false
validated: true
submitted: true
---
# iframe-frame-count-log

## Command

```html
<iframe id="ifr"></iframe><script>ifr.onload=function(){console.log(ifr.contentWindow.frames.length);}</script>
```

## Description

Sets up an iframe and logs the number of frames on load to detect page changes, distinguishing normal pages (>3 frames) from upload beta (1 frame).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | ID of the iframe (ifr) | Yes |
| onload | Function to log frames.length | Yes |

## Examples

### Basic Usage

```html
<iframe id="ifr"></iframe><script>ifr.onload=function(){console.log(ifr.contentWindow.frames.length);}</script>
```

## Expected Output

Console log of frame count (e.g., >3 for normal pages, 1 for upload beta).

## Related

- [[procedures/Detect-Navigation-to-Vulnerable-Upload-Page]]
