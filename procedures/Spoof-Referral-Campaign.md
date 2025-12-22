---
id: proc-uuid-3
tags:
  - spoofing
  - campaign-tampering
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
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.631Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Spoof-Referral-Campaign

## Summary

This procedure modifies the campaign path in Airbnb referral URLs to spoof the referral source, enhancing the IDOR exploit by disguising the origin.

## Description

The URL path after `/c/` (e.g., 'spent1') is not strictly enforced, allowing attackers to change it to arbitrary strings like 'fun' while maintaining functionality, which can help evade basic logging or filters.

## Requirements

1. Modified URL from prior IDOR parameter tampering
2. Browser for testing the altered path

## Defense

Defensive measures and detection strategies:

- Validate campaign paths against a whitelist of allowed values
- Cross-check path with session data for consistency
- Monitor for unusual campaign strings in access logs

## Objectives

1. Alter apparent referral source without breaking link validity
2. Test for additional path-based validation weaknesses
3. Support stealthy repeated exploitation

## Instructions

### Step 1: Identify Campaign Segment

**Context**: Locate the path after `/c/` in the URL.

Examine the URL, e.g., `/c/spent1`.

### Step 2: Replace with Arbitrary Value

**Context**: Spoof the campaign to test enforcement.

Change to `/c/fun`, e.g., `https://www.airbnb.com/c/fun?euid=2&ri=14052213&s=30`. Reload in browser.

**Expected Output**: Functional referral page under the new campaign name.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[spoofing]]
- [[campaign-tampering]]
- [[web]]
