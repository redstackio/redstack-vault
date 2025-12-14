---
tags:
  - verify
  - impact
  - upload
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T05:32:10.235Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3bafdbdc-0547-42d0-a8b0-6ca98d5f1e35
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forward-Modified-Request-and-Verify-Impact

## Summary

This procedure submits the tampered upload request and confirms the IDOR exploitation by checking the target profile for the unauthorized image change.

## Description

Forwarding via Burp sends the modified request to the server, which processes it without auth checks, applying the image to the wrong account. In the DoD context, this verifies impersonation potential. Requires modified request; outcomes include visible profile alteration, highlighting misinformation risks.

## Requirements

1. Modified request in Burp Suite
2. Access to target profile view
3. Valid session for verification

## Defense

Defensive measures and detection strategies:

- Audit image uploads for ownership mismatches post-upload
- Implement image approval workflows with admin review

## Objectives

1. Execute the exploit
2. Confirm unauthorized modification
3. Assess impersonation feasibility

## Instructions

### Step 1: Forward Request

**Context**: Send the altered request to the server.

In Burp, click 'Forward' or use Repeater to send.

> Expected output: Server response (e.g., 200 OK) indicating successful upload.

### Step 2: Verify on Target Profile

**Context**: Navigate to the victim's profile to check for the image.

Browse to the target account's profile page.

> Expected output: Uploaded image appears in the 'approved' tab of the profile.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[verify]]
- [[Impact]]
- [[upload]]
