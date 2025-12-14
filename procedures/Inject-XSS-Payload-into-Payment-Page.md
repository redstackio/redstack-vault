---
id: proc-starbucks-xss-inject
tags:
  - xss
  - payload-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:21.133Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Payment-Page

## Summary

This procedure crafts and delivers a URL-encoded XSS payload to the /shop/paymentmethod endpoint, reflecting it into the canonical link tag to inject malicious attributes like onclick handlers, bypassing WAF filters.

## Description

Query parameters are reflected without encoding into the <link rel='canonical' href='...?payload'> attribute, allowing injection of id and onclick via encodings like %u0022 for quotes and / after function names to evade blacklists on 'on*' and 'document'.

## Requirements

1. Authenticated session with basket item.
2. Firefox for decoding.
3. Crafted payload: ?==%u0022a%20onclick=confirm(/-/g+this.ownerDocument.domain)%20id=%u0022checkoutButton

## Defense

Defensive measures and detection strategies:

- Encode all user input in HTML attributes.
- Deploy WAF rules for encoded payloads and attribute injections.

## Objectives

1. Reflect payload in canonical link.
2. Inject executable attributes.
3. Bypass WAF.

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the URL with encoded payload.

Payload example: https://www.starbucks.co.uk/shop/paymentmethod?==%u0022a%20onclick=confirm(/-/g+this.ownerDocument.domain)%20id=%u0022checkoutButton

> This injects id='checkoutButton' and onclick=confirm(...) into the link.

### Step 2: Navigate to URL

**Context**: Load the page to trigger reflection.

In Firefox, enter the full URL.

> Expected output: Page source shows injected attributes in <link> tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[payload-injection]]
