---
data: window.top.postMessage()
tags:
  - javascript
  - injection
type: command
executor: javascript
platforms:
  - Web
id: 3940522d-1a65-4bfc-aad3-213a9756fd9e
created_at: '2025-12-11T06:10:17.862Z'
updated_at: '2025-12-11T06:10:17.862Z'
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

Sends a message to the top window, attempted in iframes to access privileged operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Message data | No |

## Examples

### Basic Usage

```javascript
window.top.postMessage({data: 'test'})
```

## Expected Output

Communication with parent window, potentially triggering actions.

## Related

- [[commands/open-steam-uri]]
- [[procedures/Abuse-OEMBED-for-JavaScript-Injection]]
