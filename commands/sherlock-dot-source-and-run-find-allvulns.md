---
id: 6afe9cbd-693c-4c34-b66a-fe0ff066772b
type: command
executor: powershell
data: . .\Sherlock.ps1; Find-AllVulns
output: |-
  PS C:\> . .\Sherlock.ps1; Find-AllVulns

  Title      : ClientCopyImage Win32k
  MSBulletin : MS15-051
  CVEID      : 2015-1701, 2015-2433
  Link       : https://www.exploit-db.com/exploits/37367/
  VulnStatus : Vulnerable

  Title      : Potato Privilege Escalation
  MSBulletin : N/A
  CVEID      : N/A
  Link       : https://www.exploit-db.com/exploits/39575/
  VulnStatus : Appears Vulnerable

  ... (additional vulnerabilities listed with status)
created_at: '2020-01-24T21:45:44.862325+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - privilege-escalation
verified: true
validated: true
---

# Sherlock Dot Source and Run Find-AllVulns

## Command

```powershell
. .\Sherlock.ps1; Find-AllVulns
```

## Description

This command dot-sources the Sherlock.ps1 script into the current PowerShell session and invokes the Find-AllVulns function to perform a comprehensive enumeration of local privilege escalation vulnerabilities on a Windows system. It is used during reconnaissance and post-exploitation to identify unpatched software and misconfigurations that could lead to privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| . .\Sherlock.ps1 | Dot-sources (loads) the Sherlock script from the current directory into the PowerShell environment, making its functions available | Yes |
| Find-AllVulns | Calls the main function within the script to check all supported vulnerabilities, including MS Bulletins, CVEs, and custom checks | Yes |

Note: The script must be present in the current working directory (or adjust the path accordingly). No additional arguments are needed for the basic scan.

## Examples

### Basic Usage

Execute in a PowerShell prompt from the directory containing Sherlock.ps1:

```powershell
. .\Sherlock.ps1; Find-AllVulns
```

### Advanced Usage

If the script is in a different location, specify the full path:

```powershell
. .\path\to\Sherlock.ps1; Find-AllVulns
```

For specific vulnerability checks, use targeted functions after sourcing:

```powershell
. .\Sherlock.ps1; Find-VulnMS15-051
```

## Expected Output

The command outputs a formatted list of checked vulnerabilities, including titles, associated MS Bulletins or CVEs, links to exploits, and vulnerability status. Example for a vulnerable system:

Title      : ClientCopyImage Win32k  
MSBulletin : MS15-051
CVEID      : 2015-1701, 2015-2433
Link       : https://www.exploit-db.com/exploits/37367/
VulnStatus : Vulnerable

Title      : Potato Privilege Escalation
MSBulletin : N/A
CVEID      : N/A
Link       : https://www.exploit-db.com/exploits/39575/
VulnStatus : Appears Vulnerable

Non-vulnerable items will show "VulnStatus : Patched" or "VulnStatus : Not Vulnerable". The output helps prioritize exploitation based on confirmed vulnerabilities.

## Related

- [[tools/Sherlock]]
- [[procedures/enumerate-windows-missing-patches-hotfixes-sherlock]]
