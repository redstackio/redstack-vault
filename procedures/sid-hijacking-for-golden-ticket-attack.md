---
type: procedure
description: >-
  Perform SID hijacking from a compromised child domain to impersonate a parent
  domain user and generate a Golden Ticket for forest-wide access.
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.249434+00:00'
updated_at: '2023-04-10T20:26:22.620442+00:00'
tactics:
  - '[[Lateral Movement]]'
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Access Token Manipulation]]'
  - '[[Application Access Token]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Child Domain to Forest Compromise - SID Hijacking]]'
  - sid-hijacking
  - golden-ticket
commands:
  - '[[commands/powershell-convert-nameto-sid]]'
  - '[[commands/impacket-lookupsid-lookup]]'
platforms:
  - Windows
tools: []
validated: true
---

# sid-hijacking-for-golden-ticket-attack

## Summary

This procedure enables attackers with access to a child domain to hijack the Security Identifier (SID) of a privileged account (such as krbtgt) from the parent domain, create a duplicate user in the child domain with that SID, and then forge a Golden Ticket Kerberos ticket for domain admin access across the forest. It leverages SID history and Kerberos ticket forging to achieve persistence and lateral movement without direct parent domain credentials.

## Description

SID Hijacking exploits the trust relationship between child and parent domains in Active Directory forests. With low-privileged access in the child domain, an attacker queries the SID of a high-privilege parent domain account (e.g., krbtgt). They then create a new user in the child domain mirroring that SID, inheriting the parent's privileges due to transitive trust. This allows impersonation and escalation. Subsequently, using tools like Rubeus, the attacker generates a Golden Ticket—a forged TGT (Ticket Granting Ticket) using the krbtgt hash—valid for the entire domain or forest. This technique is stealthy, as it doesn't require password changes or direct DC access, but relies on domain trust configurations. It's commonly used in red team engagements to simulate advanced persistent threats moving from subdomain compromise to forest dominance. Detection is challenging without monitoring SID creations and anomalous Kerberos activity.

## Requirements

1. Compromised low-privilege account in the child domain with rights to query domain information and create users.
2. Network access to a Domain Controller (DC) in the child domain; parent domain DC reachable via trust.
3. Knowledge of a target parent domain account (e.g., krbtgt@parent.domain.com) and the krbtgt NTLM hash (obtainable via DCSync if escalated in child).
4. Tools: PowerShell (native on Windows), Impacket suite (Python-based), Rubeus.exe (for Golden Ticket generation).
5. Windows environment with Active Directory domain services.

## Defense

- Enforce strict SID isolation between domains; disable SID history usage where possible.
- Monitor for unusual user creations in child domains with SIDs matching parent domain principals using tools like Microsoft ATA or custom SIEM rules on Event ID 4720 (user creation).
- Implement Protected Users group for krbtgt and enable Kerberos Armoring (FAST); rotate krbtgt password regularly.
- Audit Kerberos ticket requests for anomalies (Event ID 4769) and block forged tickets via strict validation on DCs.
- Use least privilege: Limit child domain accounts from querying parent SIDs via RBAC.

## Objectives

1. Obtain the SID of a privileged parent domain account (e.g., krbtgt) from the child domain.
2. Create a hijacked user in the child domain using the parent SID to inherit privileges.
3. Forge and inject a Golden Ticket for persistent admin access to the parent/forest resources.
4. Achieve domain/forest compromise for exfiltration, persistence, or further escalation.

## Instructions

### Step 1: Query Parent Domain SID Using PowerShell

**Context**: From a compromised child domain machine, use the native Convert-NameToSid cmdlet to resolve the SID of the target parent domain account (e.g., krbtgt). This step confirms the SID without additional tools and works if the child trusts the parent.

**Command** ([[commands/powershell-convert-nameto-sid]]):
```powershell
Convert-NameToSid 'parent.domain.com\krbtgt'
```

> This command queries the parent domain via the trust relationship. If successful, it returns the domain SID followed by the relative ID (RID) for krbtgt (typically -502). Verify no errors like 'object not found' which indicate trust issues. Store the full SID (e.g., S-1-5-21-xxx-xxx-xxx-502) for the next steps.

### Step 2: Alternative SID Lookup Using Impacket (If PowerShell Fails)

**Context**: If PowerShell access is restricted or for cross-platform use, employ Impacket's lookupsid.py to enumerate SIDs remotely against a child domain DC, specifying parent domain credentials if available. This provides the same SID via RPC calls.

**Command** ([[commands/impacket-lookupsid-lookup]]):
```bash
lookupsid.py child.domain.com/lowpriv_user:password@child-dc-ip -dc-ip parent-dc-ip 'parent.domain.com\\krbtgt'
```

> Run this from a Kali/Linux attacker machine with network access. It authenticates to the child DC and resolves the parent SID. Expected output includes the SID string. Use this if the target environment blocks PowerShell execution. Cross-reference with Step 1 output for accuracy.

### Step 3: Create Hijacked User in Child Domain

**Context**: Using the obtained SID, create a new user in the child domain via PowerShell Active Directory module. This duplicates the parent SID, allowing the child user to impersonate the parent principal due to trust propagation. Requires 'Create User' permissions in child OU.

**Command** (Native PowerShell, no separate command doc):
```powershell
New-ADUser -Name 'hijacked_krbtgt' -SamAccountName 'hijacked_krbtgt' -UserPrincipalName 'hijacked_krbtgt@child.domain.com' -ObjectSID 'S-1-5-21-xxx-xxx-xxx-502' -Enabled $true -PasswordNeverExpires $true
```

> Execute on a child domain machine with AD module imported (Import-Module ActiveDirectory). The -ObjectSID parameter directly assigns the hijacked SID. Verify creation with Get-ADUser hijacked_krbtgt -Properties ObjectSID. If SID conflicts occur, target a different parent account or OU.

### Step 4: Obtain krbtgt Hash (Prerequisite for Golden Ticket)

**Context**: To forge the ticket, extract the NTLM hash of the parent krbtgt account. If not already obtained, use DCSync from the hijacked user context or child escalation.

**Command** (Using Mimikatz or similar, referenced inline):
```powershell
# Assuming Mimikatz access
lsadump::dcsync /domain:parent.domain.com /user:krbtgt
```

> This dumps the hash (e.g., aab3cce6964e... ). Store securely for the next step. Success: Hash output without access denied errors.

### Step 5: Generate and Inject Golden Ticket

**Context**: Use the hijacked SID and krbtgt hash to create a forged Kerberos TGT with Rubeus, adding relevant SIDs for admin groups. Pass-the-ticket (/ptt) injects it into memory for immediate use.

**Code** ([[codes/rubeus-generate-golden-ticket]]):

> Download Rubeus.exe to the compromised child machine. Replace placeholders with actual values: domain, SID, hash, and additional SIDs (e.g., Domain Admins: S-1-5-21-xxx-xxx-xxx-512). Run in an elevated prompt. Success: Ticket injected; verify with klist showing the forged TGT. Use for accessing parent resources like C$ shares or RDP.

### Step 6: Validate Lateral Access

**Context**: Test the hijacked privileges by accessing parent domain resources, confirming forest compromise.

**Command** (Native, no separate doc):
```cmd
# From child machine, after ticket injection
net use \\parent-dc-ip\C$ /user:parent.domain.com\administrator *
```

> Enter any password (forged ticket bypasses). Success: Mapped drive to parent DC admin share, indicating full access.
