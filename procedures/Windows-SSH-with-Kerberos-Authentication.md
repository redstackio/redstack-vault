---
id: f5449dc2-326f-43b3-a148-dfee7d589c49
name: Windows-SSH-with-Kerberos-Authentication
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.284783+00:00'
updated_at: '2023-04-10T20:38:00.016017+00:00'
tactics:
  - '[[Credential Access]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Credential Dumping]]'
  - '[[Pass the Hash]]'
  - '[[SSH Hijacking]]'
sub_techniques: []
tags:
  - '[[tags/SSH-Protocol]]'
  - '[[tags/Windows-Using-Credentials]]'
commands:
  - '[[commands/copy-user-ccache-to-krb5cc_1045]]'
  - '[[commands/ssh-with-gssapi-authentication-to-domain]]'
platforms:
  - Windows
  - Linux
tools: []
validated: true
---

# Windows-SSH-with-Kerberos-Authentication

## Summary

This procedure enables an attacker to utilize a Kerberos ticket cache extracted from a compromised Windows machine to authenticate to an SSH server via GSSAPI, allowing unauthorized access without traditional password or key-based methods. It is particularly useful in Active Directory environments where cross-platform lateral movement is needed, bridging Windows credential access to Unix/Linux systems configured for Kerberos integration.

## Description

In scenarios involving hybrid environments with Windows domains and Linux servers joined via Kerberos (e.g., using SSSD or Winbind), attackers can extract Kerberos tickets from Windows (often via tools like Mimikatz or Rubeus) and transfer them to a Linux-based attack platform. The ticket cache, typically in ccache format, is then positioned for the SSH client to use during GSSAPI authentication. This technique bypasses local SSH authentication controls if the server trusts the Kerberos realm. Success grants shell access, enabling further pivoting, data exfiltration, or persistence. Prerequisites include ticket extraction on Windows and file transfer (e.g., via SMB or HTTP). This aligns with lateral movement in AD-integrated networks.

## Requirements

1. A valid Kerberos ticket cache (user.ccache) extracted from a compromised Windows machine with domain user privileges.
2. Attacker-controlled Linux/Unix system with OpenSSH client compiled with GSSAPI/Kerberos support (e.g., Ubuntu with libpam-krb5).
3. Network access to the target SSH server (typically port 22) that supports GSSAPI authentication and is configured to trust the Kerberos realm.
4. Kerberos configuration files (krb5.conf) on the attacker machine matching the domain's KDC.

## Defense

- Monitor and restrict access to Kerberos ticket caches on Windows machines using tools like AppLocker or filesystem auditing to prevent extraction and exfiltration.
- Implement multi-factor authentication (MFA) for SSH servers, even with GSSAPI, and disable GSSAPI if not required.
- Enable detailed SSH logging (e.g., via syslog) and monitor for GSSAPI authentication attempts from unusual sources or with unexpected principal names.
- Use network segmentation to limit cross-platform access and deploy Kerberos ticket monitoring (e.g., via Microsoft ATA or custom SIEM rules).

## Objectives

1. Authenticate to an SSH server using a stolen Kerberos ticket to gain remote shell access.
2. Bypass password or key-based SSH authentication mechanisms in Kerberos-trusting environments.
3. Facilitate data exfiltration or lateral movement from the SSH-accessible system.
4. Establish persistence or pivot to additional domain-joined resources.

## Instructions

### Step 1: Prepare Kerberos Ticket Cache

**Context**: After extracting the Kerberos ticket from the compromised Windows machine (e.g., using Rubeus or export from memory), transfer the user.ccache file to your attacker Linux machine. This step positions the ticket in a location accessible to the SSH client, using the standard Kerberos credential cache format expected by GSSAPI.

**Command** ([[commands/copy-user-ccache-to-krb5cc_1045]]):
```bash
cp user.ccache /tmp/krb5cc_1045
```

> This copies the ticket cache to /tmp/krb5cc_1045, where the UID 1045 (example attacker user) can access it. The SSH client will use KRB5CCNAME environment variable or default search paths to locate it. Verify the copy with `ls -l /tmp/krb5cc_1045` to ensure the file permissions allow reading (e.g., 600).

### Step 2: Connect via SSH with GSSAPI

**Context**: Initiate the SSH connection to the target server, enabling GSSAPI to leverage the prepared Kerberos ticket for authentication. The -vv flag provides verbose output for debugging any Kerberos negotiation issues, such as realm mismatches or ticket expiration.

**Command** ([[commands/ssh-with-gssapi-authentication-to-domain]]):
```bash
ssh -o GSSAPIAuthentication=yes user@domain.local -vv
```

> Replace 'user' with the domain principal name (e.g., DOMAIN\user) and 'domain.local' with the target hostname or IP. If successful, GSSAPI will negotiate the ticket, granting a shell without prompting for credentials. Check verbose output for lines like "GSSAPI: authenticating with Kerberos" and monitor for errors like "No valid credentials provided." Test ticket validity beforehand with `klist /tmp/krb5cc_1045`.
