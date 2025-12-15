---
id: p2b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - idor
  - unauthorized-access
  - file-download
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:28.660Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Access-Unauthorized-Attachment-as-Another-User

## Summary

This procedure exploits IDOR to access and download another user's attachment in Nextcloud Deck by directly navigating to the known URL from an unauthorized session.

## Description

After capturing the attachment URL from an upload by User A, switch to User B's session (with no shared access to the board or task). The lack of permission checks on the endpoint allows User B to view and download the file, demonstrating confidentiality breach. This targets the /apps/deck/cards/{card_id}/attachment/{attachment_id} endpoint.

## Requirements

1. Captured attachment URL from a legitimate upload.
2. Second user account (User B) with basic authentication to Nextcloud.
3. Web browser or curl for accessing the URL.

## Defense

Defensive measures and detection strategies:

- Enforce ownership checks on attachment requests using user ID from session.
- Include CSRF tokens and board/task permission validation.
- Log and alert on cross-user attachment accesses.

## Objectives

1. Bypass access controls to view unauthorized files.
2. Download sensitive attachments for exfiltration.
3. Validate IDOR impact on confidentiality.

## Instructions

### Step 1: Login as User B

**Context**: Switch to an unauthorized user session to test access controls.

Log out of User A and log in as User B at the Nextcloud URL. Ensure User B has no permissions on User A's board or task.

**Expected Output**: Successful login; Deck app accessible but no visibility to User A's content.

### Step 2: Access the Captured URL

**Context**: Directly request the attachment to exploit IDOR.

Navigate to the captured URL (e.g., https://us.cloudamo.com/apps/deck/cards/8420/attachment/30) in the browser. Alternatively, use curl to fetch:

Execute [[commands/curl-access-url]] to verify:

```bash
curl -u "UserB:password" -O https://us.cloudamo.com/remote.php/dav/files/UserB/apps/deck/cards/8420/attachment/30
```

> This downloads the file if accessible; expect HTTP 200 with file content.

**Expected Output**: File loads in browser or downloads via curl, without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- idor
- unauthorized-access
