---
tags:
  - ssh-keygen
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/git]]'
  - '[[tools/ssh]]'
  - '[[tools/cat]]'
  - '[[tools/GitLab-Wiki]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-gitlab-search-wiki-blobs]]'
  - '[[commands/cat-file-contents]]'
  - '[[commands/ssh-gitlab-access]]'
  - '[[commands/id-user-check]]'
  - '[[commands/cat-authorized-keys]]'
  - '[[commands/curl-gitlab-search-blobs]]'
platforms:
  - Linux
techniques:
  - '[[Account Manipulation]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: f72b755c-1984-48a9-af81-d5bd64f6ab59
created_at: '2025-12-11T06:10:29.666Z'
updated_at: '2025-12-11T06:10:29.666Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1098]]'
---
# Generate SSH Key Pair

## Summary

This procedure generates an RSA key pair for use in overwriting authorized_keys to gain persistent SSH access.

## Description

Standard SSH key generation is used to create a public-private key pair, with the public key embedded in a commit message for file overwrite.

## Requirements

1. Access to a system with ssh-keygen installed
2. No specific target access needed at this stage

## Defense

Defensive measures and detection strategies:

- Restrict SSH access to authorized users only
- Monitor authorized_keys file changes

## Objectives

1. Create keys for authentication
2. Prepare public key for injection
3. Enable remote access post-overwrite

## Instructions

### Step 1: Run ssh-keygen

**Context**: Generate RSA keys.

Use ssh-keygen to create the key pair, e.g., named 'gitlab'.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/ssh]]

## Tags

- [[tools/ssh]]
