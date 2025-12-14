---
tags:
  - shopify
  - data-exfiltration
  - webhook-trigger
type: procedure
tools:
  - '[[tools/requestb-in]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:32:11.021Z'
sub_techniques: []
id: be6b05e3-455e-4124-ac3d-3204b5ff7658
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Trigger-and-Confirm-Webhook-Exfiltration

## Summary

This procedure creates an order event to trigger the hidden webhook and verifies delivery of sensitive data to an external endpoint, confirming persistent exfiltration.

## Description

With permissions revoked and webhook invisible, an order is created in the admin panel to fire the orders/create event. The payload, containing sensitive order details, is sent to the external URL despite the changes. This targets Shopify's Orders and Webhooks services via the admin UI and external receiver. Outcomes include receipt of JSON data, proving the backdoor's effectiveness.

## Requirements

1. Shopify admin access to create orders
2. Active external endpoint (e.g., requestb.in)
3. Hidden webhook from prior steps

## Defense

Defensive measures and detection strategies:

- Disable or review all webhooks regularly, especially API-created ones not visible in UI
- Monitor external traffic from Shopify IPs to unexpected domains
- Implement payload inspection and alerting for webhook deliveries post-permission changes
- Use SIEM to correlate order creations with outbound API calls

## Objectives

1. Generate an order creation event
2. Receive and inspect exfiltrated data
3. Confirm persistence and undetectability

## Instructions

### Step 1: Create Test Order

**Context**: Use the admin UI to trigger the webhook event.

**Instructions**: Navigate to Orders > Create order, fill in details (e.g., test customer, product), and save.

> Order is created, triggering the invisible webhook.

### Step 2: Check External Endpoint

**Context**: Verify the payload arrival at the receiver.

**Instructions**: Refresh the requestb.in page to view incoming POST requests.

> Expected: JSON payload with order data, including sensitive info like customer details and items.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/requestb-in]]

## Tags

- shopify
- data-exfiltration
- webhook-trigger
