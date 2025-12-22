---
tags:
  - xss-execution
  - javascript
  - alert
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.405Z'
sub_techniques: []
id: 00440572-5e9c-4903-87eb-5966638cd41f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-by-Loading-URL

## Summary

This procedure loads the modified URL containing the XSS payload, causing arbitrary JavaScript to execute in the browser context on Zomato's mobile site.

## Description

By accessing the tampered URL, the unsanitized category parameter injects the payload into the page's script, leading to execution via the SVG onload attribute. This demonstrates the vulnerability's impact, such as alerting the domain, but could extend to stealing session cookies or local storage for mobile users.

## Requirements

1. Fully crafted and encoded URL
2. Active mobile user agent
3. Victim's browser environment

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all query parameters server-side
- Implement strict CSP to block inline SVG or onload handlers
- Monitor for XSS payload patterns in access logs

## Objectives

1. Execute injected JavaScript
2. Confirm vulnerability with visible alert
3. Highlight potential for broader client-side attacks

## Instructions

### Step 1: Construct Full URL

**Context**: Combine base URL with encoded payload.

Use: https://www.zomato.com/manila/artsy-cafe-diliman-quezon-city/photos?category=%22--%3E%3C%2Fscript%3E%3Csvg%2Fonload%3D%27%3Balert%28document.domain%29%3B%27%3E

### Step 2: Load and Observe

**Context**: Trigger the page load to execute the payload.

Paste the URL into the address bar and press Enter. Observe the alert dialog.

**Expected Output**: Alert box shows "www.zomato.com" or similar domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[JavaScript]]
