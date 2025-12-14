---
id: 123e4567-e89b-12d3-a456-426614174001
name: Create-Malicious-Customer-Search-Group
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.715Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - stored-xss
  - shopify
platforms:
  - Web
commands: []
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Create-Malicious-Customer-Search-Group

## Summary

This procedure injects a malicious JavaScript payload into a customer search group name in Shopify's admin interface, storing it for later exploitation in a stored XSS attack.

## Description

In the context of Shopify's Myshopify Admin Site, customer search groups allow admins to save filters for reuse. Due to insufficient input sanitization, a payload like `"><img src=x onerror=prompt(7)` can be injected into the group name. This payload is stored in the backend and remains dormant until reflected in another context, such as discount creation. Prerequisites include authenticated admin access to the dashboard. Expected outcome is successful storage without immediate execution, setting up for payload trigger.

## Requirements

1. Authenticated access to Shopify admin dashboard
2. Web browser for navigation and payload input
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all user-controlled fields, including group names
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript prompts or errors in admin logs

## Objectives

1. Store malicious payload in customer group without detection
2. Prepare for reflection in subsequent admin actions
3. Enable arbitrary JS execution in admin context

## Instructions

### Step 1: Navigate to Customer Filters

**Context**: Access the customer management section to create a saved search.

Log in to the Shopify admin and go to Customers > Filter Customers. Enter a search term like 'XSS' to populate the filter interface.

### Step 2: Save Search with Malicious Name

**Context**: Inject the payload during group naming to store it unsanitized.

Click 'Save this search'. In the name field, enter `"><img src=x onerror=prompt(7)`. Click Save.

> The payload closes any open HTML tags and injects an image with an onerror handler that executes prompt(7) when triggered.

### Step 3: Verify Storage

**Context**: Confirm the group is saved with the payload intact.

Check the saved searches list; the group name should display the payload text without executing.

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
- [[stored-xss]]
- [[shopify]]
