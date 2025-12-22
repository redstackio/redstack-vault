---
id: 6df4d650-03a1-4f95-a080-c000ae27883e
name: Brute-Force-Private-SSH-Key-Password
type: procedure
verified: true
submitted: false
created_at: '2019-10-25T19:09:24.280004+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques: []
tags:
  - cryptography
commands:
  - '[[commands/ssh2john-extract-hash-from-encrypted-ssh-key]]'
  - '[[commands/john-brute-force-hash-file]]'
  - '[[commands/openssl-remove-passphrase-from-rsa-key]]'
platforms:
  - Linux
tools: []
validated: true
---

# Brute-Force-Private-SSH-Key-Password

## Summary

This procedure demonstrates how to perform an offline brute-force attack against the passphrase protecting a private SSH key. By extracting the hash from an encrypted SSH private key file and cracking it using a dictionary attack with John the Ripper, attackers can recover weak passphrases. This is useful in scenarios where an attacker has obtained a copy of an encrypted private key through theft or exfiltration.

## Description

SSH private keys are often encrypted with a passphrase to add a layer of security beyond the key itself. However, if the passphrase is weak, an attacker with access to the encrypted key file (e.g., id_rsa.enc) can perform an offline brute-force attack. The process involves extracting the passphrase hash using ssh2john (a utility from the John the Ripper suite), then cracking it with a wordlist using John the Ripper. Optionally, once the passphrase is known, the attacker can decrypt the key for unrestricted use. This technique targets Linux environments where SSH keys are commonly used for authentication. Success depends on the passphrase strength and the quality of the wordlist used.

## Requirements

1. Access to the encrypted private SSH key file (e.g., id_rsa.enc).
2. John the Ripper suite installed, including the ssh2john.py script (typically in /usr/share/john/ on Kali Linux).
3. A wordlist file for dictionary attacks (e.g., rockyou.txt).
4. Linux environment with bash and OpenSSL installed.
5. Basic knowledge of command-line tools and file permissions.

## Defense

Defensive measures and detection strategies:

- Enforce strong passphrase policies for SSH keys, requiring at least 12 characters with mixed case, numbers, and symbols.
- Use hardware security modules (HSMs) or key agents like ssh-agent to avoid storing passphrases in files.
- Monitor for unauthorized access to private key files via file integrity monitoring (FIM) tools like OSSEC or Auditd.
- Detect brute-force attempts by logging unusual CPU usage from cracking tools or network exfiltration of key files.
- Rotate SSH keys regularly and revoke compromised ones immediately.

## Objectives

1. Extract the passphrase hash from the encrypted SSH private key.
2. Recover the plaintext passphrase through dictionary-based brute force.
3. Optionally, decrypt the private key for use in further attacks, such as SSH authentication.
4. Expected outcome: Obtain the passphrase, enabling full access to the associated SSH key pair.

## Instructions

### Step 1: Extract the Passphrase Hash

**Context**: Begin by using ssh2john to convert the encrypted SSH private key into a format compatible with John the Ripper. This extracts the hash without requiring the passphrase, allowing for offline cracking. The output is redirected to a text file for input into the cracking tool.

**Command** ([[commands/ssh2john-extract-hash-from-encrypted-ssh-key]]):
```bash
python ssh2john.py $_PRIVATE_KEY.enc > $_OUTPUT.txt
```

> This command processes the encrypted key file and generates a hash in John-compatible format. Replace $_PRIVATE_KEY.enc with the path to your encrypted key (e.g., id_rsa.enc) and $_OUTPUT.txt with the desired output file (e.g., ssh_hash.txt). The step succeeds if the output file is created and contains a valid hash line starting with something like "$sshng$".

### Step 2: Perform Dictionary Brute-Force Attack

**Context**: Use John the Ripper to attempt cracking the extracted hash using a wordlist. This simulates a dictionary attack, trying common passwords until a match is found. Monitor the progress and check for cracked passwords afterward.

**Command** ([[commands/john-brute-force-hash-file]]):
```bash
john --wordlist=$_WORDLIST $_HASH_FILE
```

> Specify $_WORDLIST as the path to your dictionary file (e.g., /usr/share/wordlists/rockyou.txt) and $_HASH_FILE as the output from Step 1 (e.g., ssh_hash.txt). After running, use `john $_HASH_FILE --show` to display cracked passwords. Success is indicated if John reports a cracked hash and shows the plaintext passphrase.

### Step 3: (Optional) Decrypt the Private Key

**Context**: If the passphrase was successfully cracked, use OpenSSL to remove the encryption from the original key file, creating an unencrypted version for easy use in SSH connections or further attacks. This step requires entering the known passphrase when prompted.

**Command** ([[commands/openssl-remove-passphrase-from-rsa-key]]):
```bash
openssl rsa -in $_PRIVATE_KEY.enc -out $_PRIVATE_KEY
```

> Provide $_PRIVATE_KEY.enc as the input encrypted file and $_PRIVATE_KEY as the output unencrypted file (e.g., id_rsa). Enter the cracked passphrase when prompted. Verify success by checking that the output file is created and can be used with `ssh -i $_PRIVATE_KEY user@host` without a passphrase prompt.
