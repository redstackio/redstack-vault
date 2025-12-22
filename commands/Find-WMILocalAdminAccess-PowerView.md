---
id: 861ee434-270b-40ac-bbd1-7fe2b1024e4f
name: Find-WMILocalAdminAccess-PowerView
type: command
executor: powershell
data: . \Find-WMILocalAdminAccess.ps1; Find-WMILocalAdminAccess -Verbose
output: null
created_at: '2023-01-12T06:56:20.752944+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - discovery
  - ad-recon
  - wmi
verified: true
validated: true
---

# Find-WMILocalAdminAccess-PowerView

## Command

```powershell
. \Find-WMILocalAdminAccess.ps1
Find-WMILocalAdminAccess -Verbose
```

## Description

This command loads and executes the Find-WMILocalAdminAccess script (compatible with PowerView) to query WMI on domain computers for local Administrators group membership. It is a fallback when RPC is blocked, using WMI to avoid direct share access. Ideal for firewalled environments; requires WMI permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Verbose | Provides detailed logging of WMI queries | No |
| -Domain | Target domain for computer enumeration | No |
| -ComputerName | Specific computers to query | No |
| -Credential | Alternate credentials for WMI access | No |
| -Throttle | Limits concurrent WMI connections to avoid detection | No |

## Examples

### Basic Usage

```powershell
. \Find-WMILocalAdminAccess.ps1
Find-WMILocalAdminAccess -Verbose
```

### Advanced Usage

```powershell
. \Find-WMILocalAdminAccess.ps1
Find-WMILocalAdminAccess -Domain contoso.com -Credential $cred
```

## Expected Output

VERBOSE: Enumerating domain computers via WMI...
ComputerName    : WORKSTATION01
IsAdmin         : True
MemberOf        : Administrators
...
ComputerName    : SERVER02
IsAdmin         : False
...

Look for 'IsAdmin: True' to identify accessible machines.

## Related

- [[procedures/Enumerate-Domain-Machines-for-Local-Admin-Access]]
- [[tools/PowerSploit]]
