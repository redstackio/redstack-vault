---
tags:
  - url-copy
  - bypass
  - uber
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
updated_at: '2025-12-14T17:31:10.979Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7fe05ea5-296f-46a4-a749-af30f8163873
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Copy-and-Test-URL-in-New-Browser

## Summary

This procedure extracts the settings URL and tests it in an unauthenticated browser session, confirming the bypass.

## Description

Copying the URL with its token and pasting into a new, cookie-less browser demonstrates that no session is required for access. Target is the Uber web app; prerequisites are the loaded settings page. Outcome: Unauthorized interaction with user data.

## Requirements

1. Loaded settings page URL
2. Second browser or incognito mode
3. Clipboard access

## Defense

Defensive measures and detection strategies:

- Use short-lived tokens
- Require CSRF tokens alongside URL
- Log direct URL accesses

## Objectives

1. Extract persistent token
2. Validate unauthenticated access
3. Enable setting modifications

## Instructions

### Step 1: Copy Full URL

**Context**: Capture the token-embedded link.

Highlight and copy the entire address bar content while on the settings page.

> Ensure the token parameter is included.

### Step 2: Paste and Load in New Session

**Context**: Test isolation from original session.

Open incognito mode, paste the URL, and press enter. Toggle a setting to verify functionality.

> Page loads and saves changes without login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-copy]]
- [[bypass]]
- [[uber]]
