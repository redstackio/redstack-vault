---
id: 75259ce4-8697-4efc-b6b0-10b544ee0c63
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:02.288090+00:00'
updated_at: '2023-04-06T21:33:38.749304+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - '[[techniques/Active Scanning|T1595 - Active Scanning]]'
  - '[[techniques/Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Recon]]'
  - '[[tags/Using PowerView]]'
commands:
  - '[[commands/get-domain-policy]]'
  - '[[commands/get-domain-policy-system-access]]'
  - '[[commands/get-domain-policy-kerberos]]'
  - '[[commands/get-net-domain-controller]]'
  - '[[commands/get-net-domain-controller-domain]]'
  - '[[commands/get-net-user]]'
  - '[[commands/get-net-user-samaccountname]]'
  - '[[commands/get-net-user-select-cn]]'
  - '[[commands/get-user-property]]'
  - '[[commands/get-user-pwdlastset]]'
  - '[[commands/find-user-field]]'
  - '[[commands/get-net-loggedon-computername]]'
  - '[[commands/get-net-session-computername]]'
  - '[[commands/find-domain-user-location]]'
  - '[[commands/get-net-computer-fulldata]]'
  - '[[commands/get-domain-group]]'
  - '[[commands/get-net-computer-ping]]'
  - '[[commands/get-net-group-member]]'
  - '[[commands/get-domain-group-identity]]'
  - '[[commands/get-domain-gpo-local-group]]'
  - '[[commands/find-domain-share]]'
  - '[[commands/find-domain-share-check-access]]'
  - '[[commands/get-net-gpo-computername]]'
  - '[[commands/find-gpo-computer-admin]]'
  - '[[commands/get-net-ou-fulldata]]'
  - '[[commands/get-net-gpo-gponame]]'
  - '[[commands/get-object-acl-samaccountname]]'
  - '[[commands/get-object-acl-adsprefix]]'
  - '[[commands/invoke-aclscanner]]'
  - '[[commands/get-path-acl-share]]'
  - '[[commands/get-net-domain-trust]]'
  - '[[commands/get-net-domain-trust-domain]]'
  - '[[commands/get-net-forest-domain]]'
  - '[[commands/get-net-forest-domain-forest]]'
  - '[[commands/get-net-forest-trust]]'
  - '[[commands/get-net-domain-trust-forest]]'
  - '[[commands/find-local-admin-access]]'
  - '[[commands/invoke-enumerate-local-admin]]'
  - '[[commands/invoke-userhunter]]'
  - '[[commands/invoke-userhunter-groupname]]'
  - '[[commands/invoke-userhunter-stealth]]'
  - '[[commands/invoke-userhunter-check-access]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
validated: true
---

# Active Directory Recon with PowerView

## Summary

Active Directory Recon with PowerView is a technique used to gather comprehensive information about an organization's Active Directory environment using the PowerView PowerShell module. This procedure enables enumeration of domain users, computers, groups, shares, trusts, policies, and access controls, identifying potential targets for further attacks like password spraying or privilege escalation.

## Description

This procedure leverages PowerView, a PowerShell tool for Active Directory reconnaissance via LDAP queries. It targets domain-joined Windows environments to map the AD structure, discover trusts, enumerate sessions and privileges, and identify misconfigurations. In an attack scenario, an initial foothold (e.g., via phishing) allows loading PowerView to perform non-intrusive discovery, revealing high-value assets like domain admins or accessible shares. Expected outcomes include detailed reports on users, policies, and trusts, aiding lateral movement planning. Prerequisites include domain credentials and PowerView loaded in a PowerShell session.

## Requirements

1. Access to a domain-joined Windows machine with PowerShell execution policy allowing scripts.
2. PowerView PowerShell module loaded (via Import-Module).
3. Valid domain user credentials for authenticated queries.
4. Network connectivity to domain controllers (ports 389/636 for LDAP, 445 for SMB if checking shares).

## Defense

- Implement least privilege access to limit enumeration scope.
- Monitor PowerShell execution logs (Module Logging, Script Block Logging) for PowerView imports and LDAP queries.
- Use tools like Microsoft ATA or BloodHound for AD anomaly detection.
- Enforce strong auditing on AD objects and restrict unsigned script execution via AppLocker or WDAC.

## Objectives

1. Gather detailed information about the Active Directory environment, including users, computers, and groups.
2. Identify potential targets for privilege escalation, such as local admin access or domain trusts.
3. Map domain policies, shares, and sessions to support targeted attacks.

