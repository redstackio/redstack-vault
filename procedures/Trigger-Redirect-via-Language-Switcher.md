---
id: proc-trigger-redirect-language-52035
tags:
  - open-redirect
  - phishing
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
updated_at: '2025-12-14T17:24:30.674Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger Redirect via Language Switcher

## Summary

This procedure exploits the language change feature on a page loaded via a malformed URL to force an open redirect to an external domain, creating a phishing vector.

## Description

After accessing a double-slash URL, the language switcher fails to strip excess slashes, causing the redirect URL to incorporate the external domain (e.g., from `//example.com`). This allows attackers to craft links that appear to come from HackerOne but redirect users to malicious sites. The vulnerability stems from combined issues in URL parsing and redirect logic in the application.

## Requirements

1. Page loaded from a malformed URL (prior procedure)
2. Web browser session active on the target site
3. Access to the language switcher UI element

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs and URL parameters in redirect endpoints, using libraries like URL.parse() to normalize paths.
- Enforce HTTPS-only redirects and domain whitelisting in language features.
- Log and alert on redirects to external domains, integrating with SIEM for anomaly detection.

## Objectives

1. Activate the language change to trigger the vulnerable redirect.
2. Redirect the user to an attacker-controlled external site.
3. Demonstrate potential for phishing by mimicking trusted navigation.

## Instructions

### Step 1: Locate the Language Switcher

**Context**: Identify the UI element for language selection on the right side of the page.

Scroll down or to the right in the browser to find the language dropdown.

> Ensure the page is loaded from the malformed URL; the switcher should be visible and functional.

### Step 2: Select a Different Language

**Context**: Change the language to invoke the redirect logic, which uses the manipulated path.

Click the dropdown and select a language like English.

> This submits a request that constructs a redirect URL incorporating the external domain, e.g., `http://example.com/`.

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
- language-switcher
- phishing
