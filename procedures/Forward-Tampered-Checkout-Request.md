---
tags:
  - request-submission
  - tamper-forward
  - checkout-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.456Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 513981b5-7854-4c29-8143-93233a614232
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forward-Tampered-Checkout-Request

## Summary

This procedure submits the modified XML payload via POST request to the server, completing the checkout with tampered prices and achieving the exploitation goal.

## Description

In Adobe's vulnerable e-commerce system, forwarding the altered request exploits the absence of validation, processing the order at manipulated prices. This final step confirms the impact, such as zero-cost purchases. Prerequisites include a successfully tampered payload. Expected outcomes are order confirmation with unauthorized discounts, demonstrating financial vulnerability.

## Requirements

1. Modified POST request ready in proxy
2. Original headers and cookies intact
3. Server endpoint accessible
4. Monitoring capability for response

## Defense

Defensive measures and detection strategies:

- Perform server-side price recalculation from database
- Log and alert on discrepancies between client-submitted and expected prices
- Use WAF rules to detect XML tampering patterns

## Objectives

1. Successfully process the tampered order
2. Verify price manipulation in the response
3. Realize financial impact through completed purchase

## Instructions

### Step 1: Prepare Request for Forwarding

**Context**: Ensure all aspects of the request (headers, body, method) are set correctly post-modification.

In the proxy tool, review the full request, including Content-Type: application/xml and session cookies.

### Step 2: Submit to Server

**Context**: Release the intercepted request to reach the server endpoint.

Click 'Forward' in Burp's Intercept tab or use Repeater to send the request.

**Expected Output**: HTTP 200 response with order confirmation, showing applied prices (e.g., total: $0.00).

### Step 3: Validate Impact

**Context**: Confirm the exploitation success by checking order details.

Inspect the response body or redirect to order summary page to verify prices were not overridden.

**Expected Output**: Order placed successfully with tampered prices.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-submission]]
- [[tamper-forward]]
- [[checkout-exploit]]
