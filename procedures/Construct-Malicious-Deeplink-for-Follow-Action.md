---
tags:
  - csrf
  - deeplink
  - android
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:27:57.889Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bfc2adc8-57f4-4302-8a52-044067102f84
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Construct-Malicious-Deeplink-for-Follow-Action

## Summary

This procedure crafts a malicious deeplink URL targeting the Periscope app's follow action, using a known user ID to force an unauthorized follow when invoked.

## Description

Based on manifest analysis, the deeplink pscp://user/<user-id>/follow directly executes the follow without consent in the Android app, differing from the web version's prompt at www.pscp.tv/<user-id>/follow. Obtain <user-id> from Periscope's user profiles or featured sections. This enables embedding in phishing links for CSRF exploitation. Expected outcome: A functional URL that triggers the app action seamlessly.

## Requirements

1. Target user ID from Periscope app or website
2. Knowledge of deeplink scheme from prior analysis
3. Text editor for URL construction

## Defense

Defensive measures and detection strategies:

- Add user confirmation or token validation in deeplink handlers
- Log and alert on unexpected deeplink invocations in app analytics
- Educate users on avoiding suspicious links that open apps

## Objectives

1. Format deeplink to target specific follow action
2. Ensure compatibility with Android intent system
3. Prepare for embedding in attack payloads

## Instructions

### Step 1: Obtain Target User ID

**Context**: Identify the victim's target account ID for the follow.

Navigate to Periscope app's featured users or website profile.

> Extract the numeric or string ID, e.g., <user-id> = 123456789.

### Step 2: Build the Deeplink

**Context**: Assemble the URL using the scheme and path.

Construct as pscp://user/<user-id>/follow.

> Example: pscp://user/123456789/follow. Test by pasting into Android browser to verify app launch (without full execution if not logged in).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- csrf
- deeplink
- android
