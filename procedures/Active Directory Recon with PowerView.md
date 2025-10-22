---
id: 75259ce4-8697-4efc-b6b0-10b544ee0c63
name: Active Directory Recon with PowerView
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.288090+00:00'
updated_at: '2023-04-06T21:33:38.749304+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Active Scanning|T1595 - Active Scanning]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Recon]]'
- '[[Using PowerView]]'
commands:
- '[[Check ACLs for specified path]]'
- '[[Check last password change]]'
- '[[Confirm admin access]]'
- '[[Enumerate domain machines of the current/specified domain where specific users
  are logged into]]'
- '[[Enumerate Domain Shares]]'
- '[[Enumerate Domain Shares with User Access]]'
- '[[Enumerate Forest Domains]]'
- '[[Enumerate Group Members]]'
- '[[Enumerate Session Information for a machine]]'
- '[[Enumerate user logged on a machine]]'
- '[[Find computers where a Domain Admin OR a specified user has a session]]'
- '[[Find local admins on all machines of the domain]]'
- '[[Find machines where current user has local admin access]]'
- '[[Find-UserField]]'
- '[[Get ACLs for specified account]]'
- '[[Get ACLs with ADSPrefix]]'
- '[[Get Active Policy on Machine]]'
- '[[Get Domain Controllers]]'
- '[[Get Domain Controllers for a specific domain]]'
- '[[Get GPOs Modifying Local Group Memberships]]'
- '[[Get Group Members]]'
- '[[Get Kerberos Policy Configuration]]'
- '[[Get Net Domain Trust]]'
- '[[Get Net Domain Trust with Domain Name]]'
- '[[Get-NetGPO]]'
- '[[Get-NetOU]]'
- '[[Get-NetUser]]'
- '[[Get-NetUser with SamAccountName]]'
- '[[Get-NetUser with select]]'
- '[[Get System Access Policy Configuration]]'
- '[[Get-UserProperty]]'
- '[[Get Users in Local Admin Group]]'
- '[[Map Forest Trust]]'
- '[[Retrieve Domain Policy Configurations]]'
- '[[Search for interesting ACEs]]'
---

# Active Directory Recon with PowerView

## Summary

Active Directory Recon with PowerView is a technique used to gather information about an organization's Active Directory environment. This technique involves using the PowerView PowerShell module to perform reconnaissance on the domain. By using PowerView, an attacker can enumerate domain users, co

## Description

# Description

Active Directory Recon with PowerView is a technique used to gather information about an organization's Active Directory environment. This technique involves using the PowerView PowerShell module to perform reconnaissance on the domain. By using PowerView, an attacker can enumerate domain users, computers, groups, and shares. This information can be used to identify potential targets for further attacks, such as password spraying or privilege escalation. Additionally, PowerView can be used to identify domain trusts, which can be leveraged to gain access to other domains in the forest.

From a technical perspective, PowerView uses LDAP queries to gather information about the domain. The module can be used to enumerate domain users, computers, groups, and shares. It can also be used to identify domain trusts and other information about the domain.

The business value of this technique lies in its ability to identify potential targets for further attacks. By identifying vulnerable computers, users, and groups, an attacker can focus their efforts on those targets that are most likely to result in a successful compromise.

## Requirements

1. Access to a domain-joined Windows machine

1. PowerView PowerShell module

## Defense

1. Limit user privileges to reduce the impact of a compromise

1. Monitor network traffic for suspicious activity

1. Implement strong password policies to prevent password spraying attacks

## Objectives

1. Gather information about the target Active Directory environment

1. Identify potential targets for further attacks

1. Identify domain trusts and other information about the domain

# Instructions

1. Use this command to retrieve the policy configurations of the Domain about system access or kerberos.

