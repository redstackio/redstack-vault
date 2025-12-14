---
id: proc-uuid-1
tags:
  - xss
  - recon
  - shopify
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:16:07.961Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Parameter in Shopify Cart Endpoint

## Summary

This procedure involves inspecting the Shopify cart addition endpoint to identify the properties[builder_id] parameter, which accepts array inputs without validation, setting the stage for XSS injection via nested arrays.

## Description

In a Shopify-hosted site, the /cart/add endpoint processes product additions with custom properties. The properties[builder_id] parameter can be manipulated as an array, and improper backend handling leads to unescaped JSON output in cart.js, enabling attribute injection. This is exploitable on public-facing e-commerce sites without authentication, affecting all users who view the cart.

## Requirements

1. Access to a Shopify site (e.g., *.shopify.com)
2. Browser with developer tools or web proxy (e.g., Burp Suite)
3. Basic understanding of HTTP parameters and JSON parsing

## Defense

Defensive measures and detection strategies:

- Input validation: Sanitize and escape array parameters before JSON serialization
- Content Security Policy (CSP) to block inline JS execution
- Monitor for anomalous parameter nesting in logs

## Objectives

1. Confirm vulnerability in properties[builder_id] handling
2. Understand output reflection in cart.js
3. Prepare for payload crafting

## Instructions

### Step 1: Inspect Endpoint

**Context**: Use dev tools to examine the /cart/add request structure and test basic array inputs.

Navigate to a product page and monitor the network tab while adding to cart. Look for properties[builder_id] in the query string.

### Step 2: Test Array Input

**Context**: Send a simple array to verify acceptance and observe backend output.

Modify the request to include properties[builder_id][]=test&properties[builder_id][]=nested. Check the response or cart.js for unescaped echoes.

**Expected Output**: JSON-like string in cart.js showing raw array data without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[recon]]
