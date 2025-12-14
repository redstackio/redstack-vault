---
id: 456b3eea-6669-4870-a507-527aabe19468
name: Force-Victim-Authentication-as-Attacker
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.341Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - csrf
  - account-takeover
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Force-Victim-Authentication-as-Attacker

## Summary

This procedure completes the OAuth flow when the victim accesses the URL, logging them in as the attacker due to missing CSRF checks.

## Description

The victim's browser processes the token-embedded URL, authenticating against the attacker's Bitbucket account without session validation, resulting in session hijacking.

## Requirements

1. Victim accessing the crafted URL
2. Active Gratipay and Bitbucket services
3. No intervening CSRF protections

## Defense

Defensive measures and detection strategies:

- Require state/nonce in OAuth responses
- Log cross-origin OAuth completions
- Session fixation prevention

## Objectives

1. Authenticate victim as attacker
2. Gain unauthorized access under attacker's identity
3. Enable follow-on exploitation

## Instructions

### Step 1: Victim Accesses URL

**Context**: Initiate flow completion.

Victim clicks the link, loading /auth/login/bitbucket:bitbucket.com/?oauth_token={token}.

> The endpoint processes without state check.

### Step 2: Authentication Succeeds

**Context**: Establish session.

Gratipay creates a session tied to attacker's account; victim sees attacker's dashboard.

> Expected output: Login complete; potential actions like payments under attacker's name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf]]
- [[account-takeover]]
