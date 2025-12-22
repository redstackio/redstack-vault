---
id: proc-uuid-2
tags:
  - xss
  - exploit-trigger
  - form-submission
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Cisco ASA/FTD
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:02.444Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-XSS-via-Browser-Form-Submission

## Summary

This procedure triggers the reflected XSS exploit by loading the crafted HTML in a browser, causing an automatic form submission to the SAML ACS endpoint and executing the injected JavaScript for potential session theft.

## Description

Building on CVE-2020-3580, this step involves opening the malicious HTML file in a victim's browser, which submits a POST request with the tainted SAMLResponse. The endpoint reflects the payload without escaping, leading to JavaScript execution in the authenticated context. This can steal cookies, hijack sessions, or perform other actions. Prerequisites include the crafted HTML from the prior procedure and network access to the target. Outcomes include confirmed XSS via alert and opportunities for further exploitation.

## Requirements

1. Crafted `xss.html` file from previous procedure
2. Web browser with JavaScript enabled
3. Network connectivity to the Cisco ASA/FTD SAML ACS endpoint

## Defense

Defensive measures and detection strategies:

- Deploy Web Application Firewall (WAF) rules to block suspicious SAMLResponse payloads
- Enable logging for ACS endpoint requests and alert on JavaScript-like content
- Educate users on phishing to avoid loading untrusted HTML

## Objectives

1. Submit the malicious form to reflect the XSS payload
2. Execute arbitrary JavaScript in the victim's browser
3. Validate exploitation for session hijacking potential

## Instructions

### Step 1: Load the HTML File

**Context**: Open the file in a browser to initiate the auto-submit process.

Navigate to `xss.html` using file:// protocol or serve it via a local web server.

> The browser will load the page, execute the script, and submit the form to the target URL.

### Step 2: Observe Execution

**Context**: Monitor the browser for payload reflection and JavaScript trigger.

Inspect network tab for POST request to https://[target]/+CSCOE+/saml/sp/acs?tgname=a with SAMLResponse payload; check for alert popup.

> Expected output: 200 OK response from endpoint, 'XSS' alert displayed, console logs showing script execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[exploit-trigger]]
- [[form-submission]]
- [[javascript-execution]]
