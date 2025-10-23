---
id: 01f0db94-e2d8-4f60-a4c8-fda218db9bc4
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:44.313713+00:00'
updated_at: '2023-04-10T20:24:38.357604+00:00'
---

# Code Snippet 01f0db94

**Language**: xml

```xml
<!DOCTYPE r [
  <!ENTITY % pe_1 "<!---->">
  <!ENTITY % pe_2 "&#37;pe_1;<!---->&#37;pe_1;">
  <!ENTITY % pe_3 "&#37;pe_2;<!---->&#37;pe_2;">
  <!ENTITY % pe_4 "&#37;pe_3;<!---->&#37;pe_3;">
  %pe_4;
]>
<r/>
```


