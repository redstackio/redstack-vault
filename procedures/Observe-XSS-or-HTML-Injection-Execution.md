---
tags:
  - payload-execution
  - verification
  - impact-assessment
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:32.010Z'
sub_techniques: []
id: fdffdf09-7b9e-415b-a6e8-eea65b08ddd1
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-XSS-or-HTML-Injection-Execution

## Summary

This procedure verifies the success of the stored XSS or HTML injection by viewing the site information page, triggering payload execution to demonstrate impact like alerts or rendered elements.

## Description

After injection, this step involves accessing the reflected context on try.pressable.com where the Display Name is output without escaping. This confirms the vulnerability, showing JavaScript alerts with cookies or HTML forms for phishing. The scenario assumes a created site; outcomes validate exploitation for further attacks like diversion to malicious sites.

## Requirements

1. Successfully created site from previous injection
2. Access to the site's dashboard or info page
3. Browser capable of executing JavaScript

## Defense

Defensive measures and detection strategies:

- Output encode all dynamic content with context-aware escaping (e.g., HTML entities)
- Implement client-side monitoring for unexpected script execution
- Alert on anomalous page renders or cookie access attempts

## Objectives

1. Trigger and observe payload execution
2. Confirm credential exposure or UI manipulation
3. Assess potential for broader impact

## Instructions

### Step 1: Navigate to Site Information

**Context**: Load the page displaying the injected Display Name to trigger reflection.

No command required; browser navigation.

After creation, go to the site's overview or dashboard page (e.g., via the Pressable dashboard link) and locate where the Display Name is shown.

> This reflects the stored payload. Expected output: Page loads with injected content visible.

### Step 2: Trigger and Verify Execution

**Context**: Interact or refresh to execute scripts or render HTML.

No command required; UI interaction.

Refresh the page or click elements involving the Display Name. For XSS, an alert should pop with document.cookie; for HTML, the form should appear and be submittable.

> Validates vulnerability. Expected output: Alert box with cookies or interactive HTML form.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[verification]]
