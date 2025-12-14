---
id: proc-identify-xss-935503-1
tags:
  - xss
  - reflected-xss
  - recon
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:09.661Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify Reflected XSS in Email Parameter

## Summary

This procedure identifies a reflected XSS vulnerability by examining how the 'email' parameter is handled and reflected on the thank-you page after newsletter subscription, confirming lack of sanitization.

## Description

The target is the thank-you page at https://cz.acronis.com/dekujeme-za-odber-novinek-produktu-disk-director/, which echoes the email input directly into the HTML response without validation or encoding. This allows injected scripts to execute in the browser context. The procedure involves accessing the page with a test email and inspecting the source to verify reflection.

## Requirements

1. Web browser with developer tools
2. Access to the public newsletter subscription flow
3. Basic knowledge of URL parameter manipulation

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., htmlspecialchars in PHP) for user inputs in HTML contexts
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in logs or WAF rules for script tags

## Objectives

1. Confirm parameter reflection without sanitization
2. Identify injection points for XSS payloads
3. Establish foundation for payload testing

## Instructions

### Step 1: Access the Thank-You Page

**Context**: Simulate a newsletter subscription to reach the vulnerable page and observe email reflection.

**Command** (Manual URL Access):

Visit: https://cz.acronis.com/dekujeme-za-odber-novinek-produktu-disk-director/?user=OK&oktosend=&email=test@example.com

> Load the page and view source (Ctrl+U or right-click > View Page Source). Search for 'test@example.com' to see if it's reflected plainly in HTML.

### Step 2: Inspect for Sanitization

**Context**: Check if the reflected value is encoded or escaped, indicating vulnerability.

**Command** (Browser Dev Tools):

Open Dev Tools (F12) > Elements tab > Search for email value.

> Expected: Value appears as raw text, e.g., <p>Thank you, test@example.com</p>, without &lt; or &amp; encoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- reconnaissance
