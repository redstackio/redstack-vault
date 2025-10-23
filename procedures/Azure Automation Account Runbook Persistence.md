---
id: 34df8668-8d53-4aad-8230-3608be6d4557
name: Azure Automation Account Runbook Persistence
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.590053+00:00'
updated_at: '2023-05-25T03:28:25.307449+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Scheduled Task|T1053 - Scheduled Task]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Cloud - Azure]]'
- '[[Persistence via Automation accounts]]'
- '[[Runbook Automation]]'
---

# Azure Automation Account Runbook Persistence

**Status**: ✓ Verified

## Summary

The Azure Automation Account User Creation procedure allows an attacker to create a new user account within an Azure Automation account. This can be used to maintain persistence within the environment, as the attacker can create a new user with elevated privileges that they can use to access the en

## Description

# Description

The Azure Automation Account User Creation procedure allows an attacker to create a new user account within an Azure Automation account. This can be used to maintain persistence within the environment, as the attacker can create a new user with elevated privileges that they can use to access the environment at a later time. 

Technical Explanation: The attacker triggers a webhook to create a new user within the Azure Automation account. This is done by using the 'Trigger Webhook to Create New User' command. Once the user is created, the attacker can use the credentials to access the environment. 

Business Value: This procedure allows an attacker to maintain access to the environment even if other methods of access are removed. This can be used to exfiltrate data, install malware, or perform other malicious activities.

 

## Requirements

1. Valid credentials for the Azure Automation account

1. Access to trigger webhooks within the Azure Automation account

 

## Defense

1. Monitor the creation of new users within Azure Automation accounts

1. Implement access controls to limit who can trigger webhooks within Azure Automation accounts

1. Use multi-factor authentication to protect against unauthorized access to Azure Automation accounts

 

## Objectives

1. Create a new user within an Azure Automation account

1. Maintain persistence within the environment

1. Gain elevated privileges within the environment

 

# Instructions



1. Save this as example as runbook.ps1. This script initiates the azure connection and context using the service principal and configures a webhook that triggers the functionality and creates a user based on the parsed data from the webhook.





**Code**: [[# runbook.ps1
# NetSPI - https://github.com/NetSPI]]





2. Fill in the variables and run this script, it will create an automation account, import, publish and configure the webhook for the runbook.ps1



**Code**: [[# Red Stack Labs

# Variables
$automationAccountNa]]





3. When the need arises for a persistent user, proceed to create a new user with this command:



**Code**: [[# Send a request to the persistent webhook to crea]]





## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Scheduled Task|T1053 - Scheduled Task]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Cloud - Azure]]
- [[Persistence via Automation accounts]]
- [[Runbook Automation]]


