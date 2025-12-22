---
id: proc-uuid-003
tags:
  - xss
  - payload-injection
  - javascript
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:32.117Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-JavaScript-Payload-into-Auth-Parameter

## Summary

This procedure exploits the unsanitized 'auth' parameter in Tableau's embeddedAuthRedirect.html by injecting a javascript: scheme payload, resulting in reflected XSS and arbitrary JavaScript execution in the browser.

## Description

The vulnerability stems from the endpoint treating the 'auth' parameter as a redirect URL without validating against javascript: schemes. Injecting javascript:alert("xElkomy") causes the browser to execute the script upon visiting the crafted URL. This is a reflected XSS, requiring social engineering to lure victims, but can lead to session hijacking or phishing on the DoD site. Test responsibly and report via HackerOne.

## Requirements

1. Identified endpoint from previous procedure
2. Web browser for testing
3. URL encoding knowledge for payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all URL parameters to block javascript: schemes
- Implement output encoding for reflected parameters and monitor for XSS payloads in logs

## Objectives

1. Craft and deliver a malicious URL with injected payload
2. Achieve JavaScript execution in the victim's context
3. Demonstrate potential for data exfiltration or session theft

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the exploit URL by appending the payload to the 'auth' parameter.

Take the base endpoint https://██████.dod.mil/en/embeddedAuthRedirect.html and add ?auth=javascript:alert(%22xElkomy%22).

> URL-encode the payload to ensure proper transmission: javascript:alert("xElkomy") becomes javascript:alert(%22xElkomy%22). The full URL is now ready for testing.

### Step 2: Test Payload Execution

**Context**: Visit the URL to trigger the XSS.

Paste the constructed URL into a browser and load it.

> An alert box should pop up with "xElkomy". If it executes, the vulnerability is confirmed. For real attacks, replace alert with malicious code like document.cookie theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[exploitation]]
