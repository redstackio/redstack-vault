---
id: proc-rocket-chat-xss-trigger-2
name: Trigger-XSS-via-Admin-Email-View-in-Android-Client
tags:
  - xss
  - email
  - android
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.141Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Admin-Email-View-in-Android-Client

## Summary

This procedure relies on the admin receiving and viewing the approval email in the Rocket.Chat Android client, where the stored payload reflects in the HTML body and executes via WebView rendering.

## Description

The email template includes the reason field unsanitized, e.g., `<p>Reason: <b>[payload]</b></p>`. When opened in the Android app's WebView (using email:// protocol), the img src="x" fails, triggering onerror to eval the base64 JS, injecting external scripts.

## Requirements

1. Admin email approval enabled in Rocket.Chat settings
2. Admin using vulnerable Android client version
3. Payload already injected from prior step

## Defense

Defensive measures and detection strategies:

- Sanitize email body with HTML purifiers (e.g., DOMPurify)
- Disable JS in email WebViews or use safe browsing modes
- Log email opens and monitor for external domain loads

## Objectives

1. Reflect payload in admin email without server-side execution
2. Trigger client-side JS in privileged context
3. Confirm execution via external callback

## Instructions

### Step 1: Await Email Delivery

**Context**: Rocket.Chat generates and sends the approval email to admin upon registration submission.

No action required; the system handles delivery via configured email service.

### Step 2: Monitor for View Trigger

**Context**: Admin opens email in Android client, rendering HTML in WebView.

Watch attacker's callback server for script load from https://2973956338.xss.ht.

**Expected Output**: Onerror fires, appending script tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[android]]
