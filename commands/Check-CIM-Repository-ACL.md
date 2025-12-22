---
id: c4f49319-84b8-48d0-aca8-72d6566067d1
name: Check CIM Repository ACL
type: command
executor: powershell
data: >-
  Get-Acl C:\Windows\System32\wbem\Repository\OBJECTS.DATA | Format-List
  -Property PSPath, Sddl
output: null
created_at: '2023-04-06T03:56:08.224475+00:00'
updated_at: '2023-04-10T20:26:02.204187+00:00'
platforms:
  - Windows
tags:
  - wmi
  - permissions
verified: true
validated: true
---

# Check-CIM-Repository-ACL

## Command

```powershell
Get-Acl C:\Windows\System32\wbem\Repository\OBJECTS.DATA | Format-List -Property PSPath, Sddl
```

## Description

This PowerShell command retrieves the Access Control List (ACL) for the WMI CIM repository file, displaying the path and Security Descriptor Definition Language (SDDL) string. Use it to verify read permissions before querying sensitive namespaces like SCCM's.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `C:\Windows\System32\wbem\Repository\OBJECTS.DATA` | Path to the CIM repository file | Yes |
| `PSPath` | Property to display file path | Built-in |
| `Sddl` | Property to display security descriptor | Built-in |

## Examples

### Basic Usage

```powershell
Get-Acl C:\Windows\System32\wbem\Repository\OBJECTS.DATA | Format-List -Property PSPath, Sddl
```

### Parse SDDL

Follow up with:
```powershell
(Get-Acl C:\Windows\System32\wbem\Repository\OBJECTS.DATA).Sddl | ConvertFrom-SddlString
```

## Expected Output

```

PSPath : Microsoft.PowerShell.Core\FileSystem::C:\Windows\System32\wbem\Repository\OBJECTS.DATA

Sddl : D:(A;;0x1200a9;;;WD) ...

```

The SDDL string shows permissions; look for entries allowing read (0x1200a9) for your user/group.

## Related

- [[procedures/SCCM-Network-Access-Account-Credential-Theft]]
