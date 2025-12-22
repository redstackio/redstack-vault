---
tags:
  - open-redirect
  - owncloud
  - unauthenticated
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:30.467Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7a87dcce-eedb-477e-8533-db2aedb6889b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Access-Malicious-PDF-Viewer-URL

## Summary

This procedure constructs and accesses the ownCloud PDF viewer endpoint with a malicious external URL in the 'file' parameter, setting up the open redirect without immediate navigation, allowing preparation for phishing exploitation.

## Description

In the context of ownCloud's files_pdfviewer app, the vulnerability stems from a lack of validation on the 'file' parameter, permitting arbitrary external URLs. Accessing this endpoint loads the viewer interface but does not auto-redirect, requiring further interaction. This step is unauthenticated and targets all ownCloud installations with the app enabled, enabling attackers to craft phishing links that appear legitimate.

## Requirements

1. Access to a web browser with JavaScript enabled
2. Publicly accessible ownCloud instance URL
3. Knowledge of a controlled malicious domain and file path

## Defense

Defensive measures and detection strategies:

- Implement URL validation in the files_pdfviewer app to restrict 'file' parameter to internal resources only
- Monitor access logs for suspicious external URLs in PDF viewer requests
- Enable Content Security Policy (CSP) to block unexpected redirects

## Objectives

1. Load the vulnerable PDF viewer with an external malicious file reference
2. Confirm the interface loads without auto-redirect
3. Prepare for download-triggered phishing

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build the endpoint URL by appending the external malicious file to the ownCloud PDF viewer path.

No command required; manually construct: https://target-owncloud.com/index.php/apps/files_pdfviewer?file=https://evildomain.xx/EvilFile.xx

> This URL scheme exploits the unvalidated parameter. Expected output: A shareable link that can be sent to victims.

### Step 2: Visit the Endpoint

**Context**: Use a browser to access the constructed URL and verify the viewer loads.

No command; open in browser.

> The page should display the PDF viewer UI, possibly with a loading error for the external file, but no redirect occurs yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- open-redirect
- owncloud
- web-exploit

---
