---
type: command
executor: powershell
data: >-
  $f=New-object -comObject HNetCfg.FwPolicy2;$f.rules | where {$_.action -eq
  "0"} | select name,applicationname,localports
platforms:
  - Windows
tags:
  - discovery
  - firewall
verified: true
validated: true
---

# powershell-enumerate-blocked-firewall-rules

## Command

```powershell
$f=New-object -comObject HNetCfg.FwPolicy2;$f.rules | where {$_.action -eq "0"} | select name,applicationname,localports
```

## Description

This PowerShell command queries the Windows Firewall policy using the HNetCfg.FwPolicy2 COM interface to list all blocking rules, displaying the rule name, associated application, and local ports affected. It is used during discovery to identify network restrictions without external tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The command has no user-defined parameters; it uses hardcoded action filter (0 for block). | N/A |

## Examples

### Basic Usage

```powershell
$f=New-object -comObject HNetCfg.FwPolicy2;$f.rules | where {$_.action -eq "0"} | select name,applicationname,localports
```

### Advanced Usage (Export to File)

```powershell
$f=New-object -comObject HNetCfg.FwPolicy2;$f.rules | where {$_.action -eq "0"} | select name,applicationname,localports | Export-Csv -Path blocked_rules.csv -NoTypeInformation
```

## Expected Output

```

Name                           ApplicationName                    LocalPorts
----                           ---------------                    ----------
Block All ICMPv4-In             %SystemRoot%\system32\svchost.exe *
Inbound Rule for File and Printer Sharing   %SystemRoot%\system32\svchost.exe 445
Core Networking - Block Rule   %SystemRoot%\system32\svchost.exe 139
```

A table listing blocking rules. Empty output suggests a default allow policy with no explicit blocks.

## Related

- [[procedures/Dump-Windows-Defender-Firewall-Configuration-and-List-Blocked-Ports]]
