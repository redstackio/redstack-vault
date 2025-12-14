---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Craft Malicious URL for DOM XSS
tags:
  - xss
  - dom-xss
  - url-crafting
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:26.016Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Malicious URL for DOM XSS

## Summary

This procedure involves constructing a malicious URL with a javascript: scheme embedded in the hash fragment to exploit a DOM-based XSS vulnerability where the hash is unsanitized and used to set an iframe's location.

## Description

In this attack scenario, the target is a web page (e.g., https://www.exampleframe.html) with client-side JavaScript that extracts document.location.hash and sets it directly as the iframe's src without validation. By crafting a URL like https://www.exampleframe.html#javascript:alert(document.domain), an attacker can trick a victim into loading the page, resulting in immediate JS execution. This is effective for phishing campaigns or direct link sharing, leading to outcomes like session token theft or keylogging in the victim's browser context. Prerequisites include knowledge of the vulnerable endpoint and a web browser for testing.

## Requirements

1. Access to a web browser for URL construction and testing
2. Knowledge of the target page URL (e.g., https://www.exampleframe.html)
3. Understanding of JavaScript URIs and hash fragments

## Defense

Defensive measures and detection strategies:

- Sanitize URL hashes before setting DOM elements like iframe src (e.g., validate against allowed schemes)
- Use Content Security Policy (CSP) to restrict script execution from data: or javascript: sources
- Monitor for anomalous JS alerts or network requests from client-side scripts

## Objectives

1. Create a functional malicious URL exploiting the hash-based DOM XSS
2. Test the payload locally before deployment
3. Enable arbitrary JS execution for further attacks like data theft

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate the target page where the iframe src is set from the URL hash without sanitization.

No command required; manually note the base URL, such as https://www.exampleframe.html.

> Expected: Confirmed vulnerable page URL.

### Step 2: Construct Payload URL

**Context**: Append a javascript: payload to the hash to inject executable code.

Manually craft the URL: https://www.exampleframe.html#javascript:alert(document.domain)

> This payload will execute alert(document.domain) when the hash is processed. For more advanced payloads, replace with code to steal cookies, e.g., #javascript:fetch('/steal?cookie='+document.cookie).

### Step 3: Test in Browser

**Context**: Load the URL in a browser to verify execution.

Open the crafted URL in a browser console or directly.

> Expected: Alert box displays the document domain, confirming XSS.

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
- [[dom-xss]]
