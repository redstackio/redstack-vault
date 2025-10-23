---
id: e70cde78-e6f7-45a9-b86f-28bf0c31f26a
name: Azure O365 Email Enumeration
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:14.829481+00:00'
updated_at: '2023-05-28T04:04:53.093358+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Active Scanning|T1595 - Active Scanning]]'
- '[[Search Open Websites/Domains|T1593 - Search Open Websites/Domains]]'
platforms:
- Cloud
tags:
- '[[Cloud - Azure]]'
- '[[Email]]'
- '[[Enumerate valid emails]]'
- '[[Enumeration]]'
- '[[o365]]'
- '[[Office 365]]'
commands:
- '[[Run o365creeper.py on emails.txt]]'
---

# Azure O365 Email Enumeration

**Status**: ✓ Verified

## Summary

Azure Email Enumeration is a technique used to identify valid email addresses associated with an Azure tenant. This technique is commonly used by attackers to gather information for spear-phishing campaigns, or to identify potential targets for further attacks. To perform this technique, an attacke

## Description

# Description

Azure Email Enumeration is a technique used to identify valid email addresses associated with an Azure tenant. This technique is commonly used by attackers to gather information for spear-phishing campaigns, or to identify potential targets for further attacks. To perform this technique, an attacker will use the 'Email Validation' command to check the validity of email addresses associated with an Azure tenant. By using this technique, an attacker can gain valuable information about a target organization's employees and potentially gain access to sensitive information.

From a technical standpoint, this technique involves querying Azure Active Directory for email addresses associated with a given tenant. The 'Email Validation' command will then attempt to validate the email addresses found using various methods, such as SMTP validation or DNS validation. If the email address is found to be valid, it will be returned as a result.

The business value of this technique lies in the potential for attackers to gain access to sensitive information or compromise a target organization's systems. By identifying valid email addresses associated with an Azure tenant, an attacker can launch targeted spear-phishing campaigns to gain access to sensitive information or compromise systems.

 

## Requirements

1. List of email addresses (emails.txt)

1. o365creeper tool

 

## Defense

1. Organizations can prevent this technique by implementing email address validation measures, such as SPF, DKIM, and DMARC.

1. Implementing multi-factor authentication can prevent attackers from gaining access to valid credentials for an Azure tenant.

1. Regularly monitoring Azure Active Directory logs can help detect and respond to unauthorized access attempts.

 

## Objectives

1. Identify valid email addresses associated with an Azure tenant

1. Gather information for spear-phishing campaigns

1. Identify potential targets for further attacks

 

# Instructions

1. To validate a list of email addresses, use the o365creeper.py script with the -f flag to specify the file containing the email addresses and the -o flag to specify the output file for the valid email addresses. The script will output the status of each email address (VALID or INVALID) next to the email address.

 



**Code**: [[PS> C:\Python27\python.exe C:\Tools\o365creeper\o3]]



> -f: Specifies the input file containing the email addresses to validate.
-o: Specifies the output file for the valid email addresses.

By default, O365 has a lockout policy of 10 tries, and it will lock out an account for one (1) minute.



**Command** ([[Run o365creeper.py on emails.txt]]):

```bash
C:\Python27\python.exe C:\Tools\o365creeper\o365creeper.py -f C:\Tools\emails.txt -o C:\Tools\validemails.txt
```



## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Active Scanning|T1595 - Active Scanning]]
- [[Search Open Websites/Domains|T1593 - Search Open Websites/Domains]]

## Commands Used

- [[Run o365creeper.py on emails.txt]]

## Tags

- [[Cloud - Azure]]
- [[Email]]
- [[Enumerate valid emails]]
- [[Enumeration]]
- [[o365]]
- [[Office 365]]


