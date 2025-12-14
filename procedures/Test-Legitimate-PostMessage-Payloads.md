---
id: proc-test-postmessage
tags:
  - testing
  - postmessage
  - payload-validation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/send-basic-postmessage]]'
  - '[[commands/send-lineitems-postmessage]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.425Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Legitimate-PostMessage-Payloads

## Summary

This procedure tests the functionality of the postMessage listener in Shopify's digital wallets dialog by sending valid payloads to confirm DOM rendering without triggering errors, establishing a baseline for exploitation.

## Description

From the browser console on a page that can communicate with the target iframe, send structured messages mimicking legitimate dialog changes. Observe how title, button, and lineItems are processed and inserted, verifying the path to vulnerable DOM updates.

## Requirements

1. Loaded iframe or direct access to /:id/digital_wallets/dialog
2. Browser console access
3. Target Shopify domain reachable

## Defense

Defensive measures and detection strategies:

- Log all postMessage events for anomaly detection.
- Validate payload structure strictly beyond basic fields.
- Use sandboxed iframes to isolate dialog.

## Objectives

1. Confirm payload acceptance and DOM updates.
2. Verify lineItems rendering as table rows.
3. Ensure no premature errors block exploitation path.

## Instructions

### Step 1: Send Basic Dialog Change

**Context**: Test minimal payload for title and button to validate handler.

**Command** ([[commands/send-basic-postmessage]]):
```javascript
window.postMessage({type:"DigitalWalletsDialog:change",digitalWalletsDialog:true,payload:{title:"placeholder",button:"placeholder"}},"*");
```

> Renders dialog with placeholders; check DOM for innerHTML updates.

### Step 2: Test LineItems Rendering

**Context**: Include array of lineItems to trigger table creation and row insertion.

**Command** ([[commands/send-lineitems-postmessage]]):
```javascript
window.postMessage({ type: "DigitalWalletsDialog:change", digitalWalletsDialog: true, payload: { title: "placeholder", button: "placeholder", lineItems: [{name: "product",amount: "$13.37",message: "added to cart" }], },}, "*");
```

> Creates product table; inspect for unescaped insertions in rows.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/send-basic-postmessage]]
- [[commands/send-lineitems-postmessage]]

## Tools Used


## Tags

- testing
- postmessage
