---
id: c02206a9-9aa3-4c4a-94c9-5f4c33c15b30
name: Find Important Linux Files
type: cheatsheet
verified: true
created_at: '2019-09-17T06:24:10.346253+00:00'
updated_at: '2023-06-08T15:06:52.608185+00:00'
---

# Find Important Linux Files

**Status**: ✓ Verified

# Description

Using Linux's find tool to search for interesting and important files in a Linux environment.







**Command** ([[find Search for Files with SUID Rights]]):

```bash
find $_DIRECTORY -perm -4000 -ls 2>/dev/null
```







**Command** ([[find Search for Files with Wildcards]]):

```bash
find $_DIRECTORY -iname "*$_WORD*" -ls 2>/dev/null
```









**Command** ([[find Search for Files and Execute a Command on Each Result]]):

```bash
find $_DIRECTORY -exec $_CMD $_ARG1 $_ARG2 {} \; 2>/dev/null
```







**Command** ([[find Search for Writable Files by User]]):

```bash
find $_DIRECTORY -user $_USER -writable ! -type l 2>/dev/null
```







**Command** ([[find Search for Multiple Files by Name]]):

```bash
find $_DIRECTORY -name $_FILE1 -o name $_FILE2 -o -name $_FILE3 2>/dev/null
```









**Command** ([[Search for Files Modified Within 60 Minutes]]):

```bash
find / -ctime -60
```






