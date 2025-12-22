---
id: a97d49fe-0667-4777-979a-09d46c4e890e
name: RDP-Session-Takeover-with-Mimikatz
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.345713+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - >-
    [[techniques/Remote Service Session Hijacking|T1563 - Remote Service Session
    Hijacking]]
sub_techniques:
  - '[[sub-techniques/RDP Hijacking|T1563.002 - RDP Hijacking]]'
tags:
  - '[[tags/RDP Session Takeover]]'
  - '[[tags/Windows - Mimikatz]]'
  - rdp-hijacking
  - credential-dumping
commands:
  - '[[commands/mimikatz-ts-multirdp-connect-session]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# RDP-Session-Takeover-with-Mimikatz

## Summary

This procedure demonstrates how to hijack an active RDP session on a Windows target using Mimikatz. By dumping credentials from memory and injecting into existing RDP sessions, an attacker can impersonate a legitimate user without triggering new logon events, enabling stealthy lateral movement and persistence.

## Description

RDP session takeover leverages Mimikatz's token manipulation and session injection capabilities to access remote desktop sessions already established on the target system. This technique is particularly effective in environments with active remote administration, as it allows attackers to inherit the session context, including any open applications and privileges, without requiring additional authentication. The process involves gaining initial administrative access, dumping LSASS credentials for validation, listing active sessions, and then connecting to a specific RDP session ID. This maps to credential access via memory dumping and lateral movement through session hijacking, commonly used post-compromise for maintaining access in Windows domains.

## Requirements

1. Administrative privileges on the target Windows system (local or domain admin).
2. Initial access to the target via shell, such as through a compromised account or exploit.
3. Mimikatz tool installed or transferred to the target (requires [[tools/Mimikatz]]).
4. Active RDP session running on the target for hijacking.
5. Windows OS (Server 2008+ or Windows 7+ with RDP enabled).

## Defense

Defensive measures and detection strategies:

- Restrict RDP to specific IP ranges and enforce Network Level Authentication (NLA).
- Enable multi-factor authentication (MFA) for all RDP connections and monitor for anomalous session activity.
- Implement LSASS protection (Credential Guard) to prevent memory credential dumping.
- Monitor for Mimikatz signatures via EDR tools, including process injections and unusual token elevations.
- Log and alert on multiple concurrent RDP sessions or unexpected session terminations.

## Objectives

1. Dump credentials from active sessions to identify valid accounts.
2. Hijack an existing RDP session for persistent, low-detection access.
3. Enable lateral movement by impersonating the session owner.
4. Maintain access without creating new logon artifacts.

## Instructions

### Step 1: Launch Mimikatz with Elevated Privileges

**Context**: Start Mimikatz in an elevated command prompt to access system memory and tokens. This ensures the tool can interact with LSASS and session processes.

Run Mimikatz as administrator on the target system.

**Expected Output**: Mimikatz prompt appears, ready for module execution.

### Step 2: Dump Credentials from Memory

**Context**: Extract plaintext credentials from LSASS to validate access and identify session owners. This step confirms available credentials before hijacking.

Use the sekurlsa module to dump logon passwords.

```cmd
sekurlsa::logonpasswords
```

**Expected Output**: List of credentials including usernames, passwords, and NTLM hashes for active sessions.

If no credentials are dumped, ensure the process is running with debug privileges using `privilege::debug`.

### Step 3: List Active Terminal Services Sessions

**Context**: Identify active RDP sessions by their IDs to select a target for hijacking. This reveals which sessions are available for takeover.

Use the ts module to list sessions.

```cmd
ts::servers
```

**Expected Output**: Table of session IDs, users, and states (e.g., Session 3: Active, User: DOMAIN\admin).

### Step 4: Connect to Specific RDP Session

**Context**: Inject into the target RDP session using the session ID obtained from listing. This allows takeover without disconnecting the original user.

**Command** ([[commands/mimikatz-ts-multirdp-connect-session]]):
```cmd
ts::multirdp /id:$_SESSION_ID
```

> This command connects Mimikatz to the specified RDP session ID, enabling control. Replace $_SESSION_ID with the numeric ID from Step 3 (e.g., 3). If multiple sessions are needed, specify additional IDs.

**Expected Output**: Successful injection message, followed by access to the session desktop or shell.

**Success Indicators**:
- No errors during injection; session desktop loads.
- Original user may experience brief freeze but remains unaware.
