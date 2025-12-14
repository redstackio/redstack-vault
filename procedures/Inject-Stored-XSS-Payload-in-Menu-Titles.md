---
id: proc-uuid-2
tags:
  - xss
  - stored-xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:57.147Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Menu-Titles

## Summary

This procedure involves entering a crafted XSS payload into Shopify Admin's menu title fields, which are stored persistently without escaping, allowing later execution.

## Description

Targeting the 'Title in Add menu' and 'Title in Menu Item' fields in Shopify's admin navigation section, this step exploits the lack of output encoding. The payload bypasses any basic filters and persists in the database. In a web-based Shopify environment with admin access, this leads to JavaScript execution upon rendering. Prerequisites are an active admin session from prior navigation.

## Requirements

1. Active Shopify Admin session
2. Access to menu creation/editing interface
3. Knowledge of XSS payloads that evade common sanitization

## Defense

Defensive measures and detection strategies:

- Enforce output encoding (e.g., HTML entity escaping) on all user inputs rendered in admin views
- Implement Content Security Policy (CSP) to restrict inline scripts and SVG execution

## Objectives

1. Store malicious JavaScript in menu titles
2. Ensure payload persistence without detection
3. Set up for execution in admin context

## Instructions

### Step 1: Enter Payload in Title Fields

**Context**: Craft and input the payload to close HTML tags and inject executable SVG.

In the 'Title in Add menu' field, type: `// # "><svg/onload=prompt(1)>`. Repeat for 'Title in Menu Item'.

> The input is accepted without validation errors, storing the payload.

### Step 2: Save the Menu Configuration

**Context**: Persist the changes to the backend, making the XSS stored.

Click 'Save' or 'Add menu' to commit the titles.

> Menu updates successfully, with payload now in the database.

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
- [[payload-injection]]
