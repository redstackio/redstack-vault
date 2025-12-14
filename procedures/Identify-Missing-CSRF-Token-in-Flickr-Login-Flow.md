---
id: proc-uuid-2
tags:
  - csrf
  - analysis
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.687Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Missing-CSRF-Token-in-Flickr-Login-Flow

## Summary

This procedure analyzes the account deletion form in Flickr's new SmugMug-based login flow to confirm the absence of CSRF tokens, contrasting it with the legacy Yahoo system's implicit protections.

## Description

Following the switch from https://login.yahoo.com to https://identity.flickr.com/, the authentication code that previously acted as CSRF protection was removed without replacement. This procedure uses browser inspection to verify the vulnerability, enabling attackers to forge requests from third-party sites. Outcomes include detailed notes on form structure and confirmation of exploitability.

## Requirements

1. Active session from previous authentication
2. Browser developer tools enabled
3. Knowledge of legacy Yahoo auth mechanics

## Defense

Defensive measures and detection strategies:

- Add synchronizer tokens to forms
- Enforce origin/referer header checks
- Log and alert on cross-origin state changes

## Objectives

1. Confirm lack of CSRF token in form
2. Document differences from legacy system
3. Assess exploit potential

## Instructions

### Step 1: Load and Inspect Form Source

**Context**: Examine the raw HTML for token presence.

Navigate to https://www.flickr.com/account/delete and view page source (Ctrl+U). Search for 'csrf' or hidden inputs like <input type="hidden" name="_token">.

### Step 2: Monitor Network Requests

**Context**: Capture form submission to verify token transmission.

Open DevTools Network tab, submit the form, and inspect the POST request payload and headers for any anti-CSRF measures.

### Step 3: Compare with Legacy System

**Context**: Recall or research Yahoo auth to highlight the gap.

Note that Yahoo's flow embedded auth codes in requests, providing implicit protection; confirm new flow lacks this or equivalents.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[analysis]]
- [[web]]
