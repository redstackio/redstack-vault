---
id: e537246f-df47-437c-985f-23ca94dadb15
name: Password Looting from SharePoint and SMB Shares
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.955905+00:00'
updated_at: '2023-04-10T20:37:31.822008+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Search for file contents]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Retrieve token using AADInternals]]'
- '[[Retrieve token using SnaffPoint binary]]'
- '[[Search on Sharepoint using search string in command line]]'
- '[[Search on Sharepoint using search strings in ./presets dir]]'
---

# Password Looting from SharePoint and SMB Shares

## Summary

Password looting from SharePoint and SMB shares is a method of escalating privileges on a Windows system. This technique involves searching for files containing sensitive information, such as passwords, within SharePoint and SMB shares. By successfully finding and stealing these passwords, an attac

## Description

# Description

Password looting from SharePoint and SMB shares is a method of escalating privileges on a Windows system. This technique involves searching for files containing sensitive information, such as passwords, within SharePoint and SMB shares. By successfully finding and stealing these passwords, an attacker can use them to escalate their privileges on the system and gain access to sensitive data. This technique is commonly used by attackers who have already gained access to a system and are looking to elevate their privileges to gain more control over the network.

From a technical perspective, this technique involves using built-in Windows tools such as PowerShell and command prompt to search for files containing sensitive information. Once these files are found, they can be copied to a location where the attacker can access them. This technique can be used to target specific users or groups within an organization, making it an effective way to gain access to sensitive data.

The business value of this technique is that it allows attackers to gain access to sensitive data and systems within an organization. This can lead to data theft, financial loss, and reputational damage.

## Requirements

1. Access to SharePoint and SMB shares

1. Authentication credentials with sufficient privileges

1. Ability to run PowerShell and command prompt

## Defense

1. Limit access to SharePoint and SMB shares to only those who need it

1. Use strong passwords and multi-factor authentication to protect authentication credentials

1. Monitor file access and usage for unusual activity

## Objectives

1. To escalate privileges on a Windows system

1. To gain access to sensitive data and systems within an organization

# Instructions

1. To search for files in remote locations such as SMB Shares and SharePoint, you can use the SnaffPoint binary. First, retrieve an access token using either the SnaffPoint binary or AADInternals. Then, use the token to search on SharePoint by providing the URL and the token to the SnaffPoint binary. You can also use search strings in the ./presets directory or in the command line with the -q flag. To use FQL search, use the -l flag.

**Code**: [[# First, retrieve a token
## Method 1: using Snaff]]

> This command provides instructions on how to search for files in remote locations such as SMB Shares and SharePoint using the SnaffPoint binary. It explains how to retrieve an access token using either the SnaffPoint binary or AADInternals and how to use the token to search on SharePoint. It also explains how to use search strings in the ./presets directory or in the command line with the -q flag, and how to use FQL search with the -l flag.

**Command** ([[Retrieve token using SnaffPoint binary]]):

```bash
$token = (.\GetBearerToken.exe https://your.sharepoint.com)
```

**Command** ([[Retrieve token using AADInternals]]):

```bash
Install-Module AADInternals -Scope CurrentUser
Import-Module AADInternals
$token = (Get-AADIntAccessToken -ClientId "9bc3ab49-b65d-410a-85ad-de819febfddc" -Tenant "your.onmicrosoft.com" -Resource "https://your.sharepoint.com")
```

**Command** ([[Search on Sharepoint using search strings in ./presets dir]]):

```bash
.\SnaffPoint.exe -u "https://your.sharepoint.com" -t $token
```

**Command** ([[Search on Sharepoint using search string in command line]]):

```bash
.\SnaffPoint.exe -u "https://your.sharepoint.com" -t $token -l -q "filename:.config"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Retrieve token using AADInternals]]
- [[Retrieve token using SnaffPoint binary]]
- [[Search on Sharepoint using search string in command line]]
- [[Search on Sharepoint using search strings in ./presets dir]]

## Tags

- [[EoP - Looting for passwords]]
- [[Search for file contents]]
- [[Windows - Privilege Escalation]]
