---
tags:
  - idor
  - authorization-bypass
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-parameter-manipulation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.336Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: f5ee1298-a5d0-4c88-912a-6a80c0e16944
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-Order-Parameter-for-Unauthorized-Access

## Summary

This procedure exploits a missing authorization check on a specific parameter in the order viewing endpoints of teavana.com and starbucks.* websites, allowing any unauthenticated user to access and view detailed order information belonging to other customers, including personal details and purchase history.

## Description

The vulnerability stems from improper implementation of access controls in the web application, where requests to retrieve order details do not verify if the requesting user owns the specified order. By manipulating a parameter such as order_id in the URL or request body, attackers can retrieve sensitive data from arbitrary orders. This was reported on HackerOne in 2016 and resulted in a bounty. The attack requires no authentication bypass beyond the absent checks and works across the affected domains. Expected outcomes include exposure of customer PII, order items, totals, and shipping addresses, potentially leading to privacy violations or further attacks like social engineering.

## Requirements

1. Public access to teavana.com or starbucks.* over HTTPS
2. Ability to craft and send HTTP GET requests (e.g., via curl or browser)
3. Knowledge of the target endpoint structure (e.g., /orders/{id})

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks to validate user ownership of requested resources
- Use session-based or token-based access controls with proper scoping to user accounts
- Monitor for anomalous access patterns, such as requests for non-owned order IDs, via web application firewalls (WAF)
- Rate-limit parameter values to prevent enumeration

## Objectives

1. Gain unauthorized read access to other users' order data
2. Exfiltrate sensitive customer information for reconnaissance or privacy breach
3. Demonstrate the vulnerability for disclosure and remediation

## Instructions

### Step 1: Identify the Vulnerable Endpoint

**Context**: Locate the order viewing functionality on the target site, typically a GET request to an endpoint like /orders/{order_id} or a similar parameter in the query string.

No specific command needed; use browser inspection or site navigation to find the endpoint.

### Step 2: Manipulate the Parameter

**Context**: Craft a request with a parameter value that corresponds to another user's order, such as incrementing or guessing an order ID from observed patterns.

**Command** ([[commands/curl-parameter-manipulation]]):
```bash
curl -X GET "https://www.teavana.com/orders/12345" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> This command sends a GET request to the orders endpoint with a manipulated order_id (e.g., 12345). Expected output is the full order details if the check is missing; look for JSON or HTML containing unauthorized data like customer name and items. If access is granted without login, the exploit succeeds.

### Step 3: Validate Unauthorized Access

**Context**: Confirm the response includes data not associated with your session or account.

Repeat the command with different IDs to enumerate multiple orders:

```bash
curl -X GET "https://www.starbucks.com/orders/67890" -H "User-Agent: Mozilla/5.0"
```

> Success is indicated by consistent access to foreign order data without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-parameter-manipulation]]

## Tools Used

- [[tools/curl]]

## Tags

- idor
- authorization-bypass
- web-exploitation
