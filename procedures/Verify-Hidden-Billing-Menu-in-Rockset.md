---
tags:
  - verification
  - ui-check
  - rockset
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:28:51.654Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7f318b75-4322-4b3b-9b3c-a70a7423d626
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-Hidden-Billing-Menu-in-Rockset

## Summary

This procedure checks the Rockset console navigation menu after member login to confirm that the billing option is hidden, illustrating the vulnerability's reliance on client-side enforcement rather than server-side checks.

## Description

Once logged in as a member, inspect the sidebar or top navigation for any 'Billing' or 'Account Settings' links. In a properly restricted view, these should be absent, but this step verifies the setup before attempting direct access. The target is the member dashboard UI, with the expected outcome being no visible path to billing, priming the bypass exploit.

## Requirements

1. Active member session in the browser
2. Familiarity with the Rockset UI layout
3. No ad blockers interfering with menu rendering

## Defense

Defensive measures and detection strategies:

- Conduct UI audits to ensure hidden elements cannot be revealed via dev tools
- Log UI interactions to detect attempts to access hidden routes
- Use client-side obfuscation combined with server-side enforcement

## Objectives

1. Confirm member privileges hide admin UI elements
2. Validate the vulnerability precondition
3. Avoid false positives in access testing

## Instructions

### Step 1: Inspect Navigation Menu

**Context**: Review visible options post-login.

After logging in, expand or scroll through the left sidebar or top menu bar.

> Look for sections like 'Settings', 'Organization', or 'Billing'; none should include billing for members.

### Step 2: Search for Hidden Options

**Context**: Attempt to locate billing via search or browse.

Use any in-app search function or manually click through available menus.

> No billing-related links should appear, confirming the hide.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- ui-check
- rockset
