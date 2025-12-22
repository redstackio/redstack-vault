---
tags:
  - poc-hosting
  - xss
  - postmessage
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e096578f-f330-4b61-a8cd-763eb5f1d32f
created_at: '2025-12-13T23:55:38.318Z'
updated_at: '2025-12-13T23:55:38.318Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Host-Malicious-POC-on-Controlled-Domain

## Summary

This procedure deploys a proof-of-concept HTML file on a controlled domain to send malicious postMessage data, exploiting the origin bypass in Marketo's forms2.min.js for DOM-based XSS.

## Description

Using the registered prefix domain (e.g., app-sj17.ma), upload an HTML file containing JavaScript that dispatches a postMessage event with a payload like a redirect or alert. This reuses payloads from prior reports (e.g., #398054) and targets the Marketo origin on the victim site (www.hackerone.com). The procedure assumes web hosting access; outcomes include the POC being accessible and ready to trigger the vulnerability upon visitation.

## Requirements

1. Control over the registered domain's hosting
2. Access to a web server or static hosting service (e.g., GitHub Pages, VPS)
3. POC HTML file with postMessage script

## Defense

Defensive measures and detection strategies:

- Scan third-party scripts for insecure postMessage handlers
- Enforce CSP to block unauthorized postMessage sources
- Log and alert on postMessage events from non-whitelisted origins

## Objectives

1. Make the malicious POC publicly accessible
2. Ensure HTTPS serving for origin matching
3. Prepare for exploit triggering

## Instructions

### Step 1: Prepare POC File

**Context**: Create or reuse the HTML file with postMessage payload.

No specific command; edit HTML to include <script>window.parent.postMessage('malicious payload', 'https://app-sj17.marketo.com');</script> targeting the flawed origin.

> Save as post2.html. Expected: File ready with JS payload for redirect or XSS.

### Step 2: Upload to Hosting

**Context**: Deploy the file to the domain's web root or subdirectory.

No specific command; use FTP/SCP or hosting panel to upload to /marketo/post2.html on app-sj17.ma.

> Verify accessibility via browser. Expected: https://app-sj17.ma/marketo/post2.html loads the script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[poc-hosting]]
- [[xss]]
