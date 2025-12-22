---
tags:
  - xss
  - execution
  - shopify
  - handshake
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
updated_at: '2025-12-14T03:16:25.593Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d01a5c3d-7aff-4aca-8267-90901762a76c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Product-Page

## Summary

This procedure triggers the stored XSS by accessing the product page on the internal Handshake website, causing the malicious script to execute due to improper rendering of the description.

## Description

Once published, the product page at handshake-web-internal.shopifycloud.com/products/[ID] loads the description without adequate HTML escaping. The injected <img> tag's onerror event fires after a short delay (approximately 3 seconds), executing JavaScript like prompting the document domain. This results in arbitrary code execution on a shared domain, potentially allowing session cookie theft, user impersonation, or content manipulation for any viewer.

## Requirements

1. Published product ID from Handshake
2. Access to the internal Handshake site (or ability to share the URL)
3. Victim or self to view the page

## Defense

Defensive measures and detection strategies:

- Escape HTML entities in all rendered user content
- Use sandboxed iframes for third-party content
- Monitor for unexpected JavaScript alerts or network requests from product pages

## Objectives

1. Render the unsanitized description to execute the payload
2. Achieve JavaScript execution on the shared domain
3. Demonstrate impact like domain disclosure or further exploitation

## Instructions

### Step 1: Obtain Product URL

**Context**: Identify the direct link to the published product page.

Retrieve the product ID from the Handshake portal and construct the URL: handshake-web-internal.shopifycloud.com/products/[ID].

### Step 2: Access the Product Page

**Context**: Load the page to trigger rendering of the description.

Open the URL in a web browser authenticated to the Handshake domain.

### Step 3: Observe Execution

**Context**: Wait for the payload to activate.

Allow ~3 seconds for the page to fully load; the onerror handler should execute the prompt.

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
- trigger
- execution
