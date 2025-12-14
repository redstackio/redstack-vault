---
tags:
  - idor
  - authorization-bypass
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Manipulate-Order-Parameter-for-Unauthorized-Access]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.338Z'
description: >-
  An attack chain exploiting missing authorization checks on a parameter in
  Starbucks and Teavana web applications to access other users' sensitive order
  details.
skill_level: beginner
impact_level: high
id: 05652154-6c86-49ce-a54e-2e75fea8a165
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Parameter Manipulation for Unauthorized Access to User Orders on Starbucks and Teavana

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper authorization in web order endpoints.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Parameter Manipulation] --> B[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or [[tools/curl]]

### Target Environment

- Web platform
- Services: teavana.com, starbucks.* domains
- No specific ports required (HTTPS/80,443)

### Initial Access Requirements

- Public internet access to the target websites
- No credentials needed due to missing authorization checks
- Basic knowledge of HTTP requests

## Detailed Attack Procedures

### Step 1: Parameter Manipulation for Unauthorized Access
procedure: [[procedures/Manipulate-Order-Parameter-for-Unauthorized-Access]]

**Objective**: Exploit the lack of authorization checks on the order parameter to view sensitive details of other users' orders.

**Instructions**: Identify the order viewing endpoint on teavana.com or starbucks.* (e.g., /orders/{order_id}). Use a tool like curl to send a request with a manipulated parameter value corresponding to another user's order. For example, replace the order_id with a known or guessed value from sequential enumeration or observed traffic.

Execute [[commands/curl-parameter-manipulation]] to test access:

```bash
curl -X GET "https://www.teavana.com/orders/12345" -H "User-Agent: Mozilla/5.0"
```

If successful, the response will include unauthorized order details such as customer info, items, and payment data.

**Expected Output**: JSON or HTML response containing other users' order information, including names, addresses, and purchase history.

**Success Indicators**:
- Response contains data not belonging to the requester's account
- No authentication error or access denied message
- Sensitive details like order totals or personal info visible

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to access cross-user order data
2. Demonstrated impact on privacy across multiple domains
3. Led to vulnerability disclosure and bounty on HackerOne

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
