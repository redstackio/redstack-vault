---
id: 7ac4a2a3-471e-4cbf-94d0-d73790ac40e0
name: PowerShell-Enumerate-AD-PAM-Trusts-and-Shadow-Principals
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:07.394248+00:00'
updated_at: '2023-04-10T20:26:01.513573+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - enumeration
  - trust
validated: true
---

# PowerShell-Enumerate-AD-PAM-Trusts-and-Shadow-Principals

## Code

```powershell
# Detect if current forest is PAM trust
Import-Module ActiveDirectory
Get-ADTrust -Filter {(ForestTransitive -eq $True) -and (SIDFilteringQuarantined -eq $False)}

# Enumerate shadow security principals 
Get-ADObject -SearchBase ("CN=Shadow Principal Configuration,CN=Services," + (Get-ADRootDSE).configurationNamingContext) -Filter * -Properties * | select Name,member,msDS-ShadowPrincipalSid | fl

# Enumerate if current forest is managed by a bastion forest
# Trust_Attribute_PIM_Trust + Trust_Attribute_Treat_As_External
Get-ADTrust -Filter {(ForestTransitive -eq $True)} 
```

## Description

This PowerShell script detects PAM trusts by querying for transitive, non-quarantined AD trusts, enumerates shadow security principals (which map bastion forest admins to local groups), and identifies bastion-managed forests by checking specific trust attributes. It helps verify trust establishment and discover exploitable configurations for lateral movement.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The script uses hardcoded filters; customize domains in SearchBase if needed | N/A |

## Usage

Execute on a domain-joined Windows machine with the Active Directory PowerShell module (install RSAT if missing). Run as a domain user with read access to AD configuration. Use in post-trust creation to validate setup or during discovery to identify PAM-enabled environments. Output can be piped to file: | Out-File trusts.txt.

## Detection

- PowerShell ScriptBlock logging (Module 4104) capturing Get-ADTrust and Get-ADObject calls.
- AD audit logs for directory service access (Event ID 4662) on configuration partition.
- EDR alerts on AD module imports and queries to CN=Services in config NC.

## Related

- [[procedures/Establish-and-Enumerate-PAM-Trust-Between-Domains]]
