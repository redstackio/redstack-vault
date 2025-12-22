---
data: window.top.postMessage()
tags:
  - javascript
  - postmessage
type: command
executor: javascript
platforms:
  - Web
id: c9ee0059-c93d-464e-b7d9-fb121f7c0588
created_at: '2025-12-14T00:11:25.284Z'
updated_at: '2025-12-14T00:11:25.284Z'
verified: false
validated: true
submitted: true
---
# window-top-postmessage

## Command

```javascript
window.top.postMessage()
```

## Description

Attempts to send messages to the parent window for privileged operations, tested in OEMBED contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```javascript
window.top.postMessage({data: 'test'}, '*')
```

## Expected Output

No effect due to sandboxing.

## Related

- [[procedures/Escalating-with-Steam-URI-Schemes]]
