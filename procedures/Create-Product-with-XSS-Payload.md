---
tags:
  - xss
  - stored-xss
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: fc73d08f-714c-4af1-bea0-bde2ac199f00
created_at: '2025-12-14T03:16:19.956Z'
updated_at: '2025-12-14T03:16:19.956Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Product-with-XSS-Payload

## Summary

This procedure involves creating a Shopify product with a malicious JavaScript payload embedded in the name field, exploiting the lack of input sanitization to store XSS for later execution in the Judge.me app.

## Description

In the context of the Judge.me stored XSS vulnerability, the product name field accepts user input without proper escaping. By encoding a simple JavaScript payload using HTML entities, the attacker can store it harmlessly until it's reflected in a privileged context like the admin question editor. This step sets up the persistent storage aspect of the stored XSS attack, targeting admins who interact with questions tied to the product. Prerequisites include a Shopify account with product creation rights.

## Requirements

1. Active Shopify store account with product management permissions
2. Judge.me app installed and enabled
3. Web browser for accessing the Shopify admin

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization for all product fields using libraries like DOMPurify
- Output encode all reflected data in admin interfaces (e.g., use Shopify's Liquid templating with auto-escaping)
- Monitor for unusual product names containing script tags or event handlers via admin audits

## Objectives

1. Store a functional XSS payload in product metadata
2. Ensure the payload survives storage and retrieval
3. Prepare for reflection in Judge.me question workflows

## Instructions

### Step 1: Access Product Creation

**Context**: Log in to the Shopify admin to initiate product setup, ensuring the payload is injected only in the name.

Navigate to Products > Add product in the Shopify admin dashboard. Fill in basic details but focus on the title field.

### Step 2: Inject Payload

**Context**: Set the product title to the encoded payload to bypass any client-side checks.

Enter the following as the product title: '&#60;img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)'. This encodes '<img src=x onerror=prompt(document.domain)>'. Complete other fields minimally and save the product.

> The payload uses an image tag with an onerror event to execute JavaScript, prompting the current domain to verify execution context.

### Step 3: Verify Storage

**Context**: Confirm the product is saved without triggering the payload prematurely.

View the product in the catalog; the name should display as encoded text without execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[stored-xss]]
- [[shopify]]
