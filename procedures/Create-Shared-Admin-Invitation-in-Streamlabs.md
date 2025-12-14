---
tags:
  - social-engineering
  - shared-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: d63ac4a1-68e3-4d03-b5ce-8b0867517303
created_at: '2025-12-13T23:52:55.375Z'
updated_at: '2025-12-13T23:52:55.375Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Shared-Admin-Invitation-in-Streamlabs

## Summary

This procedure involves tricking a victim into creating a shared administrator invitation link in Streamlabs, granting temporary access to their dashboard for subsequent exploitation.

## Description

In the Streamlabs dashboard, users can generate invitation links for shared access roles like Administrator. This procedure relies on social engineering (e.g., phishing email prompting collaboration) to get the victim to create and share such a link. Once obtained, it enables the attacker to impersonate the victim. Prerequisites include the victim having an active Streamlabs account with goal features.

## Requirements

1. Victim's cooperation via social engineering to access settings
2. Internet access to Streamlabs dashboard
3. No technical tools required beyond a browser

## Defense

Defensive measures and detection strategies:

- Educate users on risks of sharing admin links
- Monitor for unusual invitation creations in audit logs
- Expire shared access links quickly

## Objectives

1. Obtain a valid admin invitation link
2. Enable temporary privilege escalation
3. Set up for dashboard access

## Instructions

### Step 1: Prompt Victim to Create Invitation

**Context**: Use social engineering to direct the victim to the shared access settings.

**Instructions**: Send a phishing message encouraging the victim to invite you as an admin for 'collaboration'. Direct them to https://streamlabs.com/dashboard#/settings/shared-access.

**Expected Output**: Victim generates and shares the link.

### Step 2: Verify Link Format

**Context**: Ensure the link is for Administrator role.

**Instructions**: Inspect the shared link to confirm it points to shared-access with admin permissions.

**Expected Output**: Link ready for acceptance.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[Phishing]]
