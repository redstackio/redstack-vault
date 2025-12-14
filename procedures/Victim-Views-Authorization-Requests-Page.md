---
tags:
  - xss
  - phishing
  - reflection
type: procedure
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
updated_at: '2025-12-14T03:15:35.738Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: cabcc457-3543-4bd5-a8a2-af33296011b8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Victim-Views-Authorization-Requests-Page

## Summary

This procedure simulates the victim accessing the authorization requests page, where the stored XSS payload in the username begins to be reflected, priming for execution.

## Description

The victim, upon receiving the email notification, visits the requests page at https://mobilevikings.com/account/requests/. The page displays the attacker's unsanitized username, potentially loading it into the DOM without encoding. This step doesn't always trigger execution but sets the context for interactions. Prerequisites: Victim account and email access; outcomes: Page load with reflected data.

## Requirements

1. Victim account credentials
2. Email notification from attacker request
3. Browser access to the site

## Defense

Defensive measures and detection strategies:

- Encode all user-generated content on output (e.g., htmlspecialchars in PHP)
- Implement client-side validation for reflected fields
- Monitor page load logs for anomalous JavaScript errors

## Objectives

1. Load the requests page
2. Reflect the malicious username
3. Prepare for interaction-based triggers

## Instructions

### Step 1: Access Notification Link

**Context**: Follow the lure to the vulnerable page.

Click the email link or manually navigate to https://mobilevikings.com/account/requests/ after logging in.

### Step 2: View Pending Requests

**Context**: Display the list including attacker's request.

The page renders the requests table, showing the attacker's username.

> Inspect the page source to see the raw username with script tag.

### Step 3: Observe Reflection

**Context**: Confirm unsanitized display.

No immediate execution; username appears in UI elements.

**Expected Output**: Requests list with visible payload in source.

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
- [[reflection]]
- [[web]]
