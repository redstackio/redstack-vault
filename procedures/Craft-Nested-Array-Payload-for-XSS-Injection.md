---
id: proc-uuid-2
tags:
  - xss
  - payload-crafting
  - javascript
type: procedure
tools: []
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
updated_at: '2025-12-14T03:16:07.957Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Nested Array Payload for XSS Injection

## Summary

This procedure crafts a URL-encoded payload exploiting nested arrays in properties[builder_id] to inject HTML attributes like onmouseover, breaking JSON escaping in the backend output.

## Description

By using a malformed key like [%20onmouseover%3dalert(1)%20"], the payload creates invalid JSON such as 'builder_id":{"second_parameter ":"value"}', which injects attributes into HTML tags in cart.js. This leads to stored XSS executable on cart interaction, stealing cookies or performing other client-side attacks.

## Requirements

1. Knowledge of URL encoding
2. Target product ID from Shopify site
3. Testing environment for payload validation

## Defense

Defensive measures and detection strategies:

- Strict JSON validation before output
- Escape all user-controlled strings in HTML contexts
- WAF rules for nested parameter detection

## Objectives

1. Generate injectable attribute payload
2. Ensure compatibility with Shopify's parsing
3. Validate injection without execution

## Instructions

### Step 1: Design Payload Structure

**Context**: Create a nested array key that includes event handler attributes.

Use: properties[builder_id][%20onmouseover%3dalert(1)%20"]=value. The space (%20) and quotes break the JSON structure.

### Step 2: URL Encode and Test

**Context**: Encode the payload and append to a test URL.

Full encoded: properties[builder_id][%20onmouseover%3dalert(document.cookie)%20%22]=shapp_options_421549285_1455208671885. Inspect cart.js for attribute injection.

**Expected Output**: Malformed JSON injecting onmouseover into tags like <tr onmouseover=alert(document.cookie)>.

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
- [[payload-crafting]]
