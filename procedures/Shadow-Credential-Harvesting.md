---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Shadow Credentials]]'
commands:
  - '[[commands/import-module-activedirectory]]'
  - '[[commands/get-aduser-shadow-credentials]]'
  - '[[commands/get-aduser-all-shadow-credentials]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Shadow Credential Harvesting

## Summary

This procedure demonstrates how to harvest shadow credentials by enumerating the msDS-KeyCredentialLink attribute across Active Directory user accounts. Shadow credentials enable certificate-based authentication for passwordless logins, and identifying accounts with this attribute set allows attackers to discover potential targets for persistence, privilege escalation, or further abuse in a domain environment.

## Description

The msDS-KeyCredentialLink attribute in Active Directory stores binary blobs containing public key information for device registration and certificate authentication, often used in modern authentication scenarios like Windows Hello for Business. Harvesting this attribute involves querying AD for users who have it populated, revealing accounts configured for alternate authentication methods. This discovery technique helps map the attack surface for subsequent manipulation, such as adding attacker-controlled keys for backdoor access. It requires read access to user objects, which domain-authenticated users typically have, and is commonly performed during reconnaissance in Active Directory environments to identify high-value targets like service accounts or admins.

## Requirements

1. Valid domain credentials with read access to AD user objects (standard user suffices).
2. PowerShell environment with the ActiveDirectory module installed (available on domain-joined Windows machines or via RSAT).
3. Optional: Domain controller FQDN for targeted queries.

## Defense

- Enable auditing for directory service access and monitor queries to msDS-KeyCredentialLink using tools like Microsoft Advanced Threat Analytics or custom SIEM rules.
- Limit read access to sensitive attributes via ACLs on user objects.
- Regularly audit accounts with msDS-KeyCredentialLink populated and enforce just-in-time admin privileges to reduce high-value targets.
- Implement device registration restrictions and certificate authority policies to control shadow credential usage.

## Objectives

1. Identify user accounts configured with shadow credentials in the domain.
2. Extract the msDS-KeyCredentialLink binary data for analysis or targeting.
3. Map potential persistence vectors by discovering alternate authentication configurations.

## Instructions

### Step 1: Import Active Directory Module

**Context**: Load the ActiveDirectory PowerShell module to access AD cmdlets for querying user attributes. This step is necessary before performing any AD operations and ensures the environment is prepared for credential harvesting.

**Command** ([[commands/import-module-activedirectory]]):
```powershell
Import-Module ActiveDirectory
```

> This command imports the module silently if available. If the module is not installed, install RSAT-AD-PowerShell feature via DISM or Settings on Windows.

### Step 2: Harvest Shadow Credentials for a Specific User

**Context**: Query a targeted user account to retrieve its msDS-KeyCredentialLink attribute. This reveals if the account has shadow credentials and provides the binary blob for further examination, such as decoding the public key or device ID. Use this for focused reconnaissance on suspected high-privilege accounts.

**Command** ([[commands/get-aduser-shadow-credentials]]):
```powershell
Get-ADUser -Identity $_TARGET_USER -Properties msDS-KeyCredentialLink -Server $_DOMAIN_CONTROLLER | Select-Object -ExpandProperty msDS-KeyCredentialLink
```

> Replace $_TARGET_USER with the username (e.g., 'Administrator') and $_DOMAIN_CONTROLLER with the DC FQDN if specifying one (optional; defaults to current domain). The command fetches the attribute as an array of byte[] objects. If empty, no shadow credentials are set.

### Step 3: Harvest Shadow Credentials Across All Domain Users

**Context**: Perform a domain-wide enumeration to identify all users with populated msDS-KeyCredentialLink attributes. This broad scan helps discover unexpected configurations, such as service accounts or dormant admins with enabled certificate auth, providing a list for prioritization in attacks. Be cautious of detection from excessive AD queries.

**Command** ([[commands/get-aduser-all-shadow-credentials]]):
```powershell
Get-ADUser -Filter * -Properties msDS-KeyCredentialLink | Where-Object { $_.msDS-KeyCredentialLink -ne $null } | Select-Object Name, DistinguishedName
```

> This filters and lists only users with the attribute set, outputting usernames and DNs. For large domains, add -SearchBase 'OU=Users,DC=domain,DC=com' to scope to an OU. Expected result is a table of accounts with shadow credentials enabled.
