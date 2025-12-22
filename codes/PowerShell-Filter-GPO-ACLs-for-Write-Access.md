---
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - active-directory
  - acl-filtering
  - powershell
validated: true
---

# PowerShell-Filter-GPO-ACLs-for-Write-Access

## Code

```powershell
Get-DomainObjectAcl -Identity "SuperSecureGPO" -ResolveGUIDs |  Where-Object {($_.ActiveDirectoryRights.ToString() -match "GenericWrite|AllExtendedWrite|WriteDacl|WriteProperty|WriteMember|GenericAll|WriteOwner")}
```

## Description

This PowerShell snippet uses PowerView to query and filter the ACL of a specified GPO for entries granting write permissions. It helps identify exploitable misconfigurations in Active Directory by highlighting rights that allow policy modification, such as injecting malicious scripts for persistence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "SuperSecureGPO" | The Identity of the GPO or AD object to query (replace with target name or GUID) | "Default Domain Policy" |

## Usage

Execute this in a PowerShell session with PowerView loaded after enumerating GPOs. Integrate into a loop to scan multiple GPOs: `Get-DomainGPO -All | ForEach { & the-script -Identity $_.Name }`. Use in red team engagements to find low-hanging fruit for GPO abuse without full DA privileges.

## Detection

- Monitor PowerShell execution logs for PowerView imports (Module logging) or LDAP queries to GPO objects (Event ID 4662 in Security logs).
- Look for anomalous ACL queries from non-admin accounts.
- Baseline GPO ACLs and alert on filtering patterns matching write rights.

## Related

- [[Related Procedure: Exploit-Group-Policy-Objects-with-Write-Access]]
- [[Related Tool: PowerView]]
