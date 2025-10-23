---
id: 8c751ec5-05d8-4bdb-a8d3-a9279cf603c1
type: code
language: C
verified: false
created_at: '2019-09-17T20:15:01.451922+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 8c751ec5

**Language**: C

```c
#include <unistd.h>
#include <sys/types.h>
#include <grp.h>
#include <stdio.h>

int main (int argc, char** argv) {
    gid_t newGrp = 0;
    if (setuid(0) != 0) {
        perror("Setuid failed, no suid-bit set?"); return 1;
    }

    setgid(0);
    seteuid(0);
    setegid(0);

    // Replace the user's group with that of root setgroups(1, &newGrp);
    execvp("/bin/sh", argv);
    return 0;
}
```


