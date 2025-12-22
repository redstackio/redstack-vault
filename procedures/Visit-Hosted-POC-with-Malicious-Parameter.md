---
id: proc-uuid-002
name: Visit-Hosted-POC-with-Malicious-Parameter
tags:
  - xss
  - parameter-injection
type: procedure
tools:
  - '[[tools/Local-Web-Server]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.468Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Visit-Hosted-POC-with-Malicious-Parameter

## Summary

This procedure involves accessing the hosted POC page with a URL parameter containing the JavaScript payload to exploit the XSS on www.shopify.com.

## Description

The attacker or victim visits the POC URL with an appended parameter like ?x=${alert(1)}, which encodes the payload for injection. This step prepares the environment for the click-based trigger, exploiting insufficient sanitization in Shopify's reflection mechanism. Target environment is any modern browser. Outcomes: Payload embedded and ready for execution upon interaction.

## Requirements

1. Access to the hosted POC URL
2. Browser with JavaScript support
3. Knowledge of the vulnerable parameter (e.g., 'x')

## Defense

Defensive measures and detection strategies:

- URL encoding validation and parameter whitelisting
- Browser extensions like NoScript to block inline scripts
- Logging of query parameters for anomaly detection

## Objectives

1. Inject the XSS payload via URL parameter
2. Set up for reflected execution on Shopify domain
3. Mimic victim navigation to the malicious page

## Instructions

### Step 1: Construct Malicious URL

**Context**: Append the payload to the POC URL to encode the JavaScript injection.

Use a URL like: http://localhost:8000/poc.html?x=${alert(1)}

> The ${alert(1)} will be URL-encoded if needed, but template literals allow direct injection. Verify the parameter appears in the browser's address bar.

### Step 2: Load the Page

**Context**: Navigate to the URL to load the POC with the injected parameter.

Open the constructed URL in a web browser.

> Ensure the page loads without errors. Inspect the network tab in developer tools to confirm the parameter is present.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Local-Web-Server]]

## Tags

- [[xss]]
- [[parameter-injection]]
