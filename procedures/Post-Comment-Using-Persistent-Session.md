---
id: proc-003
tags:
  - authorization-bypass
  - unauthorized-posting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:52.142Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Post-Comment-Using-Persistent-Session

## Summary

This procedure exploits uninvalidated sessions to post comments on a crew wall as an ex-member, bypassing authorization checks.

## Description

After kickout, the session retains old permissions because the platform fails to invalidate tokens or re-verify membership on actions like posting to the crew wall. This is tested via the web endpoint for comments, likely a POST request to a crew-specific API without status checks. The vulnerability allows abuse of crew features, such as spamming or sensitive info disclosure.

## Requirements

1. Persistent session from prior steps
2. Web browser with original cookies
3. URL/path to crew wall posting feature

## Defense

Defensive measures and detection strategies:

- Enforce membership verification on every crew action
- Use short-lived sessions or JWTs with status claims
- Log and block actions from non-members

## Objectives

1. Submit a comment using the old session
2. Confirm posting succeeds without errors
3. Demonstrate unauthorized access impact

## Instructions

### Step 1: Navigate to Crew Wall

**Context**: Access the posting interface with the persistent session.

In the same browser, go to the crew wall page.

> Expected: Page loads without logout, showing post input.

### Step 2: Attempt to Post Comment

**Context**: Submit content to test permissions.

Enter a test message and submit the post form.

> Expected: No permission error; comment submits successfully.

### Step 3: Verify Unauthorized Post

**Context**: Confirm the action's success and impact.

Refresh the wall or check as another member to see the comment.

> Expected: Comment visible, proving bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authorization-bypass]]
- [[unauthorized-posting]]
