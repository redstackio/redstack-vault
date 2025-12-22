---
tags:
  - xss
  - trigger
  - shopify
  - execution
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
updated_at: '2025-12-14T03:15:31.668Z'
sub_techniques: []
id: 8a17af6c-6f1b-4023-bf0e-aec7b6b3d25d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Clicking-Tracking-Link-in-Order-View

## Summary

This procedure triggers the stored XSS payload by viewing the affected Shopify order details and clicking the injected tracking link, executing JavaScript in the admin's browser.

## Description

After payload injection, the malicious link appears in the order's fulfillment section. Any authenticated admin loading the page and clicking it will run the JavaScript, such as alert(1) for proof-of-concept, or more advanced payloads for session theft. This exploits the lack of sanitization in link rendering.

## Requirements

1. Updated fulfillment with malicious URL from prior procedure
2. Authenticated admin session (can be victim's)
3. Access to the order details page

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered links to strip javascript: protocols
- Log and alert on suspicious link clicks in admin panel
- Train admins not to click untrusted tracking links

## Objectives

1. Execute arbitrary JavaScript in admin context
2. Demonstrate impact like session exfiltration
3. Validate stored payload persistence

## Instructions

### Step 1: Reload Order Page

**Context**: Ensure the updated fulfillment is visible.

Visit https://<store>.myshopify.com/admin/orders/<order_id> and scroll to the fulfillment section under 'Successfully processed a payment'.

> The 'TrackingNumber' link should now point to javascript:alert(1);//.

### Step 2: Interact with Link

**Context**: Trigger execution by clicking.

Click the tracking link.

> Expected output: Alert dialog with '1' appears, confirming XSS. In a real attack, replace with payload to steal document.cookie or redirect to phishing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- javascript-execution
