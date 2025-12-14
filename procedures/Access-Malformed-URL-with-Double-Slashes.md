---
id: proc-access-malformed-url-52035
tags:
  - open-redirect
  - web-vulnerability
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
updated_at: '2025-12-14T17:24:30.678Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Malformed URL with Double Slashes

## Summary

This procedure involves crafting and accessing a URL with double slashes followed by an external domain to exploit improper path handling in the web server, setting up for subsequent redirects in features like language switchers.

## Description

In the context of the HackerOne vulnerability, navigating to URLs like `https://hackerone.com//example.com/ru/faq` causes the web server to process the request as if from the external FQDN without proper slash stripping. This loads the page but primes the environment for redirects. The attack targets public-facing web applications vulnerable to URL normalization issues, potentially leading to open redirects when combined with dynamic features.

## Requirements

1. Web browser with direct internet access
2. Knowledge of target URL structure (e.g., HackerOne paths like /ru/faq)
3. No authentication required for public pages

## Defense

Defensive measures and detection strategies:

- Implement strict URL canonicalization and slash normalization in web servers (e.g., using Nginx or Apache rewrite rules to strip excess slashes).
- Validate and sanitize all redirect parameters in application features like language switchers, ensuring only whitelisted domains are allowed.
- Monitor access logs for patterns of double-slash or malformed URLs, using WAF rules to block suspicious requests.

## Objectives

1. Load the target page with a manipulated path to bypass FQDN validation.
2. Prepare the session for triggering redirects to external sites.
3. Identify if the server responds to internal requests from spoofed domains.

## Instructions

### Step 1: Craft the Malformed URL

**Context**: Construct a URL that inserts double slashes after the domain, followed by an external domain and a valid path to ensure the page loads.

No command required; manually enter in browser address bar:

```plaintext
https://hackerone.com//example.com/ru/faq
```

> This URL loads the FAQ page but misinterprets the host due to excess slashes, allowing the server to handle it as an internal request from example.com.

### Step 2: Navigate and Load the Page

**Context**: Access the URL to confirm the page renders without errors, verifying the vulnerability setup.

Manually navigate to the crafted URL in a web browser.

> Expected: Page content from HackerOne loads, but inspect network requests to see the path manipulation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- open-redirect
- url-manipulation
