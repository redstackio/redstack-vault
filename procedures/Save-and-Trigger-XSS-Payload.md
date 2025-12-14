---
id: proc-save-and-trigger-xss-payload
tags:
  - xss
  - execution
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.434Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-and-Trigger-XSS-Payload

## Summary

This procedure covers saving the injected payload in Concrete CMS and triggering its execution by viewing the affected testimonial, confirming the Stored XSS vulnerability.

## Description

After injection, submitting the form stores the payload in the CMS database. When the testimonial is rendered on a public page, the lack of output encoding causes the JavaScript to execute in the viewer's context. This can affect any user, including admins, leading to risks like cookie theft. Assumes prior injection; outcomes include visible script execution.

## Requirements

1. Injected payload from previous procedure.
2. Ability to submit forms and view public pages.
3. Victim browser context (can be self for PoC).

## Defense

Defensive measures and detection strategies:

- Apply output escaping (e.g., htmlspecialchars) when rendering user content.
- Log and alert on anomalous JavaScript execution via browser dev tools or WAF.

## Objectives

1. Persist the malicious payload in the CMS storage.
2. Trigger execution in a viewing browser.
3. Validate impact through observable effects like alerts.

## Instructions

### Step 1: Submit the Form

**Context**: Store the payload permanently in the database.

Click 'Save' or 'Submit' on the testimonial editing form.

**Expected Output**: Confirmation message; no validation errors on payload.

### Step 2: View the Testimonial Page

**Context**: Render the content to execute the stored script.

Navigate to a page displaying the testimonial (e.g., homepage or dedicated section).

**Expected Output**: Alert(1) pops up, or console logs script execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
