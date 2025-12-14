---
id: proc-vk-reset-hash-001
tags:
  - reset-hash
  - auth-bypass
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:47.856Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Obtain VK User Reset Hash

## Summary

This procedure describes how to acquire a session reset hash for a VK.com user, which is a critical prerequisite for bypassing 2FA in subsequent steps of an account takeover attack.

## Description

In the VK.com platform, the session reset functionality generates a temporary reset_hash when a user requests to terminate active sessions, often via email or account settings. This hash is intended for the legitimate user but lacks verification in the reset process, making it exploitable. The attack scenario involves obtaining this hash through social engineering, email interception, or prior access to the user's recovery mechanisms. Expected outcomes include possession of a valid hash tied to the target account, enabling unauthorized session manipulation without credentials.

## Requirements

1. Target user's email access or social engineering capability to trigger reset
2. Knowledge of VK.com account recovery flows
3. Web browser for interacting with the platform

## Defense

Defensive measures and detection strategies:

- Implement hash expiration and IP/user binding during reset
- Monitor for unusual reset requests from unknown sources
- Require additional verification (e.g., CAPTCHA) on reset initiation

## Objectives

1. Secure a valid reset_hash for the target VK.com user
2. Ensure the hash is active and unexpired
3. Prepare for session reset exploitation

## Instructions

### Step 1: Trigger Session Reset

**Context**: Initiate the reset process to generate the hash, simulating a legitimate user action.

Navigate to VK.com account settings or use the password recovery flow to request session termination. The system emails or displays the reset_hash.

> If access to the user's email is available, retrieve the hash directly from the recovery email. Otherwise, use phishing to trick the user into triggering the reset and sharing the link.

### Step 2: Extract the Reset Hash

**Context**: Isolate the hash value from the reset mechanism.

Inspect the reset URL or email content for the `reset_hash` parameter, typically a long alphanumeric string (e.g., `abc123def456`).

> Copy the hash exactly as it appears, ensuring no modifications that could invalidate it.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[reset-hash]]
- [[auth-bypass]]
