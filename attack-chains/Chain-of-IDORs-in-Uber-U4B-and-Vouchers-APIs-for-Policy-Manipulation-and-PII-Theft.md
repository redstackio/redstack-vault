---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - idor
  - api
  - pii
  - authorization-bypass
  - financial-impact
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Identify-Uber-API-Endpoints-for-IDOR-Testing]]'
  - '[[procedures/Exploit-IDOR-to-View-Policies-and-PII]]'
  - '[[procedures/Exploit-IDOR-to-Modify-Voucher-Policies]]'
step_count: 3
techniques:
  - '[[Account Discovery]]'
  - '[[Stored Data Manipulation]]'
updated_at: '2025-12-14T17:25:17.783Z'
description: >-
  A chain of Insecure Direct Object References (IDOR) vulnerabilities in Uber's
  Uber for Business (U4B) and Vouchers APIs enables unauthorized viewing and
  modification of voucher policies, retrieval of organization employees' PII,
  and potential financial exploitation through altered vouchers.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Stored Data Manipulation]]'
---
# Chain of IDORs in Uber U4B and Vouchers APIs for Policy Manipulation and PII Theft

Multi-stage attack chain demonstrating a complete attack workflow exploiting Insecure Direct Object References (IDOR) in Uber's APIs to access sensitive data and manipulate business policies.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify API Endpoints] --> B[Exploit IDOR for Viewing] --> C[Exploit IDOR for Modification]
    C --> D[Distribute Modified Vouchers]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or API client like Postman
- Network proxy like Burp Suite for request manipulation

### Target Environment

- Web platform with access to Uber's U4B and Vouchers APIs
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to Uber's API endpoints

### Initial Access Requirements

- Valid Uber user account with access to U4B features
- Authenticated session token
- No prior elevated access needed, but organizational affiliation helps for testing

## Detailed Attack Procedures

### Step 1: Identify Uber API Endpoints for IDOR Testing
procedure: [[procedures/Identify-Uber-API-Endpoints-for-IDOR-Testing]]

**Objective**: Discover relevant API endpoints in U4B and Vouchers services to test for IDOR vulnerabilities by inspecting network traffic during normal usage.

**Instructions**: Log in to the Uber app or web interface with a U4B account. Use browser developer tools to monitor network requests while navigating to business voucher management sections. Identify endpoints handling organization IDs, voucher IDs, and policy data, such as `/v1/organizations/{org_id}/vouchers` or similar patterns.

**Expected Output**: List of API endpoints with parameter identifiers (e.g., org_id, voucher_id) visible in requests.

**Success Indicators**:
- Endpoints identified with manipulable ID parameters
- Authenticated requests captured for replay

### Step 2: Exploit IDOR to View Policies and PII
procedure: [[procedures/Exploit-IDOR-to-View-Policies-and-PII]]

**Objective**: Manipulate object identifiers in API requests to unauthorizedly access and retrieve sensitive voucher policies and organization employees' PII without proper authorization checks.

**Instructions**: Using a captured legitimate request for your own organization, replace the organization ID with another org_id (e.g., obtained from error messages or enumeration). Send the modified request via [[commands/curl-api-request]] to fetch data. Repeat for voucher endpoints to view policies and linked employee details.

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -X GET "https://api.uber.com/v1/organizations/ANOTHER_ORG_ID/vouchers" -o response.json
```

Parse the response for PII like employee names, emails, and policy details.

**Expected Output**: JSON response containing unauthorized organization data, including PII and policy configurations.

**Success Indicators**:
- Access to foreign organization data granted
- PII elements (e.g., emails, IDs) retrieved successfully

### Step 3: Exploit IDOR to Modify Voucher Policies
procedure: [[procedures/Exploit-IDOR-to-Modify-Voucher-Policies]]

**Objective**: Alter voucher policies for targeted organizations by manipulating IDs in update requests, enabling free services or financial damage through distributed modified vouchers.

**Instructions**: Capture a policy update request for your own vouchers. Modify the target org_id or voucher_id to point to a victim's resources. Adjust policy parameters (e.g., increase ride credits or remove restrictions) and submit via [[commands/curl-api-update]]:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -X PUT "https://api.uber.com/v1/organizations/VICTIM_ORG_ID/vouchers/VOUCHER_ID" -d '{"policy": {"credits": 1000, "restrictions": []}}' -o update_response.json
```

Verify changes by re-querying the endpoint, then distribute altered vouchers to users for exploitation.

**Expected Output**: Confirmation of policy update in API response, with modified settings applied.

**Success Indicators**:
- Policy modifications persisted without authorization errors
- Altered vouchers usable for free services or distributed to cause financial loss

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to multiple organizations' voucher policies and employee PII via IDOR chain.
2. Successful modification of business policies leading to potential monetary gain (e.g., free rides).
3. Demonstration of financial impact through distributable altered vouchers affecting organizational budgets.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]
- [[Stored Data Manipulation]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Impact]]

---
*Last updated: 2023-10-01T12:00:00Z*
