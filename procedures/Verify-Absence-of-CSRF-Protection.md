---
tags:
  - csrf
  - verification
  - web
type: procedure
tools:
  - '[[tools/Acunetix]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:22.897Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 1a37d367-482a-4773-81c3-01dfc79b49dc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Absence of CSRF Protection

## Summary

This procedure inspects HTTP requests, responses, and form elements to confirm the lack of CSRF protection mechanisms, such as tokens, in a web form.

## Description

For the Automattic contact form, this involves checking for CSRF tokens in the HTML form and server validation in POST responses. Headers like Server: nginx and X-Pingback: http://automattic.com/xmlrpc.php indicate a WordPress setup without CSRF safeguards. Outcomes include confirmation of vulnerability for PoC development. Requires scanner access and basic HTTP knowledge.

## Requirements

1. Access to scanning tool output from form identification
2. Ability to inspect HTTP traffic
3. Target site responsiveness

## Defense

Defensive measures and detection strategies:

- Enforce SameSite cookies for session management
- Log and alert on missing token submissions
- Regular scanning with tools like Acunetix for CSRF gaps

## Objectives

1. Confirm no CSRF tokens in form or headers
2. Identify backend tech stack
3. Validate potential for forged requests

## Instructions

### Step 1: Inspect Form and Headers

**Context**: Analyze the form HTML and response headers for protection indicators.

Use [[tools/Acunetix]] to review the scan results for /contact/.

No command; GUI inspection in Acunetix reports section.

> Look for absence of <input type="hidden" name="csrf_token"> or similar; note headers without validation.

### Step 2: Test Forged Request

**Context**: Send a sample POST without tokens to check server behavior.

Simulate in Acunetix or browser dev tools a POST with form data.

> Expected: Successful submission without token errors, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Acunetix]]

## Tags

- [[csrf]]
- [[verification]]
