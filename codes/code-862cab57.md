---
id: 862cab57-3d2d-42b6-90a6-dadebb81bc5e
type: code
language: Hashcat Mask
verified: false
created_at: '2020-03-16T08:05:49.125236+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 862cab57

**Language**: Hashcat Mask

```hashcat mask
l | abcdefghijklmnopqrstuvwxyz
u | ABCDEFGHIJKLMNOPQRSTUVWXYZ
d | 0123456789
h | 0123456789abcdef
H | 0123456789ABCDEF
s | ! "#$%&'()*+,-./:;<=>?@[\]^_`{|}~
a | ?l?u?d?s
b | 0x00 - 0xff
```
