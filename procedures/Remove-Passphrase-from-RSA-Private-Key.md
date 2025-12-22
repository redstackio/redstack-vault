---
id: 52aed7ed-96b6-49ce-9984-574263a273f7
name: Remove-Passphrase-from-RSA-Private-Key
type: procedure
verified: true
submitted: false
created_at: '2019-09-16T20:11:43.247738+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Private Keys]]'
sub_techniques: []
tags:
  - '[[tags/Setup]]'
  - credentials
  - keys
commands:
  - '[[commands/openssl-remove-passphrase-from-rsa-key]]'
platforms:
  - Linux
tools: []
validated: true
---

# Remove-Passphrase-from-RSA-Private-Key

## Summary

This procedure removes the passphrase protection from a password-protected RSA private key using OpenSSL, allowing the key to be used without prompting for a password each time. It is useful in scenarios where an attacker has obtained a passphrase-protected private key during credential access or post-exploitation and needs to prepare it for automated use in further actions like SSH access or signing operations.

## Description

Password-protected private keys enhance security by requiring a passphrase for decryption on each use, but this can hinder automated attacks or scripting. This procedure uses the OpenSSL 'rsa' command to decrypt the key with the known passphrase and output an unprotected version. The process assumes the attacker already possesses the encrypted key file and knows the passphrase. It targets Linux environments where OpenSSL is typically available. Successful execution results in a new private key file without passphrase protection, which can then be used in tools like SSH for lateral movement or persistence.

## Requirements

1. Access to a Linux system with OpenSSL installed (version 1.0.0 or later).
2. The encrypted RSA private key file (e.g., id_rsa.enc) and knowledge of its passphrase.
3. Write permissions in the working directory to save the output file.
4. Basic command-line access (e.g., shell on a compromised host).

## Defense

Defensive measures and detection strategies:

- Monitor for OpenSSL usage in unusual contexts, such as non-administrative accounts running 'openssl rsa' commands.
- Implement file integrity monitoring on private key directories (e.g., ~/.ssh/) to detect creation of new unprotected key files.
- Use full-disk encryption and passphrase enforcement policies to limit key exposure.
- Enable logging of SSH key usage and audit for unauthorized key modifications.

## Objectives

1. Decrypt the passphrase-protected RSA private key to create an unprotected version.
2. Verify the new key is functional and usable without passphrase prompts.
3. Prepare the key for integration into attack workflows like SSH tunneling or authentication.

## Instructions

### Step 1: Prepare and Execute Key Decryption

**Context**: This step decrypts the input encrypted private key using the known passphrase and generates an output file without protection. Ensure you are in a secure directory to avoid exposing the key.

**Command** ([[commands/openssl-remove-passphrase-from-rsa-key]]):
```bash
openssl rsa -in $_PRIVATE_KEY.enc -out $_PRIVATE_KEY
```

> When executed, the command will prompt for the passphrase of the input key. Enter it correctly to proceed. The output file will be a standard PEM-encoded RSA private key without encryption. Verify the key format afterward using 'openssl rsa -in $_PRIVATE_KEY -text -noout' to ensure it loads without errors.

### Step 2: Verify the Unprotected Key

**Context**: Confirm the new key is valid and unprotected by attempting to read its contents or use it in a test operation, such as generating a public key from it.

**Command**:
```bash
openssl rsa -in $_PRIVATE_KEY -pubout -out $_PUBLIC_KEY.pub
```

> This should complete without prompting for a passphrase, indicating success. If it prompts or errors, the decryption failed—recheck the input passphrase and file paths.
