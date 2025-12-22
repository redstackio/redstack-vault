---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
  - '[[techniques/OS Credential Dumping|T1003.002 - Security Account Manager]]'
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques:
  - >-
    [[techniques/Adversary-in-the-Middle/T1557.001| T1557.001 - LLMNR/NBT-NS
    Poisoning and Name Resolution Spoofing]]
tags:
  - active-directory-attacks
  - ntlm-poisoning
  - hash-cracking
  - credential-access
commands:
  - '[[commands/nbtstat-query-netbios-table]]'
  - '[[commands/responder-run-llmnr-nbt-ns-mdns-poisoning]]'
  - '[[commands/inveighzero-run-full-poisoning]]'
  - '[[commands/invoke-inveigh-run-poisoning]]'
  - '[[commands/john-crack-netntlmv2]]'
  - '[[commands/hashcat-crack-netntlmv2]]'
tools:
  - '[[tools/Responder]]'
  - '[[tools/InveighZero]]'
  - '[[tools/John-the-Ripper]]'
  - '[[tools/Hashcat]]'
platforms:
  - Windows
  - Linux
verified: true
validated: true
---

# Net-NTLMv2-Hash-Capture-and-Cracking

## Summary

This procedure demonstrates how to capture Net-NTLMv2 hashes from a target network using name resolution poisoning attacks (LLMNR, NBT-NS, and mDNS) and then crack them offline to recover plaintext passwords. It leverages tools like Responder (for Linux-based attackers) or Inveigh/InveighZero (for Windows) to intercept authentication attempts triggered by users mistyping hostnames, followed by cracking with Hashcat or John the Ripper for credential reuse in lateral movement.

## Description

Net-NTLMv2 hashes are challenge-response authentication artifacts used in Windows environments for SMB, HTTP, and other protocols. When a user attempts to access a resource by mistyping a hostname or IP, the client falls back to LLMNR (Link-Local Multicast Name Resolution) or NBT-NS (NetBIOS Name Service) to resolve it. An attacker positioned on the same network segment can poison these resolutions by responding to queries with their own IP address, prompting the victim to authenticate to the attacker using NTLMv2 hashes. These hashes can then be relayed or captured for offline cracking. This technique is effective in Active Directory environments where LLMNR and NBT-NS are enabled by default. Once cracked, the passwords enable pass-the-hash or direct logon for privilege escalation or lateral movement. The procedure assumes the attacker has layer 2/3 access to the target subnet and focuses on non-relay capture to avoid detection from SMB signing.

## Requirements

1. Attacker machine on the same local network segment as targets (no routing required for poisoning).
2. Administrative privileges on the attacker machine to run packet spoofing tools.
3. Installed tools: Responder (Linux), InveighZero or PowerShell Empire (Windows), Hashcat or John the Ripper for cracking.
4. A wordlist or mask for offline cracking (e.g., rockyou.txt for dictionary attacks).
5. Optional: Knowledge of target usernames for targeted cracking.

## Defense

- Disable LLMNR via Group Policy (Computer Configuration > Administrative Templates > Network > DNS Client > Turn off Multicast Name Resolution) and NBT-NS on clients and servers.
- Enable SMB signing (RequireSecuritySignature=1 in registry) to prevent relay attacks.
- Implement network segmentation and monitor for anomalous DNS/LLMNR traffic using tools like Zeek or Windows Event Logs (Event ID 4624 for failed logons).
- Enforce strong password policies and monitor for weak/cracked credentials via tools like Microsoft ATA.

## Objectives

1. Perform name resolution poisoning to intercept NTLMv2 authentication attempts.
2. Capture Net-NTLMv2 hashes from victim traffic.
3. Crack captured hashes offline to recover plaintext passwords.
4. Validate credentials for use in further network access.

## Instructions

### Step 1: Enumerate Network Devices via NetBIOS

**Context**: Optionally query NetBIOS names to map the network and identify potential targets or machine accounts before starting poisoning. This helps understand the environment and trigger queries more effectively.

**Command** ([[commands/nbtstat-query-netbios-table]]):
```cmd
nbtstat -a $_TARGET_IP_OR_HOSTNAME
```

