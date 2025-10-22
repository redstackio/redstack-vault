---
id: f064065c-b911-4b17-b321-59d75deb9d15
name: gcc
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:39.880300+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# gcc

**Command** ([[cross compile for 32bit (m32) and all linux flavors (gnu, sysv)]]):

```bash
apt-get install libc6-dev-i386
gcc -m32 -Wall -Wl,--hash-style=both 9545.c -o exploit

```

**Command** ([[cross compile for 32Bit windows (on 64bit linux)]]):

```bash
i686-w64-mingw32-gcc -o ms11-046.exe ms11-046.c -lws2_32

```

**Command** ([[cross compile for 32bit windows (on 32bit linux)]]):

```bash
apt-get install mingw32
i586-mingw32msvc-gcc <source>.c -o <outfile> -lws2_32

```

# static application

To compile static applications use the “-static” parameter additionally

**Code**: [[
#include <stdlib.h>
int main ()
{
int i;
    i = ]]
