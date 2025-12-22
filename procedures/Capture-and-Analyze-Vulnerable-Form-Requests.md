---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - csrf
  - request-capture
  - analysis
type: procedure
tools:
  - '[[tools/Acunetix]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.761Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-and-Analyze-Vulnerable-Form-Requests

## Summary

This procedure involves intercepting and dissecting HTTP requests from vulnerable CSRF forms using Acunetix to confirm the lack of protection mechanisms, enabling preparation for exploitation PoCs.

## Description

Following vulnerability scanning, this step captures real requests to endpoints like /user/register on the Uzbey site. The target environment is a web application on Apache, likely Drupal, where forms use POST with specific inputs but no CSRF tokens. An attacker uses this to replicate requests, understanding headers like Acunetix-Aspect for testing. Outcomes include detailed request blueprints for forging attacks that trick authenticated users.

## Requirements

1. Acunetix with interception capabilities enabled
2. Access to a vulnerable endpoint (e.g., https://staging.uzbey.com/user/register)
3. Proxy or interception setup for traffic analysis

## Defense

Defensive measures and detection strategies:

- Enforce same-origin policy strictly
- Log and alert on requests with unusual headers (e.g., Acunetix-Aspect)
- Use web application firewalls (WAF) to validate form submissions

## Objectives

1. Capture sample POST requests to vulnerable forms
2. Verify absence of CSRF tokens in request structure
3. Extract parameters for PoC development

## Instructions

### Step 1: Intercept Request During Scan

**Context**: Use Acunetix's built-in proxy to capture traffic while simulating form submissions.

Configure Acunetix to intercept a POST to https://staging.uzbey.com/user/register?destination=user/register.

> The interception reveals headers including Acunetix-Aspect: enabled, Acunetix-Aspect-Password: 082119f75623eb7abd7bf357698ff66c, and Acunetix-Aspect-Queries: filelist;aspectalerts, along with form data.

### Step 2: Analyze Captured Data

**Context**: Break down the request to identify exploitable elements.

Review the captured inputs (e.g., name, pass, form_build_id, form_id, op) and confirm no dedicated CSRF token field or header validation.

> Analysis shows the server processes the request without token checks, allowing external forgery.

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
- [[analysis]]
