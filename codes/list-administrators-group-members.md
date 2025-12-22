---
id: 22f6fdfb-35b7-4217-a312-5433d75893b5
name: list-administrators-group-members
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:28.627017+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - admin
  - groups
validated: true
---

# list-administrators-group-members

## Code

```powershell
net localgroup administrators
Get-LocalGroupMember Administrators | ft Name, PrincipalSource
Get-LocalGroupMember Administrateurs | ft Name, PrincipalSource
```

## Description

PowerShell code to list members of the Administrators group, including French localization variant (Administrateurs). Combines net for basic list and Get-LocalGroupMember for detailed sourcing, useful for multilingual environments or confirming admin access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | No variables; targets default admin groups | N/A |

## Usage

Run in PowerShell on domain or local systems to identify over-privileged users. Output helps prioritize accounts for credential dumping or impersonation in escalation chains.

## Detection

- Auditing of group queries via Event ID 4798 (group membership enumeration)
- PowerShell logging for Get-LocalGroupMember
- Net localgroup in process monitoring

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/net-localgroup-administrators]]
