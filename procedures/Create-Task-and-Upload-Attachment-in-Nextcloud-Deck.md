---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - nextcloud
  - deck
  - upload
  - capture-url
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.671Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Task-and-Upload-Attachment-in-Nextcloud-Deck

## Summary

This procedure sets up a task in the Nextcloud Deck app and uploads an attachment to capture the vulnerable URL format, enabling subsequent IDOR exploitation.

## Description

In the context of testing Nextcloud Deck, log in as a legitimate user, create a task to generate a card ID, and upload a file attachment. The attachment is assigned a sequential numeric ID, and the resulting URL lacks access controls, making it exploitable by others. This step is prerequisite for demonstrating unauthorized access and requires only basic authenticated access to the Deck app.

## Requirements

1. Valid Nextcloud user credentials (User A).
2. Access to a Nextcloud instance with Deck app installed (e.g., via web browser).
3. Browser with developer tools enabled for network inspection.

## Defense

Defensive measures and detection strategies:

- Implement proper access controls on attachment endpoints, verifying user ownership via session or token.
- Use non-sequential, high-entropy IDs for attachments (e.g., UUIDs).
- Monitor for anomalous attachment access patterns from unrelated user sessions.

## Objectives

1. Generate a task (card) with a known ID.
2. Upload and attach a file to expose the IDOR-vulnerable URL.
3. Capture the URL for use in unauthorized access tests.

## Instructions

### Step 1: Login and Navigate to Deck

**Context**: Authenticate and access the Deck app to create a new task.

Log in to Nextcloud at the target URL (e.g., https://us.cloudamo.com) using User A's credentials. Navigate to /apps/deck and select or create a board, then add a new task.

**Expected Output**: Task created with a unique card ID visible in the UI or URL (e.g., /apps/deck/boards/1/cards/8420).

### Step 2: Upload Attachment and Capture URL

**Context**: Attach a file to the task and intercept the request to obtain the attachment ID.

In the task details, click to add an attachment and upload a test file (e.g., a PDF). Open browser developer tools (F12), go to the Network tab, and filter for the upload request. The response or subsequent GET will show the URL format /apps/deck/cards/{card_id}/attachment/{attachment_id}, where {attachment_id} is sequential (e.g., 30).

**Expected Output**: File attached successfully; URL captured, e.g., https://us.cloudamo.com/apps/deck/cards/8420/attachment/30.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- deck
- upload
