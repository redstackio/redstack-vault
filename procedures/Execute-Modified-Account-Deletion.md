---
id: proc-uuid-3
tags:
  - idor
  - account-deletion
  - api-exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.193Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Modified-Account-Deletion

## Summary

This procedure submits the modified deletion request via Burp Suite to exploit the IDOR and permanently remove the victim's Firefox account, disrupting access to linked Mozilla services.

## Description

With the payload altered to the victim's email, sending the POST request to the API endpoint bypasses ownership checks due to missing session verification. This results in irreversible account deletion for SSO users, impacting services like Sync without needing victim credentials beyond their email.

## Requirements

1. Modified request prepared in Burp Repeater
2. Valid attacker session cookies in request headers
3. Victim's email in the payload

## Defense

Defensive measures and detection strategies:

- Implement strict session-to-account binding checks on destructive APIs
- Use multi-factor confirmation for deletions
- Audit logs for deletion requests and correlate with user sessions

## Objectives

1. Trigger server-side deletion of the targeted account
2. Confirm impact on victim's service access
3. Validate exploitation success without errors

## Instructions

### Step 1: Review Modified Request

**Context**: Ensure the payload and headers are correctly set before execution.

In Burp Repeater, confirm URL is https://api.accounts.firefox.com/v1/account/destroy, method POST, body {"email": "victims344@gmail.com"}, and Cookie header includes session tokens.

### Step 2: Submit the Request

**Context**: Send the tampered request to invoke the deletion.

Click 'Send' in Repeater; observe the response for success (e.g., 200 OK without validation errors).

### Step 3: Verify Deletion Impact

**Context**: Test that the victim's account is inaccessible.

Attempt victim login or check Mozilla services; confirm account is deleted or access revoked.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[account-deletion]]
- [[api-exploitation]]
