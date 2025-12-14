---
id: proc-nextcloud-decryption-001
tags:
  - nextcloud
  - data-decryption
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
  - Desktop
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:42.221Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Data from Local System]]'
---
# Compromised-Data-Upload-and-Decryption

## Summary

This procedure involves uploading data from the compromised new device, which encrypts to the attacker's public key, followed by the attacker decrypting the files using their private key.

## Description

Files uploaded from the new device are encrypted with the user's private key (restored via nonce) but addressed to the substituted public key. The attacker, with server access, downloads the encrypted files and uses their private key to decrypt, breaking E2E confidentiality. This exploits the lack of key verification in clients.

## Requirements

1. New device set up with tampered key
2. Attacker's private key
3. Access to uploaded files on server

## Defense

Defensive measures and detection strategies:

- Client-side decryption verification before upload
- Server-side anomaly detection for encryption patterns
- Encrypt server-stored files additionally

## Objectives

1. Encrypt and upload data to attacker's key
2. Access and decrypt files as attacker
3. Confirm confidentiality breach

## Instructions

### Step 1: Upload Data from New Device

**Context**: Trigger encryption to tampered key.

On new device, add files to E2E-enabled folder and sync/upload.

**Expected Output**: Files encrypted and stored on server.

### Step 2: Download Encrypted Files

**Context**: Attacker retrieves data.

As evil admin, access user files via server interface or file system.

**Expected Output**: Encrypted files downloaded.

### Step 3: Decrypt with Attacker's Private Key

**Context**: Use private key to read plaintext.

Apply decryption using tools like OpenSSL: openssl rsautl -decrypt -inkey private.pem -in encrypted_file.

**Expected Output**: Plaintext data recovered.

**Success Indicators**:
- Decryption successful without errors
- Original file content visible

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[data-decryption]]
- [[Exfiltration]]
