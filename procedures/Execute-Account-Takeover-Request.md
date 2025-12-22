---
tags:
  - account-takeover
  - password-change
  - exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:11.894Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 515a9091-e673-48b9-948b-3affe039eeb0
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
---

# Execute Account Takeover Request

## Summary

This procedure sends the modified HTTP request via Burp Repeater to change a target user's password, resulting in full account takeover and potential access to sensitive DoD information without any authentication.

## Description

Following request modification, this step executes the exploit against the vulnerable password change endpoint. The lack of authentication and proper IDOR validation allows the server to process the request as if from the victim, updating their password. Success grants the attacker login access, enabling data exfiltration or further persistence in the DoD environment.

## Requirements

1. Modified request ready in Burp Repeater
2. Network connectivity to the target endpoint
3. Post-exploitation verification method (e.g., login attempt)

## Defense

Defensive measures and detection strategies:

- Require multi-factor authentication (MFA) for password changes
- Audit logs for password update events and correlate with user sessions
- Deploy anomaly detection for unauthenticated or cross-user requests
- Use CAPTCHA or secondary verification for sensitive actions

## Objectives

1. Perform unauthorized password change
2. Gain control of the victim's account
3. Access sensitive DoD resources

## Instructions

### Step 1: Send the Request

**Context**: Transmit the modified POST request to the server to trigger the IDOR exploitation.

In Burp Repeater, click the 'Send' button to forward the request to the target endpoint.

> Request sent; monitor the response pane for status and body.

### Step 2: Analyze Response

**Context**: Verify the success of the password change operation.

Check the response code (expect 200 OK) and body for confirmation messages, such as {"success": true} or similar.

> Successful response indicates password updated; failure may show validation errors.

### Step 3: Validate Takeover

**Context**: Confirm control by logging in with the new credentials.

Use a browser or tool to attempt login with the victim's email and new password. Access account dashboard to verify.

> Login successful; account dashboard loads with sensitive data visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[account-takeover]]
- [[exploitation]]

