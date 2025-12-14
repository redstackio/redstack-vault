---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - recon
  - vulnerability-identification
  - pdf.js
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-13T23:52:21.095Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify-Outdated-PDF-js-in-Nextcloud

## Summary

This procedure involves inspecting a Nextcloud instance to detect an outdated version of the PDF.js library in its PDF viewer, confirming susceptibility to CVE-2018-5158, which enables XSS via malicious PDFs.

## Description

Nextcloud integrates PDF.js for rendering PDFs in its viewer. Versions prior to patches for CVE-2018-5158 allow arbitrary JavaScript execution when processing malicious PDFs. This reconnaissance step verifies the library's version by examining loaded scripts or documentation, setting the stage for exploitation in web-based environments. Expected outcomes include confirmation of the vulnerability, enabling targeted attacks like session hijacking upon PDF viewing.

## Requirements

1. Access to a Nextcloud instance with PDF viewing enabled (authenticated or public read access).
2. Web browser with developer tools for script inspection.
3. Knowledge of CVE-2018-5158 details from sources like NIST or Mozilla.

## Defense

Defensive measures and detection strategies:

- Regularly update Nextcloud and its dependencies, including PDF.js, to patched versions.
- Monitor for anomalous script loading in PDF viewers via web application firewalls (WAFs).
- Disable or sandbox PDF rendering if not essential, or use alternative viewers without JavaScript support.

## Objectives

1. Confirm the presence of vulnerable PDF.js to assess exploit viability.
2. Gather technical details on the target's PDF handling for payload customization.
3. Identify browser compatibility for execution (e.g., Safari/Firefox vs. Chrome).

## Instructions

### Step 1: Access Nextcloud PDF Viewer

**Context**: Navigate to the Nextcloud interface and attempt to view or upload a benign PDF to load the viewer.

Log in to the Nextcloud dashboard, go to the Files section, and select or upload a simple PDF file. Open it using the integrated viewer.

> This loads the PDF.js-based renderer; inspect the page source or network tab in browser dev tools to identify PDF.js scripts.

### Step 2: Inspect PDF.js Version

**Context**: Examine loaded resources to determine the PDF.js version and check against known vulnerable releases.

In the browser's developer tools (F12), go to the Network tab, reload the PDF viewer, and filter for 'pdf.js'. Note the file paths or version strings (e.g., in comments or metadata). Cross-reference with CVE-2018-5158 advisory for vulnerable versions (pre-2.2 or similar unpatched).

> Expected output: Script sources revealing outdated PDF.js, e.g., 'pdf.js?v=1.x' where x < patched version.

### Step 3: Validate Vulnerability

**Context**: Confirm CVE applicability by reviewing library details against exploit requirements.

Search the PDF.js source code (if accessible) or use online tools to check the version against Mozilla's bug tracker. Ensure the library supports JavaScript execution in embedded contexts.

> Success: Version matches known vulnerable state, ready for POC testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[vulnerability-scanning]]

