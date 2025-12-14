---
tags:
  - authorization
  - oauth
  - csrf
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:27:57.849Z'
sub_techniques: []
id: bd3d4222-06e0-42bd-8a3a-a81ecd0a25c0
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Trigger-Authorization-via-Victim-Interaction

## Summary

This procedure describes the victim-side interaction with the crafted URL, resulting in the unauthorized linking of their external account (e.g., GitHub) to the attacker's HackerOne via the CSRF-vulnerable OAuth flow.

## Description

When the victim clicks the link, the GET request to /oauth2/auth initiates the flow. If the victim's GitHub is already authorized in their HackerOne, it silently redirects to the callback. Otherwise, GitHub prompts for consent; upon approval, it redirects to /oauth2/token with code and state parameters. The backend validates the state (tied to attacker's ID) without CSRF checks, linking the account to the attacker.

## Requirements

1. Victim must click the provided URL
2. Victim's GitHub account linked or consenting to HackerOne
3. No additional attacker action needed here

## Defense

Defensive measures and detection strategies:

- Require explicit user confirmation for integrations
- Validate CSRF on all OAuth endpoints
- Audit linked accounts regularly

## Objectives

1. Forge authorization request
2. Link victim's credentials to attacker
3. Enable post-exploitation access

## Instructions

### Step 1: Victim Clicks URL

**Context**: Link loads the OAuth auth page.

Victim browser navigates to the crafted GET URL, starting the flow.

### Step 2: Handle Authorization Prompt

**Context**: Process consent or silent redirect.

If unlinked, GitHub shows consent screen; victim approves, leading to redirect: https://hackerone.integration-authentication.com/oauth2/token?code=...&state=....

If linked, direct redirect to callback: https://hackerone.integration-configuration.com/auth/cb?id=<Auth ID>.

### Step 3: Backend Processes Linkage

**Context**: State parameter causes linkage to attacker's account.

The /oauth2/token endpoint exchanges code for token, associating with attacker's authentication ID.

**Expected Output**: Account linked; attacker gains access via Tray.io.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authorization]]
- [[oauth]]
- [[csrf]]
