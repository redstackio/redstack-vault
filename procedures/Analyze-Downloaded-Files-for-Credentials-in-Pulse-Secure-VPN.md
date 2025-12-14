---
id: proc-uuid-2
tags:
  - credential-analysis
  - hash-extraction
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credential Dumping]]'
updated_at: '2025-12-14T17:31:53.008Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credential Dumping]]'
---
# Analyze Downloaded Files for Credentials in Pulse Secure VPN

## Summary

Parse downloaded files from the VPN exploit to extract usernames, hashed passwords, plaintext credentials, and Duo keys for further attacks.

## Description

After file reads, analyze mtmp/system for hashes and data.mdb for cached plaintext post-login. This reveals LDAP users, Duo integration details, and session data, enabling auth bypass. Use standard Linux tools like grep on the local machine.

## Requirements

1. Downloaded files from Step 1
2. Local Linux environment for analysis
3. Basic scripting knowledge

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive runtime files
- Rotate Duo keys regularly
- Log and monitor file access anomalies

## Objectives

1. Identify valid credentials
2. Extract 2FA keys
3. Prepare for login attempts

## Instructions

### Step 1: Grep for Hashes and Keys

**Context**: Search mtmp/system for password hashes and Duo config.

Execute grep locally:

```bash
grep -i "password\|duo" mtmp_system.txt
```

> Output shows hashed passwords and keys like integration_key, secret_key, api_hostname.

### Step 2: Parse Session Data for Plaintext

**Context**: Extract cached passwords from data.mdb.

Use strings or hex editor:

```bash
strings data.mdb | grep -i password
```

> Reveals plaintext passwords masked in reports for security.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Credential Dumping]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- credential-analysis
- hash-extraction
