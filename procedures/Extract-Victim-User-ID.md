---
tags:
  - id-extraction
  - discovery
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:12.352Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ebcf7443-dc78-4da9-8f12-21eec4b1f251
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-Victim-User-ID

## Summary

This procedure logs into the victim account and uses Burp Suite to capture the profile update request, extracting the numeric user ID without making changes, to enable targeted IDOR attacks.

## Description

User IDs in the target application are predictable numerics exposed in endpoint paths. By simulating a profile update action in the victim session and intercepting the request, the ID is revealed. This step is non-destructive as the request is not forwarded, preserving the victim's profile.

## Requirements

1. Active victim account
2. Separate browser instance with Burp Suite proxy
3. Knowledge of profile update navigation from prior steps

## Defense

Defensive measures and detection strategies:

- Obfuscate or UUID-ize user IDs instead of sequential numerics
- Enforce session isolation and log cross-session activities
- Rate limit profile access attempts

## Objectives

1. Access victim account session
2. Trigger and capture ID-revealing request
3. Note the numeric ID for exploitation

## Instructions

### Step 1: Log In to Victim Account

**Context**: Establish a session for the target account.

Use a clean browser session to log in to the victim account on mtnmobad.mtnbusiness.com.ng.

### Step 2: Navigate to Profile Update

**Context**: Initiate the action that exposes the ID.

Go to the profile settings and start an update (e.g., edit a field) to generate the request.

### Step 3: Capture and Extract ID

**Context**: Inspect without altering the profile.

Intercept the request in Burp Proxy, note the ID in the path (e.g., /update/12345), then drop or cancel the request to avoid changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[id-extraction]]
- [[Discovery]]
