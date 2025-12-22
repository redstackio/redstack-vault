---
id: proc-uuid-1
tags:
  - xss
  - shopify
  - reflective-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/shopify-newsletter-xss-alert]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.647Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify Reflective XSS in Newsletter Form

## Summary

This procedure identifies a reflective XSS vulnerability in Shopify's newsletter signup form by injecting a basic JavaScript payload into the contact[email] parameter, exploiting Ruby on Rails mass assignment to break out of the input value attribute and execute code on page load.

## Description

The newsletter form on *.myshopify.com domains reflects user input from URL parameters into an HTML input tag without proper escaping. By crafting a payload with unescaped quotes, attackers can inject additional attributes like onfocus and autofocus, leading to JavaScript execution when the page loads and the input gains focus. This is ideal for drive-by attacks via shared links. Prerequisites include a target Shopify store URL and a browser for testing.

## Requirements

1. Public access to a Shopify store's newsletter form (no auth needed)
2. URL encoding knowledge for payload construction
3. Browser with developer console

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in form reflections using HTML entity encoding
- Implement Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for anomalous JavaScript fetches to internal admin paths in browser logs

## Objectives

1. Confirm XSS vulnerability presence
2. Validate attribute injection capability
3. Establish foundation for advanced exploitation

## Instructions

### Step 1: Craft and Test Basic XSS Payload

**Context**: Build a URL that injects an onfocus attribute with an alert to demonstrate execution.

**Command** ([[commands/shopify-newsletter-xss-alert]]):
```bash
https://testbuguser.myshopify.com/?contact[email]%20onfocus%3djavascript:alert(%27xss%27)%20autofocus%20a=a&form_type[a]aaa
```

> This URL uses mass assignment via form_type[a] to set the malicious attributes. On load, autofocus triggers onfocus, popping an alert. Expected output: 'xss' alert confirming vuln.

### Step 2: Verify Injection in Browser

**Context**: Load the URL and inspect for successful injection.

**Command** (Browser Navigation):
```bash
Navigate to the crafted URL in a web browser
```

> Observe the alert and use dev tools (F12) to inspect the input element. Success if attributes are present in DOM.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-newsletter-xss-alert]]

## Tools Used


## Tags

- [[xss]]
- [[shopify]]
- [[reflective-xss]]
