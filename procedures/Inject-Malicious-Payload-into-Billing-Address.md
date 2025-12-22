---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - payload-injection
  - javascript
type: procedure
tools:
  - '[[tools/Burp-Repeater]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.412Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Billing-Address

## Summary

This procedure modifies the billing[address] parameter in a captured POST request using Burp Repeater by injecting a reflected XSS payload, exploiting lack of sanitization to enable JavaScript execution upon reflection.

## Description

The WordPress checkout endpoint at /store/checkout/ reflects user input from billing[address] without proper HTML escaping, allowing attackers to close HTML tags and inject <script> elements. The payload '1 Main Streetzbn0b"><script>alert(document.cookie)</script>k8ez0' breaks out of the attribute context and executes JS to steal cookies. This targets PHP-based WordPress sites with WooCommerce or similar plugins, assuming no CSP blocks inline scripts.

## Requirements

1. Captured POST request in Burp Repeater from prior step
2. Knowledge of URL-encoding for payloads
3. Target endpoint vulnerable to reflection (testable via parameter tampering)
4. Browser for observing execution

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs with htmlspecialchars() in PHP before output
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous payloads in logs (e.g., <script> tags in billing fields)

## Objectives

1. Craft a payload that evades basic filters and reflects executable JS
2. Ensure encoding prevents request breakage
3. Prepare for execution to demonstrate cookie theft

## Instructions

### Step 1: Locate Parameter in Repeater

**Context**: Identify the billing[address] field in the request body for modification.

In Burp Repeater, switch to the request tab and scroll to the body section. Find 'billing[address]=1 Main Street' or similar.

> Expected output: Parameter highlighted and editable in the text area.

### Step 2: Insert Raw Payload

**Context**: Replace the value with the XSS payload to test reflection.

Edit the value to: 1 Main Streetzbn0b"><script>alert(document.cookie)</script>k8ez0

This closes a presumed quote in the HTML attribute (e.g., value="input") and injects the script.

> Expected output: Updated body with payload visible.

### Step 3: Apply URL-Encoding

**Context**: Encode special characters to ensure the request parses correctly on the server.

Use Burp's built-in encoder or manually replace: space=%20, ">=%22%3E, <script>=%3Cscript%3E, </script>=%3C%2Fscript%3E.

Resulting encoded payload: 1%20Main%20Streetzbn0b%22%3e%3cscript%3ealert(document.cookie)%3c%2fscript%3ek8ez0

> Expected output: Fully encoded request body ready for sending.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Repeater]]

## Tags

- xss
- payload-injection
- javascript
