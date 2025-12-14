---
id: proc-uuid-3
tags:
  - idor
  - verification
  - profile
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.152Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Social-Link-Modification-on-Reddit-Profile

## Summary

This procedure confirms the success of social link modifications by inspecting the target user's Reddit profile page for the updated links.

## Description

After executing the modification mutation, changes may take a few seconds to propagate. This step involves manual verification via the web interface to ensure the IDOR exploit worked as intended, observing the new URL, title, or type in the social links section.

## Requirements

1. Access to a web browser
2. URL of the target user's profile

## Defense

Defensive measures and detection strategies:

- Implement real-time profile change notifications to users
- Monitor for rapid profile edits from suspicious IPs
- Use client-side validation to flag unexpected link changes

## Objectives

1. Validate exploit success
2. Confirm persistence of modifications
3. Identify any delays in propagation

## Instructions

### Step 1: Access Profile

**Context**: Navigate to the target user's profile page.

**Instructions**: Open https://www.reddit.com/user/targetuser in a browser.

### Step 2: Refresh and Inspect

**Context**: Check the social links section multiple times.

**Instructions**: Reload the page 2-3 times or wait 10-30 seconds, then scroll to the social links area to verify the updated content.

> Look for the new 'outboundUrl', 'title', and 'type' matching your modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- verification
- reddit
