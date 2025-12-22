---
id: c0ff5de5-f6fa-4ad1-aeb1-a44f7b036d6b
name: OverPass-the-Hash-with-Rubeus
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.162198+00:00'
updated_at: '2023-04-10T20:26:24.155649+00:00'
tactics:
  - '[[tactics/Lateral-Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Use-Alternate-Authentication-Material|T1550.002 - Pass the
    Hash]]
sub_techniques: []
tags:
  - '[[tags/Active-Directory-Attacks]]'
  - '[[tags/OverPass-the-Hash]]'
  - '[[tags/Rubeus]]'
  - '[[tags/Kerberos-Abuse]]'
commands:
  - '[[commands/rubeus-asktgt-request-tgt-with-rc4-ntlm-hash]]'
  - '[[commands/rubeus-asktgt-request-tgt-with-aes256-hash]]'
  - '[[commands/rubeus-asktgt-pass-ticket-to-sacrificial-process]]'
platforms:
  - Windows
tools:
  - '[[tools/Rubeus]]'
validated: true
---

# OverPass-the-Hash-with-Rubeus

## Summary

OverPass-the-Hash is an advanced credential abuse technique that allows an attacker to authenticate as a domain user by requesting a Kerberos Ticket Granting Ticket (TGT) using the user's NTLM (RC4) or AES256 hash instead of the plaintext password. This procedure details how to use the Rubeus tool to perform OverPass-the-Hash on a domain-joined Windows system, injecting the obtained ticket into the current session for immediate impersonation or into a sacrificial process for stealthier operations. It is commonly used for lateral movement within Active Directory environments after obtaining hashes via methods like credential dumping.

## Description

In a typical Active Directory attack scenario, an attacker has compromised a domain-joined workstation and extracted NTLM or AES256 hashes from memory or LSASS using tools like Mimikatz. Rather than cracking the hashes offline, OverPass-the-Hash enables direct use of the hash to request a TGT from the Key Distribution Center (KDC), bypassing the need for the password. Rubeus, a C# utility, handles the Kerberos protocol interactions to generate and inject the ticket. The /ptt flag injects the ticket into the current logon session, allowing access to network resources as the target user. For operational security, the AES256 variant uses stronger encryption and avoids certain detections. If elevated privileges are available, passing the ticket to a hidden sacrificial process (e.g., cmd.exe) allows token theft without altering the primary session. This technique targets Windows domains with Kerberos enabled and assumes the attacker has local execution on a domain-joined host.

## Requirements

1. Domain-joined Windows system with network access to the Domain Controller (ports 88/TCP for Kerberos).
2. NTLM (RC4) hash or AES256 hash of a valid domain user account (e.g., obtained via [[procedures/Dump-LSASS-Credentials-with-Mimikatz]]).
3. Rubeus.exe executable available on the target system ([[tools/Rubeus]]).
4. For sacrificial process injection: Local administrator privileges on the current system.
5. PowerShell or Command Prompt execution rights.

## Defense

- Enforce strong password policies, Kerberos pre-authentication, and multi-factor authentication (MFA) to limit hash usability and require additional factors for ticket requests.
- Monitor for anomalous Kerberos activity using tools like Sysmon (Event ID 4768 for TGT requests), Windows Security Auditing, or Microsoft Defender for Identity to detect unusual AS-REQ patterns or ticket injections.
- Implement Least Privilege Access and restrict local admin rights to prevent execution of tools like Rubeus; use AppLocker or WDAC to block unsigned executables.
- Enable Protected Users group for high-privilege accounts to enforce AES encryption and limit ticket lifetimes.

## Objectives

1. Request a valid Kerberos TGT for the target user using their hash without the plaintext password.
2. Inject the TGT into the current session or a new process to impersonate the user.
3. Enable lateral movement, resource access, or privilege escalation as the impersonated user.

## Instructions

### Step 1: Prepare the Session by Purging Existing Tickets

**Context**: Before injecting a new TGT, clear any existing Kerberos tickets in the current session to avoid conflicts or detection from multiple active tickets. This ensures clean impersonation of the target user.

**Command** (built-in Windows):
```cmd
klist purge
```

> This command removes all Kerberos tickets from the current logon session. Run it from Command Prompt or PowerShell. Expected output: "Current LogonId is {0:0x...}:0x...\n A ticket has been purged from the logon session." If no tickets exist, it will indicate none were found. Verify with `klist` afterward to confirm an empty list.

### Step 2: Request TGT Using NTLM (RC4) Hash and Inject into Current Session

**Context**: Use the user's NTLM hash to request a TGT and pass-the-ticket (/ptt) directly into the current session. This allows immediate authentication as the user for network access, such as SMB shares or RDP.

**Command** ([[commands/rubeus-asktgt-request-tgt-with-rc4-ntlm-hash]]):
```cmd
.\Rubeus.exe asktgt /user:$_USERNAME /rc4:$_NTLM_HASH /ptt
```

> Replace $_USERNAME with the target domain user (e.g., Administrator) and $_NTLM_HASH with the 32-character NTLM hash (e.g., aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0). Rubeus will contact the KDC, generate the TGT, and inject it. Expected output includes: "[+] Action success!" followed by ticket details like "Requesting TGT for user 'DOMAIN\Administrator'..." and "[+] Tickets successfully injected into memory." Verify success by running `klist` to see the new TGT or attempting network access (e.g., `dir \\DC01\C$`). If the hash is invalid, expect an error like "[-] KRB-ERROR (5/KDC_ERR_PREAUTH_FAILED)."

### Step 3: Request TGT Using AES256 Hash for Stealthier Injection

**Context**: If the AES256 hash is available (from accounts with AES enabled), use this variant for better operational security (/opsec flag randomizes some behaviors to evade detection). Inject into the current session as before.

**Command** ([[commands/rubeus-asktgt-request-tgt-with-aes256-hash]]):
```cmd
.\Rubeus.exe asktgt /user:$_USERNAME /aes256:$_AES256_HASH /opsec /ptt
```

> Replace $_USERNAME and $_AES256_HASH (64-character hex, e.g., from Mimikatz). The /opsec flag enhances stealth by using randomized session keys. Expected output similar to Step 2: "[+] Action success!" and ticket injection confirmation. This method is preferred for modern domains enforcing AES, as RC4 is deprecated. Verify with `klist` or resource access; errors may indicate AES not supported for the user.

### Step 4: Pass Ticket to a Sacrificial Hidden Process (Elevated)

**Context**: For scenarios requiring isolation (e.g., to avoid session pollution or enable token duplication), create a new hidden process and inject the ticket there. This requires elevation and allows attaching a debugger or stealing the token later.

**Command** ([[commands/rubeus-asktgt-pass-ticket-to-sacrificial-process]]):
```cmd
.\Rubeus.exe asktgt /user:$_USERNAME /rc4:$_NTLM_HASH /createnetonly:$_PROCESS_PATH
```

> Replace $_USERNAME, $_NTLM_HASH, and $_PROCESS_PATH (e.g., C:\Windows\System32\cmd.exe). Run from an elevated prompt. Rubeus requests the TGT and creates a network-only logon context in the new process. Expected output: "[+] Action success!" and process creation confirmation (e.g., "Created process with PID: 1234"). The process runs hidden; use Task Manager or `tasklist` to verify. To interact, attach via debugger or use tools like ProcDump for token theft. If unelevated, this will fail with access denied.
