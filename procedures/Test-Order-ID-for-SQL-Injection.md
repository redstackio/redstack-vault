---
tags:
  - sqli
  - testing
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-sqli-payload]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 307dc821-142e-45b6-9cae-eaca61cf3bab
created_at: '2025-12-14T03:15:30.580Z'
updated_at: '2025-12-14T03:15:30.580Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Order-ID-for-SQL-Injection

## Summary

This procedure tests the order_id parameter for SQL injection vulnerability by injecting a conditional payload and observing response changes, such as length variations, to detect injection without explicit errors.

## Description

SQL Injection occurs when user input like order_id is concatenated into SQL queries without sanitization. Here, a boolean payload '-if(1=2,'0','1')-' is used to alter query behavior subtly. The attack targets web endpoints on platforms like Zomato, assuming a SQL backend. Prerequisites: Identified endpoint from prior recon. Outcomes: Confirmation of injectable point via blind indicators.

## Requirements

1. Burp Suite or similar for request modification
2. Baseline response from legitimate order_id request
3. Knowledge of expected response format (e.g., JSON length)

## Defense

Defensive measures and detection strategies:

- Input validation: Enforce numeric-only order_id with regex
- Prepared statements or ORM to prevent injection
- Monitor for response time/length anomalies in logs

## Objectives

1. Inject test payload to probe for SQL execution
2. Detect vulnerability through non-error indicators
3. Avoid detection by using subtle blind techniques

## Instructions

### Step 1: Prepare Baseline Request

**Context**: Send a normal request to establish response metrics.

In Burp Repeater, forward a legitimate request with a valid order_id.

**Expected Output**: Standard response, e.g., 200 OK with order data, note length ~500 bytes.

### Step 2: Inject Test Payload

**Context**: Modify order_id to include the SQLi payload and resend.

Execute [[commands/curl-test-sqli-payload]] to test:

```bash
curl -X GET "https://www.zomato.com/api/orders?order_id='-if(1=2,'0','1')-'" -H "User-Agent: Mozilla/5.0" -s | wc -c
```

> This command sends the payload and counts response bytes; expect different length from baseline.

**Expected Output**: Response length change, e.g., 300 bytes, indicating injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-sqli-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[sqli]]
- [[testing]]
