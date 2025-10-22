---
id: 017af6fe-dc0e-438e-a607-1c4e97e38f5a
name: Powershell GPO functions
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:12.147078+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Powershell GPO functions

# Description

Windows Group Policy Object Functions based on scripts from PowerView & PowerSploit.

**Command** ([[Get GptTmpl.inf and pasre to a custom object]]):

```bash
Get-GptTmpl

```

**Command** ([[Get all current GPOs for a given domain]]):

```bash
Get-NetGPO

```

**Command** ([[Get all GPOs in a domain that set "Restricted Groups" on on target machines]]):

```bash
Get-NetGPOGroup

```

**Command** ([[Find a user/group and makes machines they have effective rights over through GPO enumeration and correlation]]):

```bash
Find-GPOLocation

```

**Command** ([[Find a computer and determines who has admin rights over it through GPO enumeration]]):

```bash
Find-GPOComputerAdmin

```

**Command** ([[Get the default domain or DC policy]]):

```bash
Get-DomainPolicy

```
