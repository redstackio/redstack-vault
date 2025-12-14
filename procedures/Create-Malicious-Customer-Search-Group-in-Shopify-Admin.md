---
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
updated_at: '2025-12-14T03:15:31.967Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f28ed983-a946-4eb3-a204-01756d6fb708
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Customer-Search-Group-in-Shopify-Admin

## Summary

This procedure injects a malicious JavaScript payload into a customer search group name in Shopify's admin interface, exploiting the lack of input validation to prepare for later reflection and execution.

## Description

In Shopify's Myshopify Admin Site, the customer search functionality allows saving filtered searches as named groups. User input in the group name is not sanitized, enabling XSS payloads to be stored. This step sets up the payload for reflection in the discounts creation form. The attack requires authenticated admin access and targets the web-based admin panel. Successful injection leads to stored payload availability for subsequent steps, ultimately allowing JavaScript execution in the admin's browser context for potential session hijacking or data exfiltration.

## Requirements

1. Authenticated access to Shopify admin dashboard (myshopify.com/admin).
2. Web browser for navigation and payload crafting.
3. Basic knowledge of XSS payloads (e.g., img onerror).

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization and HTML escaping for all user-controlled fields, including group names.
- Use Content Security Policy (CSP) to restrict inline script execution in the admin interface.
- Monitor for anomalous JavaScript execution or unexpected prompts in admin sessions.

## Objectives

1. Store an XSS payload in a customer group name without triggering immediate execution.
2. Verify the payload is saved and retrievable.
3. Prepare for reflection in discount-related interfaces.

## Instructions

### Step 1: Access Customers Section

**Context**: Log in and navigate to the customers area to initiate a search filter.

No command required; use the web UI:

- Log in to the Shopify admin.
- Click on "Customers" in the left sidebar.
- Use the search bar to filter customers (e.g., enter "XSS" to create a minimal filter).

> This sets up a savable search without affecting real data.

### Step 2: Save Search as Malicious Group

**Context**: Apply the filter and save it with the payload in the name.

No command required; UI action:

- Click "Save this search" button.
- In the "Save search as" field, enter payload: `'><img src=x onerror=prompt(7)>`.
- Click "Save".

> The payload is stored as the group name. Expected output: Group appears in the saved searches list with the full payload visible.

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
- [[shopify]]
- [[admin]]
