---
id: 6f7e4ebb-c847-432e-88e6-e15d4cb68ba0
name: Windows Registry Keys Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T18:20:57.453237+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Windows Registry Keys Cheatsheet

**Code**: [[
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\]]

This key specifies what program should be launched right after a user logs into Windows. The default program for this key is C:\windows\system32\userinit.exe. Userinit.exe is a program that restores your profile, fonts, colors, etc for your user name. It is possible to add further programs that will launch from this key by separating the programs with a comma.

**Code**: [[
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Cur]]

**Code**: [[
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\Curr]]

**Code**: [[
HKLM\Software\MS\WindowsNT\CurrentVersion\Image F]]

# AppInit_DLLs

This value corresponds to files being loaded through the AppInit_DLLs Registry value. The AppInit_DLLs registry value contains a list of dlls that will be loaded when user32.dll is loaded. As most Windows executables use the user32.dll, that means that any DLL that is listed in the AppInit_DLLs registry key will be loaded also. This makes it very difficult to remove the DLL as it will be loaded within multiple processes, some of which can not be stopped without causing system instability. The user32.dll file is also used by processes that are automatically started by the system when you log on. This means that the files loaded in the AppInit_DLLs value will be loaded very early in the Windows startup routine allowing the DLL to hide itself or protect itself before we have access to the system.

**Code**: [[
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Wi]]
