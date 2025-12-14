---
tags:
  - xss-execution
  - payload-verification
  - stored-xss
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
updated_at: '2025-12-13T23:52:33.735Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 72307e4b-23c2-436d-9c5d-619f2e016d13
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Comment-and-Verify-Stored-XSS-Execution

## Summary

This procedure covers submitting the form to store the XSS payload server-side and reloading the page to confirm execution, demonstrating the vulnerability's impact on subsequent visitors.

## Description

Upon submission, the unsanitized comment is stored in the backend and rendered raw on page load. Refreshing simulates a new user, triggering the JavaScript redirect. This confirms the stored nature of the XSS, with potential for real-world abuse like phishing job seekers or stealing cookies via modified payloads.

## Requirements

1. Fully populated comment form with payload
2. Server-side storage without immediate rejection
3. Ability to reload the page

## Defense

Defensive measures and detection strategies:

- Scan stored comments for script tags or suspicious patterns
- Encode outputs using libraries like DOMPurify
- Monitor for unexpected redirects on page loads

## Objectives

1. Persist the malicious payload
2. Trigger and observe code execution
3. Validate impact for reporting

## Instructions

### Step 1: Submit the Form

**Context**: Post the data to the server.

Click the submit button on the comment form.

> Submission should succeed without errors; comment may appear immediately or after refresh.

### Step 2: Reload the Page

**Context**: Simulate visitor load to execute stored content.

Press F5 or click refresh in the browser.

> Page reloads, rendering the stored comment.

### Step 3: Verify Execution

**Context**: Check for payload effects.

Observe the fixed div at the bottom, hidden paragraphs, and automatic redirect to https://hackerone.com.

> Success if JS runs and alters page behavior.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[payload-verification]]
- [[stored-xss]]
