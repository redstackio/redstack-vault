---
tags:
  - xss
  - execution
  - self-xss
  - ok.ru
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
updated_at: '2025-12-14T03:16:14.516Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
id: 5f3e1c90-00ca-4051-9ed8-6f9f05297522
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-and-Execute-Self-XSS-via-Add-Poll

## Summary

This procedure triggers the stored XSS by clicking the 'add poll' button in the ok.ru post form, causing the injected payload to execute in the attacker's browser.

## Description

The add poll function processes the topic field without proper sanitization, storing the HTML/JS payload and rendering it, which executes the onload event. This results in self-XSS, prompting the document domain. It requires the prior payload injection and is limited to the attacker's session. Outcomes include visible JavaScript execution confirming the vulnerability.

## Requirements

1. Payload already injected in topic field
2. Open post form with add poll option
3. Browser allowing script execution

## Defense

Defensive measures and detection strategies:

- Sanitize outputs during rendering (e.g., strip script tags)
- Implement strict CSP headers
- Log and alert on script execution attempts

## Objectives

1. Process the post to store and render the payload
2. Achieve JavaScript execution in the browser
3. Verify self-XSS impact

## Instructions

### Step 1: Locate Add Poll Button

**Context**: Identify the trigger mechanism in the post form.

In the new post interface, find and hover over the 'Add Poll' or equivalent button.

> Button is clickable and form is complete.

### Step 2: Click Add Poll

**Context**: Submit the post via poll addition to invoke processing.

Click the 'Add Poll' button to handle the topic field content.

> The form submits, and the page updates with the post.

### Step 3: Observe Execution

**Context**: Monitor for the payload's effect post-submission.

Watch for a browser prompt displaying 'ok.ru' or the document domain.

> JavaScript executes, confirming XSS.

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
- [[Execution]]
- [[self-xss]]
- [[ok.ru]]
