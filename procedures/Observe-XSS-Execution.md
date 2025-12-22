---
id: proc-uuid-003
name: Observe-XSS-Execution
tags:
  - xss
  - execution
  - observation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:03.336Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-XSS-Execution

## Summary

This procedure monitors the Zomato contact form page after CSRF injection to confirm XSS payload execution and data exfiltration.

## Description

Following CSRF submission, the form reflects the injected scripts, executing JavaScript in the victim's browser context. This can alert cookies or perform further actions like session theft.

## Requirements

1. Victim's browser open to the contact form post-submission
2. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Output encode all user inputs on reflection
- Deploy XSS auditors or WAF rules for script detection
- Log and alert on JavaScript errors or unusual alerts

## Objectives

1. Verify script execution
2. Capture sensitive data like cookies
3. Assess potential for escalation

## Instructions

### Step 1: Load Contact Form Post-Submission

**Context**: Navigate to or refresh https://www.zomato.com/contact after CSRF trigger.

Observe for immediate alert popups.

> Expected: Alert with '1' from name payload, then document.cookie from email.

### Step 2: Validate Impact

**Context**: Check browser console for errors or executed code.

Screenshot the alert as evidence (e.g., CSRF_XSS.jpg).

> Success: Cookies displayed, confirming theft potential.

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
- [[Collection]]
