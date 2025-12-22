---
id: proc-identify-clickjacking-form-001
tags:
  - clickjacking
  - recon
  - web
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
updated_at: '2025-12-14T17:28:12.210Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Web Form for Clickjacking

## Summary

This procedure involves inspecting a target website to identify forms lacking clickjacking protections, such as the beta program form on Legal Robot, enabling potential UI redressing attacks to harvest user data.

## Description

In a clickjacking attack, attackers exploit sites without anti-framing headers like X-Frame-Options. This procedure targets public web forms collecting sensitive info (e.g., name, email, company) on https://www.legalrobot.com/. The root cause is AWS S3 static hosting limitations, which prevent custom headers, compounded by CloudFlare's lack of support at the time. Expected outcome: Confirmation of vulnerability for PoC development.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Internet access to the target site
3. Basic knowledge of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header
- Use Content-Security-Policy: frame-ancestors 'none'
- Monitor for unusual iframe embeddings via web application firewall (WAF)

## Objectives

1. Locate unprotected forms on the target site
2. Verify absence of framing protections
3. Document the form's data collection fields

## Instructions

### Step 1: Navigate and Inspect Target Site

**Context**: Access the site and locate the vulnerable form to understand its structure and data fields.

Open https://www.legalrobot.com/ in your browser and find the beta program application form. Note fields for name, email, and company.

### Step 2: Check Security Headers

**Context**: Use developer tools to inspect responses for anti-clickjacking headers.

Press F12 to open DevTools, go to the Network tab, reload the page, and select the main request. Examine response headers for X-Frame-Options or CSP frame-ancestors. Absence confirms vulnerability.

> Expected: No X-Frame-Options header due to AWS S3 constraints.

### Step 3: Document Findings

**Context**: Record details for PoC creation.

Screenshot the form and headers, noting the URL and lack of protections.

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
- [[web-recon]]
