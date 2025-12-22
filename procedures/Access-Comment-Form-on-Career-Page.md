---
tags:
  - web-interaction
  - form-access
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
updated_at: '2025-12-13T23:52:33.760Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 90ec23ca-4a21-4326-b94f-6e2bf7fc00e0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Comment-Form-on-Career-Page

## Summary

This procedure describes interacting with the 'Leave a Comment' button on Starbucks career landing pages to open the user submission form, enabling subsequent payload injection.

## Description

Once vulnerable pages are identified, the next step is to engage with the comment functionality. The form typically includes fields for Name, Email, and Comment, submitted without authentication. This interaction exploits the public-facing nature of the page, preparing for XSS payload delivery. No tools are needed; it's pure manual browser use.

## Requirements

1. Access to a vulnerable page (e.g., career-landing-1)
2. Standard web browser
3. No prior credentials

## Defense

Defensive measures and detection strategies:

- Rate-limit form accesses to prevent abuse
- Log all form interactions for anomaly detection
- Disable comments on sensitive pages like career sections

## Objectives

1. Reveal the comment submission interface
2. Confirm form fields are present and editable
3. Transition to payload crafting

## Instructions

### Step 1: Locate Comment Section

**Context**: Identify the interactive element on the page.

Scroll to the bottom of the career landing page and find the 'Leave a Comment' button.

> The button should be visible below existing comments.

### Step 2: Activate the Form

**Context**: Open the input fields for submission.

Click the 'Leave a Comment' button.

> This expands the form with Name, Email, and Comment textarea fields.

### Step 3: Verify Accessibility

**Context**: Ensure no barriers to input.

Check that all fields are focusable and accept text.

> Form is ready if no JavaScript errors or disabled states appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-interaction]]
- [[form-access]]
