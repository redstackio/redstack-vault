---
id: proc-vimeo-access-videos
tags:
  - idor
  - data-access
  - web
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.781Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Private-Videos-via-IDOR

## Summary

This procedure constructs and loads a URL with the manipulated 'badge_channel' parameter to display videos from a private Vimeo channel without requiring membership.

## Description

Using the tampered parameters from interception (e.g., user_id=36807051, badge_channel=870575, badge_album=3231945), build the full URL and open in a browser. The endpoint lacks checks, rendering private videos. Assumes logged-in session. Outcome: Visible private content.

## Requirements

1. Manipulated URL parameters
2. Logged-in browser session
3. Target private channel details

## Defense

Defensive measures and detection strategies:

- Enforce session-based channel membership verification in widget rendering
- Scan for direct URL access to sensitive endpoints

## Objectives

1. Load private videos via tampered URL
2. Bypass privacy restrictions
3. Expose sensitive video content

## Instructions

### Step 1: Construct and Open URL

**Context**: Paste the full URL into the browser address bar.

Visit: https://vimeo.com/tools/widget/montage?widget=1&preview=1&user_id=36807051&badge_stream=channel&badge_channel=870575&badge_album=3231945&badge_layout=horizontal&badge_quantity=6&show_titles=no&badge_size=80

> Widget loads showing private channel videos.

**Expected Output**: Thumbnails and playable videos from the private channel.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[data-access]]
