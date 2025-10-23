---
id: 6b2c949f-a44b-428d-8640-28b08ee1a821
type: code
language: C
verified: false
created_at: '2019-09-17T20:15:01.437099+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 6b2c949f

**Language**: C

```c
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    if (argc > 1) printf("%s", execvp(argv[1], &argv[1]));
    return 0;
}

```


