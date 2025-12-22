---
id: 8e9f1b83-a8d4-4452-8db1-5318a8494079
name: Request-User-Certificate-and-TGT-for-Domain-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.367785+00:00'
updated_at: '2023-04-10T20:37:28.914061+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
sub_techniques:
  - '[[sub-techniques/Kerberos|T1558.001 - Kerberos]]'
tags:
  - '[[tags/Domain]]'
  - '[[tags/User Certificate]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/certify-request-user-certificate]]'
  - '[[commands/openssl-convert-pkcs12-to-pfx-for-rubeus]]'
  - '[[commands/rubeus-asktgt-with-certificate]]'
platforms:
  - Windows
tools: []
validated: true
---

# Request-User-Certificate-and-TGT-for-Domain-Persistence

## Summary

This procedure enables attackers to obtain a user certificate from a Windows Certificate Authority and use it to request a Kerberos Ticket Granting Ticket (TGT) for persistent domain access. By leveraging certificate templates like 'User', attackers can authenticate without traditional credentials, maintaining access even after initial compromises are remediated.

## Description

In a compromised Windows Active Directory environment, attackers with domain credentials can abuse certificate services to request certificates that support PKINIT (Public Key Cryptography for Initial Authentication in Kerberos). This allows forging a TGT, which grants broad domain access. The process involves requesting a certificate via Certify.exe, exporting and converting it to a format compatible with Rubeus (a Kerberos abuse tool), and then using the certificate to obtain a TGT. This technique is stealthy as it mimics legitimate certificate enrollment and can evade credential-based detection. It requires enrollment rights on the 'User' template and access to a domain-joined machine. Success provides a TGT usable for service tickets, lateral movement, and DCSync attacks.

## Requirements

1. Domain-joined Windows machine with network access to the Certificate Authority (CA).
2. Valid domain user credentials with 'Enroll' permissions on the 'User' certificate template.
3. Installed tools: Certify.exe, OpenSSL, and Rubeus.exe (download from GitHub repositories).
4. Administrative access may be needed for tool execution if UAC is enforced.

## Defense

- Monitor Certificate Services logs for unusual enrollment requests, especially for the 'User' template from non-standard users.
- Restrict certificate template permissions to limit enrollment to authorized users and service accounts.
- Enable multi-factor authentication (MFA) for all domain accounts to prevent initial credential compromise.
- Implement Kerberos logging (Event ID 4768/4769) and alert on TGT requests using certificates from unexpected sources.
- Use tools like Microsoft ATA or EDR solutions to detect anomalous Kerberos activity.

## Objectives

1. Obtain a user certificate to enable PKINIT-based authentication.
2. Forge a TGT for the target user to achieve credential-less domain access.
3. Establish persistence in the Active Directory environment post-compromise.

## Instructions

### Step 1: Request User Certificate

**Context**: Use Certify.exe to enroll in the 'User' certificate template from the specified CA. This step authenticates with current domain credentials and retrieves a certificate suitable for Kerberos authentication. Verify the CA name and template availability beforehand.

**Command** ([[commands/certify-request-user-certificate]]):
```bash
.\Certify.exe request /ca:CA01.megacorp.local\CA01 /template:User
```

> This command outputs a PEM-formatted certificate (cert.pem) and private key if enrollment succeeds. Look for success messages indicating certificate issuance; failure may indicate insufficient permissions or CA misconfiguration.

### Step 2: Convert Certificate for Rubeus Compatibility

**Context**: The obtained certificate must be converted from PEM to PFX format using OpenSSL, with specific CSP settings for Windows compatibility. This prepares it for import into Rubeus, which requires a password-protected PFX file.

**Command** ([[commands/openssl-convert-pkcs12-to-pfx-for-rubeus]]):
```bash
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
```

> Prompt for export password (e.g., 'Passw0rd123!'). Success produces cert.pfx; verify with file existence and no errors. This step ensures the certificate can be used in Windows Kerberos contexts.

### Step 3: Request TGT Using Certificate

**Context**: Load the converted certificate into Rubeus to request a TGT via PKINIT. Specify the target username and certificate path; the TGT can then be exported for use in tools like Mimikatz or for further attacks.

**Command** ([[commands/rubeus-asktgt-with-certificate]]):
```bash
.\Rubeus.exe asktgt /user:username /certificate:C:\Temp\cert.pfx /password:Passw0rd123!
```

> Replace 'username' with the target account. Expected output includes a base64-encoded TGT (e.g., '[...] Group Memberships: [...]'). Success is indicated by the TGT hash or ticket export; use it immediately as TGTs expire (typically 10 hours).
