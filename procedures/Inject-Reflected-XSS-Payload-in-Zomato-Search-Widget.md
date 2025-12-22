---
id: proc-uuid-123
tags:
  - xss
  - reflected-xss
  - javascript
  - web
  - php
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.607Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Reflected-XSS-Payload-in-Zomato-Search-Widget

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in Zomato's res_search_widget API by injecting a crafted payload into the restaurant search input field, leading to arbitrary JavaScript execution in the victim's browser and bypassing the Same-Origin Policy (SOP).

## Description

The Zomato restaurant search widget at https://www.zomato.com/widgets/res_search_widget.php reflects user input from the search field without adequate sanitization or output encoding. By injecting a payload that evades filters using quote characters, HTML comments, and script tags, attackers can execute JavaScript code. This allows for client-side attacks such as alerting the document domain to prove execution, stealing cookies, session hijacking, or phishing. The vulnerability was identified by adapting payloads from similar reports and testing directly on the widget page.

## Requirements

1. Web browser access to the internet
2. No authentication required; public-facing endpoint
3. Basic knowledge of XSS payloads and browser developer tools for verification

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization on all user inputs, especially reflected fields
- Use Content Security Policy (CSP) headers to restrict script execution
- Encode output properly (e.g., HTML entity encoding) before rendering user input
- Monitor for anomalous JavaScript execution or unexpected alerts in browser logs
- Employ Web Application Firewall (WAF) rules to detect common XSS payloads

## Objectives

1. Execute arbitrary JavaScript in the context of the Zomato domain
2. Bypass SOP to access domain-specific data like cookies
3. Demonstrate potential for broader client-side exploitation

## Instructions

### Step 1: Prepare the Payload

**Context**: Craft a payload that closes any existing HTML attributes or tags and injects a script tag to execute JavaScript. The payload `'-->">'>'"<script>prompt(document.domain)</script>;' f0r=TRUE` uses comment closure (`-->`), quote evasion (`">'>'"`), and a benign alert to test execution without harm.

No command required; manually construct in a text editor or directly in the browser.

### Step 2: Inject and Submit the Payload

**Context**: Locate the search input field on the widget page and submit the payload to trigger reflection and execution.

Navigate to https://www.zomato.com/widgets/res_search_widget.php, enter the payload into the search input, and submit the form.

> Upon submission, the input reflects back into the page, executing the script and displaying an alert with the document.domain, confirming the vulnerability.

### Step 3: Verify Execution

**Context**: Confirm the XSS by observing the alert and inspecting the page source for reflected payload.

Use browser developer tools (F12) to check the network response or DOM for the injected script.

**Expected Output**: Alert box with domain name; page source shows unsanitized input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- reflected-xss
- javascript
- web
- php
