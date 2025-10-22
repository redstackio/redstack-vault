---
id: 44e640be-8a14-4022-8ed6-caaee1460485
name: Azure Retrieving Passwords using Microburst
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.369848+00:00'
updated_at: '2023-05-24T19:52:38.532026+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Cloud - Azure]]'
- '[[Stealing Tokens]]'
commands:
- '[[Import the Microburst Module into Powershell]]'
- '[[Retrieve Azure Passwords in a graphical grid with Microburst]]'
- '[[Retrieve Azure Passwords with Microburst]]'
---

# Azure Retrieving Passwords using Microburst

**Status**: ✓ Verified

## Summary

This procedure guides you through the process of using the Microburst  PowerShell module to retrieve Azure passwords. The Microburst module  provides cmdlets specifically designed for managing Azure passwords. By  following these steps, you can easily retrieve Azure passwords and view  them in an o

## Description

# Description

This procedure guides you through the process of using the Microburst  PowerShell module to retrieve Azure passwords. The Microburst module  provides cmdlets specifically designed for managing Azure passwords. By  following these steps, you can easily retrieve Azure passwords and view  them in an organized manner using the Out-GridView cmdlet. By using this tool, attackers can gain access to user accounts, cloud resources, and sensitive data. This tool is often used in combination with other attacks, such as phishing or social engineering, to gain initial access to the target environment. Once the attacker has stolen the tokens, they can use them to move laterally within the environment and escalate privileges.

## Requirements

To successfully execute this procedure, ensure the following prerequisites:

- PowerShell is installed and accessible.

- The Microburst module is installed and imported.

## Defense

1. Implement multi-factor authentication to prevent attackers from using stolen passwords and tokens

1. Monitor for suspicious activity, such as unusual login attempts or access to sensitive data

1. Regularly review and update access controls and permissions to prevent unauthorized access

## Objectives

1. Steal Azure tokens and passwords

1. Gain access to user accounts, cloud resources, and sensitive data

1. Move laterally within the environment and escalate privileges

# Instructions

<u>*Overvie</u>w*

**Code**: [[# Import the module
Import-Module Microburst.psm1
]]

> The 'Get-AzurePasswords' command imports the 'Microburst' PowerShell module and retrieves the Azure passwords. The 'Out-GridView' command is used to display the passwords in a graphical interface. The '-Verbose' flag can be used to display more detailed information about the password retrieval process.

## Steps

1. Import the Microburst Module

**Command** ([[Import the Microburst Module into Powershell]]):

```bash
Import-Module Microburst.psm1
```

2. Get Azure Passwords

**Command** ([[Retrieve Azure Passwords with Microburst]]):

```bash
Get-AzurePasswords
```

3. (Optional) Retrieve Azure Passwords in a graphical grid

**Command** ([[Retrieve Azure Passwords in a graphical grid with Microburst]]):

```bash
Get-AzurePasswords -Verbose | Out-GridView
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Import the Microburst Module into Powershell]]
- [[Retrieve Azure Passwords in a graphical grid with Microburst]]
- [[Retrieve Azure Passwords with Microburst]]

## Tags

- [[Cloud - Azure]]
- [[Stealing Tokens]]
