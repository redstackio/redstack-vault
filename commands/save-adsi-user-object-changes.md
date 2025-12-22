---
id: fb998744-2ac4-4dbe-83fd-f3cfab20b023
name: Save ADSI User Object Changes
type: command
executor: powershell
data: $UserObject.SetInfo()
output: null
created_at: '2023-04-06T03:56:06.779560+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - adsi
verified: true
validated: true
---

# Save ADSI User Object Changes

## Command

```powershell
$UserObject.SetInfo()
```

## Description

This command commits all pending modifications to an Active Directory user object bound via ADSI, saving changes like attribute updates to the domain database. It must be called after setting properties to persist them across the network.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | Relies on pre-bound $UserObject variable | N/A |

## Examples

### Basic Usage

```powershell
$UserObject.SetInfo()
```

### Advanced Usage

With error handling:

```powershell
try { $UserObject.SetInfo() ; Write-Output "Changes saved" } catch { Write-Error "Save failed: $_" }
```

## Expected Output

No output if successful. The changes are replicated to AD. On failure, a COM or LDAP exception is raised (e.g., "The directory operation failed" for replication issues or access denied). Verify by querying the object with Get-ADUser.

## Related

- [[Abuse AD ACLs GenericWrite to Configure RCM Persistence]]
- [[Retrieve ADSI User Object]]
