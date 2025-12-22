---
id: 82e64568-e1a5-43ff-afb0-52d134c4ffe0
name: Retrieve ADSI User Object
type: command
executor: powershell
data: '$UserObject = ([ADSI]("LDAP://$_USER_DN"))'
output: null
created_at: '2023-04-06T03:56:06.779340+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - adsi
verified: true
validated: true
---

# Retrieve ADSI User Object

## Command

```powershell
$UserObject = ([ADSI]("LDAP://$_USER_DN"))
```

## Description

This command uses the Active Directory Service Interfaces (ADSI) provider in PowerShell to bind to a specific user object in Active Directory via LDAP. It loads the object into the $UserObject variable for further manipulation, such as attribute modification. Use this when you have LDAP access and need to interact with AD objects programmatically.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USER_DN | The distinguished name (DN) of the target user object, e.g., CN=targetuser,OU=Users,DC=domain,DC=com | Yes |

## Examples

### Basic Usage

```powershell
$UserObject = ([ADSI]("LDAP://CN=targetuser,OU=Users,DC=domain,DC=com"))
```

### Advanced Usage

Combine with error handling:

```powershell
try { $UserObject = ([ADSI]("LDAP://$_USER_DN")) } catch { Write-Error "Failed to bind: $_" }
```

## Expected Output

No console output on success; the $UserObject variable is set and can be inspected with `$UserObject | Get-Member` to view available properties and methods. On failure, a COM exception is thrown (e.g., "The server is not operational" for connectivity issues or "Access denied" for permission problems).

## Related

- [[Abuse AD ACLs GenericWrite to Configure RCM Persistence]]
- [[commands/Set Terminal Services Initial Program]]
