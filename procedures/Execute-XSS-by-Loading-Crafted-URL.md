---
tags:
  - xss
  - execution
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.696Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5967ac8f-fea1-426d-a578-aba6ea1f6c75
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute XSS by Loading Crafted URL

## Summary

This procedure loads the malicious URL in a browser, triggering the reflected XSS payload in the unauthorized modal, resulting in arbitrary JavaScript execution such as alerting the domain.

## Description

The crafted URL, when loaded, omits client_id and provides the malicious redirect_uri. The server renders the template, and client-side JS displays the modal, injecting the payload into the DOM. This executes onload, demonstrating XSS for session theft or exfiltration in victim browsers.

## Requirements

1. Crafted URL from previous procedure
2. Compatible web browser (Chrome, Firefox, etc.)
3. Victim context (e.g., direct load or phishing link)

## Defense

Defensive measures and detection strategies:

- Escape all dynamic content in templates (e.g., use text helpers in JS templates)
- Implement XSS filters or WAF rules blocking SVG onload or alert payloads
- Monitor browser console errors and anomalous JS execution

## Objectives

1. Render the modal with injected payload
2. Achieve JavaScript execution in page context
3. Validate impact like domain alert

## Instructions

### Step 1: Load the Malicious URL

**Context**: Open the crafted URL to initiate the request and modal rendering.

Paste and enter the URL in the browser address bar:

```url
https://www.mapbox.com/authorize/?redirect_uri=%27%3E%3Csvg%20onload=%27alert%28document.domain%29%27%3E
```

> The page loads, modal appears, and alert triggers immediately.

### Step 2: Verify Execution

**Context**: Confirm the payload ran by observing the alert and inspecting DOM.

Check for the alert popup showing 'mapbox.com'. Use dev tools to see the injected SVG in the modal HTML.

> Expected: No CSP blocks; JS executes freely.

### Step 3: Assess Impact

**Context**: Test for broader exploitation potential.

Replace alert with document.cookie access or fetch to exfiltrate data.

> Success: Arbitrary code runs in high-privilege context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- xss-trigger
- javascript-execution
