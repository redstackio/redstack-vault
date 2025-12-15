---
tags:
  - upload
  - modification
  - defacement
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/update-autodesk-profile-photo]]'
platforms:
  - Web
techniques:
  - '[[Account Manipulation]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: dce14361-4509-455e-ba6a-46d407914999
created_at: '2025-12-14T17:30:27.255Z'
updated_at: '2025-12-14T17:30:27.255Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Submit Unauthorized Photo Update

## Summary

This procedure completes the IDOR attack by submitting a photo upload request with the manipulated 'id' parameter, resulting in unauthorized modification of the target user's profile picture on Autodesk.

## Description

Following parameter manipulation, the photo update endpoint processes file uploads without verifying user ownership of the referenced profile. This allows attackers to deface or tamper with any user's visible profile image, potentially leading to social engineering or privacy issues. The attack relies on multipart form data submission over HTTPS.

## Requirements

1. Manipulated session with target ID from previous step
2. Local image file for upload (e.g., JPG under size limits)
3. Proxy for final interception if needed

## Defense

Defensive measures and detection strategies:

- Enforce strict authorization on all update endpoints, rejecting mismatched IDs
- Scan uploaded files for malware and validate against user permissions
- Implement audit trails for profile changes, alerting on anomalous IPs or rapid modifications

## Objectives

1. Transmit the upload request with tampered ID
2. Achieve successful profile update for the target
3. Validate the impact without triggering alerts

## Instructions

### Step 1: Prepare and Intercept Upload

**Context**: Use the edit form to select and submit the photo while ensuring the ID remains manipulated.

**Instructions**: In the browser (proxied through Burp), select a new photo file in the edit interface and click submit. Intercept the resulting POST request in Burp, verify 'id=target_user_id', adjust if needed, and forward.

### Step 2: Simulate or Execute Upload

**Context**: Directly send the request if form details are known, bypassing the UI.

**Command** ([[commands/update-autodesk-profile-photo]]):
```bash
curl -X POST -v -H "Cookie: your_session_cookie" -F "id=target_user_id" -F "photo=@/path/to/new_photo.jpg" "https://profile.autodesk.com/update-photo"
```

> This performs the multipart upload. Extract session cookie and endpoint from prior inspections; add other form fields (e.g., -F "csrf_token=...") if required. Expected output: Success response (e.g., JSON {"status": "updated"}) or redirect to profile.

### Step 3: Verify Modification

**Context**: Confirm the attack's effect on the target profile.

**Instructions**: Log out or use incognito to view the target's profile at profile.autodesk.com/user/target_user_id. The new photo should appear, indicating successful tampering.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/update-autodesk-profile-photo]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- unauthorized-upload
- profile-defacement
