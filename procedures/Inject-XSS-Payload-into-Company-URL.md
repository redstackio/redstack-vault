---
tags:
  - xss
  - stored-xss
  - concrete-cms
  - web
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
updated_at: '2025-12-14T03:15:35.415Z'
sub_techniques: []
id: 3d3008c0-8614-49cd-a65c-0d7caa8fb220
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Company-URL

## Summary

This procedure details the injection of a JavaScript payload into the Company URL field of Concrete CMS testimonials, exploiting lack of sanitization to store malicious code for later execution.

## Description

The Company URL field in Concrete CMS accepts arbitrary input without HTML escaping or JavaScript filtering. By injecting a payload like `'><img src=x onerror=alert(1)>`, attackers close the URL attribute and embed executable script. This stored XSS persists in the database and activates on page render, affecting all viewers. Prerequisites include access to the form from the previous procedure.

## Requirements

1. Access to the testimonials add/edit form
2. Knowledge of basic HTML/JS payloads
3. Web browser for manual input

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding on output
- Use Content Security Policy (CSP) to restrict inline scripts
- Log and monitor form submissions for anomalous strings like '<script>' or 'onerror'

## Objectives

1. Bypass input validation to store the payload
2. Ensure the payload is accepted and saved
3. Set up for execution in the viewing context

## Instructions

### Step 1: Locate Company URL Field

**Context**: Focus on the vulnerable input to prepare injection.

No specific command; select the URL input in the form.

> Verify it's a text field without restrictions.

### Step 2: Enter Payload

**Context**: Inject the XSS string to break out of the attribute context.

Manually type: `'><img src=x onerror=alert(1)>`

> This payload uses an invalid image source to trigger the onerror handler, executing alert(1). Submit the form to test acceptance.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
