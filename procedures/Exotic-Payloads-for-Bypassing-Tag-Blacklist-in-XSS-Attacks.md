---
id: 3f1ac115-238c-4245-9f82-2303f586a097
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.342130+00:00'
updated_at: '2023-04-10T20:21:51.600397+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Bypass-tag-blacklist]]'
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/Filter-Bypass-and-exotic-payloads]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Exotic-Payloads-for-Bypassing-Tag-Blacklist-in-XSS-Attacks

## Summary

This procedure demonstrates how to craft and inject exotic payloads to bypass tag blacklist filters in Cross-Site Scripting (XSS) attacks, allowing execution of malicious JavaScript in a victim's browser despite filtering mechanisms that block standard <script> tags.

## Description

Exotic payloads exploit weaknesses in web application filters that blacklist specific HTML tags like <script> but fail to account for malformed, nested, or alternative tag structures. By using incomplete or non-standard tags, attackers can evade detection and inject JavaScript code, such as alerts or data exfiltration scripts. This technique is particularly effective against reflected or stored XSS vulnerabilities in web applications with incomplete input sanitization. The target environment is typically client-side browsers interacting with vulnerable web pages. Successful execution leads to arbitrary code running in the victim's session context, enabling session hijacking, credential theft, or further exploitation.

## Requirements

1. Identification of a reflected or stored XSS vulnerability in a web application.
2. Knowledge of the application's filter rules, such as blacklisted tags (e.g., <script>).
3. Access to a testing tool like a browser developer console or proxy for injection (e.g., Burp Suite).
4. A target URL or input field where user input is reflected without proper encoding.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding using libraries like OWASP ESAPI or DOMPurify to neutralize script tags and attributes.
- Deploy a Content Security Policy (CSP) with strict script-src directives to block inline and unevaluated JavaScript execution.
- Use Web Application Firewalls (WAFs) trained on common XSS bypass patterns, including exotic payloads.
- Conduct regular security testing with tools like XSS auditors and educate developers on secure coding practices to identify and avoid phishing vectors leading to XSS.

## Objectives

1. Bypass tag blacklist filters to inject and execute JavaScript in the victim's browser.
2. Demonstrate payload execution by triggering an alert or similar visible effect.
3. Steal sensitive information, such as cookies or form data, from the victim's session.

## Instructions

### Step 1: Identify the XSS Vulnerability and Filter Rules

**Context**: Determine the input point (e.g., search field, comment form) where user input is reflected back without encoding, and test basic payloads to confirm the blacklist (e.g., <script>alert('XSS')</script> is blocked).

Use browser developer tools or a proxy to inspect reflected input and note blocked patterns.

### Step 2: Craft the Exotic Payload

**Context**: Create a payload using malformed tags that avoid the blacklisted <script> while still triggering JavaScript execution, such as incomplete or nested structures.

Reference the exotic payload code: [[codes/XSS-Tag-Blacklist-Bypass-Payload]]

This payload uses <script x> and <script y> to create an unbalanced structure that may slip past simplistic filters.

### Step 3: Inject the Payload

**Context**: Submit the crafted payload into the vulnerable input field to test execution in the victim's browser context.

Manually enter or use a tool to inject the payload into the target field (e.g., via URL parameter or form submission). For example, in a reflected XSS: https://vulnerable-site.com/search?q=<script+x>alert('XSS')<script+y>

Observe if the alert triggers without filter intervention.

### Step 4: Verify Execution and Escalate

**Context**: Confirm the payload executes by checking for the alert or console output, then modify for real attacks like document.cookie exfiltration.

If successful, replace alert('XSS') with malicious code, such as sending data to an attacker-controlled server via XMLHttpRequest.

Expected outcome: JavaScript runs, confirming bypass.
