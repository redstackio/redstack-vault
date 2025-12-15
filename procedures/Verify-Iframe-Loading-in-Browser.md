---
id: proc-verify-iframe-browser
tags:
  - clickjacking
  - verification
  - browser-test
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.834Z'
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
# Verify-Iframe-Loading-in-Browser

## Summary

This procedure loads a local HTML PoC in a browser to confirm that the target site (e.g., Yelp) embeds in an iframe without frame-busting protections, validating clickjacking exposure.

## Description

Verification involves executing the PoC in a real browser environment to mimic an attacker's malicious page. This step confirms the vulnerability by observing unrestricted rendering, which could allow overlay attacks. Requires the PoC file from prior steps; outcomes include visual proof of embedding, essential for reporting.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Saved PoC HTML file
3. Stable internet connection

## Defense

Defensive measures and detection strategies:

- Deploy X-Frame-Options: SAMEORIGIN
- Log iframe load attempts in server access logs
- Use browser extensions to detect framing

## Objectives

1. Confirm successful embedding
2. Observe lack of restrictions
3. Validate vulnerability impact

## Instructions

### Step 1: Open PoC File

**Context**: Launch the HTML in browser.

Double-click the "yelp-iframe-poc.html" file or drag it into the browser window.

> Browser renders the page with iframe.

### Step 2: Inspect Rendering

**Context**: Check for successful load and no blocks.

Observe if Yelp content appears inside the 500x500 iframe without errors or blank frames.

> Expected output: Full Yelp page visible in iframe. Success if no "refused to connect" messages.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- [[clickjacking]]
- [[verification]]
