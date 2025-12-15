---
id: proc-uuid-003
tags:
  - shopify
  - image-upload
  - s3
type: procedure
tools:
  - '[[tools/Shopify-Ping-iOS-App]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Mobile (iOS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:25:18.270Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Send-Image-via-Staff-Account-in-Shopify-Ping

## Summary

This procedure uses the staff account in the Shopify Ping app to upload an image during a chat, triggering storage in the vulnerable S3 bucket.

## Description

From the staff perspective, sending an image via the app stores it publicly in the S3 bucket due to misconfiguration. This step assumes an active chat session and uses the app's native upload function. Details like exact image paths are redacted, but the process exposes the backend storage URL. Outcome: Image is sent and accessible via URL.

## Requirements

1. Active chat session from customer side
2. Staff login in Shopify Ping app
3. Test image file on device

## Defense

Defensive measures and detection strategies:

- Scan uploads for malicious content
- Log all image uploads and review for patterns
- Restrict upload sizes and types

## Objectives

1. Upload image to trigger S3 storage
2. Ensure image appears in customer chat
3. Expose backend URL indirectly

## Instructions

### Step 1: Switch to Staff App

**Context**: Access staff controls.

Open [[tools/Shopify-Ping-iOS-App]] and ensure logged in as staff.

> Expected: Dashboard shows active chats.

### Step 2: Send Image in Chat

**Context**: Use upload feature.

Select the ongoing chat and tap the image send button to upload a file (e.g., a test photo).

> Expected: Image sends successfully, visible in chat.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Shopify-Ping-iOS-App]]

## Tags

- image-upload
- staff-access
