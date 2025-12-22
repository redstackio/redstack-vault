---
id: proc-uuid-6
tags:
  - hash-cracking
  - password-capture
type: procedure
tools:
  - '[[tools/GPU-Hash-Cracking-Tool]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Keylogging]]'
updated_at: '2025-12-14T17:31:52.989Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Keylogging]]'
---
# Crack Admin Hash or Capture Plaintext Password in Pulse Secure VPN

## Summary

Crack the admin password hash using GPU acceleration or monitor admin logins to capture plaintext for post-auth access.

## Description

From earlier file reads or admin page, obtain the hash and crack offline. Alternatively, proxy traffic to snag plaintext during legit admin login.

## Requirements

1. Admin hash from files
2. [[tools/GPU-Hash-Cracking-Tool]] like hashcat
3. Wordlist for cracking

## Defense

Defensive measures and detection strategies:

- Use strong, salted hashes (e.g., bcrypt)
- Monitor for offline cracking attempts via logs
- Enforce MFA for admin

## Objectives

1. Obtain admin password
2. Enable post-auth exploits
3. Escalate to RCE

## Instructions

### Step 1: Offline Hash Cracking

**Context**: Run GPU tool on extracted hash.

Use [[tools/GPU-Hash-Cracking-Tool]]:

```bash
hashcat -m 0 -a 0 admin_hash.txt wordlist.txt --force
```

> Cracks to plaintext password.

### Step 2: Capture Plaintext

**Context**: Monitor for admin login.

Sniff or proxy traffic:

```bash
# Use tcpdump or Burp to capture POST to admin login
tcpdump -i any -w capture.pcap port 443
```

> Extract password from unencrypted POST if possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Brute Force]]
- [[Keylogging]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GPU-Hash-Cracking-Tool]]

## Tags

- hash-cracking
- password-capture
