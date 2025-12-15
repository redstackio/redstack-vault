---
id: proc-shopify-reuse-on-storefront
tags:
  - shopify
  - storefront-bypass
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:56.844Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reuse-Token-on-Regular-Storefront-URLs

## Summary

This procedure extends the token reuse to non-preview paths on the target store, such as collections or products, fully disclosing protected content.

## Description

The vulnerability allows ?_bt= tokens to bypass auth on any storefront URL, not just previews. This targets myshopify.com paths like /collections/all. Prerequisites: Valid token and bypassed preview access. Outcome: Comprehensive unauthorized browsing of store data.

## Requirements

1. Working token from previous bypass
2. Knowledge of target store's domain (e.g., yourshop.myshopify.com)
3. Paths to test (e.g., /collections/all)

## Defense

Defensive measures and detection strategies:

- Apply token validation to all storefront endpoints
- Log and block anomalous query parameters
- Use CSRF tokens alongside previews for path protection

## Objectives

1. Apply token to arbitrary store paths
2. Confirm universal bypass
3. Expose sensitive store information

## Instructions

### Step 1: Identify Storefront Paths

**Context**: Select protected URLs to target.

Note paths like /collections/all or /products/example.

> Expected output: List of paths that normally require password.

### Step 2: Construct Modified URLs

**Context**: Add token to base domain paths.

Form URLs like https://yourshop.myshopify.com/collections/all?_bt=<token>.

> Expected output: Ready-to-load modified paths.

### Step 3: Access and Verify

**Context**: Execute the bypass on paths.

Load each URL and inspect content.

> Expected output: Direct access to collections/products without auth; data disclosed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[storefront-bypass]]
- [[information-disclosure]]
