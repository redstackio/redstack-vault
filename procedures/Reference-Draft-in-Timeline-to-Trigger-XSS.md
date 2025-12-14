---
tags:
  - xss
  - execution
  - shopify
  - timeline
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 23e16d0e-7586-434d-93a7-0b63b28c02f5
created_at: '2025-12-14T03:16:25.336Z'
updated_at: '2025-12-14T03:16:25.336Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reference-Draft-in-Timeline-to-Trigger-XSS

## Summary

This procedure creates a timeline post referencing the manipulated draft order, causing the unsanitized payload to render and execute JavaScript in the browser of any admin viewing the timeline, achieving the XSS exploit.

## Description

The Draft Orders Timeline in Shopify Admin allows posts referencing orders. Without a product link, the description renders raw HTML, executing the injected script on post submission and view. Requires timeline access; impacts include session theft via payloads like stealing document.cookie. Outcomes: Payload execution confirmed by alert or network activity.

## Requirements

1. Manipulated completed draft order URL
2. Access to Draft Orders Timeline
3. Another admin account to view (for testing impact)

## Defense

Defensive measures and detection strategies:

- Enforce strict HTML escaping in timeline rendering
- Use sandboxed iframes or text-only rendering for references
- Monitor for XSS payload indicators in admin logs or browser consoles

## Objectives

1. Render unsanitized payload in timeline context
2. Execute arbitrary JavaScript cross-admin
3. Facilitate data theft or session hijacking

## Instructions

### Step 1: Access Timeline

**Context**: Navigate to the timeline feature.

UI action: Go to Orders > Draft Orders > Timeline.

> Expected: New post interface loads.

### Step 2: Create Reference Post

**Context**: Insert the draft URL to trigger rendering.

UI action: In post body, paste order URL (e.g., https://store.myshopify.com/admin/draft_orders/18344449).

> Expected: URL recognized; post preview shows raw text.

### Step 3: Submit and View

**Context**: Submit to render; view as another admin.

UI action: Click POST; have victim view timeline.

> Expected: XSS executes (e.g., alert('XSS') or prompt).

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
- [[shopify]]
- [[timeline]]
