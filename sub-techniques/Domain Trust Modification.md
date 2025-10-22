---
id: 2e14e2d4-bb26-40d0-b65a-65c0d70b8c4b
name: Domain Trust Modification
type: sub-technique
mitre_id: T1484.002
mitre_url: null
created_at: '2023-04-06T00:31:25.748280+00:00'
updated_at: '2023-04-06T00:31:25.748280+00:00'
parent_technique: '[[Group Policy Modification|T1484 - Group Policy Modification]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Domain Trust Modification

**MITRE ID**: T1484.002

**Parent Technique**: [[Group Policy Modification|T1484 - Group Policy Modification]]

This is a sub-technique of T1484 - Group Policy Modification.

## Summary

Adversaries may add new domain trusts or modify the properties of existing domain trusts to evade defenses and/or elevate privileges. Domain trust details, such as whether or not a domain is federated, allow authentication and authorization properties to apply between domains for the purpose of acce

## Description

Adversaries may add new domain trusts or modify the properties of existing domain trusts to evade defenses and/or elevate privileges. Domain trust details, such as whether or not a domain is federated, allow authentication and authorization properties to apply between domains for the purpose of accessing shared resources.(Citation: Microsoft - Azure AD Federation) These trust objects may include accounts, credentials, and other authentication material applied to servers, tokens, and domains.

Manipulating the domain trusts may allow an adversary to escalate privileges and/or evade defenses by modifying settings to add objects which they control. For example, this may be used to forge [SAML Tokens](https://attack.mitre.org/techniques/T1606/002), without the need to compromise the signing certificate to forge new credentials. Instead, an adversary can manipulate domain trusts to add their own signing certificate. An adversary may also convert a domain to a federated domain, which may enable malicious trust modifications such as altering the claim issuance rules to log in any valid set of credentials as a specified user.(Citation: AADInternals zure AD Federated Domain) 

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
