---
id: a140cb8b-262c-4ef0-aaba-b22d8312c0ce
name: Golden-Ticket-Creation-via-Kerberos-Purge
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.451339+00:00'
updated_at: '2023-04-10T20:37:25.722827+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
sub_techniques:
  - '[[sub-techniques/Golden-Ticket|T1558.001 - Golden Ticket]]'
tags:
  - '[[tags/Domain]]'
  - '[[tags/Golden-Ticket]]'
  - '[[tags/Windows-Persistence]]'
  - kerberos
  - forgery
commands:
  - '[[commands/Purge-Kerberos-Tickets]]'
  - '[[commands/Generate-Golden-Kerberos-Ticket]]'
  - '[[commands/Request-TGT-with-Golden-Ticket]]'
platforms:
  - Windows
tools:
  - '[[tools/Rubeus]]'
validated: true
---

# Golden-Ticket-Creation-via-Kerberos-Purge

## Summary

This procedure demonstrates how to forge a Golden Ticket in a Windows Active Directory environment by first purging existing Kerberos tickets from the current session and then using the krbtgt account hash to create a forged Ticket Granting Ticket (TGT). This allows an attacker with domain admin privileges or the krbtgt hash to impersonate any user and gain persistent, unrestricted access to domain resources without further authentication.

## Description

In a Kerberos-authenticated domain like Active Directory, a Golden Ticket is a forged TGT created using the NTLM hash of the krbtgt account. This technique bypasses normal authentication by injecting the forged ticket into the current session, enabling pass-the-ticket attacks for lateral movement, privilege escalation, and persistence. The process begins by purging any existing tickets to ensure a clean session, followed by generating the Golden Ticket with specified user, domain, SID, and krbtgt hash details. Finally, a new TGT is requested using the injected ticket. This is typically performed after obtaining the krbtgt hash through other means like dumping LSASS or DCSync. The target environment is a Windows domain with domain-joined machines and Active Directory services running.

## Requirements

1. Valid domain user credentials with access to a compromised domain-joined machine.
2. The NTLM hash of the krbtgt account (obtainable via tools like Mimikatz or SecretsDump).
3. The domain SID (can be queried using whoami /user or similar).
4. Rubeus tool compiled and available on the target system (or executed in memory).
5. PowerShell execution policy allowing script execution (bypass if needed).

## Defense

- Monitor Kerberos event logs for anomalous ticket requests, especially those involving the krbtgt account (Event ID 4769 with unusual service names or lifetimes).
- Implement privileged access management (PAM) and just-in-time administration to limit krbtgt hash exposure.
- Enable advanced auditing for Kerberos authentication failures and ticket grants.
- Use tools like Microsoft ATA or ETW logging to detect ticket forging attempts.
- Regularly rotate the krbtgt account password to invalidate existing Golden Tickets.

## Objectives

1. Clear existing Kerberos tickets to prepare a clean session for ticket injection.
2. Forge and inject a Golden Ticket using the krbtgt hash for domain-wide impersonation.
3. Request a valid TGT to verify the Golden Ticket and enable further domain access.
4. Achieve persistence and lateral movement without re-authentication.

## Instructions

### Step 1: Purge Existing Kerberos Tickets

**Context**: This step removes all current Kerberos tickets from the session to prevent conflicts when injecting the new forged ticket. Purging ensures the Golden Ticket can be applied cleanly, simulating a fresh authentication state.

**Command** ([[commands/Purge-Kerberos-Tickets]]):
```powershell
kerberos::purge
```

> This command clears the ticket cache. Run it in a PowerShell session with domain access. If successful, no output is typically shown, but subsequent ticket queries (e.g., klist) will show an empty list.

### Step 2: Generate and Inject Golden Ticket

**Context**: Using the krbtgt hash and domain details, forge a TGT for a specified user (e.g., a domain admin). The /ptt flag injects the ticket directly into the current session for immediate use, enabling pass-the-ticket functionality.

**Command** ([[commands/Generate-Golden-Kerberos-Ticket]]):
```powershell
kerberos::golden /user:$_USERNAME /domain:$_DOMAIN /sid:$_DOMAIN_SID /krbtgt:$_KRBGTG_HASH /ticket:$_TICKET_FILE /ptt
```

> Replace placeholders with actual values (e.g., /user:Administrator /domain:example.com /sid:S-1-5-21-... /krbtgt:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c /ticket:golden.tgt /ptt). Success is indicated by a message like "Ticket successfully imported to the current logon session." Verify with klist to see the injected ticket.

### Step 3: Request TGT with Injected Golden Ticket

**Context**: After injection, request a new TGT to confirm the Golden Ticket's validity and prepare for service ticket requests. This step validates the forgery and allows access to domain resources.

**Command** ([[commands/Request-TGT-with-Golden-Ticket]]):
```powershell
kerberos::tgt
```

> This requests a TGT using the injected ticket. Expected output includes details of the granted TGT, such as validity period (often set to max age in Golden Tickets). Use this to then request service tickets for lateral movement.
