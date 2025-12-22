---
id: e91db040-203f-4db2-a98d-1bd67873b20b
name: Find-LocalAdminAccess-PowerView
type: command
executor: powershell
data: Find-LocalAdminAccess -Verbose
output: null
created_at: '2023-01-12T06:56:20.751942+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - discovery
  - ad-recon
verified: true
validated: true
---

# Find-LocalAdminAccess-PowerView

## Command

```powershell
Find-LocalAdminAccess -Verbose
```

## Description

This command, from the PowerView module in PowerSploit, enumerates domain-joined computers and tests if the current user has local administrator access by attempting connections to remote admin shares (e.g., ADMIN$). Use it during Active Directory reconnaissance to identify lateral movement targets. Assumes PowerView is imported.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Verbose | Enables detailed output during enumeration and testing | No |
| -Domain | Specifies the target domain (defaults to current) | No |
| -ComputerName | Limits to specific computer names or file of names | No |
| -AdminGroup | Custom group to check instead of Administrators | No |
| -Quiet | Suppresses non-success output | No |

## Examples

### Basic Usage

```powershell
Find-LocalAdminAccess -Verbose
```

### Advanced Usage

```powershell
Find-LocalAdminAccess -Domain contoso.com -ComputerFilePath computers.txt -Quiet
```

## Expected Output

VERBOSE: Querying 50 domain computers for local administrator access...
ComputerName         : WORKSTATION01
AccessGranted        : True
GroupDN              : CN=Administrators,CN=Builtin,DC=contoso,DC=com
...
ComputerName         : SERVER02
AccessGranted        : False
...

Success is shown by 'AccessGranted: True' entries, listing exploitable hosts.

## Related

- [[procedures/Enumerate-Domain-Machines-for-Local-Admin-Access]]
- [[tools/PowerSploit]]
