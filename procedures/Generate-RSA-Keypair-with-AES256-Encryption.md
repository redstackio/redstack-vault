---
type: procedure
verified: true
submitted: false
tactics: []
techniques: []
sub_techniques: []
tags:
  - '[[tags/Setup]]'
  - cryptography
  - ssh-keys
commands:
  - '[[commands/openssl-genrsa-aes256-private-key]]'
  - '[[commands/openssl-rsa-extract-public-key]]'
platforms:
  - Linux
tools:
  - '[[tools/openssl]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Generate-RSA-Keypair-with-AES256-Encryption

## Summary

This procedure generates a secure RSA keypair where the private key is protected by an AES-256 encrypted passphrase. It is commonly used in penetration testing to establish secure SSH access to client systems without exposing the private key in plaintext, enhancing the security of red team operations.

## Description

RSA keypairs are essential for secure remote access, such as SSH connections during authorized penetration tests. Encrypting the private key with AES-256 ensures that even if the key file is compromised, it cannot be used without the passphrase. This procedure uses OpenSSL to create a 4096-bit RSA private key with AES-256 encryption and then derives the corresponding public key. The resulting keys can be used for SSH authentication, ensuring encrypted communication and protecting sensitive testing activities from unauthorized access.

## Requirements

1. OpenSSL installed on a Linux system (version 1.1.0 or later recommended).
2. Write permissions in the working directory for key file output.
3. A strong passphrase to encrypt the private key (at least 12 characters, mixing letters, numbers, and symbols).
4. Basic command-line knowledge for executing OpenSSL commands.

## Defense

This procedure is a defensive setup for red teaming and does not involve adversarial actions. However, to secure generated keys:
- Store private keys in protected locations with restricted permissions (e.g., chmod 600).
- Use a password manager for passphrases.
- Rotate keys periodically and revoke compromised ones via SSH authorized_keys management.
- Monitor for unauthorized SSH attempts using tools like fail2ban.

## Objectives

1. Generate a 4096-bit RSA private key encrypted with AES-256.
2. Extract the public key from the private key for distribution to target systems.
3. Verify the keypair integrity for secure SSH usage.

## Instructions

### Step 1: Generate AES-256 Encrypted Private Key

**Context**: This step creates the RSA private key file with strong encryption to protect it during storage and transport. The 4096-bit modulus provides high security against brute-force attacks.

**Command** ([[commands/openssl-genrsa-aes256-private-key]]):
```bash
openssl genrsa -aes256 -out $_PRIVATE_KEY 4096
```

> This command prompts for a passphrase twice for verification. Enter a secure passphrase when prompted. The output file ($_PRIVATE_KEY, e.g., id_rsa) will contain the encrypted private key. Success is indicated by the generation progress messages and no errors.

### Step 2: Extract Public Key from Private Key

**Context**: The public key is derived from the private key and can be safely shared with target systems (e.g., added to ~/.ssh/authorized_keys) to enable SSH access without exposing the private key.

**Command** ([[commands/openssl-rsa-extract-public-key]]):
```bash
openssl rsa -in $_PRIVATE_KEY -pubout -out $_PUBLIC_KEY
```

> This command will prompt for the private key's passphrase. The output file ($_PUBLIC_KEY, e.g., id_rsa.pub) will contain the public key in PEM format. Verify success by checking that the files exist and the public key starts with '-----BEGIN PUBLIC KEY-----'.
