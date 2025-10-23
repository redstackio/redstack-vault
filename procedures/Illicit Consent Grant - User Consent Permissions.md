---
id: 8ef3cdbe-8f9b-4aca-ab0e-604b2ed3993a
name: Illicit Consent Grant - User Consent Permissions
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:15.120372+00:00'
updated_at: '2023-04-10T20:19:34.262374+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Internal Spearphishing|T1534 - Internal Spearphishing]]'
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[Cloud - Azure]]'
- '[[Illicit Consent Grant]]'
---

# Illicit Consent Grant - User Consent Permissions

## Summary

Illicit Consent Grant - User Consent Permissions is a tactic used by attackers to gain access to a victim's cloud resources. Attackers can use phishing or social engineering techniques to trick the victim into granting them consent permissions. Once an attacker has been granted these permissions, t

## Description

# Description

Illicit Consent Grant - User Consent Permissions is a tactic used by attackers to gain access to a victim's cloud resources. Attackers can use phishing or social engineering techniques to trick the victim into granting them consent permissions. Once an attacker has been granted these permissions, they can gain access to sensitive data, resources, and services. This technique is commonly used in initial access and persistence stages of an attack. To protect against this type of attack, it is important to implement multi-factor authentication and to educate users on how to recognize and avoid phishing attacks.

 

## Requirements

1. Valid user credentials

1. Access to the cloud service dashboard

1. Knowledge of how to manipulate access tokens

 

## Defense

1. Implement multi-factor authentication to prevent unauthorized access

1. Educate users on how to recognize and avoid phishing attacks

1. Monitor user activity and review access permissions regularly

 

## Objectives

1. Gain access to a victim's cloud resources

1. Prolong access to the victim's cloud resources

 

# Instructions

1. To check if users are allowed to consent to apps, run the following command in PowerShell: Get-AzureADMSAuthorizationPolicy | Select-Object -ExpandProperty PermissionGrantPolicyIdsAssignedToDefaultUserRole

 



**Code**: [[PS AzureADPreview&gt; (GetAzureADMSAuthorizationPo]]



> This command retrieves the permission grant policy IDs assigned to the default user role. If the policy allows users to consent to apps, it will be listed in the output. If the policy does not allow users to consent to apps, the output will be blank.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Internal Spearphishing|T1534 - Internal Spearphishing]]
- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Tags

- [[Cloud - Azure]]
- [[Illicit Consent Grant]]


