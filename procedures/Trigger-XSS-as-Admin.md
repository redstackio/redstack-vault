---
tags:
  - xss
  - stored-xss
  - admin-exploitation
  - concrete-cms
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.382Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e92ec80c-e2bc-48d4-8215-8db7bc1fcf8e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-as-Admin

## Summary

This procedure demonstrates triggering the stored XSS payload in an administrator's browser context by viewing the malicious calendar, leading to arbitrary JavaScript execution with elevated privileges.

## Description

After injection, switching to the admin session and selecting the tainted calendar causes the unsanitized name to render, executing the JS payload. This affects any user viewing the calendar, including admins, allowing actions like browser history access or phishing. The attack relies on the lack of output encoding in Concrete CMS 8.3.1's calendar rendering. Expected outcomes include JS alerts or more advanced exploits, though HttpOnly flags protect sessions.

## Requirements

1. Admin session active in a separate browser window
2. Malicious calendar already created via prior injection
3. Access to Dashboard > Calendar & Events

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., htmlspecialchars) when rendering user inputs in views
- Implement role-based access controls to limit calendar visibility
- Deploy runtime application self-protection (RASP) to detect and block JS injection attempts

## Objectives

1. View the malicious calendar in admin context
2. Execute the stored payload for JS control
3. Validate cross-context impact

## Instructions

### Step 1: Switch to Admin Session

**Context**: Return to the primary admin browser to avoid session pollution.

Close or switch from the test user incognito window to the original admin session.

**Expected Output**: Admin dashboard accessible.

### Step 2: Navigate to Calendars

**Context**: Access the list of calendars to locate the malicious one.

Go to Dashboard > Calendar & Events.

**Expected Output**: List of calendars displayed, including the injected one (e.g., 'Hi, Admin').

### Step 3: Select and Trigger

**Context**: Interact with the calendar to render the vulnerable name field.

Click on or select the malicious calendar to view it.

**Expected Output**: Payload executes, showing a prompt with the admin page's document location.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- xss
- admin-exploitation
- concrete-cms
