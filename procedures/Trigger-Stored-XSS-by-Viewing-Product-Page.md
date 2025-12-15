---
id: proc-uuid-3
tags:
  - xss
  - execution
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
updated_at: '2025-12-14T17:25:53.002Z'
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
# Trigger-Stored-XSS-by-Viewing-Product-Page

## Summary

This procedure triggers the stored XSS by accessing the product page on the Handshake internal site, causing the malicious script to execute in the viewer's browser after a short delay.

## Description

Once published, the product description is rendered on `handshake-web-internal.shopifycloud.com/products/[ID]`. The lack of output encoding allows the injected `<img>` tag to load and fire the onerror event, executing JavaScript on the shared domain, potentially compromising sessions of authenticated users.

## Requirements

1. Published product with XSS payload in Handshake
2. Browser access to the internal Handshake site
3. Victim or tester viewing the page (e.g., admin or buyer)

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., escape HTML) when rendering product descriptions
- Implement strict CSP to prevent script execution from user content
- Monitor browser consoles and error logs for unexpected JS errors or prompts

## Objectives

1. Render the page to load and execute the stored payload
2. Demonstrate arbitrary JS execution (e.g., domain prompt)
3. Highlight potential for session theft or data exfiltration

## Instructions

### Step 1: Obtain Product URL

**Context**: Identify the exact URL for the published product on the Handshake site.

After publishing, note the product ID from the Handshake portal (e.g., [ID] = 12345).

### Step 2: Navigate to Product Page

**Context**: Visit the page in a browser to trigger rendering of the description.

Open `https://handshake-web-internal.shopifycloud.com/products/[ID]` (replace [ID] with the actual ID).

### Step 3: Observe Execution

**Context**: Wait for the delayed script execution and verify impact.

After ~3 seconds, a prompt should appear showing `handshake-web-internal.shopifycloud.com`. Inspect the page source to confirm the payload rendered as HTML.

> Success confirms XSS; extend payload for real attacks (e.g., cookie theft via `document.cookie`).

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
- [[Execution]]
- [[JavaScript]]
