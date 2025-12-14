---
tags:
  - csp-bypass
  - javascript-injection
  - resource-load
type: procedure
tools:
  - '[[tools/Browser-Developer-Console]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-dynamic-img-element]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:17.963Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 91d54ec3-973a-41e5-aabf-96378793cfe0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Dynamic-Image-for-CSP-Bypass

## Summary

This procedure exploits a CSP misconfiguration lacking img-src directives by using JavaScript to dynamically create and append an external image element, allowing unauthorized resource loading.

## Description

Targeting sites like https://portswigger.net/ with incomplete CSP policies, this involves injecting JavaScript via the browser console to bypass static restrictions. The payload creates an img element, sets an external src (e.g., YouTube image), clears the body for visibility, sets dimensions, and appends it. This demonstrates the bypass, as dynamic creation evades policy checks on static tags, potentially enabling further escalations like tracking or phishing.

## Requirements

1. Active session on the target site.
2. Browser console access.
3. Knowledge of external resource URL (e.g., https://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg).

## Defense

Defensive measures and detection strategies:

- Add explicit img-src directives to CSP (e.g., img-src 'self' data:).
- Enable CSP reporting to log violations.
- Use Content-Security-Policy-Report-Only for testing.

## Objectives

1. Load external image dynamically.
2. Confirm CSP does not block img creation via JS.
3. Visualize the bypass impact.

## Instructions

### Step 1: Execute Image Creation Payload

**Context**: Use JavaScript to bypass CSP by creating the element programmatically.

**Command** ([[commands/create-dynamic-img-element]]):
```javascript
var demo=document.createElement("img"); demo.src="https://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg"; document.body.innerHTML=""; demo.width="1000"; demo.height="1000"; document.body.appendChild(demo);
```

> This creates the img, sets src to external URL, clears body, sizes to 1000x1000, and appends; image loads if bypass succeeds.

### Step 2: Verify Load

**Context**: Check for successful rendering without policy enforcement.

Inspect the page and console for errors.

> No 'Refused to load the image' CSP errors; image displays.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/create-dynamic-img-element]]

## Tools Used

- [[tools/Browser-Developer-Console]]

## Tags

- csp-bypass
- javascript-injection
- resource-load
