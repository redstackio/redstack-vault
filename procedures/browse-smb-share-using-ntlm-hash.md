---
type: procedure
tactics:
  - '[[tactics/Lateral Movement|TA0008]]'
techniques:
  - '[[techniques/Use Alternate Authentication Material|T1550]]'
  - '[[techniques/Valid Accounts: Pass the Hash|T1550.002]]'
sub_techniques: []
tags:
  - network
  - smb
  - lateral-movement
  - pass-the-hash
commands:
  - '[[commands/smbclient-connect-to-smb-share-ntlm]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/smbclient]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
verified: true
validated: true
---

# Browse SMB Share Using NTLM Hash

## Summary

This procedure demonstrates how to use the smbclient tool to browse and access files on a remote SMB share by authenticating with an NTLM password hash instead of a plaintext password. This technique is useful in lateral movement scenarios where an attacker has obtained an NTLM hash (e.g., via Responder or credential dumping) but not the cleartext password, allowing pass-the-hash attacks against SMB services.

## Description

SMB (Server Message Block) shares are commonly used in Windows environments for file sharing. The smbclient utility, part of the Samba suite, allows Linux-based attackers to interact with these shares. By supplying an NTLM hash in the classic NT hash format (LM:NT, where LM can be a placeholder), authentication can be performed without knowing the password. This leverages the NTLM protocol's support for hash-based authentication, mapping to MITRE ATT&CK technique T1550.002 (Pass the Hash). The procedure assumes the attacker has domain or local credentials in hash form and network access to the target. Success enables file enumeration, download, or upload on the share, potentially leading to data exfiltration or persistence.

## Requirements

1. smbclient tool installed (part of Samba package).
2. Valid username and corresponding NTLM hash (32-character hexadecimal).
3. Network access to the target SMB server (port 445 open).
4. Target share name (e.g., IPC$, C$, Users).
5. Kali Linux or similar environment for execution.

## Defense

Defensive measures and detection strategies:

- Enable SMB signing (RequireSecuritySignature=1 in SMB config) to prevent relay and hash-based attacks.
- Monitor for unusual SMB connections using tools like Sysmon or Windows Event Logs (Event ID 4624 for logons with NTLM auth).
- Implement least privilege: Restrict share access and use multi-factor authentication where possible.
- Use network segmentation to limit lateral movement.
- Detect hash usage via anomaly detection in authentication logs (e.g., unexpected NTLM auth from Linux clients).

## Objectives

1. Authenticate to the SMB share using only the NTLM hash.
2. Enumerate and browse the contents of the share.
3. Verify access without requiring plaintext credentials.
4. Enable further post-exploitation actions like file transfer.

## Instructions

### Step 1: Prepare the NTLM Hash Format

**Context**: smbclient requires the hash in classic NT format: a 32-character LM hash followed by a colon and the 32-character NTLM hash. Since LM hashes are often disabled or empty in modern systems, duplicate the NTLM hash for the LM portion to satisfy the format.

No command needed here; manually construct the hash string. For example, if the NTLM hash is `81ABA903C80B8F4DAAD5225F7D996FBC`, format it as `81ABA903C80B8F4DAAD5225F7D996FBC:81ABA903C80B8F4DAAD5225F7D996FBC`. This ensures compatibility without altering the actual hash.

> This step prepares the credential for pass-the-hash authentication, avoiding the need for password cracking.

### Step 2: Connect to the SMB Share Using smbclient

**Context**: Use the formatted hash to authenticate and enter an interactive smbclient session. This allows browsing directories, listing files, and performing other SMB operations as if logged in with valid credentials.

**Command** ([[commands/smbclient-connect-to-smb-share-ntlm]]):
```bash
smbclient -U $_USERNAME%$_LM_HASH:$_NTLM_HASH --pw-nt-hash //$_TARGET_IP/$_SHARE_NAME
```

> Replace placeholders: $_USERNAME (e.g., bob), $_LM_HASH (duplicated NTLM hash), $_NTLM_HASH (actual hash), $_TARGET_IP (e.g., 10.10.10.10), $_SHARE_NAME (e.g., Users). The --pw-nt-hash flag specifies NTLM hash usage. Upon success, you'll enter an smb: \> prompt for further commands like `ls` to list files or `get filename` to download.

### Step 3: Verify Access and Browse the Share

**Context**: Once connected, use smbclient's built-in commands to confirm access and enumerate contents. This validates the authentication and identifies valuable data.

In the smbclient prompt:
```bash
ls
```

> The `ls` command lists directory contents. Look for sensitive files (e.g., config files, credentials). If access is granted, proceed to download or upload as needed. Exit with `exit`.

**Expected Output**: A prompt like `smb: \> ls` showing directory listings with file names, sizes, and timestamps.
