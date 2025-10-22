---
id: d2512d5b-79ef-44f3-869f-334b320daab3
name: Enumerate Linux Misconfigurations
type: cheatsheet
verified: true
created_at: '2019-09-17T06:34:44.853085+00:00'
updated_at: '2023-05-30T20:11:20.438818+00:00'
---

# Enumerate Linux Misconfigurations

**Status**: ✓ Verified

# Description

Linux admins commonly make mistakes and security exceptions. These scripts can help identify vulnerabilities.

**Command** ([[linuxprivchecker.py Scan a Linux Filesystem for Vulnerabilities]]):

```bash
python linuxprivchecker.py
```

**Command** ([[Scan a Linux Filesystem for Vulnerabilities (LinEnum)]]):

```bash
LinEnum.sh
```

**Command** ([[lse.sh Scan a Linux Filesystem for Vulnerabilities]]):

```bash
lse.sh 
```

Enumerate processes discarding processes which remain unchanged. This can be useful for identifying cronjobs.

**Code**: [[#!/bin/bash

IFS=$'\n'

old_process=$(ps -eo comma]]
