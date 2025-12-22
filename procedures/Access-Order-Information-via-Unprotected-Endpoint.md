---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - broken-access-control
  - information-disclosure
  - api
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-get-orders]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:30:17.906Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
---
---

# Access-Order-Information-via-Unprotected-Endpoint

## Summary

This procedure exploits a web API endpoint lacking proper access controls to retrieve sensitive order information for unauthorized users, resulting in critical information disclosure.

## Description

In the context of an e-commerce application like Azbuka Vkusa, an unprotected API endpoint (e.g., /api/v1/orders/{id}) allows any unauthenticated request to access order details, including customer PII, purchased items, and payment information. This bypasses authorization checks, enabling attackers to enumerate and exfiltrate data by varying order IDs. The attack requires only network access to the application and knowledge of the endpoint path, discovered through testing or API exploration.

## Requirements

1. Network access to the target web application domain.
2. Knowledge of the API endpoint URL (e.g., via app testing or documentation leaks).
3. Order ID to target (can be guessed sequentially or enumerated from public sources).
4. Tool like curl for HTTP requests.

## Defense

Defensive measures and detection strategies:

- Implement proper authentication (e.g., JWT tokens) and authorization (e.g., role-based checks) on all API endpoints.
- Use rate limiting and input validation to prevent ID enumeration.
- Monitor API logs for anomalous access patterns, such as high-volume GET requests from single IPs.
- Employ WAF rules to block unauthenticated sensitive endpoint access.

## Objectives

1. Retrieve unauthorized order details to expose customer privacy.
2. Demonstrate the impact of broken access control.
3. Collect data for further attacks like social engineering.

## Instructions

### Step 1: Prepare the Request

**Context**: Identify the target endpoint and order ID. Assume /api/v1/orders/12345 as the vulnerable path.

**Command** ([[commands/curl-get-orders]]):
```bash
curl -X GET "https://target-app.com/api/v1/orders/12345" -H "Content-Type: application/json" -v
```

> This command sends a GET request to fetch the order. The -v flag provides verbose output for debugging. Expected output includes JSON with fields like user_id, items, address, and status. If successful, no auth errors occur.

### Step 2: Parse and Exfiltrate Data

**Context**: Review the response for sensitive data and save it for analysis.

**Command** ([[commands/curl-get-orders]]):
```bash
curl -X GET "https://target-app.com/api/v1/orders/12345" -H "Content-Type: application/json" | jq '.' > order_data.json
```

> Pipe the output to jq for pretty-printing and save to file. Success looks like a JSON object with disclosed PII.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-orders]]

## Tools Used


## Tags

- [[broken-access-control]]
- [[information-disclosure]]
- [[api]]

---