## Instructions

### Step 1: Retrieve Domain Policy Configurations

**Context**: Start by querying domain policies for system access and Kerberos configurations to understand password and authentication rules, which inform attack strategies like pass-the-hash or Kerberoasting.

**Command** ([[commands/get-domain-policy]]):
```powershell
Get-DomainPolicy
```

> This retrieves overall domain policy data. Success is indicated by policy objects returned without errors.

**Command** ([[commands/get-domain-policy-system-access]]):
```powershell
(Get-DomainPolicy)."system access"
```

> Extracts system access policy details like lockout thresholds. Expected output: Hashtable of policy settings.

**Command** ([[commands/get-domain-policy-kerberos]]):
```powershell
(Get-DomainPolicy)."kerberos policy"
```

> Pulls Kerberos-specific policies. Look for weak settings like short ticket lifetimes.

### Step 2: Enumerate Domain Controllers

**Context**: Identify domain controllers to target for further queries or attacks, noting their sites, IPs, and OS versions for exploitation planning.

**Command** ([[commands/get-net-domain-controller]]):
```powershell
Get-NetDomainController
```

> Lists DCs in the current domain. Expected: Table with ComputerName, Site, IPv4Address, OperatingSystem.

**Command** ([[commands/get-net-domain-controller-domain]]):
```powershell
Get-NetDomainController -Domain <DomainName>
```

> Targets a specific domain. Replace <DomainName> with e.g., 'child.domain.com'. Success: Filtered DC list.

### Step 3: Enumerate Domain Users and Properties

**Context**: Gather user details to identify high-privilege accounts, recent password changes, or interesting attributes for social engineering or spraying.

**Command** ([[commands/get-net-user]]):
```powershell
Get-NetUser
```

> Enumerates all users. Expected: SamAccountName, Description, etc.

**Command** ([[commands/get-net-user-samaccountname]]):
```powershell
Get-NetUser -SamAccountName <user>
```

> Details a specific user. Expected: Full user object.

**Command** ([[commands/get-net-user-select-cn]]):
```powershell
Get-NetUser | select cn
```

> Lists common names. Useful for quick overview.

**Command** ([[commands/get-user-property]]):
```powershell
Get-UserProperty
```

> Gets user properties.

**Command** ([[commands/get-user-pwdlastset]]):
```powershell
Get-UserProperty -Properties pwdlastset
```

> Checks last password changes. Expected: Timestamps for targeting stale accounts.

**Command** ([[commands/find-user-field]]):
```powershell
Find-UserField -SearchField Description -SearchTerm "wtver"
```

> Searches attributes. Expected: Matching users.

**Command** ([[commands/get-net-loggedon-computername]]):
```powershell
Get-NetLoggedon -ComputerName <ComputerName>
```

> Users logged on a machine. Expected: User list.

**Command** ([[commands/get-net-session-computername]]):
```powershell
Get-NetSession -ComputerName <ComputerName>
```

> Session details. Expected: Session info.

**Command** ([[commands/find-domain-user-location]]):
```powershell
Find-DomainUserLocation -Domain <DomainName> | Select-Object UserName, SessionFromName
```

> Locates user sessions. Expected: Machine-user mappings.

### Step 4: Enumerate Domain Computers and Groups

**Context**: Map computers and groups to find live hosts and membership for privilege identification.

**Command** ([[commands/get-net-computer-fulldata]]):
```powershell
Get-NetComputer -FullData
```

> Full computer details. Expected: Comprehensive AD computer objects.

**Command** ([[commands/get-domain-group]]):
```powershell
Get-DomainGroup
```

> All groups.

**Command** ([[commands/get-net-computer-ping]]):
```powershell
Get-NetComputer -Ping
```

> Live computers. Expected: Ping-responsive hosts.

### Step 5: Enumerate Group Memberships and GPOs

**Context**: Identify group members, especially admins, and GPOs affecting local groups for escalation paths.

**Command** ([[commands/get-net-group-member]]):
```powershell
Get-NetGroupMember -GroupName "<GroupName>" -Domain <DomainName>
```

> Specific group members. Expected: Member list.

**Command** ([[commands/get-domain-group-identity]]):
```powershell
Get-DomainGroup -Identity <GroupName> | Select-Object -ExpandProperty Member
```

> Alternative group enum.

