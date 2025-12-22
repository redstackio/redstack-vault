---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: powerview-get-unconstrained-accounts
type: command
executor: powershell
data: 'Get-DomainComputer -Unconstrained | Select samaccountname, distinguishedname'
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - active-directory
  - delegation
verified: true
validated: true
---

# powerview-get-unconstrained-accounts

## Command

```powershell
Get-DomainComputer -Unconstrained | Select samaccountname, distinguishedname
```

## Description

This command uses PowerView to query Active Directory for computer accounts with Kerberos unconstrained delegation enabled, identifying potential targets for delegation abuse attacks like PetitPotam.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses current domain context; requires domain creds | No |

## Examples

### Basic Usage

```powershell
Get-DomainComputer -Unconstrained | Select samaccountname, distinguishedname
```

### Filter for Specific Server

```powershell
Get-DomainComputer -Unconstrained | Where-Object {$_.samaccountname -like "*ADCS*"}
```

## Expected Output

A table of unconstrained accounts:

samaccountname DistinguishedName
-------------- ----------------
ADCS01$        CN=ADCS01,CN=Computers,DC=domain,DC=com

## Related

- [[procedures/MS-EFSRPC-Abuse-via-PetitPotam-and-Unconstrained-Delegation]]
- [[tools/PowerView]]
