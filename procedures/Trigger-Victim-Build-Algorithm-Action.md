---
id: proc-837328-trigger-post
tags:
  - social-engineering
  - post-exploitation
  - account-takeover
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.003Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Victim-Build-Algorithm-Action

## Summary

This procedure relies on social engineering to induce the victim to click the 'Build Algorithm' button after element manipulation, causing their browser to issue a POST request to a path-traversed URL under their authenticated session, executing arbitrary actions like profile updates or message sending.

## Description

Once #algo-id is set to a traversal payload, the button's JavaScript constructs a POST to /algorithms/{id}/validate, but {id} traversal redirects to other endpoints (e.g., /users/send_user_message). This exploits the lack of URL sanitization and runs in the victim's context, bypassing server-side auth checks. Applicable in collaborative web sessions; impacts include spam, deletions, and settings changes.

## Requirements

1. Manipulated #algo-id in victim's browser
2. Active collaboration session
3. Ability to communicate with victim (e.g., in-app chat)

## Defense

Defensive measures and detection strategies:

- Server-side path normalization and endpoint validation for all dynamic requests
- Client-side confirmation dialogs before critical actions like 'Build'
- Anomaly detection on POST requests from collaboration contexts

## Objectives

1. Prompt victim to perform the triggering action
2. Execute the traversed POST under victim's credentials
3. Achieve desired impact (e.g., disable notifications, send spam)

## Instructions

### Step 1: Social Engineering Prompt

**Context**: Convince victim to click 'Build Algorithm' without suspicion.

In the collaboration chat, suggest testing the algorithm or building it, e.g., "Hey, try building to see the changes."

**Expected Output**: Victim agrees and prepares to click.

### Step 2: Observe Execution

**Context**: Monitor for the POST request and effects.

Watch victim's browser network tab or backend logs; no direct command, but verify via secondary effects (e.g., check if message was sent).

**Expected Output**: POST issued to manipulated URL, action completes (e.g., preferences updated).

### Step 3: Validate Impact

**Context**: Confirm the arbitrary action succeeded.

Access victim's account indirectly (e.g., via recipient for messages) or observe changes in session.

**Expected Output**: Evidence of action, like disabled emails or altered profile.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[social-engineering]]
- [[post-exploitation]]
- [[account-takeover]]
