---
id: proc-uuid-1
tags:
  - clickjacking
  - header-check
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:05.400Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Clickjacking-Vulnerable-URLs

## Summary

This procedure involves checking HTTP response headers of target web URLs to identify the absence of the X-Frame-Options header, which indicates susceptibility to clickjacking attacks.

## Description

Clickjacking exploits misconfigurations where websites can be embedded in iframes on malicious pages, tricking users into unintended interactions. This procedure targets public-facing web applications like the Sifchain documentation site. By inspecting headers during security testing, attackers confirm if framing is allowed, enabling UI redress attacks that could lead to unauthorized actions, data disclosure, or credential theft. Prerequisites include basic knowledge of HTTP headers and access to browser dev tools or command-line tools.

## Requirements

1. Internet access to target URLs (e.g., https://docs.sifchain.finance)
2. Web browser with developer tools (e.g., Chrome DevTools)
3. Optional: curl for header inspection

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses
- Use Content-Security-Policy (CSP) frame-ancestors directive
- Monitor for anomalous iframe embeddings in web logs

## Objectives

1. Confirm missing X-Frame-Options header on target URLs
2. Document vulnerable endpoints for POC development
3. Assess potential for UI redress attacks

## Instructions

### Step 1: Load Target URL and Inspect Headers

**Context**: Access the target page and examine its HTTP response headers to check for X-Frame-Options.

Open the URL in a browser, open DevTools (F12), go to the Network tab, reload the page, and select the main request to view response headers.

> Look for the absence of 'X-Frame-Options'. If missing, the site is vulnerable to embedding.

### Step 2: Test Multiple In-Scope URLs

**Context**: Repeat the inspection on additional URLs to map the vulnerability scope.

Test URLs like https://docs.sifchain.finance and note any without the header.

> Expected output: List of vulnerable URLs confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web-security]]
- [[header-misconfig]]
