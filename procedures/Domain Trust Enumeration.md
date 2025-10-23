---
id: 147e6d7c-59d7-424b-8ad3-63fed1b84837
name: Domain Trust Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.215967+00:00'
updated_at: '2023-04-10T20:36:04.600880+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[Network Sniffing|T1040 - Network Sniffing]]'
- '[[Query Registry|T1012 - Query Registry]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Enumerate trusts between domains]]'
- '[[Trust relationship between domains]]'
commands:
- '[[List Trusted Domains]]'
---

# Domain Trust Enumeration

## Summary

Domain Trust Enumeration is a technique used to identify trust relationships between domains in an Active Directory environment. This technique is often used by attackers to identify potential targets for lateral movement. To perform this technique, an attacker can use tools like 'List Trusted Doma

## Description

# Description

Domain Trust Enumeration is a technique used to identify trust relationships between domains in an Active Directory environment. This technique is often used by attackers to identify potential targets for lateral movement. To perform this technique, an attacker can use tools like 'List Trusted Domains' and 'ListAllTrustRelationships' to query the Active Directory for trust relationships between domains. This information can then be used to plan and execute further attacks.

 

## Requirements

1. Access to an Active Directory environment

1. Authenticated access to the Active Directory

 

## Defense

1. Monitor and analyze network traffic for suspicious activity

1. Implement least privilege access control to limit the impact of a potential breach

1. Regularly review and update trust relationships between domains

 

## Objectives

1. Identify trust relationships between domains

1. Identify potential targets for lateral movement

 

# Instructions

1. This command lists all the trusted domains for the current domain.

 



**Code**: [[nltest /trusted_domains]]



> The 'nltest' command is used to test the network connectivity and trust relationship between a computer and a domain. The '/trusted_domains' switch is used to list all the trusted domains for the current domain. This command can be useful in troubleshooting domain trust issues and verifying the trust relationships between domains.



**Command** ([[List Trusted Domains]]):

```bash
nltest /trusted_domains
```



2. To list all trust relationships between the current domain and other domains, run the following PowerShell command:

 



**Code**: [[([System.DirectoryServices.ActiveDirectory.Domain]]]



> This command lists all trust relationships between the current domain and other domains. The output includes the source domain name, target domain name, trust type, and trust direction. This information can be useful for troubleshooting authentication issues and verifying trust relationships between domains.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[Network Sniffing|T1040 - Network Sniffing]]
- [[Query Registry|T1012 - Query Registry]]

## Commands Used

- [[List Trusted Domains]]

## Tags

- [[Active Directory Attacks]]
- [[Enumerate trusts between domains]]
- [[Trust relationship between domains]]