**Code**: [[Get-DomainPolicy

#This command is used to retriev]]

> The command 'Get-DomainPolicy' is used to retrieve the policy configurations of the Domain about system access or kerberos. The command can be used to retrieve specific policy configurations by using the commands '(Get-DomainPolicy)."system access"' or '(Get-DomainPolicy)."kerberos policy"'. The first command retrieves the system access policy configuration and the second command retrieves the kerberos policy configuration.

**Command** ([[Retrieve Domain Policy Configurations]]):

```bash
Get-DomainPolicy
```

**Command** ([[Get System Access Policy Configuration]]):

```bash
(Get-DomainPolicy)."system access"
```

**Command** ([[Get Kerberos Policy Configuration]]):

```bash
(Get-DomainPolicy)."kerberos policy"
```

2. Use the Get-NetDomainController command to retrieve information about domain controllers in the current domain or a specified domain. Use the -Domain parameter to specify the domain name.

**Code**: [[Get-NetDomainController
Get-NetDomainController -D]]

> This command retrieves information about domain controllers in the specified domain. This can include details such as the domain controller's name, site name, IP address, operating system version, and more. By specifying the -Domain parameter, you can retrieve information about domain controllers in a specific domain. If you do not specify the -Domain parameter, information about domain controllers in the current domain will be returned.

**Command** ([[Get Domain Controllers]]):

```bash
Get-NetDomainController
```

**Command** ([[Get Domain Controllers for a specific domain]]):

```bash
Get-NetDomainController -Domain <DomainName>
```

3. Use the following commands to enumerate domain users:

**Code**: [[Get-NetUser
Get-NetUser -SamAccountName <user> 
Ge]]

> The provided commands can be used to retrieve various details about domain users. Get-NetUser can be used to retrieve information about all domain users or a specific user. Get-UserProperty can be used to check the last password change. Find-UserField can be used to search for a specific string on a user's attribute. Get-NetLoggedon and Get-NetSession can be used to enumerate user sessions and machines. Find-DomainUserLocation can be used to find domain machines where specific users are logged into. The output of Find-DomainUserLocation includes the username and the session information.

**Command** ([[Get-NetUser]]):

```bash
Get-NetUser
```

**Command** ([[Get-NetUser with SamAccountName]]):

```bash
Get-NetUser -SamAccountName <user>
```

**Command** ([[Get-NetUser with select]]):

```bash
Get-NetUser | select cn
```

**Command** ([[Get-UserProperty]]):

```bash
Get-UserProperty
```

**Command** ([[Check last password change]]):

```bash
Get-UserProperty -Properties pwdlastset
```

**Command** ([[Find-UserField]]):

```bash
Find-UserField -SearchField Description -SearchTerm "wtver"
```

**Command** ([[Enumerate user logged on a machine]]):

```bash
Get-NetLoggedon -ComputerName <ComputerName>
```

**Command** ([[Enumerate Session Information for a machine]]):

```bash
Get-NetSession -ComputerName <ComputerName>
```

**Command** ([[Enumerate domain machines of the current/specified domain where specific users are logged into]]):

```bash
Find-DomainUserLocation -Domain <DomainName> | Select-Object UserName, SessionFromName
```

4. This command is used to enumerate all the computers in the domain. It retrieves the full data of the computers and groups in the domain. It also pings and enumerates the live machines in the domain.

**Code**: [[Get-NetComputer -FullData
Get-DomainGroup

#Enumer]]

> The `Get-NetComputer` command is used to retrieve information about the computers in the domain. The `-FullData` parameter retrieves all the information available about the computers. The `Get-DomainGroup` command retrieves all the groups in the domain. The `-Ping` parameter of the `Get-NetComputer` command is used to ping and retrieve information about the live machines in the domain.

5. Replace <GroupName> and <DomainName> with the name of the group and domain you want to enumerate.

**Code**: [[Get-NetGroupMember -GroupName "<GroupName>" -Domai]]

> This command retrieves the members of a specified group of the domain, as well as all the GPOs in a domain that modify local group memberships through Restricted Groups or Group Policy Preferences. This information can be helpful for troubleshooting group membership issues or identifying potential security vulnerabilities.

**Command** ([[Get Group Members]]):

```bash
Get-NetGroupMember -GroupName "<GroupName>" -Domain <DomainName>
```

**Command** ([[Enumerate Group Members]]):

```bash
Get-DomainGroup -Identity <GroupName> | Select-Object -ExpandProperty Member
```

**Command** ([[Get GPOs Modifying Local Group Memberships]]):

```bash
Get-DomainGPOLocalGroup | Select-Object GPODisplayName, GroupName
```

6. Use the Find-DomainShare command to enumerate domain shares. This command can be used to identify all shares on a domain or to specifically identify shares that the current user has access to. To enumerate all shares, simply run the command without any additional arguments. To identify shares that the current user has access to, use the -CheckShareAccess argument.

**Code**: [[#Enumerate Domain Shares
Find-DomainShare

#Enumer]]

> The Find-DomainShare command is used to enumerate domain shares. This command can be useful for identifying shares that may be accessible to an attacker or shares that may contain sensitive information. The -CheckShareAccess argument can be used to specifically identify shares that the current user has access to. This can be useful for identifying shares that may contain sensitive information that the current user should not have access to. Overall, this command can be a useful tool for identifying potential attack vectors or for auditing share permissions on a domain.

**Command** ([[Enumerate Domain Shares]]):

```bash
Find-DomainShare
```

**Command** ([[Enumerate Domain Shares with User Access]]):

```bash
Find-DomainShare -CheckShareAccess
```

7. Use this command to retrieve information about the Group Policies that are currently active on a specified machine. You can also use this command to find the users that are part of a machine's local admin group.

**Code**: [[Get-NetGPO

# Shows active Policy on specified mac]]

> The `Get-NetGPO` command is used to retrieve information about the Group Policies that are currently active on a specified machine. The `-ComputerName` parameter is used to specify the name of the machine you want to retrieve information about. The `Get-NetGPOGroup` command is used to retrieve information about the Group Policy Objects (GPOs) that are currently active on the specified machine. The `Find-GPOComputerAdmin` command is used to find the users that are part of a machine's local admin group. The `-ComputerName` parameter is used to specify the name of the machine you want to retrieve information about.

**Command** ([[Get Active Policy on Machine]]):

```bash
Get-NetGPO -ComputerName <Name of the PC>
```

**Command** ([[Get Users in Local Admin Group]]):

```bash
Find-GPOComputerAdmin -ComputerName <ComputerName>
```

8. This command will retrieve all the OUs in the current domain and display their full data. 

To get a specific GPO by GUID, replace '<The GUID of the GPO>' with the actual GUID of the GPO you want to retrieve.

**Code**: [[Get-NetOU -FullData 
Get-NetGPO -GPOname <The GUID]]

> The 'Get-NetOU' command retrieves all the OUs in the current domain and displays their full data, including the distinguished name, object class, object GUID, and other attributes.

The 'Get-NetGPO' command retrieves a specific GPO by its GUID and displays its properties, including the display name, domain name, GPO status, and other details.

**Command** ([[Get-NetOU]]):

```bash
Get-NetOU -FullData
```

**Command** ([[Get-NetGPO]]):

```bash
Get-NetGPO -GPOname <The GUID of the GPO>
```

9. Use this command to enumerate the Access Control Lists (ACLs) associated with a specified account or path. The command can be used to retrieve ACLs for a specific account by providing the account name or for a specific path by providing the path to the share. The command can also be used to search for interesting Access Control Entries (ACEs) using the Invoke-ACLScanner function.

**Code**: [[# Returns the ACLs associated with the specified a]]

> -SamAccountName: Specifies the name of the account for which to retrieve the ACLs.
-ADSprefix: Specifies the LDAP prefix of the Active Directory object for which to retrieve the ACLs.
-Verbose: Specifies that detailed information about the ACLs should be displayed.
-ResolveGUIDs: Specifies that the output should contain the resolved GUIDs for any SIDs present in the ACLs.
-Path: Specifies the path to the share for which to retrieve the ACLs.

**Command** ([[Get ACLs for specified account]]):

```bash
Get-ObjectAcl -SamAccountName <AccountName> -ResolveGUIDs
```

**Command** ([[Get ACLs with ADSPrefix]]):

```bash
Get-ObjectAcl -ADSprefix 'CN=Administrator, CN=Users' -Verbose
```

**Command** ([[Search for interesting ACEs]]):

```bash
Invoke-ACLScanner -ResolveGUIDs
```

**Command** ([[Check ACLs for specified path]]):

```bash
Get-PathAcl -Path "\\Path\Of\A\Share"
```

10. Use the Get-NetDomainTrust command to enumerate the trust relationships between domains.

**Code**: [[Get-NetDomainTrust
Get-NetDomainTrust -Domain <Dom]]

> The Get-NetDomainTrust command can be used to retrieve information about the trust relationships between domains in an Active Directory forest. The command can be run without any parameters to retrieve information about all trust relationships in the forest, or you can specify a domain using the -Domain parameter to retrieve information about the trust relationships for a specific domain. The output of the command includes information about the trust type, direction, and status, as well as the domain and forest names of the trusted domain.

**Command** ([[Get Net Domain Trust]]):

```bash
Get-NetDomainTrust
```

**Command** ([[Get Net Domain Trust with Domain Name]]):

```bash
Get-NetDomainTrust -Domain <DomainName>
```

11. To enumerate the trust relationships of a forest, use the Get-NetForestDomain and Get-NetForestTrust commands. First, use Get-NetForestDomain to enumerate the domains in the forest. Then, use Get-NetForestTrust to map the trust relationships of the forest. You can specify the forest name using the Forest parameter.

**Code**: [[Get-NetForestDomain
Get-NetForestDomain Forest <Fo]]

> The Get-NetForestDomain command is used to enumerate the domains in a forest. You can use the Forest parameter to specify the name of the forest to enumerate. The Get-NetForestTrust command is used to map the trust relationships of a forest. You can use the Forest parameter to specify the name of the forest to map. The Get-NetDomainTrust command can also be used to map the trust relationships of a forest by specifying the Forest parameter with the name of the forest.

**Command** ([[Enumerate Forest Domains]]):

```bash
Get-NetForestDomain
Get-NetForestDomain Forest <ForestName>
```

**Command** ([[Map Forest Trust]]):

```bash
Get-NetForestTrust
Get-NetDomainTrust -Forest <ForestName>
```

12. The following commands can be used to find machines on the current domain where the current user has local admin access, find local admins on all machines of the domain, find computers where a Domain Admin or a specified user has a session, and confirm admin access.

**Code**: [[#Finds all machines on the current domain where th]]

> 1. Find-LocalAdminAccess -Verbose: This command finds all machines on the current domain where the current user has local admin access.

2. Invoke-EnumerateLocalAdmin -Verbose: This command finds local admins on all machines of the domain.

3. Invoke-UserHunter: This command finds computers where a Domain Admin or a specified user has a session. It can be used with the -GroupName flag to specify a group name, or with the -Stealth flag to run the command in stealth mode.

4. Invoke-UserHunter -CheckAccess: This command confirms admin access.

**Command** ([[Find machines where current user has local admin access]]):

```bash
Find-LocalAdminAccess -Verbose
```

**Command** ([[Find local admins on all machines of the domain]]):

```bash
Invoke-EnumerateLocalAdmin -Verbose
```

**Command** ([[Find computers where a Domain Admin OR a specified user has a session]]):

```bash
Invoke-UserHunter
Invoke-UserHunter -GroupName "RDPUsers"
Invoke-UserHunter -Stealth
```

**Command** ([[Confirm admin access]]):

```bash
Invoke-UserHunter -CheckAccess
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Active Scanning|T1595 - Active Scanning]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]

## Commands Used

- [[Check ACLs for specified path]]
- [[Check last password change]]
- [[Confirm admin access]]
- [[Enumerate domain machines of the current/specified domain where specific users are logged into]]
- [[Enumerate Domain Shares]]
- [[Enumerate Domain Shares with User Access]]
- [[Enumerate Forest Domains]]
- [[Enumerate Group Members]]
- [[Enumerate Session Information for a machine]]
- [[Enumerate user logged on a machine]]
- [[Find computers where a Domain Admin OR a specified user has a session]]
- [[Find local admins on all machines of the domain]]
- [[Find machines where current user has local admin access]]
- [[Find-UserField]]
- [[Get ACLs for specified account]]
- [[Get ACLs with ADSPrefix]]
- [[Get Active Policy on Machine]]
- [[Get Domain Controllers]]
- [[Get Domain Controllers for a specific domain]]
- [[Get GPOs Modifying Local Group Memberships]]
- *...and 15 more*

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Recon]]
- [[Using PowerView]]
