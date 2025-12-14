---
tags:
  - bitwarden
  - credential
  - trigger
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
updated_at: '2025-12-14T04:08:55.250Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: c1b6995a-23dc-494c-a077-96712e369a9c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add Credential in Bitwarden to Trigger Fetch

## Summary

Add a new login credential in the Bitwarden UI with a URL pointing to the attacker's domain, triggering the vulnerable icon fetching SSRF.

## Description

When a credential is added with a URL like http://www.yourdomain.com, Bitwarden's IconsController.cs fetches the favicon, following the redirect chain to internal hosts if enabled.

## Requirements

1. Active Bitwarden session
2. Icon fetching enabled in settings
3. Valid organization or personal vault access

## Defense

Defensive measures and detection strategies:

- Disable automatic icon fetching
- Whitelist allowed domains for fetches
- Audit credential URLs for suspicious patterns

## Objectives

1. Initiate the SSRF via legitimate feature
2. No authentication bypass needed
3. Observe fetch in service logs

## Instructions

### Step 1: Log In to Bitwarden

**Context**: Access the web vault.

Navigate to https://your-bitwarden-ip and log in with created account.

> Expected: Dashboard loaded.

### Step 2: Add New Login Item

**Context**: Input malicious URL.

Click "Add Item" > Login, set URL: http://www.yourdomain.com, fill dummy username/password, save.

> Expected: Item saved; icon fetch queued in background.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- bitwarden
- credential
- trigger
