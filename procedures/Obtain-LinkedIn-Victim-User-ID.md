---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - recon
  - user-discovery
  - linkedin
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:27:57.355Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Obtain-LinkedIn-Victim-User-ID

## Summary

This procedure retrieves the publicly available fsd_profile user ID from a LinkedIn profile, which is essential for targeting in CSRF attacks on LinkedIn endpoints.

## Description

LinkedIn exposes user IDs via the fsd_profile parameter in profile page requests, allowing attackers to identify and target specific users without authentication. This step is non-technical and relies on public profile access, setting up the payload for follow actions. Expected outcome is obtaining a unique identifier for the entityUrn in the CSRF URL.

## Requirements

1. Internet access to LinkedIn.com
2. Target user's public profile URL
3. Browser with developer tools for inspection (optional but recommended)

## Defense

Defensive measures and detection strategies:

- Limit profile visibility to connections only
- Monitor for unusual profile access patterns
- Educate users on public data exposure risks

## Objectives

1. Gather target user ID for CSRF payload construction
2. Enable precise targeting without authentication
3. Prepare for unauthorized action simulation

## Instructions

### Step 1: Access Target Profile

**Context**: Navigate to the victim's LinkedIn profile to access public metadata.

Open a browser and visit the target's profile, e.g., https://www.linkedin.com/in/username.

> Inspect the page source or network tab in developer tools (F12) for requests containing fsd_profile.

### Step 2: Extract fsd_profile Value

**Context**: Identify the user ID from profile data.

Search for "fsd_profile" in the network requests or page elements to retrieve the value, typically a numeric ID like "123456789".

> Copy the ID for use in subsequent steps; no execution required beyond manual extraction.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[user-discovery]]
- [[linkedin]]