> This command queries the NetBIOS name table of a remote host, revealing registered names, types (e.g., <00> workstation, <20> file server), and statuses. Run it against known IPs to build a target list. If the target responds, expect a table listing names; no response indicates firewall blocks or offline host.

### Step 2: Run Responder for Poisoning (Linux Attacker)

**Context**: Start Responder to listen for and spoof LLMNR, NBT-NS, and mDNS queries. It will respond to victim queries with the attacker's IP, capturing NTLMv2 hashes during authentication attempts. Wait for a victim to mistype a hostname (e.g., via ping or file share access) to trigger a capture.

**Command** ([[commands/responder-run-llmnr-nbt-ns-mdns-poisoning]]):
```bash
sudo ./Responder.py -I $_INTERFACE -wfrd -P -v
```

> Responder will output poisoned requests in real-time, such as "[LLMNR] Poisoned answer sent to <IP> for name <hostname>". Successful hash capture appears as "[SMB] NTLMv2-SSP Hash: <username>::<domain>:<challenge>:<hash>:...". Hashes are saved to Responder-Session.log and hashes/NTLMv2-<IP>.txt. Press Ctrl+C to stop after captures.

### Step 3: Run InveighZero for Poisoning (Windows Attacker Alternative)

**Context**: If using a Windows attacker machine, use InveighZero to spoof protocols and capture hashes. It supports additional features like machine account targeting and IPv6. Monitor console output for captures.

**Command** ([[commands/inveighzero-run-full-poisoning]]):
```powershell
.\InveighZero.exe -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts Y -DHCPv6 Y -LLMNRv6 Y
```

> InveighZero logs to console and files (e.g., InveighZero.log). Look for lines like "[+] NBNS Spoofed Response Sent" followed by "[+] NTLMv2 Hash Captured: <hash>". Captured hashes are in CSV format for easy extraction. Use -Elevated N if not running as admin.

### Step 4: Run Invoke-Inveigh for Poisoning (PowerShell Alternative)

**Context**: For PowerShell-based environments, Invoke-Inveigh provides similar spoofing capabilities. Specify your IP if needed for binding. This is useful in restricted environments without .NET executables.

**Command** ([[commands/invoke-inveigh-run-poisoning]]):
```powershell
Invoke-Inveigh -IP $_ATTACKER_IP -ConsoleOutput Y -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts Y
```

> Output includes real-time notifications like "[NBT-NS] Poisoner Started" and hash captures as "[HTTP] NTLMv2 Challenge/Response Captured". Hashes saved to Inveigh-Hashes.txt. The -IP parameter binds to a specific interface if multiple are available.

### Step 5: Extract and Prepare Captured Hashes

**Context**: After capturing, locate the hash file (e.g., from Responder's hashes/ directory or Inveigh logs). Format should be: username::domain:challenge:hash:clientchallenge. Copy to a file like hashes.txt for cracking. Verify the hash is valid Net-NTLMv2 by checking length and format.

### Step 6: Crack Hashes with John the Ripper

**Context**: Use John the Ripper for dictionary or brute-force cracking of the captured Net-NTLMv2 hashes. This recovers plaintext if the password is in the wordlist or guessable via rules.

**Command** ([[commands/john-crack-netntlmv2]]):
```bash
john --format=netntlmv2 $_HASH_FILE --wordlist=$_WORDLIST
```

> John loads the hashes and begins cracking, showing progress like "Loaded 1 password hash". On success: "password (username)". Use --show to view results post-crack. Expected output includes cracked passwords; if no crack, try incremental mode with --incremental.

### Step 7: Crack Hashes with Hashcat (Alternative)

**Context**: Hashcat offers GPU-accelerated cracking for faster results on Net-NTLMv2 hashes. Use dictionary mode for efficiency or mask for brute-force.

**Command** ([[commands/hashcat-crack-netntlmv2]]):
```bash
hashcat -m 5600 -a 0 $_HASH_FILE $_WORDLIST
```

> Hashcat initializes with "Session...", then shows cracking speed and progress. Success: "Cracked: <password>". For brute-force, use -a 3 with masks like ?l?l?l?l?l?d?d. Output file hashcat.potfile contains recovered passwords.
