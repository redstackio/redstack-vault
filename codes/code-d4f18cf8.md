---
id: d4f18cf8-ccbd-4f95-8838-eaef9428fa23
type: code
language: Python
verified: false
created_at: '2020-07-14T18:15:02.618476+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet d4f18cf8

**Language**: Python

```python
python3
from pwn import *
# n = 4 == 32Bit; n = 8 == 64 Bit
cyclic(128, n=4)
cyclic_find('6161616', n=4)
Where 61616161 = value not address

```
