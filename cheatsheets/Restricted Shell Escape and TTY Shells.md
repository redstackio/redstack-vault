---
id: 969e27d1-618e-4dda-a513-f0ec58d33e9e
name: Restricted Shell Escape and TTY Shells
type: cheatsheet
verified: true
created_at: '2019-09-20T19:50:15.519746+00:00'
updated_at: '2023-05-30T20:11:56.837287+00:00'
---

# Restricted Shell Escape and TTY Shells

**Status**: ✓ Verified

# Description

Interactive tools require a TTY Shell to launch or even used properly. This is an issue when a reverse shell is picked up by Netcat, it does not natively provide a tty shell back to the user. This list of commands can help convert a non-tty shell to a tty shell or escape a restricted shell.

**Command** ([[python Spawn TTY Shell]]):

```bash
python -c 'import pty;pty.spawn("/bin/bash")'
```

**Command** ([[echo Execute TTY Shell]]):

```bash
echo os.system('/bin/bash')
```

**Command** ([[sh Execute TTY Shell]]):

```bash
/bin/sh -i
```

**Command** ([[perl Execute TTY Shell]]):

```bash
perl -e 'exec "/bin/sh";'
```

**Command** ([[perl Interactive mode TTY Shell]]):

```bash
exec "/bin/sh";
```

**Command** ([[ruby Execute TTY Shell]]):

```bash
ruby -e 'exec "/bin/sh"'
```

**Command** ([[ruby Interactive mode TTY Shell]]):

```bash
exec "/bin/sh"
```

**Command** ([[lua Execute TTY Shell]]):

```bash
lua -e 'os.execute("/bin/sh")'
```

**Command** ([[lua Interactive mode TTY Shell]]):

```bash
os.execute('/bin/sh')
```

**Command** ([[vi Interactive mode TTY Shell]]):

```bash
:!bash
```

**Command** ([[vi Interactive mode Set TTY Shell]]):

```bash
:set shell=/bin/bash:shell
```

**Command** ([[nmap Interactive mode TTY Shell]]):

```bash
!sh
```
