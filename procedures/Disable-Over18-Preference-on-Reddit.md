---
tags:
  - setup
  - reddit
  - preferences
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 644bf5aa-9a24-4875-a2f5-f27acca2fb6e
created_at: '2025-12-14T17:27:57.280Z'
updated_at: '2025-12-14T17:27:57.280Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Disable-Over18-Preference-on-Reddit

## Summary

This procedure sets up a test environment by disabling the over18 preference on a Reddit account, simulating a user restricted from viewing adult content.

## Description

In the context of testing the CSRF vulnerability on Reddit's /over18 endpoint, this step ensures the account starts in a 'restricted' state. By turning off the preference, any subsequent access to NSFW subreddits will trigger a consent prompt, allowing verification of the exploit's effect. This is a prerequisite for demonstrating the unauthorized modification via CSRF.

## Requirements

1. Valid Reddit account
2. Web browser with login capabilities
3. Access to old.reddit.com for legacy interface

## Defense

Defensive measures and detection strategies:

- Monitor account preference changes for anomalies
- Educate users on secure browsing to avoid unauthorized modifications

## Objectives

1. Simulate underage or restricted user state
2. Confirm initial NSFW block
3. Prepare for CSRF testing

## Instructions

### Step 1: Log In and Access Preferences

**Context**: Authenticate and navigate to user settings to modify the over18 option.

Navigate to https://old.reddit.com/prefs/ in your browser while logged in.

> Scroll to the 'I am over eighteen years old and willing to view adult content' checkbox and uncheck it. Save changes.

### Step 2: Verify Disable

**Context**: Confirm the preference is off by checking settings or attempting NSFW access.

Refresh the preferences page or visit a non-NSFW area to ensure no adult content appears.

> Expected: Checkbox is unchecked; no NSFW in feeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[reddit]]
- [[preferences]]
