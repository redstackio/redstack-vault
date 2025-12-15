---
id: proc-003
tags:
  - form-submission
  - self-xss-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:15.886Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit Form to Trigger Self-XSS

## Summary

This procedure completes and submits the form to reflect the injected XSS payload, triggering self-XSS execution in the attacker's own browser and confirming the vulnerability.

## Description

After injecting the payload, the form is filled with valid data for other fields and submitted via POST to https://██████████/. The lack of sanitization causes the payload to execute on the response page, demonstrating self-XSS. This step validates the issue before chaining with CSRF.

## Requirements

1. Payload already injected in 'first_name' field
2. Knowledge of required form fields
3. Active authenticated session

## Defense

Defensive measures and detection strategies:

- Validate all form fields server-side before processing
- Use anti-automation measures like CAPTCHA on submissions
- Monitor for anomalous POST requests to form endpoints

## Objectives

1. Successfully submit the tampered form
2. Trigger payload reflection and execution
3. Capture evidence of self-XSS

## Instructions

### Step 1: Fill Other Fields

**Context**: Provide benign data to ensure submission succeeds.

Enter placeholder values in fields like middle_name ('test'), last_name ('test'), and any others required.

> Avoid payloads in non-vulnerable fields to isolate the issue.

### Step 2: Submit the Form

**Context**: Initiate the POST request to reflect the input.

Click the submit button to send the form data to https://██████████/.

> Watch the network tab in developer tools for the POST request containing the payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[form-submission]]
- [[self-xss-trigger]]
