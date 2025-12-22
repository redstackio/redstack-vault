---
id: 64a1000d-77f7-43f5-9f87-be377120e9da
name: active-directory-recon-using-ad-module
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:02.472447+00:00'
updated_at: '2023-04-10T20:36:08.291570+00:00'
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
  - '[[tags/Using AD Module]]'
commands:
  - '[[commands/enumerate-domains-of-forest]]'
  - '[[commands/get-ad-forest-default]]'
  - '[[commands/get-ad-forest-by-identity]]'
  - '[[commands/get-all-ad-computers]]'
  - '[[commands/get-all-ad-groups]]'
  - '[[commands/get-all-properties-of-specific-user]]'
  - '[[commands/get-details-of-specific-ad-trust]]'
  - '[[commands/get-ad-domain-controller-default]]'
  - '[[commands/get-specific-domain-controller-information]]'
  - '[[commands/get-user-with-specific-string-in-description]]'
  - '[[commands/list-all-ad-trusts-in-domain]]'
  - '[[commands/get-applocker-policy-rule-collections]]'
platforms:
  - Windows
tools: []
validated: true
---

# active-directory-recon-using-ad-module

## Summary

This procedure uses the Active Directory PowerShell module to perform comprehensive reconnaissance on an Active Directory environment, gathering details on domain controllers, users, computers, groups, trust relationships, forests, and AppLocker policies to map the network structure and identify potential attack vectors.

## Description

Active Directory reconnaissance with the AD Module involves leveraging PowerShell cmdlets to query the directory service for critical information. This technique is commonly used during the discovery phase of an attack to understand the domain topology, enumerate assets, and spot misconfigurations or weak points for lateral movement or privilege escalation. It requires domain-joined access or valid credentials and assumes the AD Module is available, typically on Windows Server or via RSAT on client machines. The output provides insights into the environment's scale, trust boundaries, and policy enforcement, aiding in planning subsequent exploits like pass-the-hash or Kerberoasting.

## Requirements

1. Valid domain user credentials with read access to Active Directory objects.
2. PowerShell execution policy allowing script execution (e.g., RemoteSigned or Unrestricted).
3. Active Directory PowerShell module installed (part of RSAT or Windows Server features).
4. Network connectivity to a domain controller on ports 389 (LDAP) or 636 (LDAPS).

## Defense

- Restrict AD Module usage to privileged administrative accounts via Group Policy or just-in-time access.
- Enable PowerShell logging (Module, Script Block, and Transcription) to monitor cmdlet invocations.
- Implement behavioral analytics to detect anomalous AD queries from non-administrative accounts.
- Use tools like Microsoft Defender for Identity to alert on reconnaissance patterns.

## Objectives

1. Enumerate domain controllers, users, computers, and groups to build an asset inventory.
2. Discover trust relationships and forest structure to identify expansion opportunities.
3. Extract policy details like AppLocker to assess enforcement gaps.
4. Compile a complete view of the AD environment for targeted follow-on attacks.

## Instructions

### Step 1: Enumerate Domain Controllers

**Context**: Start by identifying domain controllers in the current or specified domain to understand the authentication infrastructure and potential high-value targets.

**Command** ([[commands/get-ad-domain-controller-default]]):
```powershell
Get-ADDomainController
```

> This cmdlet retrieves all domain controllers in the current domain. For a specific domain, use the -Identity parameter. Expected output includes details like name, site, and IPv4 address.

**Command** ([[commands/get-specific-domain-controller-information]]):
```powershell
Get-ADDomainController -Identity <DomainName>
```

> Specify the domain name with -Identity to filter results. Success is indicated by a list of DC objects with properties like OperatingSystem and IsGlobalCatalog.

### Step 2: Enumerate Users and Search for Specific Attributes

**Context**: Query user accounts to gather details on personnel and search for indicators like keywords in descriptions that may reveal sensitive information or backdoors.

**Command** ([[commands/get-all-properties-of-specific-user]]):
```powershell
Get-ADUser -Identity <user> -Properties *
```

> Use -Identity to target a specific user and -Properties * to retrieve all attributes. This helps profile individual accounts. Expected output: Full user object with attributes like email, lastLogon, and memberOf.

**Command** ([[commands/get-user-with-specific-string-in-description]]):
```powershell
Get-ADUser -Filter 'Description -like "*wtver*"' -Properties Description | Select-Object Name, Description
```

> The -Filter parameter uses LDAP syntax to match patterns in attributes. Pipe to Select-Object for focused output. Success: List of matching users with their descriptions.

### Step 3: Enumerate Computers and Groups

**Context**: List all computer objects and security groups to map the asset base and membership hierarchies, revealing potential lateral movement paths.

**Command** ([[commands/get-all-ad-computers]]):
```powershell
Get-ADComputer -Filter * -Properties *
```

> -Filter * retrieves all computers; -Properties * expands attributes like operatingSystem and lastLogonTimestamp. Expected: Comprehensive list of computer objects for inventory.

**Command** ([[commands/get-all-ad-groups]]):
```powershell
Get-ADGroup -Filter *
```

> Enumerates all groups without extra properties for a quick overview. For details, add -Properties *. Success: Group names and categories (e.g., Domain Local, Global).

### Step 4: Enumerate Domain Trusts

**Context**: Identify trust relationships to discover interconnected domains or forests that could be pivoted to during an attack.

**Command** ([[commands/list-all-ad-trusts-in-domain]]):
```powershell
Get-ADTrust -Filter *
```

> Retrieves all trusts in the current domain. Output includes trust type (e.g., Forest, External) and direction (Inbound/Outbound).

**Command** ([[commands/get-details-of-specific-ad-trust]]):
```powershell
Get-ADTrust -Identity <DomainName>
```

> Targets a specific trust for deeper details like trustAttributes and whenCreated. Use if initial enumeration reveals interesting trusts.

### Step 5: Enumerate Forest and Domains

**Context**: Query the forest to understand the higher-level structure, including child domains, which informs cross-domain attacks.

**Command** ([[commands/get-ad-forest-default]]):
```powershell
Get-ADForest
```

> Gets properties of the current forest, such as Domains and TopLevelName. Expected: Forest object with schema, domain, and application partitions.

**Command** ([[commands/get-ad-forest-by-identity]]):
```powershell
Get-ADForest -Identity <ForestName>
```

> Specifies a forest for targeted query. Useful in multi-forest environments.

**Command** ([[commands/enumerate-domains-of-forest]]):
```powershell
(Get-ADForest).Domains
```

> Extracts just the domain list from the forest object. Success: Array of domain names for quick reference.

### Step 6: Retrieve AppLocker Policy Details

**Context**: Check AppLocker configurations to evaluate application whitelisting enforcement, which could indicate bypass opportunities.

**Command** ([[commands/get-applocker-policy-rule-collections]]):
```powershell
Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections
```

> Fetches the effective AppLocker policy and expands rule collections. Expected output: Details on executable, script, and MSI rules, including enforcement mode.
