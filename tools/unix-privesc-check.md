---
id: 3736fab7-8a0c-421f-8b5b-f388e2d50089
name: unix-privesc-check
type: tool
verified: false
created_at: '2019-08-28T21:17:42.308534+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# unix-privesc-check

## Overview

Unix-privesc-checker is a script that runs on Unix systems (tested on Solaris 9, HPUX 11, Various Linuxes, FreeBSD 6.2). It tries to find misconfigurations that could allow local unprivileged users to escalate privileges to other users or to access local apps (e.g. databases). It is written as a si

## Description

Unix-privesc-checker is a script that runs on Unix systems (tested on Solaris 9, HPUX 11, Various Linuxes, FreeBSD 6.2). It tries to find misconfigurations that could allow local unprivileged users to escalate privileges to other users or to access local apps (e.g. databases). It is written as a single shell script so it can be easily uploaded and run (as opposed to un-tarred, compiled and installed). It can run either as a normal user or as root (obviously it does a better job when running as root because it can read more files).
