---
id: proc-steam-submit-modified
tags:
  - idor
  - submit
  - bypass
  - exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Firefox-Quantum]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.150Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Modified-Comment-Request

## Summary

This procedure forwards the IDOR-tampered comment request to the Steam server, verifying the bypass by checking if the unauthorized comment appears on the restricted workshop item.

## Description

Sending the modified POST bypasses the ownership check due to inadequate backend validation, resulting in the comment being added. Refresh the target page to confirm persistence, demonstrating the full impact of spam potential in game communities.

## Requirements

1. Modified request ready in Burp
2. Target page open in browser
3. Awareness of potential account risks

## Defense

Defensive measures and detection strategies:

- Audit logs for anomalous comment sources
- Ownership verification on every write operation
- CAPTCHA on suspicious posts

## Objectives

1. Execute the exploited request
2. Receive successful response
3. Validate comment visibility

## Instructions

### Step 1: Forward Request

**Context**: Send tampered POST to server.

In Burp Repeater, click 'Send' on the modified request.

> Server responds with 200 OK, no auth error.

### Step 2: Verify on Target Page

**Context**: Check for successful bypass.

Refresh https://steamcommunity.com/sharedfiles/filedetails/?id=1404861377 in the browser; look for the test comment.

> Comment appears in the list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Firefox-Quantum]]

## Tags

- bypass
- submit
- verify
