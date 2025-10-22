---
id: 71060de5-36ba-4895-bb27-b9bb16d10712
name: Domain Admins Group Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.373470+00:00'
updated_at: '2023-04-10T20:25:47.698360+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Privileged Access Management (PAM) Trust]]'
commands:
- '[[List Domain Admins]]'
---

# Domain Admins Group Access

## Summary

This procedure involves gaining access to the Domain Admins group within Active Directory by exploiting trust relationships between domains. By gaining access to this group, an attacker can essentially have full control over the entire Active Directory environment. To accomplish this, the attacker 

## Description

# Description

This procedure involves gaining access to the Domain Admins group within Active Directory by exploiting trust relationships between domains. By gaining access to this group, an attacker can essentially have full control over the entire Active Directory environment. To accomplish this, the attacker may use various techniques such as abusing trust relationships between domains, exploiting vulnerabilities in Active Directory, or using stolen credentials. The business value of this procedure is that it allows an attacker to gain complete control over the target organization's Active Directory environment, which can be used to further compromise the entire network.

## Requirements

1. Valid credentials or knowledge of a vulnerability in Active Directory

1. Access to the target network

## Defense

1. Implement strict access controls to limit access to the Domain Admins group

1. Regularly monitor and audit Active Directory for suspicious activity

1. Implement multi-factor authentication to prevent stolen credentials from being used

## Objectives

1. Gain access to the Domain Admins group within Active Directory

1. Maintain persistence within the target environment

1. Compromise the entire network

# Instructions

1. Use this command to identify potential access to the Domain Admins group.

**Code**: [[Domain Admins]]

> The 'Domain Admins' group is a powerful group in Active Directory that grants complete control over all domain-joined computers. This command may be used to identify systems that have potential access to the Domain Admins group, which can help identify systems that may be at a higher risk of compromise. The output of this command should be reviewed carefully to determine if any systems identified require further investigation.

**Command** ([[List Domain Admins]]):

```bash
Domain Admins
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]

## Commands Used

- [[List Domain Admins]]

## Tags

- [[Active Directory Attacks]]
- [[Privileged Access Management (PAM) Trust]]
