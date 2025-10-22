---
id: 09ab80fe-b4f2-4758-aa63-aa8d82bcee31
name: Powershell Meta-Functions
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:04.765224+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Powershell Meta-Functions

# Description

Enumerate Windows meta information using these PowerView & PowerSploit functions.

**Command** ([[Find shares on hosts local domain]]):

```bash
Invoke-ShareFinder

```

Can identify potentially sensitive files.

**Command** ([[Find files on hosts local domain]]):

```bash
Invoke-FileFinder

```

**Command** ([[ Find machines on the domain the current user has local admin access to]]):

```bash
Find-LocalAdminAccess

```

**Command** ([[Search a user field for a particular term]]):

```bash
Find-UserField

```

**Command** ([[Search a computer field for a particular term]]):

```bash
Find-ComputerField

```

**Command** ([[Find systems likely vulnerable to common exploits]]):

```bash
Get-ExploitableSystem

```

**Command** ([[Enumerate members of the local Administrators groups across all machines in the domain]]):

```bash
Invoke-EnumerateLocalAdmin

```
