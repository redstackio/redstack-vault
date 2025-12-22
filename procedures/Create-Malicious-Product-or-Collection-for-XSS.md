---
id: procedure-create-malicious-product-xss
tags:
  - xss
  - injection
  - shopify
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.250Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Product-or-Collection-for-XSS

## Summary

This procedure involves injecting a malicious JavaScript payload into a Shopify product name or collection title, setting up the conditions for reflected XSS in downstream applications like the Bulk Discount App.

## Description

In the context of Shopify stores, product and collection names are user-controlled fields that are stored and later retrieved for display in app interfaces. By injecting an HTML-breaking payload, attackers can escape any quoting and inject executable JavaScript. This step requires admin access to the store and targets the myshopify.com platform. Expected outcome is the payload being persisted without sanitization, ready for reflection.

## Requirements

1. Valid Shopify store owner credentials with admin privileges.
2. Access to the Shopify admin dashboard via web browser.
3. Target store on myshopify.com domain.

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization for product/collection names using libraries like DOMPurify.
- Monitor for unusual characters or script tags in admin-submitted data via logging and anomaly detection.
- Use Content Security Policy (CSP) to restrict inline script execution on app domains.

## Objectives

1. Persist a malicious payload in store data for later reflection.
2. Validate that no immediate sanitization blocks the injection.
3. Prepare for XSS triggering in integrated apps.

## Instructions

### Step 1: Log In and Navigate to Products/Collections

**Context**: Gain access to the admin panel and locate the input fields for user-controlled data.

Log in to the Shopify admin at yourstore.myshopify.com/admin. Navigate to "Products" or "Collections" in the left sidebar.

> This loads the creation interface where names/titles can be edited.

### Step 2: Inject and Save Payload

**Context**: Enter the payload to break HTML context and execute JS on reflection.

Create a new product or collection, and in the "Name" or "Title" field, enter: `'><img src=x onerror=prompt(document.domain)>`. Save the entry.

> The payload closes any open tag, adds a faulty image, and triggers a prompt on error, revealing the domain for proof-of-concept.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[shopify]]
