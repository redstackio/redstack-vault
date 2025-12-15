---
tags:
  - broken-access-control
  - idor
  - pii-disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:35.182Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1090f0cc-8714-4718-8b43-b95f54f6cbfc
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Modify-customer_id-to-Access-Other-Users-Data

## Summary

This procedure exploits the lack of authorization checks by altering the customer_id parameter in the /api/v2/rechargeTransactionHistory request to retrieve transaction history for any valid MTN phone number, disclosing sensitive PII.

## Description

The endpoint fails to verify if the provided customer_id matches the authenticated user's MSISDN, allowing horizontal privilege escalation. By changing customer_id to another 11-13 digit MTN number (starting with 234), the attacker receives details like recharge dates, balances, transaction IDs, and adjustment types. This leads to privacy breaches and potential targeting for fraud.

## Requirements

1. Intercepted request from previous step
2. List of target MTN numbers (e.g., from public sources or enumeration)
3. Active proxy session

## Defense

Defensive measures and detection strategies:

- Enforce strict authorization: Validate customer_id against session MSISDN
- Implement parameter binding and input sanitization
- Log and alert on mismatched customer_id in requests; use WAF rules for IDOR patterns

## Objectives

1. Bypass access controls to access unauthorized data
2. Extract PII including transaction details
3. Validate exploit success for further abuse

## Instructions

### Step 1: Edit Request Payload

**Context**: Modify the JSON in the proxy tool.

No command; GUI edit in Burp.

> In Burp Repeater or Proxy, change "customer_id": "2347032233323" to "customer_id": "2348063223665" (target number). Keep other fields intact.

### Step 2: Forward Modified Request

**Context**: Send the altered request to the endpoint.

No command; forward action.

> Click 'Forward' in Burp. The server processes without checks, returning 200 OK with target data.

### Step 3: Review Disclosed Data

**Context**: Parse the response for sensitive information.

No command.

> Response JSON: [{"rechargeDate": "2023-09-15", "amountBefore": 1000, "amountAfter": 2000, "transactionId": "TXN123", "subscriberId": "2348063223665", "adjustmentType": "Recharge"}]. Save or exfiltrate as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- broken-access-control
- idor
- pii-disclosure
