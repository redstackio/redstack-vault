---
id: proc-uuid-1
tags:
  - clickjacking
  - poc
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-13T23:52:24.832Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open-Clickjacking-POC-in-Browser

## Summary

This procedure loads a local HTML proof-of-concept file in a web browser to initiate a clickjacking attack, embedding the vulnerable edoverflow.com/tools/respond page in an iframe and overlaying it with decoy elements to hide the malicious form interaction.

## Description

The clickjacking PoC is a self-contained HTML file that uses an iframe to load the target site, positions the iframe off-screen or behind visual elements like frog images, and aligns interactive decoys with the site's form fields. This setup allows an attacker to trick the victim into submitting data to the hidden form without realizing it. The target environment is any modern web browser with access to the internet, and the procedure requires a pre-created PoC file based on the vulnerability analysis.

## Requirements

1. Firefox browser installed
2. Local HTML PoC file embedding https://edoverflow.com/tools/respond/
3. Internet connectivity to load the iframe content

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options or Content-Security-Policy headers to prevent iframe embedding
- Educate users on recognizing suspicious overlays or unexpected interactions
- Monitor for unusual form submissions from embedded contexts

## Objectives

1. Load the PoC to set up the clickjacking environment
2. Verify iframe embedding without blocking
3. Position decoys over form elements for interaction

## Instructions

### Step 1: Launch Browser and Open PoC

**Context**: Start the browser and navigate to the local PoC file to initialize the attack setup.

No command required; manually open the file.

> Open the HTML file in Firefox. The page should display frog images with the underlying iframe loaded invisibly.

### Step 2: Verify Iframe Loading

**Context**: Confirm the target site is embedded and positioned correctly using browser developer tools.

Inspect the page source or use dev tools to ensure the iframe src is https://edoverflow.com/tools/respond/ and positioned with z-index or absolute positioning to overlay forms.

> Expected: No CORS or framing errors; form elements are hidden behind decoys.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[clickjacking]]
- [[poc]]
