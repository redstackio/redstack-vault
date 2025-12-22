---
id: proc-nextcloud-key-substitution-001
tags:
  - nextcloud
  - key-substitution
  - server-compromise
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:42.229Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Server-Public-Key-Substitution

## Summary

This procedure allows an attacker with server access to replace the user's public key with their own, enabling future decryption of data encrypted to the substituted key.

## Description

Assuming server compromise (e.g., evil admin), the attacker locates the user's public key in Nextcloud's storage (often in /data/user/files_encryption/keys/ or database). They generate their own keypair and overwrite the user's public key file or entry. This substitution goes undetected because clients do not verify key matches during setup, violating E2E standards.

## Requirements

1. Administrative or file system access to Nextcloud server
2. Knowledge of user directory structure
3. Attacker's own keypair generated (e.g., via OpenSSL)

## Defense

Defensive measures and detection strategies:

- Implement key integrity checks on server
- Log all modifications to user key files
- Use immutable storage for public keys

## Objectives

1. Identify and access user's public key storage
2. Substitute with attacker's key
3. Ensure no immediate detection

## Instructions

### Step 1: Locate User Public Key

**Context**: Find the key file on the server.

SSH or access server file system; navigate to /nextcloud/data/[username]/files_encryption/keys/ and identify publickey.pem or similar.

**Expected Output**: Key file located.

### Step 2: Generate Attacker Keypair

**Context**: Create replacement keys.

Use tools like OpenSSL to generate RSA keypair: openssl genrsa -out private.pem 2048; openssl rsa -in private.pem -pubout -out public.pem.

**Expected Output**: Attacker's public.pem ready.

### Step 3: Substitute the Key

**Context**: Overwrite the user's key.

Backup original, then cp attacker's public.pem to user's key location; adjust permissions to match.

**Expected Output**: Key replaced; server continues normally.

**Success Indicators**:
- File modification timestamp updated
- No server errors on restart

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[key-substitution]]
- [[server-compromise]]
