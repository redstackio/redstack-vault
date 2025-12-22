---
id: proc-uuid-3
tags:
  - clickjacking
  - verification
  - browser-test
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
updated_at: '2025-12-14T17:28:05.394Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Clickjacking-Embedding-in-Browser

## Summary

This procedure tests the clickjacking POC by loading the HTML file in a web browser to confirm that the target site embeds and remains interactive within the iframe.

## Description

Verification confirms the exploitability of the missing X-Frame-Options header. By opening the POC locally or via a simple server, the procedure checks if the Sifchain site renders without frame-busting protections, allowing potential attacks like overlaying invisible elements to hijack clicks or keystrokes. This step is crucial in security reports to prove the vulnerability's impact, such as enabling unauthorized actions on the embedded page.

## Requirements

1. Web browser (e.g., Google Chrome)
2. POC HTML file from previous procedure
3. Local file access or basic HTTP server

## Defense

Defensive measures and detection strategies:

- Deploy frame-ancestors CSP to restrict embedding sources
- Log and alert on unusual browser behaviors or iframe loads
- Use browser extensions to detect clickjacking attempts

## Objectives

1. Load POC and observe embedding
2. Test interactivity within the iframe
3. Document evidence of vulnerability

## Instructions

### Step 1: Open POC File in Browser

**Context**: Launch the HTML file directly to test local embedding.

Double-click poc.html or drag it into Chrome.

> The browser should display the Sifchain site inside the iframe without errors.

### Step 2: Interact with Embedded Content

**Context**: Verify that the embedded page is fully functional.

Click elements, scroll, or enter text in the iframe to ensure no restrictions.

> Expected output: Site is visible, interactive, and responsive, confirming clickjacking feasibility.

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
- [[browser-verification]]
- [[iframe-test]]
