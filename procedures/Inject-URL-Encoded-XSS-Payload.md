---
tags:
  - xss
  - exploit
  - web
  - bypass
  - javascript
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
updated_at: '2025-12-14T03:16:14.530Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1d382763-8657-4d9d-95dd-d99107814786
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-URL-Encoded-XSS-Payload

## Summary

This procedure exploits a reflected XSS vulnerability in the Adobe eDex search functionality by injecting a URL-encoded payload that bypasses the '=' stripping filter, resulting in arbitrary JavaScript execution within the victim's browser context.

## Description

Building on the identified escaping flaw in http://edex.adobe.com/search/global/, this procedure crafts a malicious search query using %3D to encode the equals sign in an XSS payload (e.g., <script>alert('XSS')</script>). When a victim accesses the crafted URL, the unsanitized input is reflected into the page, executing the script. This can lead to session hijacking, data exfiltration, or further attacks. The target environment is a public web search interface with no authentication, making it suitable for drive-by compromises via shared links.

## Requirements

1. Confirmed vulnerability from prior testing (e.g., %3D bypass)
2. Web browser for payload crafting and testing
3. Method to deliver the URL to victims (e.g., email, social engineering)

## Defense

Defensive measures and detection strategies:

- Decode all URL parameters before sanitization and apply strict output encoding (e.g., HTML entity encoding)
- Deploy Web Application Firewall (WAF) rules to block encoded XSS patterns
- Log and alert on anomalous JavaScript in reflected content

## Objectives

1. Deliver a functional XSS payload via the search parameter
2. Achieve JavaScript execution in the browser
3. Demonstrate potential for arbitrary code execution

## Instructions

### Step 1: Craft the Encoded Payload

**Context**: Replace the equals sign in a standard XSS payload with %3D and encode other special characters to ensure reflection.

Construct the URL: http://edex.adobe.com/search/global/%3Cscript%3Ealert('XSS')%3C/script%3E. Use a URL encoder tool or browser dev tools to verify encoding (e.g., < becomes %3C, > becomes %3E).

> Ensure the payload is a valid JavaScript snippet that executes on reflection.

### Step 2: Test and Deploy the Payload

**Context**: Verify execution locally before targeting victims.

Load the crafted URL in a browser. Check for alert popup or console errors indicating successful execution. Once confirmed, distribute the URL to induce victim access.

> Successful test shows JavaScript running, such as an alert dialog confirming 'XSS'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- exploit
- javascript
