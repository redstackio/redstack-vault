---
tags:
  - xss
  - payload-creation
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f894fea9-13d7-400b-9bad-66db58a3cf67
created_at: '2025-12-14T17:28:45.057Z'
updated_at: '2025-12-14T17:28:45.057Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Product-Collection-for-XSS

## Summary

This procedure creates a product collection in Shopify's admin with a malicious name containing an XSS payload, setting up the vector for later reflection in the TAX Overrides UI.

## Description

In the context of exploiting a reflected XSS in Shopify's myshopify.com admin, this step involves crafting a collection name that includes JavaScript to break out of HTML attributes. The payload `'><IMG SRC=x onerror=prompt(7)>` is used, which closes any enclosing tags and injects an image element that executes on error. This requires authenticated admin access and targets the Products > Collections section. Expected outcome is a persisted collection ready for assignment, with no immediate execution.

## Requirements

1. Authenticated access to Shopify admin dashboard
2. Web browser for UI navigation
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization for collection names
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous collection names via admin audit logs

## Objectives

1. Embed XSS payload in a persistent shop entity
2. Prepare for reflection in tax override UI
3. Achieve client-side execution without direct input

## Instructions

### Step 1: Access Collections Management

**Context**: Log in and navigate to the collections area to create a new entry.

Navigate to Products > Collections in the Shopify admin. Click 'Create collection'.

### Step 2: Inject Malicious Payload

**Context**: Enter the payload in the name field to ensure it persists and reflects later.

In the 'Collection name' field, input: `'><IMG SRC=x onerror=prompt(7)>`. Optionally, add a description or image, then click 'Save'.

> This payload closes any HTML attribute (e.g., title="...") and injects an <IMG> tag that triggers JS on load error, displaying a prompt box upon execution.

### Step 3: Verify Creation

**Context**: Confirm the collection is listed with the payload intact.

Return to the collections list; the new entry should display the full malicious name without truncation or sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[shopify]]
- [[payload-injection]]
