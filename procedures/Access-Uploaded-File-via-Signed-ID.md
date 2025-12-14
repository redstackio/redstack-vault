---
id: proc-uuid-5
tags:
  - file-access
  - signed-id
  - verification
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T05:32:13.702Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Uploaded-File-via-Signed-ID

## Summary

This procedure constructs and accesses the uploaded file URL using the signed ID from the upload response, verifying successful exploitation and persistent access.

## Description

In Rails Active Storage, blobs are accessible via redirect endpoints with signed IDs, which remain valid even for closed accounts if not revoked. This confirms the upload and highlights exfiltration or abuse risks.

## Requirements

1. Signed_id and filename from POST response
2. Direct access to the app URL

## Defense

Defensive measures and detection strategies:

- Expire signed IDs on account closure
- Log accesses to blob redirects and tie to user status
- Implement signed ID validation against active accounts

## Objectives

1. Retrieve and serve the uploaded file
2. Validate the full bypass chain
3. Demonstrate impact of unauthorized storage

## Instructions

### Step 1: Construct Access URL

**Context**: Build the redirect endpoint.

Use signed_id: https://app.hey.com/rails/active_storage/blobs/redirect/<signed_id>/<filename>.

### Step 2: Access the File

**Context**: Verify serving without auth.

Navigate to the URL in a browser or use curl to fetch.

**Expected Output**: File content served directly.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-access
- signed-id
- verification
