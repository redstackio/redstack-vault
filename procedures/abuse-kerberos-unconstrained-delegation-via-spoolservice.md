---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.590699+00:00'
updated_at: '2023-04-10T20:25:48.049932+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Use-Alternate-Authentication-Material|T1550 - Use Alternate
    Authentication Material]]
  - '[[techniques/OS-Credential-Dumping|T1003 - OS Credential Dumping]]'
sub_techniques:
  - '[[sub-techniques/Pass-the-Ticket|T1550.001 - Pass the Ticket]]'
  - '[[sub-techniques/DCSync|T1003.006 - DCSync]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Unconstrained Delegation]]'
  - '[[tags/Load the ticket]]'
  - '[[tags/SpoolService Abuse with Unconstrained Delegation]]'
commands:
  - '[[commands/rubeus-asktgs-for-dc-services]]'
  - '[[commands/mimikatz-extract-kerberos-tickets]]'
  - '[[commands/mimikatz-dcsync-krbtgt-hash]]'
platforms:
  - Windows
tools:
  - '[[tools/Rubeus]]'
  - '[[tools/Mimikatz]]'
validated: true
---

# Abuse Kerberos Unconstrained Delegation via SpoolService

## Summary

This procedure demonstrates how to abuse Kerberos Unconstrained Delegation by leveraging the SpoolService (Print Spooler) to coerce authentication from a target user or service to a controlled domain-joined machine configured for unconstrained delegation. Once the Ticket Granting Ticket (TGT) is captured, it is used to request service tickets for domain controller services, inject them into the current session, and perform a DCSync attack to extract sensitive credential data like the KRBTGT hash. This allows lateral movement and privilege escalation in Active Directory environments.

## Description

Kerberos Unconstrained Delegation permits a service account to impersonate users to any service in the domain without restrictions, which can be exploited if an attacker controls a machine with this delegation enabled. The SpoolService abuse involves using RPC calls to the Print Spooler (MS-RPRN) to force a target to authenticate to the attacker's machine, capturing the resulting TGT in memory. Tools like Rubeus are then used to request Ticket Granting Service (TGS) tickets for critical services (e.g., LDAP and CIFS on the DC) using the captured TGT, and Mimikatz injects these tickets for impersonation. Finally, DCSync replicates Active Directory data to dump hashes. This technique is effective in domain environments with legacy delegation configurations and requires initial low-privilege access to a domain-joined host. Expected outcomes include impersonation of delegated users and extraction of domain credentials, enabling further attacks like Golden Ticket forgery.

## Requirements

1. Valid domain user credentials with access to a domain-joined Windows machine.
2. The target machine must have Unconstrained Delegation enabled (via msDS-AllowedToDelegateTo attribute) and the Print Spooler service running.
3. Tools: Rubeus.exe and Mimikatz installed or executable on the attacker's machine.
4. Network access to the domain controller (ports 88, 445, 389 open).
5. Administrative privileges on the local machine for ticket injection.

## Defense

- Disable Unconstrained Delegation on service accounts where not explicitly needed; prefer Resource-Based Constrained Delegation.
- Monitor for abnormal Kerberos activity, such as unusual TGS requests or ticket injections (Event IDs 4769, 4672, 4624).
- Implement strong password policies and monitor for DCSync replication attempts (Event ID 4662 on DCs).
- Restrict RPC access to Print Spooler (MS-RPRN) and disable unnecessary delegation features.
- Use tools like Microsoft Defender for Identity to detect delegation abuse.

## Objectives

1. Coerce authentication via SpoolService to capture a TGT from a high-privilege user.
2. Impersonate the delegated user to access domain controller services.
3. Extract domain credentials via DCSync for further persistence or escalation.

## Instructions

### Step 1: Request TGS Tickets Using Captured TGT

**Context**: Assuming a TGT has been captured via SpoolService coercion (e.g., using tools like SpoolSample to trigger MS-RPRN authentication), use Rubeus to request TGS tickets for LDAP and CIFS services on the domain controller. This leverages the unconstrained delegation to impersonate the authenticating user. The /ptt flag injects the tickets into the current session for immediate use.

**Command** ([[commands/rubeus-asktgs-for-dc-services]]):
```powershell
.\Rubeus.exe asktgs /ticket:<ticket base64> /service:LDAP/dc.lab.local,cifs/dc.lab.local /ptt
```

> This command performs Service for User (S4U2self) extension to obtain impersonation tickets. Replace <ticket base64> with the base64-encoded TGT from the coercion step. Success is indicated by no errors and new tickets visible in klist output. If injection fails, ensure local admin rights.

### Step 2: Extract Kerberos Tickets from Memory

**Context**: After ticket injection, extract all Kerberos tickets from the LSASS process to verify the impersonation and identify usable tickets for further actions. This step confirms the delegation abuse succeeded and provides tickets for export if needed.

**Command** ([[commands/mimikatz-extract-kerberos-tickets]]):
```bash
mimikatz # sekurlsa::tickets
```

> Run Mimikatz as administrator. The output lists tickets by user, service, and session. Look for tickets to LDAP/DC and CIFS/DC with the impersonated user's SID. Export specific tickets if required using sekurlsa::tickets /export.

### Step 3: Perform DCSync to Dump KRBTGT Hash

**Context**: With impersonated DC access via the injected tickets, execute DCSync to replicate the KRBTGT account hash from the domain controller. This enables Golden Ticket attacks for domain dominance.

**Command** ([[commands/mimikatz-dcsync-krbtgt-hash]]):
```bash
mimikatz # lsadump::dcsync /user:HACKER\krbtgt
```

> Replace HACKER with your domain name. The command mimics DC replication to pull NTLM hash and other attributes. Success yields the hash in the output, which can be cracked or used directly. Requires the injected tickets to authenticate as a domain admin equivalent.
