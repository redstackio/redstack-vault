---
tags:
  - xss
  - payload-injection
  - observation
type: procedure
tools:
  - '[[tools/H1-Triage-Wizard-Chrome-Extension]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Chrome Browser Extension
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.483Z'
sub_techniques: []
id: 8fdd7146-a9bd-4d80-a1bf-83f016f56a0f
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-HTML-Payload-Injection

## Summary

This procedure verifies the injection of an HTML payload into the triage modal, confirming stored XSS execution due to lack of sanitization in the extension's .replace() method.

## Description

With a payload like <script>alert('XSS')</script> stored in questionnaireResponses[1] or similar, the buildTriageQuestionnaireModal function injects it unsanitized, rendering and executing the HTML/JS in the modal's browser context, potentially compromising viewer sessions on HackerOne.

## Requirements

1. Open triage modal with pre-set malicious responses
2. Browser developer tools for inspection
3. Payload prepared in extension storage

## Defense

Defensive measures and detection strategies:

- Audit extension code for .replace() usage on user inputs
- Implement output encoding (e.g., escape HTML entities)
- Detect XSS via browser security features like XSS Auditor

## Objectives

1. Confirm payload rendering without escaping
2. Execute JS to demonstrate impact
3. Highlight integrity risks for confidential report data

## Instructions

### Step 1: Prepare Payload in Responses

**Context**: Ensure questionnaireResponses contain the HTML payload prior to modal load.

Use extension storage or prior setup to inject payload into responses array (e.g., via dev tools or simulated user input).

> Payload example: questionnaireResponses[1] = '<img src=x onerror=alert("XSS")>'

### Step 2: Inspect and Observe Execution

**Context**: Monitor the modal for injection and execution.

Reload the modal if needed and watch for alert or console output; inspect the DOM for raw HTML insertion.

> Success: Script executes, showing alert; DOM shows unescaped HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/H1-Triage-Wizard-Chrome-Extension]]

## Tags

- payload-observation
- xss-execution
