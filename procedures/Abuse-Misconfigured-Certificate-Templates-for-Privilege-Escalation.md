---
type: procedure
description: >-
  Abuse misconfigured PKI Certificate Templates in Active Directory to request
  rogue certificates that allow impersonation of users or service accounts for
  privilege escalation.
verified: true
submitted: false
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Certificate Services]]'
  - '[[tags/ESC2 - Misconfigured Certificate Templates]]'
commands:
  - '[[commands/get-adobject-enumerate-misconfigured-cert-templates]]'
  - '[[commands/certreq-new-certificate-request]]'
  - '[[commands/certreq-submit-certificate-request]]'
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Abuse-Misconfigured-Certificate-Templates-for-Privilege-Escalation

## Summary

Misconfigured Certificate Templates can be abused by attackers to elevate privileges in an Active Directory environment. By identifying vulnerable PKI Certificate Templates that allow unauthorized enrollment without renewal authority approval and support client authentication, an attacker can request a rogue certificate, export it, and use it to impersonate a legitimate user or service account. This bypasses access controls and enables actions like lateral movement or data exfiltration.

## Description

This procedure targets misconfigurations in Active Directory Certificate Services (AD CS) where certificate templates have overly permissive enrollment rights, lack renewal authority (RA) signatures, and include the Client Authentication Extended Key Usage (EKU). Attackers with domain user access can enroll in such templates to obtain certificates that function as alternate authentication material. Technically, this exploits the template's object control access (e.g., Enroll permission granted to Authenticated Users) and configuration attributes like msPKI-Enrollment-Flag and msPKI-RA-Signature. In a business context, successful abuse can lead to unauthorized access to sensitive systems, data breaches, and compliance violations. This technique is part of the ESC2 attack from SpecterOps and is commonly used in privilege escalation chains within Windows/AD environments.

## Requirements

1. Domain user credentials with access to a domain-joined Windows machine.
2. Active Directory PowerShell module installed (Import-Module ActiveDirectory).
3. Access to the Certification Authority (CA) server via RPC/DCOM for certificate submission.
4. Knowledge of the target domain's configuration partition (e.g., CN=Configuration,DC=domain,DC=com).

## Defense

- Properly configure permissions on Certificate Templates to restrict Enroll rights to specific groups (e.g., Domain Admins only for privileged templates).
- Enable renewal authority (RA) approval by setting msPKI-RA-Signature and msPKI-Enrollment-Flag appropriately.
- Monitor Certificate Services logs (Event ID 4886 for enrollments, 4887 for issuances) for anomalous requests, especially from low-privilege accounts.
- Implement least privilege: Remove Enroll permissions from Authenticated Users on sensitive templates.
- Use tools like CertifyFind or BloodHound to audit template permissions regularly.

## Objectives

1. Identify vulnerable certificate templates in the AD configuration.
2. Request and obtain a rogue certificate using the vulnerable template.
3. Export the certificate for use in impersonation attacks.
4. Achieve privilege escalation by authenticating as a higher-privileged principal.

## Instructions

### Step 1: Enumerate Misconfigured Certificate Templates

**Context**: Query Active Directory for PKI certificate templates that are potentially vulnerable to abuse. This filter targets templates that are not pending approval (no RA signature required), support client authentication EKU, and are enrollable without restrictions. This step identifies candidates like 'Machine Authentication' or custom vulnerable templates.

**Command** ([[commands/get-adobject-enumerate-misconfigured-cert-templates]]):
```powershell
Get-ADObject -LDAPFilter '(&(objectclass=pkicertificatetemplate)(!(mspki-enrollment-flag:1.2.840.113556.1.4.804:=2))(|(mspki-ra-signature=0)(!(mspki-ra-signature=*)))(|(pkiextendedkeyusage=2.5.29.37.0)(!(pkiextendedkeyusage=*))))' -SearchBase '$_SEARCH_BASE' -Properties *
```

> This command searches the AD configuration partition for vulnerable templates. The LDAP filter excludes templates requiring RA approval and includes those with Client Authentication EKU (2.5.29.37.0). Run this from a domain-joined machine with the ActiveDirectory module loaded. If no results, no vulnerable templates exist or permissions are restricted.

### Step 2: Create Certificate Request INF File

**Context**: Prepare an INF file specifying the vulnerable template for the certificate request. This file defines the key type, exportability, and template name. Use a template identified in Step 1, ensuring the attacker has Enroll permission on it (verifiable via Get-Acl on the template object).

**Code** ([[codes/misconfigured-cert-template-inf-request]]):

> Create a file named request.inf with the content from the linked code, substituting the $_TEMPLATE_NAME with the vulnerable template (e.g., 'VulnerableTemplate'). This step ensures the request is formatted correctly for submission to the CA. The KeySpec=1 makes the private key exportable, allowing PFX export later.

### Step 3: Generate and Submit Certificate Request

**Context**: Use certreq to generate a certificate signing request (CSR) from the INF file and submit it to the CA, specifying the vulnerable template. This obtains the issued certificate if enrollment succeeds. Decision point: If submission fails with access denied, the template lacks Enroll permission—abort or escalate.

**Command** ([[commands/certreq-new-certificate-request]]):
```cmd
certreq -new $_INF_FILE $_REQ_FILE
```

> This generates the .req file from the INF. Expected output: Success message with .req file created. If errors, check INF syntax.

**Command** ([[commands/certreq-submit-certificate-request]]):
```cmd
certreq -submit -attrib "CertificateTemplate:$_TEMPLATE_NAME" $_REQ_FILE $_PFX_FILE.pfx
```

> Submit the CSR to the default CA (-config - for machine default). The -attrib specifies the template. Expected output: Prompt to select CA (choose enterprise CA), then success with certificate issued. Export as PFX for private key inclusion. If successful, you now have a rogue certificate usable for authentication (e.g., via S4U or Pass-the-Cert).
