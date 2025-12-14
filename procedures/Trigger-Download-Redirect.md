---
tags:
  - open-redirect
  - phishing
  - ui-interaction
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
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:24:30.456Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 746e9a6b-695e-467f-ac00-0d8331b94cf2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.001]]'
---
---

# Trigger-Download-Redirect

## Summary

This procedure involves interacting with the download button in the ownCloud PDF viewer to trigger the open redirect to an arbitrary external domain, enabling the phishing attack without authentication.

## Description

Once the malicious URL is loaded in the viewer, the download functionality directly uses the unvalidated 'file' parameter to redirect the browser. This bypasses any internal checks, allowing unauthenticated users to be sent to malicious sites. The root cause is the app's failure to restrict the parameter or add auth checks on download actions, impacting phishing by tricking users into file downloads and site visits.

## Requirements

1. Loaded PDF viewer page from previous step
2. Web browser capable of handling redirects and downloads
3. Victim interaction (e.g., via social engineering to click download)

## Defense

Defensive measures and detection strategies:

- Patch the files_pdfviewer app to validate and sanitize the 'file' parameter on download
- Log and alert on download requests with external URLs
- User training to avoid clicking downloads from untrusted PDF viewers

## Objectives

1. Initiate the redirect via UI download action
2. Force browser navigation to external malicious domain
3. Deliver phishing payload through download and site access

## Instructions

### Step 1: Locate Download Button

**Context**: Identify the UI element in the PDF viewer interface.

No command; visually inspect the upper right corner for the download icon.

> Expected output: Download button visible and clickable.

### Step 2: Click to Trigger Redirect

**Context**: Perform the interaction to exploit the vulnerability.

No command; click the download button.

> This directly redirects to the external URL (e.g., https://evildomain.xx/EvilFile.xx), starting the download and navigation. Expected output: Browser leaves ownCloud and loads malicious content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[T1566.001]] Phishing: Spearphishing Attachment

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- redirect
- download-exploit

---
