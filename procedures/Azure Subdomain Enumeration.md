---
id: 2e1ba3e3-cdcc-4975-b43d-22d735f09387
name: Azure Subdomain Enumeration
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:14.879645+00:00'
updated_at: '2023-05-23T16:52:02.616495+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
platforms:
- Cloud
tags:
- '[[Cloud - Azure]]'
- '[[Enumerate Azure Subdomains]]'
- '[[Enumeration]]'
- '[[Searching for subdomains]]'
- '[[Subdomains Enumeration]]'
commands:
- '[[Enumerate Azure Subdomains]]'
---

# Azure Subdomain Enumeration

**Status**: ✓ Verified

## Summary

Azure Subdomain Enumeration is a technique used to discover subdomains within an Azure environment. This technique can be used by an attacker to identify potential targets for further attacks, such as phishing or domain hijacking. To perform this technique, an attacker would use various tools and m

## Description

# Description

Azure Subdomain Enumeration is a technique used to discover subdomains within an Azure environment. This technique can be used by an attacker to identify potential targets for further attacks, such as phishing or domain hijacking. To perform this technique, an attacker would use various tools and methods to enumerate subdomains within the Azure environment. This can include using DNS queries, web scraping, and other reconnaissance methods. From there, the attacker can use the discovered subdomains to target specific services or applications within the Azure environment.

## Requirements

1. Access to the Azure environment

1. Tools for subdomain enumeration

## Defense

1. Implement strong access controls to limit access to the Azure environment

1. Monitor DNS queries and traffic for suspicious activity

1. Regularly review and update DNS records to ensure only authorized subdomains are in use

## Objectives

1. Discover subdomains within an Azure environment

1. Identify potential targets for further attacks

1. Target specific services or applications within the Azure environment

# Instructions

1. To use this command, first open PowerShell and navigate to the directory where the InvokeEnumerateAzureSubDomains.ps1 script is saved.

Replace <TENANT NAME> with the name of your Azure tenant.

This command will return a list of subdomains and their corresponding services.

**Code**: [[PS> . C:\Tools\MicroBurst\Misc\InvokeEnumerateAzur]]

> This command is used to enumerate the subdomains associated with an Azure tenant. The -Base parameter specifies the name of the tenant. The -Verbose parameter causes the command to display detailed information about the subdomains and their associated services. The output of this command includes a table that lists each subdomain and the service it corresponds to.

**Command** ([[Enumerate Azure Subdomains]]):

```powershell
PS> . C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureSubDomains.ps1
PS> Invoke-EnumerateAzureSubDomains -Base <TENANT NAME> -Verbose

```

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

## Commands Used

- [[Enumerate Azure Subdomains]]

## Tags

- [[Cloud - Azure]]
- [[Enumerate Azure Subdomains]]
- [[Enumeration]]
- [[Searching for subdomains]]
- [[Subdomains Enumeration]]
