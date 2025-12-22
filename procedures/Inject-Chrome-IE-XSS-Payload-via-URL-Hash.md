---
id: proc-inject-chrome-ie-xss
tags:
  - xss
  - dom-xss
  - chrome
  - ie
  - onclick-payload
type: procedure
tools:
  - '[[tools/DominatorPro]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.349Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Chrome-IE-XSS-Payload-via-URL-Hash

## Summary

This procedure uses a browser-specific anchor tag with onclick event in the URL hash to exploit prettyPhoto's DOM insertion on Chrome and IE, achieving JavaScript execution despite parsing differences from Firefox.

## Description

Chrome and IE handle hash parsing differently, so this payload leverages an `<a>` tag with onclick to trigger on DOM processing or user interaction. The plugin's failure to escape quotes and attributes in hashRel allows direct event handler injection. This DOM-based XSS enables attacks like phishing or data exfiltration in the victim's context. No server processing occurs; impact includes cross-site scripting leading to session hijacks. Verify via alert on domain.

## Requirements

1. Chrome or Internet Explorer browser
2. Access to eng.uber.com
3. Understanding of event handler payloads

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation for URL fragments
- Deploy XSS filters or WAF rules for client-side scripts
- Audit plugin updates and deprecate legacy ones like prettyPhoto

## Objectives

1. Embed onclick executable code in hash
2. Force DOM insertion and event firing in Chrome/IE
3. Confirm execution with domain alert

## Instructions

### Step 1: Construct Malicious URL

**Context**: Format the hash to simulate a gallery item, injecting the anchor tag for onclick execution.

No command; construct: `http://eng.uber.com/#prettyPhoto[gallery]/1,<a onclick="alert(document.domain);">/`

> The `[gallery]/1,` structure mimics valid input; onclick executes on element creation or click.

### Step 2: Navigate and Trigger

**Context**: Load the URL and interact if needed to fire the event.

Open the URL in Chrome or IE; click the injected element if no auto-trigger.

> Expected output: Alert displays "eng.uber.com". Console logs show anchor insertion in DOM.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/DominatorPro]]

## Tags

- [[xss]]
- [[dom-xss]]
