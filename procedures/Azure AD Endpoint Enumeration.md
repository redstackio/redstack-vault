---
id: 71541f6a-8c18-4dce-aeb0-a288ef4facae
name: Azure AD Endpoint Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:15.960864+00:00'
updated_at: '2023-04-10T20:19:36.224933+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Application Endpoint]]'
- '[[Cloud - Azure]]'
commands:
- '[[Enumerate possible endpoints for applications starting/ending with PREFIX]]'
---

# Azure AD Endpoint Enumeration

## Summary

Azure AD Endpoint Enumeration is a technique used to identify Azure AD endpoints associated with a specific PREFIX. This technique can be used to discover additional targets that may be of interest to an attacker. By using the List Azure AD endpoints with PREFIX command, an attacker can quickly ide

## Description

# Description

Azure AD Endpoint Enumeration is a technique used to identify Azure AD endpoints associated with a specific PREFIX. This technique can be used to discover additional targets that may be of interest to an attacker. By using the List Azure AD endpoints with PREFIX command, an attacker can quickly identify all endpoints that match a specific prefix. This technique can be used for reconnaissance purposes to gather information about a target's infrastructure.

 

## Requirements

1. Valid Azure AD credentials

1. Network access to Azure AD

 

## Defense

1. Limit access to Azure AD to only authorized personnel

1. Regularly review Azure AD logs for suspicious activity

1. Implement network segmentation to limit lateral movement within the network

 

## Objectives

1. Identify Azure AD endpoints associated with a specific PREFIX

 

# Instructions

1. To list Azure AD endpoints with PREFIX, run the following commands in PowerShell:

 



**Code**: [[# Enumerate possible endpoints for applications st]]



> This command will retrieve a list of possible endpoints for applications starting with PREFIX by using the Get-AzureADServicePrincipal command with the -Filter parameter set to "startswith(displayName,'PREFIX')". The command will then pipe the output to the ForEach-Object cmdlet and retrieve the ReplyUrls property of each service principal.

The second command will retrieve a list of possible endpoints for applications ending with PREFIX by using the Get-AzureADApplication command with the -Filter parameter set to "endswith(displayName,'PREFIX')". The command will then select the ReplyUrls, WwwHomePage, and HomePage properties of each application.



**Command** ([[Enumerate possible endpoints for applications starting/ending with PREFIX]]):

```bash
Get-AzureADServicePrincipal -All $true -Filter "startswith(displayName,'PREFIX')" | % {$_.ReplyUrls}
Get-AzureADApplication -All $true -Filter "endswith(displayName,'PREFIX')" | Select-Object ReplyUrls,WwwHomePage,HomePage
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Enumerate possible endpoints for applications starting/ending with PREFIX]]

## Tags

- [[Application Endpoint]]
- [[Cloud - Azure]]


