---
id: proc-uuid-3
tags:
  - xss
  - execution
  - dom-xss
type: procedure
tools: []
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
updated_at: '2025-12-14T03:47:12.752Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-DOM-based-XSS-via-Malicious-URL

## Summary

This procedure executes the crafted XSS payload by loading a malicious URL, triggering JavaScript in the browser context of vulnerable Starbucks subdomains.

## Description

Upon navigation to the URL with the malicious hash, the page's JavaScript processes location.hash using jQuery 1.10.1, inserting the payload into DIV.innerHTML. This creates an img element that fails to load (src=x.jpg), firing the onerror event to run alert(document.domain). The attack is client-side, affecting browsers like Chrome and IE 11, with potential for escalation to session theft or phishing.

## Requirements

1. Crafted malicious URL from prior procedure.
2. Vulnerable browser (Chrome or IE 11; modern browsers may vary).
3. Direct access to the target subdomain.

## Defense

Defensive measures and detection strategies:

- Patch jQuery to mitigate selector injection.
- Log and monitor URL parameters for suspicious hashes.
- Educate users on phishing risks from shared links.

## Objectives

1. Achieve JavaScript execution in the target domain.
2. Verify impact through alert or console output.
3. Demonstrate potential for further client-side exploitation.

## Instructions

### Step 1: Load Malicious URL

**Context**: Navigate to the full URL to initiate hash processing.

Enter the complete URL in the browser address bar, e.g., http://store.starbucks.de/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start#a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/> and press Enter.

> The page loads, processes the hash, and injects the payload.

### Step 2: Observe Execution

**Context**: Confirm the onerror handler fires.

Watch for the alert box displaying the document domain (e.g., store.starbucks.de). In developer tools Console, check for any errors or logs indicating injection.

> Successful execution shows the alert; replace alert with other JS for advanced payloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
