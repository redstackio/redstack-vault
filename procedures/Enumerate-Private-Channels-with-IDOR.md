---
id: proc-vimeo-enumerate-channels
tags:
  - enumeration
  - idor
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.773Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate-Private-Channels-with-IDOR

## Summary

This procedure iteratively modifies the 'badge_channel' parameter with different IDs to discover and access videos from multiple private Vimeo channels, exploiting the IDOR for broad enumeration.

## Description

Starting from the base manipulated URL, replace badge_channel with sequential or guessed valid IDs (e.g., increment from known channels). Reload each time to check for content. No validation ties the parameter to user_id, enabling discovery. Requires prior URL construction. Outcome: Access to various private contents.

## Requirements

1. Base manipulated URL
2. List of potential channel IDs
3. Browser for repeated testing

## Defense

Defensive measures and detection strategies:

- Implement ID validation and user-channel authorization on all widget requests
- Use anomaly detection for rapid parameter changes in sessions

## Objectives

1. Enumerate private channels via parameter changes
2. Bypass controls for multiple targets
3. Collect sensitive videos across channels

## Instructions

### Step 1: Iterate Parameter Values

**Context**: Systematically test different channel IDs.

Modify badge_channel={any valid value} (e.g., 870576, 870577) and reload the URL.

> Successful loads reveal private videos; failures show errors.

**Expected Output**: Videos from enumerated private channels displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[enumeration]]
- [[idor]]
