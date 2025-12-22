---
id: proc-inject-xss-zip-learnboost
tags:
  - xss
  - injection
  - stored-xss
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
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
updated_at: '2025-12-14T03:47:18.365Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Malicious Payload into ZIP Code Field

## Summary

This procedure demonstrates injecting a JavaScript payload into the ZIP code field of the LearnBoost network panel, exploiting lack of input sanitization to store malicious code that can later be triggered.

## Description

In the LearnBoost web application, the network panel allows users to add schools with associated ZIP codes. ZIP codes are not properly sanitized or escaped when stored, enabling stored XSS. By associating the payload with a school name using a common search prefix like 'fro', attackers can target users likely to search for it. This leads to execution in the browser context, allowing data theft or session hijacking.

## Requirements

1. Valid LearnBoost user account with access to the network panel
2. Web browser like Mozilla Firefox for testing
3. Knowledge of basic JavaScript payloads for XSS

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization for all user inputs, especially ZIP codes
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript alerts or network requests from search endpoints

## Objectives

1. Store malicious JavaScript in the database via ZIP code field
2. Associate payload with searchable school names for broad impact
3. Set up for execution on victim searches

## Instructions

### Step 1: Access Network Panel

**Context**: Log in to LearnBoost and navigate to the settings where school entries can be added.

No command required; use the web interface in [[tools/Mozilla-Firefox]] to go to the Network panel.

> Enter a school name like 'Frogs Academy' to associate with the payload.

### Step 2: Inject Payload

**Context**: Input the malicious payload into the ZIP code field to bypass storage validation.

Use the following payload in the ZIP code input:

```html
1"><img src=x onerror=alert(document.domain)>
```

> Submit the form. The payload closes the input tag and injects an img element that triggers on error, alerting the domain to confirm storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]

## Tags

- xss
- injection
