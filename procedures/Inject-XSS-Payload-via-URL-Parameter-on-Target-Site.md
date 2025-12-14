---
id: proc-uuid-3
tags:
  - xss
  - injection
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:18.414Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Inject-XSS-Payload-via-URL-Parameter-on-Target-Site

## Summary

This procedure injects the crafted XSS payload into a URL parameter on the target site, triggering DOM-based execution in the victim's browser for arbitrary JavaScript.

## Description

On Grab.com, appending the encoded payload to ?xss= on pages like https://www.grab.com/sg/partnerships/ causes the client-side JS to process it through stripHtml, failing to remove the img onerror, leading to confirm('XSSED') execution. This affects all pages and enables attacks like session theft.

## Requirements

1. Valid encoded payload from prior crafting
2. Browser access to the target domain
3. No authentication required for public pages

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all query parameters server-side
- Implement CSP to restrict script sources
- Use WAF rules to block encoded HTML in URLs and monitor for XSS alerts

## Objectives

1. Deliver payload without server-side filtering
2. Trigger JS execution upon page load
3. Validate impact with a harmless alert

## Instructions

### Step 1: Construct Malicious URL

**Context**: Append payload to target endpoint.

Form the URL: https://www.grab.com/sg/partnerships/?xss=%3C%3Ca/%3A%3C%22a%22%3Eimg%20src%3D%23%20onerror%3Dconfirm%28%27XSSED%27%29%3E

### Step 2: Load and Observe Execution

**Context**: Simulate victim by visiting the URL.

Paste into browser address bar and load; the page processes the parameter, sets innerHTML, and fires onerror on the img tag, showing the confirm dialog.

### Step 3: Verify and Escalate

**Context**: Confirm success and note potential for real payloads.

If dialog appears, vulnerability confirmed. Replace confirm with document.cookie for session theft demo.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
