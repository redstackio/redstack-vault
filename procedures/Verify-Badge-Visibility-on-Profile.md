---
id: proc-uuid-3
tags:
  - visibility-check
  - profile-audit
  - reddit
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.827Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Badge-Visibility-on-Profile

## Summary

This procedure checks if an unpinned badge is hidden from public view by accessing the target user's achievements page from an external account.

## Description

After unpinning, badges should not appear on the profile. Using a secondary account or incognito mode simulates an external viewer. This confirms the hiding mechanism works as intended before exploiting the IDOR bypass. Applies to Reddit's web profile pages.

## Requirements

1. Secondary logged-in Reddit account
2. Target username
3. Achievements URL pattern: https://www.reddit.com/user/<username>/achievements/

## Defense

Defensive measures and detection strategies:

- Enforce consistent access controls across endpoints
- Monitor profile views for anomalies
- User notifications for profile access

## Objectives

1. Access target achievements page externally
2. Confirm hidden badge absence
3. Validate public visibility controls

## Instructions

### Step 1: Log In to Secondary Account

**Context**: Switch to external viewpoint.

Log in to the secondary account at reddit.com/login.

### Step 2: Navigate to Target Profile

**Context**: Inspect achievements.

Visit https://www.reddit.com/user/<username>/achievements/ where <username> is the primary account.

### Step 3: Observe Badge Status

**Context**: Check for hidden badge.

Scan the page; the 'New Share' badge should not be visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[visibility-check]]
- [[profile-audit]]
- [[reddit]]
