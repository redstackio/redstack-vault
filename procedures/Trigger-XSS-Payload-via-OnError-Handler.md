---
tags:
  - xss
  - onerror
  - trigger
  - javascript
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ce9ba686-f2d6-45d8-98bf-5a883c8493b5
created_at: '2025-12-13T23:52:34.186Z'
updated_at: '2025-12-13T23:52:34.186Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Payload-via-OnError-Handler

## Summary

This procedure triggers the injected XSS payload by rendering the page, causing the SVG 'use' tag to load the base64 data URI and execute JavaScript via an onerror handler on an invalid image reference.

## Description

Once the malicious SVG is rendered in the browser, the 'use' tag resolves the href data URI, embedding the inner SVG. The <image href="1"> fails to load (invalid URL), firing the onerror event that runs alert(window.origin), confirming XSS. This can be extended to steal cookies, session data, or perform further actions.

## Requirements

1. Payload injected and page rendered (from prior procedures)
2. Web browser accessing the Rails application
3. No CSP blocking data URIs or inline JS

## Defense

Defensive measures and detection strategies:

- Implement strict CSP: script-src 'self'; img-src 'self' data: (but carefully for SVG)
- Sanitize SVG attributes to remove event handlers like onerror
- Use server-side rendering checks or tools like DOMPurify for client-side sanitization
- Monitor browser console and network for data URI loads or unexpected alerts

## Objectives

1. Execute arbitrary JavaScript in the victim's browser
2. Demonstrate data exfiltration potential (e.g., alert origin)
3. Enable follow-on attacks like session hijacking

## Instructions

### Step 1: Render the Page

**Context**: Load the ERB template containing the payload in a browser.

Navigate to the endpoint (e.g., http://localhost:3000) where the sanitized SVG is rendered.

> The browser parses the SVG, loads the data URI via 'use', and attempts to fetch the inner <image>.

### Step 2: Observe Execution

**Context**: The onerror fires due to failed image load, running the JS.

Expected: Alert dialog with the page origin (e.g., alert(http://localhost:3000)).

> Inspect the DOM: The inner SVG should be visible; replace alert with fetch to exfil data to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[onerror]]
- [[JavaScript]]
