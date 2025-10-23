---
id: 5af6e892-82eb-42e5-9cbb-d415bffa9d17
name: Windows File System Enumeration
type: cheatsheet
verified: true
created_at: '2019-11-26T16:37:00.902810+00:00'
updated_at: '2023-09-27T03:13:37.912100+00:00'
---

# Windows File System Enumeration

**Status**: ✓ Verified

# Description

Basic built-in Windows tools for file system enumeration.





## Command Prompt (cmd.exe)





**Command** ([[dir /s "$_STRING"]]):

```bash
dir /s "$_STRING"
```









**Command** ([[findstr Grep Files Recursively for a Case Insensitive String]]):

```bash
findstr /si $_STRING *.*
```









**Command** ([[List Directory Contents Including ADS]]):

```bash
dir /R
```









**Command** ([[more Extract ADS Embedded Data from a File]]):

```bash
more < $_FILE:$_ADS
```





**Common Environmental Variables (Windows Vista+)**





**Code**: [[# KEY                           # VALUE
%ALLUSERSP]]





**Common Environmental Variables (Windows XP and earlier)**





**Code**: [[# KEY                           # VALUE
%ALLUSERSP]]



List all current Environmental Variables in a command prompt with the "SET" command.





## PowerShell





**Command** ([[Get-ChildItem Recursive Search for Files and Folders]]):

```bash
Get-ChildItem -Recurse -Filter "$_FILENAME"
```









**Command** ([[Get-ChildItem Grep Files Recursively for a String]]):

```bash
Get-ChildItem -Recurse -Path $_PATH | Select-String -Pattern "$_STRING"
```









**Command** ([[Get-ChildItem List Files with ADS]]):

```bash
Get-ChildItem -Recurse -Path $_PATH | % { Get-Item $_.FullName -stream * } | where stream -ne ':$Data'
```









**Command** ([[Extract ADS Embedded Data from a File (PowerShell)]]):

```bash
Get-Content -Path $_FILE -stream $_ADS
```









**Command** ([[PowerShell List Installed Versions of .NET Framework]]):

```bash
Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' -recurse | Get-ItemProperty -name Version,Release -EA 0 |  Where { $_.PSChildName -match '^(?!S)\p{L}'} | Select PSChildName, Version, Release
```









**Common Environmental Variables**





**Code**: [[# KEY                          # VALUE
_NT_SYMBOL_]]



List all current Environmental Variables in a PowerShell session with the "gci env:" command.






