---
id: 8a3beb2c-5f44-4e3c-a6ae-512178200d54
type: code
language: C
verified: false
created_at: '2019-09-17T20:08:40.308770+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 8a3beb2c

**Language**: C

```c
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    if (argc > 1) printf("%s", execvp(argv[1], &argv[1])); 
    return 0;
}
```
