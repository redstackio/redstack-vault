---
tags:
  - xss
  - stored-xss
  - injection
  - udemy
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 2813024f-4a7a-412f-9a12-eb5784fd9df1
created_at: '2025-12-14T03:15:10.464Z'
updated_at: '2025-12-14T03:15:10.464Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Link-for-Stored-XSS-in-Udemy-Discussions

## Summary

This procedure exploits insufficient input sanitization in Udemy's discussion link insertion feature to inject a stored XSS payload, allowing JavaScript execution when the link is clicked by the user.

## Description

In Udemy's course discussion editor, the 'Insert Link' functionality fails to properly sanitize URL inputs, enabling attackers to break out of the href attribute using a closing quote and inject HTML elements with JavaScript handlers like onerror. The payload executes in the browser context upon clicking the link, prompting the document domain. While stored in the discussion, it only affects the injecting user due to non-persistence for others, resulting in low impact rated as 'Informative'.

## Requirements

1. Valid Udemy account with enrollment in a course.
2. Access to the course discussion section.
3. Web browser such as Google Chrome for testing.

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to whitelist safe protocols (http, https) and escape HTML attributes.
- Use Content Security Policy (CSP) to restrict inline JavaScript execution.
- Sanitize all user inputs in rich text editors with libraries like DOMPurify.
- Monitor for anomalous JavaScript prompts or console errors in discussion interactions.

## Objectives

1. Inject and store a malicious link payload in a course discussion.
2. Trigger JavaScript execution to demonstrate domain access.
3. Validate the vulnerability's self-contained impact.

## Instructions

### Step 1: Open Link Insertion Dialog

**Context**: Access the vulnerable input field in the discussion editor.

**Instructions**: In the Udemy course discussion editor, click the Link icon and select 'Insert Link' to open the dialog.

### Step 2: Inject XSS Payload

**Context**: Enter the payload to breakout and execute JavaScript via an image onerror handler.

**Instructions**: In the URL field, input: `"><img src=x onerror=prompt(document.domain);>`. This closes the href attribute, injects an img tag, and sets an onerror event to prompt the domain.

### Step 3: Set Link Text and Insert

**Context**: Complete the link creation to embed the payload.

**Instructions**: Enter display text like 'Test Link' in the text field, then click 'Insert' to add it to the discussion.

### Step 4: Trigger and Verify Execution

**Context**: Interact with the link to execute the payload and confirm XSS.

**Instructions**: Click the inserted link in the discussion preview. Observe the prompt dialog displaying the document domain (e.g., 'udemy.com').

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- [[xss]]
- [[stored-xss]]
- [[web-injection]]
