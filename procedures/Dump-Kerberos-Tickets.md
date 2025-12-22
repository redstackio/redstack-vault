---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Active-Directory-Attacks]]'
  - '[[tags/Dump-Kerberos-Tickets]]'
  - '[[tags/Kerberos-Tickets]]'
commands:
  - '[[commands/rubeus-triage-list-tickets]]'
  - '[[commands/rubeus-dump-ticket-by-luid]]'
platforms:
  - Windows
tools:
  - '[[tools/Rubeus]]'
validated: true
---

# Dump-Kerberos-Tickets

## Summary

This procedure extracts Kerberos tickets from the memory of a compromised Windows system in an Active Directory environment. The tickets can then be used for authenticating to other services, enabling lateral movement or privilege escalation without needing plaintext credentials.

## Description

Kerberos is the primary authentication protocol in Windows Active Directory domains. Upon user login, Kerberos tickets (TGTs and service tickets) are generated and stored in the system's memory (LSASS process) or ticket cache. Dumping these tickets allows attackers to impersonate users or service accounts across the network. This procedure uses Rubeus, a lightweight C# tool, to enumerate and export tickets in Kirbi format (a portable binary format for Kerberos tickets). It is typically employed post-compromise during credential access phases, assuming local administrator privileges on the target host. The technique bypasses some protections by directly interacting with the Kerberos API rather than injecting into LSASS like Mimikatz.

## Requirements

1. Local administrator access on a domain-joined Windows system.
2. Rubeus.exe tool available on the compromised host (download or transfer via SMB).
3. Network connectivity to the domain controller for ticket validation (though dumping is local).
4. PowerShell or Command Prompt execution rights (bypass AMSI if needed).

## Defense

- Enable Protected Process Light (PPL) for LSASS and monitor for unauthorized access.
- Implement credential guard (Windows 10/11 Enterprise) to isolate LSASS.
- Monitor for suspicious process executions like Rubeus.exe or unusual Kerberos ticket requests via Event ID 4769.
- Use EDR tools to detect memory scraping or unsigned executable runs.

## Objectives

1. Enumerate all available Kerberos tickets in the current session.
2. Export a specific ticket for offline use or injection into other sessions.
3. Enable authentication to remote services using dumped tickets.
4. Facilitate lateral movement without password cracking.

## Instructions

### Step 1: Enumerate Available Kerberos Tickets

**Context**: First, list all Kerberos tickets cached in the current logon session to identify valuable ones, such as TGTs for privileged users or service tickets for high-value accounts. This step reveals ticket details like user, service, and LUID for targeting.

**Command** ([[commands/rubeus-triage-list-tickets]]):
```cmd
Rubeus.exe triage
```

> This command queries the Kerberos ticket cache and displays a summary of all tickets, including session LUIDs, encryption types, and endpoints. Run it from an elevated Command Prompt or PowerShell on the compromised host. If no tickets are shown, ensure you are in an interactive session or use /user:DOMAIN\username to specify a session.

### Step 2: Dump a Specific Kerberos Ticket

**Context**: Once tickets are enumerated, select a high-value ticket (e.g., a TGT for a domain admin) by its LUID and dump it to a file. The output in Kirbi format can be transferred off-host for later use with tools like Mimikatz or Rubeus for pass-the-ticket attacks.

**Command** ([[commands/rubeus-dump-ticket-by-luid]]):
```cmd
Rubeus.exe dump /luid:0x12d1f7 /service:krbtgt
```

> Replace 0x12d1f7 with the actual LUID from Step 1. The /service flag optionally filters by service principal (e.g., krbtgt for TGTs). This exports the ticket as a binary .kirbi file. Verify the dump by checking file creation and size (>0 bytes). If the LUID is invalid, re-run triage to confirm.
