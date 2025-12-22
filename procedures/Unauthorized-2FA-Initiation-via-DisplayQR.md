---
tags:
  - improper-authentication
  - forced-setup
  - algolia
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.634Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 53b36842-5ecb-4375-a6da-b421bdc9bf1f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized-2FA-Initiation-via-DisplayQR

## Summary

This procedure leverages the unauthenticated /users/displayqr endpoint in Algolia to forcibly start 2FA setup on another user's account by sharing a link, potentially causing disruption without consent.

## Description

The /users/displayqr endpoint lacks proper authentication checks, allowing anyone with the URL to trigger 2FA initiation for the linked account. This can lead to confusion, forced setup prompts, or lockouts if the victim does not complete verification. The attack requires obtaining the link during a legitimate setup and sharing it; it targets web users of Algolia.

## Requirements

1. Access to generate the displayqr URL (from an initiated 2FA setup)
2. Means to share the URL (e.g., email or messaging)
3. Victim must click the link while logged in or accessible

## Defense

Defensive measures and detection strategies:

- Require authentication tokens for all user-specific endpoints
- Log and alert on unexpected 2FA initiations
- Implement CSRF tokens on setup flows
- Scan shared links for sensitive endpoints

## Objectives

1. Disrupt target user's account by forcing 2FA setup
2. Create confusion or denial-of-service via incomplete setup
3. Potentially chain with social engineering

## Instructions

### Step 1: Generate the DisplayQR URL

**Context**: During 2FA initiation, capture the vulnerable endpoint URL.

In the 2FA setup interface, note the URL: https://www.algolia.com/users/displayqr.

> This URL is shareable and triggers setup without checks.

### Step 2: Share the URL with Target

**Context**: Deliver the link to the victim to initiate unauthorized setup.

Send the URL via email, chat, or phishing. When accessed, it starts 2FA on their account.

> Victim sees QR code prompt unexpectedly.

### Step 3: Verify Impact

**Context**: Confirm the forced initiation.

Ask victim or monitor for reports of sudden 2FA prompts.

> Account enters pending 2FA state, risking lockout.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- improper-authentication
- forced-setup
