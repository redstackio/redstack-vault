---
tags:
  - form-completion
  - dummy-input
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:33.738Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 6c4f16dc-639e-436f-af16-4bfae4a6a7a3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Fill-Name-and-Email-Fields-in-Comment-Form

## Summary

This procedure involves populating the required Name and Email fields with innocuous dummy values to satisfy form validation and allow submission of the XSS payload.

## Description

Many comment forms require Name and Email for submission. Using generic values like 'Test' and 'test@live.com' bypasses basic checks without drawing attention. This step is crucial to complete the form before injecting the payload, ensuring the stored XSS is successfully posted.

## Requirements

1. Comment form open with payload already in Comment field
2. No email verification enabled
3. Standard browser input

## Defense

Defensive measures and detection strategies:

- Enforce email format validation and disposable email blacklisting
- Require CAPTCHA for form submissions
- Log suspicious dummy inputs

## Objectives

1. Meet minimum form requirements
2. Avoid triggering validation blocks
3. Enable payload submission

## Instructions

### Step 1: Input Name

**Context**: Fill the identifier field.

Enter 'Test' in the Name input.

> Field accepts alphanumeric text.

### Step 2: Input Email

**Context**: Provide a plausible email address.

Enter 'test@live.com' in the Email field.

> No verification if it accepts without bounce check.

### Step 3: Confirm Form Readiness

**Context**: Ensure all fields are complete.

Review for required field indicators.

> Form submit button should be enabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[form-completion]]
- [[dummy-input]]
