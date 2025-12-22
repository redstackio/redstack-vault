---
tags:
  - url-delivery
  - payload-injection
  - xss
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
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
id: fff94e2c-56bc-4856-8deb-fb56a63c8a21
created_at: '2025-12-13T23:55:20.680Z'
updated_at: '2025-12-13T23:55:20.680Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Visit-Malicious-Redirect-URL

## Summary

This procedure involves delivering a specially crafted URL to the victim, embedding a javascript: URI in the redirect parameter of the Semmle application to set up DOM-based XSS execution.

## Description

The Semmle application's redirect parameter lacks validation for javascript: schemes, allowing attackers to inject payloads. By having the victim visit the URL while logged out, the parameter is stored in the DOM. Upon login, it executes, running arbitrary JS like prompting the document domain for reconnaissance.

## Requirements

1. Crafted malicious URL: https://lgtm-com.pentesting.semmle.net/?redirect=javascript:prompt(document.domain)%2f%2f
2. Victim access to browser and internet
3. Delivery method (e.g., email, social engineering)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize redirect parameters to block javascript: URIs
- Use URL encoding/decoding safely and whitelist allowed schemes (http/https)
- Log and monitor suspicious redirect parameter values

## Objectives

1. Inject javascript: payload into the redirect parameter
2. Load the page without immediate execution
3. Position for login-triggered payload

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Construct the URL with the encoded javascript: payload to evade basic filters.

The payload `javascript:prompt(document.domain)//` is URL-encoded as `javascript:prompt(document.domain)%2f%2f`.

> Full URL: https://lgtm-com.pentesting.semmle.net/?redirect=javascript:prompt(document.domain)%2f%2f. Expected output: URL ready for delivery.

### Step 2: Deliver and Visit URL

**Context**: Have the victim access the URL to set the tainted parameter.

Send via phishing or direct link; victim clicks and loads the page.

> Page loads showing login prompt; inspect DOM to confirm redirect param presence if testing. Success if no errors and login option available.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[url-injection]]
