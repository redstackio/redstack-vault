---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - clickjacking
  - testing
  - browser
  - iframe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:05.406Z'
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
# Test-Iframe-Embedding-in-Browser

## Summary

This procedure tests the embedding of a target webpage in an iframe within a local HTML file using a web browser, confirming the presence of a Clickjacking vulnerability by observing unrestricted rendering.

## Description

In a Clickjacking attack, the absence of anti-framing headers allows malicious sites to embed victim pages in iframes, enabling UI manipulation. For the Pushwoosh registration page, testing involves loading a local PoC HTML file in a browser to verify if the page loads without blocks. Success indicates medium-severity risk (CVSS 6.1), as attackers could overlay elements to induce unintended actions like unauthorized registrations. This step validates the root cause: missing X-Frame-Options or CSP protections, despite any non-blocking JavaScript detection.

## Requirements

1. Local HTML PoC file (e.g., index.html from prior procedure)
2. Modern web browser (Chrome, Firefox, Edge)
3. Internet access to load the target URL

## Defense

Defensive measures and detection strategies:

- Enforce strict framing policies via server headers
- Use browser developer tools to inspect for embedded iframes
- Implement client-side frame-busting scripts that break out of iframes

## Objectives

1. Confirm iframe embedding works without restrictions
2. Observe interactive functionality in the embedded page
3. Assess potential for UI redressing exploitation

## Instructions

### Step 1: Load PoC in Browser

**Context**: Open the HTML file to initiate the embedding test and check for any browser or server-side blocks.

Navigate to the file using the browser's file:// protocol or serve it locally (e.g., via Python's http.server).

For local serving (optional, using built-in tools):

```bash
python -m http.server 8000
```

Then visit http://localhost:8000/index.html.

> The page should render the iframe sourcing https://go.pushwoosh.com/register. Expected: Full page load without errors or blocks.

### Step 2: Verify Interactivity and Restrictions

**Context**: Interact with the embedded page to ensure scripts and forms function, confirming vulnerability.

In the browser, attempt to fill out the registration form or click buttons within the iframe.

Inspect the console for any JavaScript warnings about iframe detection, but confirm no prevention occurs.

> Successful test shows the form submitting or page elements responding as if standalone. If blocked, vulnerability is mitigated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[testing]]
- [[browser]]
- [[web]]
