---
tags:
  - xss
  - stored-xss
  - web-portal
  - execution
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 40d22c85-cc6b-4a73-bb1d-d044b9ee851e
created_at: '2025-12-14T03:15:26.750Z'
updated_at: '2025-12-14T03:15:26.750Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-Veris-Web-Portal

## Summary

This procedure exploits stored XSS by accessing the Veris web portal's visitor log, where previously injected payloads from the Android app execute arbitrary JavaScript in the viewer's browser context.

## Description

After payloads are stored via the app, logging into the web portal at https://sandbox.veris.in and viewing the visitor log causes the unsanitized inputs to render without escaping, triggering JavaScript like alert() functions. This can lead to session hijacking, cookie theft, or further attacks on authenticated users. The attack relies on the portal's failure to sanitize stored data during display. Prerequisites: Valid portal credentials and the injected visitor entry existing in the log.

## Requirements

1. Web browser (e.g., Chrome) with JavaScript enabled
2. Valid login credentials for https://sandbox.veris.in
3. Network access to the portal; prior app injection completed

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity encoding) when rendering user inputs in the visitor log
- Implement strict CSP headers to prevent script execution
- Log and alert on JavaScript errors or unexpected DOM changes in the portal
- Regularly scan for XSS payloads in database-stored visitor data

## Objectives

1. Authenticate and access the vulnerable visitor log page
2. Trigger JavaScript execution upon payload reflection
3. Demonstrate impact like alert popups or potential data exfiltration

## Instructions

### Step 1: Access and Login to Portal

**Context**: Gain authenticated access to view protected resources like the visitor log.

Navigate to https://sandbox.veris.in and enter credentials.

> Dashboard loads post-login; no errors indicate success.

### Step 2: Navigate to Visitor Log

**Context**: Reach the page that reflects stored visitor data without sanitization.

Click Visitor Log or directly visit https://sandbox.veris.in/portal/visitor-log/.

> Log table displays entries, including the injected one.

### Step 3: View and Trigger Payloads

**Context**: Render the log to execute the stored JavaScript in the current session.

Scroll or interact with the log entry containing payloads.

> Alerts (e.g., alert(3), alert(4)) appear; inspect element shows unescaped HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[xss]]
- [[stored-xss]]
- [[web-portal]]
