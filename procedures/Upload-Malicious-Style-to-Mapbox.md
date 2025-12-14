---
id: proc-uuid-3
tags:
  - upload
  - mapbox-api
  - persistence
type: procedure
tools:
  - '[[tools/Mapbox-Studio-Classic]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:16:30.263Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
---

# Upload-Malicious-Style-to-Mapbox

## Summary

This procedure saves and uploads the XSS-infused map style to the attacker's Mapbox account, making the payload persistent and accessible via API for project creation.

## Description

Using Mapbox Studio Classic's upload feature, the modified style (including the malicious attribution) is pushed to Mapbox.com's servers. This exploits the platform's trust in user styles. The target is the Mapbox upload endpoint, resulting in a hosted style ID usable in projects. Requires authenticated session in the tool.

## Requirements

1. Logged-in Mapbox account in Studio Classic
2. Internet connectivity for upload
3. Modified style ready in editor

## Defense

Defensive measures and detection strategies:

- Scan uploaded styles for malicious JS in attribution (e.g., regex for script tags/onerror)
- Rate-limit style uploads per account
- Audit logs for anomalous style metadata

## Objectives

1. Persist the malicious style online
2. Obtain style ID for project integration
3. Verify upload without rejection

## Instructions

### Step 1: Save Changes

**Context**: Commit local edits before upload.

In Mapbox Studio Classic, click 'Save' in the editor menu to store the style locally.

> Expected output: 'Saved' confirmation dialog.

### Step 2: Upload to Account

**Context**: Transmit the style to Mapbox servers.

Select 'Upload' from the file menu, authenticate if prompted, and confirm the upload to your account.

> Expected output: Progress bar completes; success message with style URL or ID.

### Step 3: Close Application

**Context**: Clean up after upload.

Exit Mapbox Studio Classic to end the session.

> Expected output: Application closes without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mapbox-Studio-Classic]]

## Tags

- [[upload]]
- [[Persistence]]

