---
type: procedure
description: >-
  Create a forged Kerberos trust ticket using Mimikatz to enable inter-forest or
  inter-domain lateral movement by impersonating a trusted domain's krbtgt
  account.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Golden Ticket|T1558.001 - Golden Ticket]]'
  - '[[techniques/Pass the Ticket|T1550.003 - Pass the Ticket]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Trust Ticket Forgery]]'
  - '[[tags/Kerberos Attacks]]'
  - '[[tags/Forest to Forest Compromise]]'
commands:
  - '[[commands/mimikatz-dcsync-krbtgt-hash]]'
  - '[[commands/mimikatz-kerberos-golden-trust-ticket]]'
  - '[[commands/mimikatz-kerberos-ticket-inject]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
---

# Forge-AD-Trust-Ticket-with-Mimikatz

## Summary

This procedure demonstrates how to forge an inter-realm Kerberos Ticket Granting Ticket (TGT) using Mimikatz, leveraging the krbtgt NTLM hash from a compromised domain to impersonate a trusted domain's krbtgt account. This allows attackers to authenticate across trust relationships between domains or forests, facilitating lateral movement and privilege escalation without valid credentials in the target domain.

## Description

In Active Directory environments with trust relationships, attackers who compromise one domain can exploit the trust by forging tickets signed with the trusted domain's krbtgt hash. This technique mimics the creation of a 'trust ticket' or 'silver ticket' variant for inter-forest access. The process requires domain admin-level access in the source domain to extract the krbtgt hash via DCSync, then uses Mimikatz's kerberos::golden module to generate the forged ticket. Once injected, the ticket enables service requests in the trusted domain as any user, such as Administrator. This is particularly effective in multi-forest setups where trusts are one-way or bidirectional. Prerequisites include a foothold with DA privileges and Mimikatz execution rights. Success grants persistent access to the trusted domain's resources, bypassing local authentication.

## Requirements

1. Domain Admin or equivalent privileges in the source domain to perform DCSync for krbtgt hash extraction.
2. Access to a Windows system where Mimikatz can be executed (typically post-compromise shell).
3. Knowledge of the target domain name, source domain SID, and trust details (e.g., via [[procedures/Enumerate-AD-Trusts]]).
4. The NTLM hash of the krbtgt account from the source domain (for signing the forged ticket).
5. Network connectivity between source and target domains over required Kerberos ports (88/TCP, 445/TCP).

## Defense

- Implement protected users groups and restrict krbtgt hash exposure via Group Managed Service Accounts (gMSAs).
- Monitor for DCSync replication attempts using Event ID 4662 (RPC calls to LSASS) and anomalous Kerberos ticket requests (Event ID 4769 with unusual service names).
- Use Microsoft Defender for Identity or tools like BloodHound to detect trust exploitation paths.
- Enforce strict trust configurations (e.g., SID filtering, selective authentication) and regularly rotate krbtgt passwords.
- Deploy endpoint detection for Mimikatz signatures, such as process injection into LSASS (Event ID 4688 with lsass.exe parent).

## Objectives

1. Extract the source domain's krbtgt NTLM hash to enable ticket forgery.
2. Generate a forged trust TGT impersonating the target domain's krbtgt for cross-trust authentication.
3. Inject and utilize the forged ticket to access resources in the trusted domain.
4. Achieve lateral movement and potential domain/forest dominance.

## Instructions

### Step 1: Extract krbtgt Hash

**Context**: Obtain the NTLM hash of the krbtgt account from the source domain using Mimikatz's DCSync functionality. This hash is required to sign the forged ticket and is typically done after gaining DA access. This step simulates replication from the Domain Controller.

**Command** ([[commands/mimikatz-dcsync-krbtgt-hash]]):
```bash
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "lsadump::dcsync /domain:$_DOMAIN /user:krbtgt" exit
```

> Run this in an elevated command prompt on a compromised domain-joined machine. Replace $_DOMAIN with the source domain FQDN (e.g., dollarcorp.moneycorp.local). The command escalates privileges, then performs a DCSync to dump the krbtgt hash. This why: The hash authenticates the forged ticket as legitimate from the trusted side.

**Expected Output**: Output includes the NTLM hash, e.g., "Hash NTLM: e4e47c8fc433c9e0f3b17ea74856ca6b". Verify no errors like 'Access Denied'.

### Step 2: Forge the Trust Ticket

**Context**: Use the extracted krbtgt hash to create a golden ticket configured for the trust relationship. This forges an inter-realm TGT that impersonates the target domain's krbtgt, allowing requests as any user (e.g., Administrator) in the trusted domain.

**Command** ([[commands/mimikatz-kerberos-golden-trust-ticket]]):
```bash
mimikatz.exe "kerberos::golden /domain:$_SOURCE_DOMAIN /sid:$_SOURCE_SID /rc4:$_KRBGTG_HASH /user:$_TARGET_USER /service:krbtgt /target:$_TARGET_DOMAIN /ticket:$_OUTPUT_PATH" exit
```

> Execute on the same machine. Parameters: $_SOURCE_DOMAIN (e.g., dollarcorp.moneycorp.local), $_SOURCE_SID (e.g., S-1-5-21-1874506631-3219952063-538504511), $_KRBGTG_HASH (from Step 1), $_TARGET_USER (e.g., Administrator), $_TARGET_DOMAIN (e.g., moneycorp.local), $_OUTPUT_PATH (e.g., c:\ad\tools\trust-ticket.kirbi). This step crafts the ticket file (.kirbi) for injection. Why: It bypasses the need for real credentials in the target by forging the trust signature.

**Expected Output**: "Ticket exported to $_OUTPUT_PATH". The .kirbi file is created successfully.

### Step 3: Inject and Use the Forged Ticket

**Context**: Load the forged ticket into the current session's memory to impersonate the target domain user. This enables immediate use for authentication to trusted resources, such as RDP or SMB access.

**Command** ([[commands/mimikatz-kerberos-ticket-inject]]):
```bash
mimikatz.exe "kerberos::ptt $_TICKET_PATH" exit
```

> Run after forging. $_TICKET_PATH is the .kirbi from Step 2. This injects the ticket into the LSA (Local Security Authority). Why: Injection makes the ticket available for Kerberos auth without re-logon.

**Expected Output**: "Ticket successfully imported". Verify with "dir \\$_TARGET_DOMAIN\C$" to test SMB access.

**Success Indicators**:
- Successful hash extraction without replication errors.
- Forged ticket file generated and injectable.
- Cross-domain access granted (e.g., no 'Access Denied' on target resources).
