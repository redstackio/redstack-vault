---
tags:
  - csrf-poc
  - burp-suite
  - html-form
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:07.441Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 803a8156-7ff6-4774-915d-154cfdca6a84
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Generate-CSRF-POC-from-Captured-Request

## Summary

This procedure generates a CSRF HTML PoC using Burp Suite's built-in tool from a captured POST request to the Tucows notes endpoint.

## Description

Right-clicking the captured request in Burp and selecting Engagement tools → Generate CSRF PoC creates an HTML file with a form that auto-submits via JavaScript, replicating the request. This exploits the absence of CSRF protection, allowing forged requests from external sites. Used in web attack scenarios targeting state-changing endpoints.

## Requirements

1. Captured POST request in Burp history
2. Burp Suite with Engagement tools enabled
3. Basic HTML editing knowledge

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all POST forms
- Scan for and block auto-submitting forms from external domains

## Objectives

1. Produce exploitable HTML PoC
2. Mimic original request accurately
3. Test for CSRF vulnerability

## Instructions

### Step 1: Locate Request in Burp

**Context**: Identify the notes POST.

In HTTP history, find the entry for the redacted endpoint with ajax=save_note.

> Filter by POST method if needed.

### Step 2: Generate PoC

**Context**: Use Burp tool to create HTML.

Right-click the request → Engagement tools → Generate CSRF PoC; save the output HTML.

> Expected: HTML with <form> to endpoint, inputs for params, and <script> for submit.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf-poc
- burp-suite
