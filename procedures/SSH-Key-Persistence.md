---
type: procedure
tactics:
  - '[[Persistence]]'
techniques:
  - '[[SSH Authorized Keys]]'
sub_techniques: []
tags:
  - ssh-persistence
  - linux-backdoor
commands:
  - '[[commands/generate-ssh-key-pair]]'
  - '[[commands/add-ssh-public-key-via-copy-id]]'
  - '[[commands/add-ssh-public-key-manually]]'
platforms:
  - Linux
tools: []
verified: true
validated: true
---

# SSH-Key-Persistence

## Summary

This procedure demonstrates how to establish persistence on a compromised Linux system by adding an attacker's public SSH key to the target's authorized_keys file, allowing passwordless access using the corresponding private key. It is commonly used post-exploitation to maintain access even if user passwords are changed or the system is rebooted.

## Description

SSH key-based authentication enables secure, passwordless logins by verifying a public key stored on the target against a private key held by the attacker. In an attack scenario, after gaining initial shell access (e.g., via a reverse shell or exploited service), the attacker generates an SSH key pair on their controlled machine and appends the public key to the target's ~/.ssh/authorized_keys file. This creates a backdoor that survives reboots and credential changes, as long as the file permissions remain intact (typically 600 for authorized_keys and 700 for .ssh). The technique targets Linux/Unix systems with OpenSSH enabled and is effective against users with shell access. Detection can be challenging if the key is obfuscated or the file is monitored infrequently.

## Requirements

1. Initial shell access to the target Linux machine (e.g., via compromised credentials or RCE).
2. SSH server running on the target with key-based authentication enabled.
3. Attacker machine with SSH client installed (Linux/macOS/Windows with OpenSSH).
4. Network connectivity between attacker and target for SSH.

## Defense

- Regularly audit ~/.ssh/authorized_keys files for unauthorized entries using tools like auditd or file integrity monitoring (e.g., Tripwire, OSSEC).
- Enforce strict file permissions (chmod 700 ~/.ssh, 600 ~/.ssh/authorized_keys) and restrict modifications to authorized users.
- Implement multi-factor authentication (MFA) for SSH to complement key-based auth.
- Disable password authentication in sshd_config (PasswordAuthentication no) after enabling keys for legitimate users.
- Monitor SSH logs (/var/log/auth.log) for successful key-based logins from unknown sources.

## Objectives

1. Add attacker's public SSH key to target's authorized_keys for persistent access.
2. Ensure backdoor survives system reboots and credential rotations.
3. Enable stealthy, passwordless re-entry without triggering password prompts.

## Instructions

### Step 1: Generate SSH Key Pair

**Context**: On the attacker's machine, generate a new RSA key pair dedicated to this persistence mechanism. Use a strong key size (e.g., 4096 bits) to avoid easy cracking, and store it securely outside the default location to avoid conflicts.

**Command** ([[commands/generate-ssh-key-pair]]):
```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_persist -N ""
```

> This command creates a private key (~/.ssh/id_persist) and public key (~/.ssh/id_persist.pub) without a passphrase for automated use. Expected output includes key fingerprint and random art visualization. Verify with ls ~/.ssh/id_persist* to confirm files exist.

### Step 2: Add Public Key Using ssh-copy-id

**Context**: If password-based SSH access is still available, use this automated method to append the public key to the target's authorized_keys. This requires knowing the target's username and having the current password.

**Command** ([[commands/add-ssh-public-key-via-copy-id]]):
```bash
ssh-copy-id -i ~/.ssh/id_persist.pub username@target_ip
```

> Enter the target's password when prompted. The command creates ~/.ssh if needed and appends the key. Expected output: "Number of key(s) added: 1". Test by attempting SSH login with the private key: ssh -i ~/.ssh/id_persist username@target_ip (should succeed without password).

### Step 3: Manually Add Public Key via SSH

**Context**: If ssh-copy-id is unavailable or password access is restricted, use an existing shell session on the target to manually create the directory and append the key. This method pipes the public key content over SSH.

**Command** ([[commands/add-ssh-public-key-manually]]):
```bash
cat ~/.ssh/id_persist.pub | ssh username@target_ip 'mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys'
```

> This one-liner creates the .ssh directory if absent, appends the key, and sets correct permissions to prevent SSH from rejecting the file. Expected output: No errors, and the file size of authorized_keys increases. If already in a shell on target, manually: mkdir -p ~/.ssh; chmod 700 ~/.ssh; echo "$(cat ~/.ssh/id_persist.pub)" >> ~/.ssh/authorized_keys; chmod 600 ~/.ssh/authorized_keys. Verify with cat ~/.ssh/authorized_keys to see the added key.
