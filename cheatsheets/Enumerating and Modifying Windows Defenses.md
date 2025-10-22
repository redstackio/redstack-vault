---
id: 0471a298-0304-4c78-9988-d5554c452e81
name: Enumerating and Modifying Windows Defenses
type: cheatsheet
verified: true
created_at: '2020-03-10T21:52:48.655963+00:00'
updated_at: '2023-05-30T20:06:29.621958+00:00'
---

# Enumerating and Modifying Windows Defenses

**Status**: ✓ Verified

# Description

Commands used to perform view,  modify, and bypass security settings on a Windows system with Administrator rights. Many of these commands require elevated privileges, and are generally used after compromising a computer's Administrator account.

## PowerShell Execution Policy

**Command** ([[Get PowerShell Execution Policy]]):

```bash
Get-ExecutionPolicy
```

**Command** ([[Disable PowerShell Execution Policy Restrictions]]):

```bash
Set-ExecutionPolicy Unrestricted
```

## Language Mode

**Command** ([[PowerShell Show Current Language Mode]]):

```bash
$ExecutionContext.SessionState.LanguageMode
```

## AppLocker

**Command** ([[Export AppLocker Rules in XML]]):

```powershell
powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective -Xml"
```

## Windows  Defender

**Command** ([[PowerShell Check for Anti-Virus in Windows (SecurityCenter2)]]):

```bash
Get-WmiObject -Namespace root\SecurityCenter2 -Class AntiVirusProduct
```

Tip: If no data is found in "SecurityCenter2", try  "SecurityCenter".

**Command** ([[Set-MpPreference -DisableRealtimeMonitoring $true]]):

```bash
Set-MpPreference -DisableRealtimeMonitoring $true
```

**Command** ([[Exclude a Folder from Windows Defender (PowerShell 4+)]]):

```bash
Add-MpPreference -ExclusionPath "$_PATH"
```

## Windows Firewall (WIndows 7+)

**Command** ([[Disable Windows Firewall (Windows 7+)]]):

```bash
netsh advfirewall set allprofiles state off
```

**Command** ([[Allow a Port Through Windows Firewall (Windows 7+)]]):

```bash
netsh advfirewall firewall add rule name="Open Port $_PORT" dir=in action=allow protocol=TCP localport=$_PORT
```

**Command** ([[Allow an Application Through Windows Firewall (Windows 7+)]]):

```bash
netsh advfirewall firewall add rule name="Allow $_Program to bypass firewall rules" dir=in action=allow program="C:\$_PATH\$_PROGRAM.exe" enable=yes
```

## Windows Firewall (Windows 2008 and earlier)

**Command** ([[Windows Firewall Disable Firewall (Windows 2008 and Earlier)]]):

```bash
netsh firewall set opmode DISABLE
```

**Command** ([[Allow a Port Through Windows Firewall (Windows 2008 and Earlier)]]):

```bash
netsh firewall add portopening TCP $_PORT "Open Port $_PORT"
```

## Bypassing AMSI

There are many approaches to bypassing AMSI, including disabling logging, patching the amsi.dll in memory, using PowerShell 2, etc. See  S3cu3Th1sS1t's GitHub for a list of popular approaches: [https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell](https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell)

Unfortunately most public AMSI bypasses are known to Microsoft and will be flagged. This can often be avoided by identifying and obfuscating parts of the code. For example, Matt Graeber's Reflection method will be flagged on patched Windows 2019/10, but by splitting up the string "amsiInitFailed" into two words, it works (as of July 2020).

**Code**: [[[Ref].Assembly.GetType('System.Management.Automati]]

For a detailed breakdown and workshop on bypassing AMSI, see BCSecurity's Defcon 27 Workshop: [Introduction to Sandbox Evasion and AMSI Bypasses - Jake Krasnov, Anthony Rose, Vincent Rose](https://youtu.be/F_BvtXzH4a4)
