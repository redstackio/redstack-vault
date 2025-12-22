---
id: 95e37f66-6bbb-4619-be6a-07d168445550
name: adaclscan-scan-user-permissions
type: command
executor: powershell
data: >-
  ADACLScan.ps1 -Base "DC=contoso,DC=com" -Filter "(&(AdminCount=1))" -Scope
  subtree -EffectiveRightsPrincipal User1 -Output HTML -Show
output: null
created_at: '2023-04-06T03:56:06.673244+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl-scan
verified: true
validated: true
---

# adaclscan-scan-user-permissions

## Command

```powershell
ADACLScan.ps1 -Base "$_BASE_DN" -Filter "$_LDAP_FILTER" -Scope $_SCOPE -EffectiveRightsPrincipal $_USER -Output $_OUTPUT_FORMAT -Show
```

## Description

This command invokes the ADACLScan PowerShell script to enumerate effective permissions for a specified user principal across Active Directory objects matching an LDAP filter. It helps discover permission misconfigurations for privilege escalation planning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Base `$_BASE_DN` | Base distinguished name for the LDAP search (e.g., domain root) | Yes |
| -Filter `$_LDAP_FILTER` | LDAP query filter to select objects (e.g., for admin objects) | Yes |
| -Scope `$_SCOPE` | Search scope: base, onelevel, or subtree | Yes |
| -EffectiveRightsPrincipal `$_USER` | Username or SID to check effective rights for | Yes |
| -Output `$_OUTPUT_FORMAT` | Output format: HTML, CSV, or JSON | No (default: console) |
| -Show | Display results in console immediately | No |

## Examples

### Basic Usage

Scan effective rights for a user on admin objects:

```powershell
ADACLScan.ps1 -Base "DC=contoso,DC=com" -Filter "(&(AdminCount=1))" -Scope subtree -EffectiveRightsPrincipal User1 -Output HTML -Show
```

### Advanced Usage

Full domain scan without admin filter:

```powershell
ADACLScan.ps1 -Base "DC=contoso,DC=com" -Filter "(objectClass=*)" -Scope subtree -EffectiveRightsPrincipal User1 -Output CSV
```

## Expected Output

Console and/or file output listing objects with permissions:

```
Object DN: CN=Users,DC=contoso,DC=com
Rights: GenericRead, ReadProperty
Path: LDAP://CN=Users,DC=contoso,DC=com

Object DN: CN=Domain Admins,CN=Users,DC=contoso,DC=com
Rights: WriteDacl, DeleteTree
Path: LDAP://CN=Domain Admins,CN=Users,DC=contoso,DC=com
```

An HTML file (e.g., report.html) with a table of objects, rights, and GUIDs for visual analysis.

## Related

- [[procedures/Active-Directory-ACL-Scanning-for-User]]
- [[tools/ADACLScan]]
