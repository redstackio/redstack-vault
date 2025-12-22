---
type: procedure
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
  - '[[techniques/Indirect Command Execution|T1202 - Indirect Command Execution]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Certificate Services]]'
  - '[[tags/ESC6 - EDITF_ATTRIBUTESUBJECTALTNAME2]]'
commands:
  - '[[commands/certify-check-ca-san-flag]]'
  - '[[commands/certify-request-user-cert-with-altname]]'
tools:
  - '[[tools/Certify]]'
platforms:
  - Windows
  - Active Directory
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Request-Alternative-Name-Certificate-via-AD-CS

## Summary

This procedure uses the Certify tool to check the UserSpecifiedSAN flag (EDITF_ATTRIBUTESUBJECTALTNAME2) on an Active Directory Certificate Services (AD CS) Certificate Authority and, if enabled, requests a user certificate with a specified alternative name. This technique allows attackers to impersonate high-privilege accounts by embedding their target in the certificate's Subject Alternative Name (SAN) field, enabling authentication bypass and privilege escalation in domain environments.

## Description

In Active Directory environments with misconfigured AD CS, the EDITF_ATTRIBUTESUBJECTALTNAME2 flag permits users to specify arbitrary SANs in certificate requests. By default, the User certificate template does not allow this, but if the flag is set on the CA, attackers can request certificates that include alternate names like domain admin UPNs. This certificate can then be used for Kerberos authentication to impersonate the targeted account without needing its password. The procedure first enumerates the CA configuration to confirm vulnerability, then submits a certificate request. This is commonly used in post-compromise scenarios for lateral movement or persistence, targeting Windows domain-joined systems with accessible AD CS.

## Requirements

1. Valid domain user credentials with enrollment rights on the User certificate template
2. Network access to the AD CS Certificate Authority (typically over RPC/DCOM ports 135, 445)
3. Certify.exe tool downloaded and executable on a Windows machine
4. PowerShell execution policy allowing script execution (or run via cmd)

## Defense

- Disable the EDITF_ATTRIBUTESUBJECTALTNAME2 flag on all CAs using certutil -setreg policy\EditFlags +EDITF_ATTRIBUTESUBJECTALTNAME2 (to disable)
- Monitor certificate enrollment events in AD CS logs (Event ID 13, 14) for requests with unexpected SANs
- Restrict User template permissions to prevent low-privilege enrollment and audit all certificate requests
- Implement certificate transparency logging and validate SANs during authentication

## Objectives

1. Verify if the CA allows user-specified SANs to confirm exploitability
2. Request a certificate with an alternate name matching a high-privilege account (e.g., domain admin)
3. Obtain a .pfx file usable for impersonation and privilege escalation

## Instructions

### Step 1: Check CA Configuration for UserSpecifiedSAN Flag

**Context**: Use Certify to query the Certificate Authority and determine if the EDITF_ATTRIBUTESUBJECTALTNAME2 flag is enabled, which allows arbitrary SAN specification in requests. This step confirms the vulnerability before proceeding.

**Command** ([[commands/certify-check-ca-san-flag]]):
```powershell
Certify.exe cas
```

> This command enumerates all accessible CAs and their flags. Look for 'EDITF_ATTRIBUTESUBJECTALTNAME2: Enabled' in the output to confirm the misconfiguration. If disabled, the attack cannot proceed with this technique.

### Step 2: Request User Certificate with Alternative Name

**Context**: If the flag is enabled, submit a certificate signing request (CSR) using the User template, specifying an alternate name (e.g., a domain admin UPN) in the SAN extension. This generates a certificate that can authenticate as the alternate identity.

**Command** ([[commands/certify-request-user-cert-with-altname]]):
```powershell
.\Certify.exe request /ca:$_CA_NAME /template:User /altname:$_ALTNAME
```

> Replace $_CA_NAME with the CA path (e.g., dc.domain.local\domain-DC-CA) and $_ALTNAME with the target UPN (e.g., administrator@domain.local). The command outputs a .pfx file with the certificate, private key, and password. Success is indicated by 'Certificate requested successfully' and the file creation. Use the certificate for authentication via tools like Rubeus or export for further use.
