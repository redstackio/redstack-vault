---
type: procedure
description: >-
  Exploit vulnerable certificate templates in AD CS to request certificates
  without security extensions, enabling impersonation and NT hash retrieval for
  privilege escalation.
verified: true
submitted: false
tactics:
  - '[[Privilege Escalation]]'
  - '[[Defense Evasion]]'
  - '[[Credential Access]]'
techniques:
  - '[[Bypass User Account Control]]'
  - '[[Credential Dumping]]'
  - '[[Exploitation for Credential Access]]'
sub_techniques: []
tags:
  - active-directory-attacks
  - active-directory-certificate-services
  - esc9-no-security-extension
commands:
  - '[[commands/certipy-shadow-auto-retrieve-hash]]'
  - '[[commands/certipy-account-update-user-upn]]'
  - '[[commands/certipy-req-esc9-certificate]]'
  - '[[commands/certipy-auth-with-pfx]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/Certipy]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Active-Directory-Certificate-Services-ESC9-Attack

## Summary

The Active Directory Certificate Services (AD CS) ESC9 attack exploits certificate templates that lack proper security extensions, allowing an attacker with low-privileged domain access to request a certificate that can authenticate as any user (e.g., Administrator) without including the object's SID. This enables impersonation, NT hash extraction via PKINIT, and potential privilege escalation by updating user principal names (UPNs) and leveraging shadow credentials for initial hash retrieval.

## Description

AD CS ESC9 vulnerabilities occur in templates where the 'Client Authentication' extended key usage lacks strong subject mapping or security extensions, permitting arbitrary UPN specification in certificate requests. An attacker enrolls in such a template using tools like Certipy, sets the UPN to a high-privilege account, and obtains a certificate usable for authentication. Combined with shadow credentials (msDS-KeyCredentialLink), this allows adding a backdoor certificate to a target account, requesting the impersonating cert, and extracting the NT hash. This procedure assumes the attacker has GenericWrite permissions on the target user via an initial foothold account. The target environment is an Active Directory domain with misconfigured AD CS. Success leads to domain admin-level access if the impersonated account is privileged.

## Requirements

1. Domain user credentials (e.g., John@corp.local) with GenericWrite on the target account (e.g., Jane) and enrollment rights to a vulnerable ESC9 template.
2. Installed Certipy tool on a Linux/Kali machine with network access to the domain controller and CA.
3. Knowledge of the domain name (corp.local), CA name (corp-DC-CA), and vulnerable template name (ESC9).
4. Hashes or password for the initial account to authenticate requests.

## Defense

- Regularly audit and restrict AD CS template permissions: Disable enrollment for low-priv users on vulnerable templates and enable 'Require strong certificate mapping'.
- Monitor certificate enrollment events (Event ID 4886/4887) for anomalous UPNs or templates.
- Implement certificate transparency logging and block PKINIT authentication if not needed.
- Use tools like Certify or PowerView to hunt for ESC9/ESC8 templates and patch via MS updates.

## Objectives

1. Retrieve the target user's NT hash using shadow credentials for initial access.
2. Update the target user's UPN to impersonate a privileged account like Administrator.
3. Request an ESC9 certificate with the impersonated UPN and no object SID.
4. Authenticate with the certificate to extract the NT hash of the impersonated account.

## Instructions

### Step 1: Add Shadow Credential and Retrieve Target Hash

**Context**: Use the initial account's permissions to add a shadow credential to the target user (Jane), request a certificate, and retrieve her NT hash. This exploits ESC8-like behavior to bootstrap the ESC9 impersonation.

**Command** ([[commands/certipy-shadow-auto-retrieve-hash]]):
```bash
certipy shadow auto -username $_USERNAME -p $_PASSWORD -account $_TARGET_ACCOUNT
```

> This automates adding msDS-KeyCredentialLink to the target, requesting a certificate, and authenticating to dump the NT hash. Replace $_USERNAME with the attacker's account (e.g., John@corp.local), $_PASSWORD with its password, and $_TARGET_ACCOUNT with the target (e.g., Jane). The step succeeds if GenericWrite is available, providing the hash for further actions.

### Step 2: Update Target User UPN for Impersonation

**Context**: Using the retrieved hash or initial credentials, update the target user's UPN to match a privileged account (Administrator), preparing for ESC9 certificate enrollment.

**Command** ([[commands/certipy-account-update-user-upn]]):
```bash
certipy account update -username $_USERNAME -password $_PASSWORD -user $_TARGET_USER -upn $_NEW_UPN
```

> Authenticate with the initial account and modify the target's UPN. Parameters: $_USERNAME/$_PASSWORD for auth, $_TARGET_USER (Jane), $_NEW_UPN (Administrator). This requires write access to the user object. Expected: Confirmation of UPN update, enabling impersonation in subsequent cert requests.

### Step 3: Request Vulnerable ESC9 Certificate

**Context**: Enroll in the ESC9 template using the target's credentials, specifying the impersonated UPN in the certificate (Administrator) without object SID extension.

**Command** ([[commands/certipy-req-esc9-certificate]]):
```bash
certipy req -username $_USERNAME -hashes $_HASHES -ca $_CA_NAME -template ESC9 -upn $_IMPERSONATED_UPN
```

> Request the certificate from the vulnerable template. Use $_USERNAME (jane@corp.local), $_HASHES (from Step 1, e.g., aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0), $_CA_NAME (corp-DC-CA), and $_IMPERSONATED_UPN (Administrator@corp.local). The cert will lack SID, allowing domain-agnostic auth. Save the output PFX file for Step 4.

### Step 4: Authenticate with Certificate to Extract NT Hash

**Context**: Use the issued ESC9 certificate to perform PKINIT authentication as the impersonated user, retrieving the Administrator's NT hash.

**Command** ([[commands/certipy-auth-with-pfx]]):
```bash
certipy auth -pfx $_PFX_FILE -domain $_DOMAIN
```

> Authenticate using the PFX from Step 3. Parameters: $_PFX_FILE (administrator.pfx), $_DOMAIN (corp.local). If no domain in cert, the flag ensures proper targeting. Success yields the NT hash for pass-the-hash attacks or further escalation.
