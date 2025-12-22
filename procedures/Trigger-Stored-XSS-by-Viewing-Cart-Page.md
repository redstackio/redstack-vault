---
id: proc-trigger-stored-xss-001
tags:
  - xss
  - execution
  - client-side
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.368Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Cart-Page

## Summary

This procedure loads the cart page after payload injection, causing the stored JavaScript to execute in the viewer's browser, demonstrating the XSS impact.

## Description

Once injected, the payload in properties[Artwork file] is rendered on pages like /cart without escaping, executing as javascript:alert(document.domain). This runs in the site's context (e.g., hardware.shopify.com), allowing arbitrary JS like cookie theft. Affects any user viewing the cart, including admins or customers across shops. No additional tools needed beyond a browser.

## Requirements

1. Prior successful injection (Step 2 of chain)
2. Browser access to the cart page
3. Victim context (e.g., logged-in user)

## Defense

Defensive measures and detection strategies:

- Output encoding for all user-controlled data in templates (e.g., htmlspecialchars)
- Implement strict CSP to block unsafe-inline scripts
- Scan stored data for XSS patterns before rendering

## Objectives

1. Execute the stored payload
2. Verify domain context and alert
3. Assess potential for data exfiltration

## Instructions

### Step 1: Navigate to Cart Page

**Context**: Load the page that renders the stored properties.

Visit http://hardware.shopify.com/cart in the target browser.

> The payload executes on load. Expected output: Alert box with "hardware.shopify.com".

### Step 2: Inspect Execution

**Context**: Confirm via console.

Open DevTools Console; look for alert or errors.

> Success: JS runs without blocks, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
