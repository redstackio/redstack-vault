---
id: proc-craft-insightly-csrf-poc
tags:
  - csrf-poc
  - html-form
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
updated_at: '2025-12-14T17:27:57.461Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft CSRF PoC HTML Form

## Summary

This procedure creates a malicious HTML form that auto-submits a POST request to Insightly's disable endpoint using the victim's linked account ID, exploiting the CSRF vulnerability when loaded in the victim's browser.

## Description

Based on the captured request, an HTML page is crafted to forge the disable action. The form targets the specific victim's ID and includes the necessary parameter (_pjax=#main) without requiring user interaction, relying on the victim's existing authenticated session. This PoC is hosted on an attacker-controlled domain and delivered via phishing or social engineering. The lack of CSRF tokens or header checks on the endpoint makes this effective.

## Requirements

1. Captured request details from Burp Suite
2. Victim's linked account ID
3. Text editor for HTML creation
4. Web server to host the PoC (e.g., local or remote)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Enforce same-site cookie attributes (Lax/Strict)
- Monitor for anomalous POST requests to sensitive endpoints

## Objectives

1. Replicate the disable request in HTML form
2. Enable auto-submission for drive-by exploitation
3. Target specific victim ID for precision

## Instructions

### Step 1: Create HTML Form Structure

**Context**: Build the basic form mimicking the captured POST request.

Use a text editor to create an HTML file with a form element: action set to https://crm.na1.insightly.com/Users/GoogleDisable/{victim_id}, method POST, and a hidden input for _pjax=#main.

### Step 2: Add Auto-Submit Script

**Context**: Ensure the form submits automatically on page load to exploit the session without interaction.

Add JavaScript to submit the form on document load, e.g., <script>document.getElementById('csrfForm').submit();</script>.

**Expected Output**: Complete HTML file that, when opened, immediately POSTs to the endpoint.

**Success Indicators**:
- Form submission triggers without errors in browser console
- Request matches captured payload

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-poc]]
- [[html-form]]
