---
id: d642976d-6347-433e-a430-2e7e7ce408eb
name: Pass-the-Ticket-with-Silver-Tickets
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.886202+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
sub_techniques:
  - '[[sub-techniques/Silver Ticket|T1558.002 - Silver Ticket]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Tickets]]'
  - '[[tags/Pass-the-Ticket]]'
commands:
  - '[[commands/ticketer-request-silver-ticket]]'
  - '[[commands/rubeus-diamond-forge-ticket]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
  - '[[tools/Rubeus]]'
validated: true
---

# Pass-the-Ticket-with-Silver-Tickets

## Summary

This procedure demonstrates how to forge a Silver Kerberos Ticket (TGS) to impersonate a privileged user in an Active Directory environment, enabling Pass-the-Ticket attacks without needing the user's password. Silver Tickets are forged using the krbtgt account's keys, allowing access to specific services as any user, typically for lateral movement or privilege escalation.

## Description

Pass-the-Ticket attacks involve using stolen or forged Kerberos tickets to authenticate to services. A Silver Ticket specifically forges a service ticket (TGS) for a target service using the krbtgt NTLM hash or AES key, without contacting the Key Distribution Center (KDC). This differs from Golden Tickets, which forge Ticket Granting Tickets (TGTs) for domain-wide access. The technique targets Windows Active Directory domains, requiring prior compromise to obtain the krbtgt hash (e.g., via DCSync). Once forged, the ticket can be injected into memory for authentication to services like CIFS, RDP, or WMI. This procedure uses Impacket's ticketer.py for Python-based forging and Rubeus for .NET-based ticket generation, both outputting tickets in formats like .kirbi for import via Mimikatz or lsass injection.

## Requirements

1. Compromised domain user credentials with access to query domain info (e.g., via PowerView or ldapsearch).
2. krbtgt account NTLM hash or AES256 key (obtainable via [[procedures/DCSync-Attack]] or similar).
3. Domain SID and target user RID (e.g., 500 for Administrator).
4. Installed tools: Impacket suite (Python 3) and Rubeus.exe (compiled C# binary).
5. Network access to the domain controller or target service.
6. Windows target environment with Kerberos enabled.

## Defense

- Enable Kerberos Armoring (FAST) and monitor for anomalous TGS requests without corresponding TGTs.
- Use tools like Microsoft ATA or Splunk to detect unusual ticket lifetimes, service PNs, or encryption types.
- Rotate krbtgt password regularly and implement Protected Users group to limit ticket delegation.
- Enable Advanced Audit Policy for Kerberos authentication events (Event ID 4769) and monitor for forged ticket indicators like mismatched SIDs.

## Objectives

1. Gather domain-specific parameters including SID, hashes, and group RIDs.
2. Forge a Silver Ticket for a target user and service.
3. Export the ticket in a usable format for injection and authentication.
4. Verify access to a target service using the forged ticket.

## Instructions

### Step 1: Gather Domain Parameters

**Context**: Before forging the ticket, collect essential domain information such as the domain name, SID, krbtgt hash, and group RIDs (e.g., 512 for Domain Admins). This ensures the forged ticket is valid and includes appropriate privileges.

Use domain enumeration tools like PowerView or ldapsearch to query this info. For example, obtain the domain SID via [[commands/powerview-get-domainsid]].

**Expected Output**: Domain SID (e.g., S-1-5-21-1234567890-1234567890-1234567890), krbtgt NTLM hash (e.g., from DCSync), and group RIDs.

### Step 2: Forge Silver Ticket with ticketer.py

**Context**: Use Impacket's ticketer.py to generate a forged TGS ticket for a specific service (e.g., CIFS) and user. This step creates the ticket offline using the provided krbtgt key, specifying the target user, groups, and service principal.

**Command** ([[commands/ticketer-request-silver-ticket]]):
```python
ticketer.py -request -domain 'lab.local' -user 'domain_user' -password 'password' -nthash 'krbtgt NTLM hash' -aesKey 'krbtgt AES256 key' -domain-sid 'S-1-5-21-...' -user-id '500' -groups '512,513,518,519,520' cifs/dc.lab.local
```

> Replace placeholders with actual values: domain name, target user, krbtgt hash/key, SID, user RID (500 for Admin), group RIDs, and service (e.g., cifs/<DC-hostname>). The command outputs a .ccache file containing the ticket. If AES key is unavailable, NTLM hash can be used for RC4 encryption.

**Expected Output**: A .ccache file (e.g., baduser.ccache) with the forged ticket, verifiable via klist or ticket inspection tools.

### Step 3: Alternatively Forge with Rubeus Diamond

**Context**: If operating on a Windows host, use Rubeus to forge the ticket directly in .kirbi format. This is useful for environments where Python tools are restricted, and it supports AES256 encryption for stronger tickets.

**Command** ([[commands/rubeus-diamond-forge-ticket]]):
```cmd
Rubeus.exe diamond /domain:lab.local /user:domain_user /password:password /dc:dc.lab.local /enctype:AES256 /krbkey:krbtgt_AES256_key /ticketuser:baduser /ticketuserid:500 /groups:512,513,518,519,520 /service:cifs
```

> Provide domain, user creds (for initial auth if needed), DC hostname, encryption type, krbkey (hex AES key), target ticket user/RID, groups, and service. Outputs a .kirbi file.

**Expected Output**: Forged ticket in baduser.kirbi format, ready for import.

### Step 4: Import and Use the Ticket

**Context**: Inject the forged ticket into the current session's memory to enable Pass-the-Ticket authentication. Use Mimikatz for injection, then access services like SMB shares or RDP.

**Command** (using Mimikatz, referenced via [[tools/Mimikatz]]):
```cmd
mimikatz.exe "kerberos::ptt baduser.kirbi" exit
```

> After injection, test access: dir \\dc.lab.local\C$ or use psexec.

**Expected Output**: Successful authentication without password prompts; access to restricted shares or services as the impersonated user.

### Step 5: Verify and Clean Up

**Context**: Confirm the ticket's validity and privileges, then remove it to avoid detection. Monitor for success indicators like elevated access.

Use klist to view loaded tickets and test service access.

**Expected Output**: klist shows the forged TGS with target service and user; successful remote command execution.
