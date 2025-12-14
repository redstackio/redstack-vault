---
tags:
  - xss
  - stored-xss
  - payload-injection
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
updated_at: '2025-12-14T03:16:20.387Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9cb3f18e-5f73-4835-99ba-27d211976737
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-in-Calendar-Name

## Summary

This procedure exploits insufficient input sanitization in the Concrete CMS 8.3.1 Calendar Name field to inject and store a malicious JavaScript payload, which executes upon form submission and calendar viewing.

## Description

The vulnerability allows HTML and JavaScript injection in the Dashboard > Calendar & Events > Add Calendar feature. By entering a payload like `<img src=K onerror=prompt(document.location)>`, the script is stored in the database without escaping and rendered unsafely when the calendar is displayed. This leads to arbitrary JS execution in the viewer's browser context, potentially enabling keylogging, DOM manipulation, or phishing. Session cookies are protected by HttpOnly, limiting direct hijacking, but other impacts remain severe. Prerequisites include admin access to the calendar section.

## Requirements

1. Logged-in session with admin privileges in Concrete CMS 8.3.1
2. Access to Dashboard > Calendar & Events
3. Web browser for payload testing

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML escaping for all user-controlled fields like calendar names
- Use Content Security Policy (CSP) to restrict inline script execution
- Regularly scan for XSS with tools like OWASP ZAP and monitor for suspicious prompts or JS errors in logs

## Objectives

1. Store malicious payload in the calendar name
2. Trigger immediate execution in the injecting user's context
3. Prepare for cross-context execution upon admin viewing

## Instructions

### Step 1: Navigate to Add Calendar

**Context**: Access the calendar creation form to reach the vulnerable input field.

In the test user session, go to Dashboard > Calendar & Events and click Add Calendar.

**Expected Output**: Form loads with Calendar Name input field visible.

### Step 2: Enter Payload

**Context**: Inject the XSS payload into the name field to bypass sanitization.

Enter 'Hi, Admin<img src=K onerror=prompt(document.location) width=1px height=1px>' in the Calendar Name field. Set width and height to 1px to hide the image.

**Expected Output**: Payload accepted without validation errors.

### Step 3: Submit and Observe

**Context**: Store the payload and verify initial execution.

Click the Add Calendar button to submit.

**Expected Output**: Calendar added, payload executes showing a prompt with the current document location.

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
- stored-xss
- concrete-cms
