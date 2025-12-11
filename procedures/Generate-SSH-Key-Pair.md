---
tags:
  - ssh
  - key-generation
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Account Manipulation]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: e71226a1-a017-4531-bae1-7cf44fdedbb9
created_at: '2025-12-11T03:47:47.593Z'
updated_at: '2025-12-11T03:47:47.593Z'
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

This procedure generates an RSA SSH key pair for use in authentication and access escalation.

## Description

Create a new key pair to inject the public key into authorized_keys for remote access. This is a standard setup step for SSH-based exploits.

## Requirements

1. SSH keygen tool available

## Defense

Defensive measures and detection strategies:

- Monitor for unauthorized key additions
- Use key management systems

## Objectives

1. Create private/public key pair
2. Prepare for key injection

## Instructions

### Step 1: Run Key Generation

**Context**: Generate RSA keys.

> Use ssh-keygen to create the pair named 'gitlab'.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[tools/ssh]]
- #key-generation
