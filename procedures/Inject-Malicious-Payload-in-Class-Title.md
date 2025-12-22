---
id: proc-khan-xss-injection-001
tags:
  - xss
  - reflected-xss
  - web
  - self-xss
  - khan-academy
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
updated_at: '2025-12-14T03:15:41.557Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-in-Class-Title

## Summary

This procedure exploits a reflected XSS vulnerability in the Khan Academy class creation form by injecting a malicious JavaScript payload into the class title field, resulting in arbitrary code execution within the authenticated user's browser context during the form submission response. It is a self-XSS, affecting only the user performing the action on the initial page load.

## Description

The Khan Academy web application at '/coach/roster/' fails to properly sanitize user input in the class title field when creating the first class. By injecting a payload like '><img src=x onerror=prompt(0);>', attackers can break out of the HTML attribute context and execute JavaScript upon form submission. This is discovered through manual testing of input fields in the coach dashboard. The vulnerability allows execution of arbitrary JS but is non-persistent and does not impact other users, limiting it to self-XSS scenarios. Prerequisites include an authenticated coach account and access to the class creation feature.

## Requirements

1. Authenticated Khan Academy account with coach/teacher privileges
2. Web browser capable of executing JavaScript (e.g., Chrome)
3. Direct access to khanacademy.org without network restrictions

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all user inputs, using libraries like DOMPurify
- Employ Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript prompts or errors in application logs during form submissions

## Objectives

1. Inject and reflect a JavaScript payload to execute code in the user's session
2. Demonstrate vulnerability without affecting other users or persisting the exploit
3. Validate self-XSS impact on the initial class creation page load

## Instructions

### Step 1: Access Coach Dashboard and Manage Students

**Context**: Log in and navigate to the vulnerable form to prepare for payload injection.

No specific command; use the web interface to log in at khanacademy.org, go to 'Coach', and select 'Manage students'.

> Expected: Student management page loads, showing option to create a class.

### Step 2: Open Class Creation Form

**Context**: Initiate the first class creation to expose the title input field.

Click 'Create your first class' to reach '/coach/roster/' form.

> Expected: Form with title field appears.

### Step 3: Enter XSS Payload

**Context**: Insert the payload to exploit lack of sanitization.

In the title field, input: `'><img src=x onerror=prompt(0);>'`

> Expected: Payload accepted; no immediate error.

### Step 4: Submit and Verify Execution

**Context**: Trigger reflection and JS execution.

Click 'Create class' to submit.

> Expected: Prompt dialog appears on response page, confirming execution.

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
- [[reflected-xss]]
- [[web]]
- [[self-xss]]
