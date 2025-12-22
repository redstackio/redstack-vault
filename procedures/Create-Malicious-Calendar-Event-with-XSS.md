---
tags:
  - xss
  - injection
  - concrete-cms
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: aad5740d-069c-4ad0-8b99-07eb740edaf6
created_at: '2025-12-14T03:16:20.410Z'
updated_at: '2025-12-14T03:16:20.410Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Calendar-Event-with-XSS

## Summary

This procedure involves creating a calendar and injecting a stored XSS payload into the event name field in Concrete CMS, triggering immediate execution in the creator's browser.

## Description

As an authenticated user with calendar permissions, navigate to the Dashboard > Calendar & Events section. Create a new calendar, add an event, and insert a JavaScript payload like '"<img src=K onerror=prompt(document.domain)>' into the Name field. The lack of input sanitization allows the payload to be stored and executed when the event is saved, due to improper output escaping in the dashboard rendering.

## Requirements

1. Authenticated session as a user with event creation permissions
2. Access to Dashboard > Calendar & Events
3. Knowledge of XSS payloads targeting HTML attributes like onerror

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in event fields using HTML entity encoding
- Implement Content Security Policy (CSP) to restrict inline scripts
- Audit event creations for suspicious payloads via WAF or logging

## Objectives

1. Store malicious JavaScript in the event name
2. Achieve initial payload execution in the attacker's session
3. Prepare the event for cross-user triggering

## Instructions

### Step 1: Navigate to Calendar Management

**Context**: Access the interface for creating calendars and events.

In the user2 session, go to Dashboard > Calendar & Events.

**Expected Output**: Calendar management page loaded.

### Step 2: Add New Calendar

**Context**: Create a container for the malicious event.

Click 'Add Calendar' and name it 'User2 Calendar', then save.

**Expected Output**: New calendar created.

### Step 3: Add Event with Payload

**Context**: Inject the XSS payload in the name field.

Click 'Add Event', fill in date/time details, and in the Name field enter: ' "><img src=K onerror=prompt(document.domain)>'.

**Expected Output**: Payload stored upon save.

### Step 4: Save and Observe Trigger

**Context**: Submit the form to store and execute the payload.

Click 'Save & Close'.

**Expected Output**: Prompt box appears showing the domain, confirming XSS execution.

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

- [[xss]]
- [[stored-xss]]
