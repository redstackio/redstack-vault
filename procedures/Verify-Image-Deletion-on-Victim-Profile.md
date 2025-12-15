---
id: proc-verify-deletion
tags:
  - verification
  - post-exploit
  - profile-check
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Resource Hijacking]]'
updated_at: '2025-12-14T17:25:47.458Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Resource Hijacking]]'
---
# Verify-Image-Deletion-on-Victim-Profile

## Summary

This procedure confirms the success of the IDOR exploitation by refreshing the victim's public profile and checking for the absence of the targeted featured image.

## Description

Post-exploitation validation ensures the deletion occurred without alerting the victim immediately. Access the public profile URL, navigate to Featured, and inspect for the missing media. This step highlights the impact: unauthorized profile disruption. If the image persists, recheck request parameters or API response.

## Requirements

1. Victim profile URL
2. Web browser
3. Recent exploitation timestamp for timing

## Defense

Defensive measures and detection strategies:

- Notify users of profile changes via email/SMS
- Log media deletions and correlate with user activity

## Objectives

1. Validate unauthorized modification
2. Assess impact on victim profile
3. Identify any partial failures

## Instructions

### Step 1: Refresh Victim Profile

**Context**: Check current state post-request.

Open the victim's profile in an incognito browser tab and wait 10-30 seconds for propagation.

### Step 2: Inspect Featured Section

**Context**: Confirm image removal.

Scroll to Featured; targeted image should be gone. Compare with screenshot if available.

**Expected Output**: Image no longer listed or viewable.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Resource Hijacking]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[post-exploit]]
- [[profile-check]]
