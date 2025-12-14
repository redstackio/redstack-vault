---
id: proc-shopify-inject-xss-001
tags:
  - xss
  - injection
  - payload
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
updated_at: '2025-12-14T03:46:37.789Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-First-Name-Field

## Summary

This procedure exploits the input validation flaw in Shopify's first name field by injecting a crafted HTML payload that includes an <html> tag with JavaScript, bypassing filters for a stored XSS.

## Description

The vulnerability stems from rejecting most HTML but allowing <html>, combined with unsanitized output in the <title> tag on the thank you page. The payload `'</title></head><html onmouseover=alert(2)>` closes the title/head and injects executable HTML/JS. This stores the payload for later execution on .myshopify.com domains.

## Requirements

1. Checkout form at customer details stage
2. Knowledge of the bypass payload
3. Web browser developer tools for testing

## Defense

Defensive measures and detection strategies:

- Sanitize all outputs, especially in <title> tags, using HTML entity encoding
- Reject or strip all HTML tags in input validation, including <html>
- Implement Content Security Policy (CSP) to block inline JS execution
- Scan for XSS payloads in logs and inputs

## Objectives

1. Bypass HTML tag filters
2. Store malicious payload in order data
3. Enable JS execution on thank you page

## Instructions

### Step 1: Locate First Name Field

**Context**: Target the vulnerable input.

Return to the first name input on the checkout form.

### Step 2: Enter Payload

**Context**: Craft and inject the bypass.

Type `'</title></head><html onmouseover=alert(2)>` into the first name field.

### Step 3: Submit Field

**Context**: Test acceptance.

Tab out or click continue; observe if the input is accepted without stripping.

**Expected Output**: Payload stored and form proceeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- payload-injection
