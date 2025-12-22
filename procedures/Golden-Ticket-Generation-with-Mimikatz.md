---
id: f6d436f9-082f-43ba-a0f9-f3a4f27794ea
name: Golden-Ticket-Generation-with-Mimikatz
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.272004+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/TA0003 - Persistence]]'
  - '[[tactics/TA0004 - Privilege Escalation]]'
  - '[[tactics/TA0005 - Defense Evasion]]'
  - '[[tactics/TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/T1550.003 - Pass the Ticket: Kerberos]]'
sub_techniques: []
tags:
  - golden-ticket
  - windows
  - mimikatz
  - kerberos
commands:
  - '[[commands/mimikatz-kerberos-golden-ticket]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Golden-Ticket-Generation-with-Mimikatz

## Summary

This procedure uses Mimikatz to forge a Kerberos Golden Ticket, allowing an attacker to impersonate any domain user, including administrators, for persistent access across the Windows domain even after password changes. It leverages the KRBTGT account's NTLM hash to create a ticket-granting ticket (TGT) that bypasses normal authentication.

## Description

In a Windows Active Directory environment, Kerberos authentication relies on tickets issued by the Key Distribution Center (KDC). A Golden Ticket attack exploits this by forging a TGT using the KRBTGT hash, which is derived from the KRBTGT account password. Once injected, the ticket provides domain-wide access without needing valid credentials. This is typically performed after obtaining domain admin privileges or extracting the KRBTGT hash via tools like DCSync. The technique is highly stealthy as it mimics legitimate Kerberos traffic and persists until the KRBTGT password is rotated.

## Requirements

1. Local Administrator or Domain Administrator access on a domain-joined Windows system.
2. Mimikatz tool installed or available on the target system.
3. Knowledge of the domain details: FQDN, SID, a target user RID (e.g., 500 for Administrator), and the KRBTGT NTLM hash (obtainable via DCSync or LSADump).
4. The system must be domain-joined with network access to the Domain Controller.

## Defense

- Rotate the KRBTGT account password regularly (at least every 6-12 months) using Microsoft guidelines to invalidate existing Golden Tickets.
- Monitor Kerberos logs for anomalous TGT requests, especially those with long lifetimes or from unusual service accounts (Event ID 4768/4769).
- Enable Protected Users group and restrict Kerberos delegation to limit ticket abuse.
- Deploy endpoint detection for Mimikatz signatures, such as process injection or LSASS access (Sysmon Event ID 10).
- Use network segmentation and just-in-time administration to contain lateral movement.

## Objectives

1. Forge a persistent Kerberos TGT for domain-wide impersonation.
2. Achieve persistence and lateral movement without relying on stolen credentials.
3. Access restricted resources like Domain Controllers or file shares as any domain user.

## Instructions

### Step 1: Gather Required Domain Information

**Context**: Before generating the ticket, collect the necessary domain artifacts. This includes the domain FQDN, domain SID, a target user RID, and the KRBTGT NTLM hash. The hash can be extracted using DCSync if you have DA privileges.

Use built-in tools or prior procedures to query this information:
- Domain FQDN: Run `echo %USERDNSDOMAIN%` in cmd.
- Domain SID: Use `whoami /user` or PowerShell `([System.Security.Principal.WindowsIdentity]::GetCurrent()).Groups`.
- KRBTGT hash: Reference a prior procedure like DCSync if not already obtained.
- Target RID: Typically 500 for Administrator.

**Expected Output**: Noted values, e.g., Domain: contoso.com, SID: S-1-5-21-xxx, RID: 500, Hash: a1b2c3d4...

### Step 2: Execute Golden Ticket Generation

**Context**: Run the Mimikatz command to forge and inject the Golden Ticket into the current session. This step requires elevated privileges and Mimikatz execution.

**Command** ([[commands/mimikatz-kerberos-golden-ticket]]):
```powershell
.\mimikatz.exe "kerberos::golden /admin:$_ADMIN_USER /domain:$_DOMAIN_FQDN /sid:$_DOMAIN_SID /krbtgt:$_KRBTGT_HASH /ptt" exit
```

> This command generates a Golden Ticket for the specified admin user and injects it (/ptt flag) for immediate use. Replace placeholders with gathered values. The ticket defaults to a 10-year validity unless customized with /startoffset, /endin, or /renewmax flags. Success is indicated by Mimikatz output showing ticket creation and injection without errors.

**Expected Output**:
```
* Kerberos::Golden successfullly generated
Ticket exported to file if needed
User injected
```

### Step 3: Verify Ticket Usage

**Context**: Test the ticket by accessing domain resources, such as listing shares on the DC or running `whoami /all` to confirm elevated privileges.

Use `klist` to view the injected ticket:
```cmd
klist
```

Or attempt lateral movement, e.g., `dir \\DC01\C$`

**Expected Output**: Ticket details in klist showing the forged TGT with long expiration; successful access to admin-only resources without prompting for credentials.

**Success Indicators**:
- No authentication prompts for domain resources.
- `whoami` shows the impersonated user context.
- Kerberos ticket visible in `klist` with extended validity.