**Command** ([[commands/get-domain-gpo-local-group]]):
```powershell
Get-DomainGPOLocalGroup | Select-Object GPODisplayName, GroupName
```

> GPOs modifying locals. Expected: GPO impacts.

### Step 6: Enumerate Domain Shares

**Context**: Discover accessible shares for sensitive data or further foothold.

**Command** ([[commands/find-domain-share]]):
```powershell
Find-DomainShare
```

> All shares. Expected: Share paths and permissions.

**Command** ([[commands/find-domain-share-check-access]]):
```powershell
Find-DomainShare -CheckShareAccess
```

> Accessible shares. Success: User-readable shares.

### Step 7: Retrieve GPOs and Local Admins

**Context**: Check applied GPOs and local admin memberships via policy.

**Command** ([[commands/get-net-gpo-computername]]):
```powershell
Get-NetGPO -ComputerName <Name of the PC>
```

> Active GPOs on machine.

**Command** ([[commands/find-gpo-computer-admin]]):
```powershell
Find-GPOComputerAdmin -ComputerName <ComputerName>
```

> Local admins from GPO. Expected: Admin users.

### Step 8: Enumerate OUs and Specific GPOs

**Context**: Map organizational units and retrieve specific GPO details.

**Command** ([[commands/get-net-ou-fulldata]]):
```powershell
Get-NetOU -FullData
```

> All OUs. Expected: OU structure.

**Command** ([[commands/get-net-gpo-gponame]]):
```powershell
Get-NetGPO -GPOname <The GUID of the GPO>
```

> Specific GPO.

### Step 9: Enumerate ACLs and ACEs

**Context**: Scan for permissive ACLs indicating weak permissions for escalation.

**Command** ([[commands/get-object-acl-samaccountname]]):
```powershell
Get-ObjectAcl -SamAccountName <AccountName> -ResolveGUIDs
```

> Account ACLs.

**Command** ([[commands/get-object-acl-adsprefix]]):
```powershell
Get-ObjectAcl -ADSprefix 'CN=Administrator, CN=Users' -Verbose
```

> Object ACLs.

**Command** ([[commands/invoke-aclscanner]]):
```powershell
Invoke-ACLScanner -ResolveGUIDs
```

> Interesting ACEs. Expected: Abusable permissions.

**Command** ([[commands/get-path-acl-share]]):
```powershell
Get-PathAcl -Path "\\Path\Of\A\Share"
```

> Share ACLs.

### Step 10: Enumerate Domain Trusts

**Context**: Discover trusts for cross-domain attacks.

**Command** ([[commands/get-net-domain-trust]]):
```powershell
Get-NetDomainTrust
```

> Current domain trusts.

**Command** ([[commands/get-net-domain-trust-domain]]):
```powershell
Get-NetDomainTrust -Domain <DomainName>
```

> Specific domain.

### Step 11: Enumerate Forest Domains and Trusts

**Context**: Map the entire forest for broader scope.

**Command** ([[commands/get-net-forest-domain]]):
```powershell
Get-NetForestDomain
```

> Forest domains.

**Command** ([[commands/get-net-forest-domain-forest]]):
```powershell
Get-NetForestDomain Forest <ForestName>
```

> Specific forest.

**Command** ([[commands/get-net-forest-trust]]):
```powershell
Get-NetForestTrust
```

> Forest trusts.

**Command** ([[commands/get-net-domain-trust-forest]]):
```powershell
Get-NetDomainTrust -Forest <ForestName>
```

> Forest trust map.

### Step 12: Find Admin Access and Sessions

**Context**: Locate machines with admin access or DA sessions for lateral movement.

**Command** ([[commands/find-local-admin-access]]):
```powershell
Find-LocalAdminAccess -Verbose
```

> Current user admin machines.

**Command** ([[commands/invoke-enumerate-local-admin]]):
```powershell
Invoke-EnumerateLocalAdmin -Verbose
```

> All local admins.

**Command** ([[commands/invoke-userhunter]]):
```powershell
Invoke-UserHunter
```

> DA sessions.

**Command** ([[commands/invoke-userhunter-groupname]]):
```powershell
Invoke-UserHunter -GroupName "RDPUsers"
```

> Specific group.

**Command** ([[commands/invoke-userhunter-stealth]]):
```powershell
Invoke-UserHunter -Stealth
```

> Stealth mode.

**Command** ([[commands/invoke-userhunter-check-access]]):
```powershell
Invoke-UserHunter -CheckAccess
```

> Verify access.
