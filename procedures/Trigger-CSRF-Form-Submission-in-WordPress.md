---
tags:
  - csrf
  - form-submission
  - wordpress
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
updated_at: '2025-12-14T17:27:42.753Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: cb5ad74a-40e5-4fc1-a90a-d256cda0b84f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-CSRF-Form-Submission-in-WordPress

## Summary

This procedure involves delivering and executing the malicious HTML form in the victim's browser while authenticated, forging a POST request to the vulnerable WordPress AJAX endpoint to alter the background image.

## Description

With the user logged in, opening the HTML file sends a cross-origin POST to admin-ajax.php without a nonce, exploiting the lack of CSRF checks in the deprecated handler. The request includes attachment_id and size, updating the custom_background option and applying the change site-wide.

## Requirements

1. Prepared malicious HTML file from prior procedure
2. Authenticated admin session in the same browser
3. Victim interaction (e.g., clicking a link to open the file)

## Defense

Defensive measures and detection strategies:

- Add nonce verification to all AJAX actions in WordPress core or plugins
- Implement SameSite=Strict cookies to prevent cross-site requests
- Use web application firewalls (WAF) to block anomalous POSTs to admin-ajax.php
- Monitor for rapid theme changes post-deprecation

## Objectives

1. Forge and send the unauthorized request using victim's session
2. Modify the theme without direct access
3. Achieve persistence via site-wide visual disruption

## Instructions

### Step 1: Deliver the Payload

**Context**: Send the HTML file to the victim for opening in their authenticated browser.

Email or link the csrf-exploit.html file, instructing or tricking them to open it (e.g., "Click to view update").

> Expected: Victim opens file; auto-script triggers form submission.

### Step 2: Execute Submission

**Context**: Ensure the form posts the payload to the endpoint.

If not auto-submitted, prompt click. Monitor network tab for POST to admin-ajax.php with action=set-background-image.

> Expected: 200 OK response; no error about missing nonce due to vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[wordpress]]
- [[exploitation]]
