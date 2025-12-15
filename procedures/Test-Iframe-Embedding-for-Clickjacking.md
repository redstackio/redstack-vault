---
tags:
  - clickjacking
  - testing
  - browser
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:05.415Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c3d116ad-6706-4754-9628-2eb770d49722
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Test-Iframe-Embedding-for-Clickjacking

## Summary

This procedure tests the malicious HTML page by loading it in a browser to confirm the Nextcloud login embeds without restrictions, validating clickjacking feasibility.

## Description

To confirm exploitation, load the crafted HTML file locally or via a simple server and observe the iframe rendering the login page. Interactions like form submissions or modals should work due to sandbox settings, allowing overlays to trick users into actions (e.g., entering credentials on a fake overlay). Success indicates the vulnerability; impacts include phishing or CSRF-like attacks. Requires a browser; local file access suffices for proof-of-concept.

## Requirements

1. Web browser for rendering
2. Created malicious HTML file from prior step
3. Local file system access

## Defense

Defensive measures and detection strategies:

- Browser-level protections like X-Frame-Options enforcement
- Monitor user-agent strings and referer headers for anomalous requests
- Implement client-side frame-busting JavaScript

## Objectives

1. Verify iframe loads target content
2. Test interactive functionality
3. Confirm no framing blocks

## Instructions

### Step 1: Load the Malicious Page

**Context**: Open the HTML file to initiate embedding.

Double-click the malicious.html file or drag it into a browser window.

> The page should display with the iframe containing the Nextcloud login form.

### Step 2: Observe and Interact

**Context**: Check for restrictions and simulate attack.

Interact with the embedded login (e.g., click forgot password); inspect console for errors.

> No errors like 'Refused to display' should appear; full rendering confirms vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- clickjacking
- testing
- validation
