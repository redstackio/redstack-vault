---
id: proc-uuid-4
tags:
  - xss
  - exploitation
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:07.946Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS via Victim Interaction

## Summary

This procedure delivers the malicious URL to a victim, triggering the stored XSS payload execution when they interact with the carted product, such as on mouseover.

## Description

Once the victim visits the URL, the payload adds to their cart and persists in cart.js. Viewing the cart injects the attributes, executing JS like alert(document.cookie) on hover, allowing cookie theft or keylogging without authentication.

## Requirements

1. Malicious URL from prior procedure
2. Social engineering vector (e.g., email link)
3. Victim access to the Shopify site

## Defense

Defensive measures and detection strategies:

- JS sandboxing and event handler restrictions
- User education on suspicious links
- Anomaly detection in cart interactions

## Objectives

1. Infect victim's cart
2. Execute arbitrary JS
3. Exfiltrate sensitive data

## Instructions

### Step 1: Deliver URL

**Context**: Share the URL via phishing or direct link.

Send: http://hardware.shopify.com/cart/add?id=1106494145&... (full malicious URL).

### Step 2: Observe Execution

**Context**: Victim visits, adds to cart, then views cart and hovers over product.

Monitor for JS alert or network requests indicating theft.

**Expected Output**: JS execution, e.g., alert popup with cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[exploitation]]
