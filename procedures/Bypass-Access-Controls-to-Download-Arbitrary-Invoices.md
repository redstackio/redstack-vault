---
tags:
  - broken-access-control
  - idor
  - uuid-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-uuid-invoice-download]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.656Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: d3f79619-a17b-4b4a-b849-77b28fe51665
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Access-Controls-to-Download-Arbitrary-Invoices

## Summary

This procedure exploits a broken access control vulnerability in Uber's invoice download functionality, allowing any user to download invoices belonging to other users by directly accessing the endpoint with a known UUID, without any authentication or ownership checks. It demonstrates how UUID-based access without proper authorization leads to unauthorized data exposure.

## Description

The vulnerability occurs in the invoice download feature where the endpoint accepts a UUID parameter to retrieve and serve the corresponding invoice file. Due to missing server-side checks for user authentication and invoice ownership, an attacker can simply provide any valid UUID to download sensitive financial documents. This was reported in 2016 via HackerOne, highlighting the risk of exposing PII and financial data. The procedure assumes the attacker has a valid UUID, which could be obtained through other means like enumeration or social engineering. Expected outcomes include successful file retrieval and potential data leakage for further exploitation.

## Requirements

1. Network access to Uber's web application (public internet)
2. A valid invoice UUID (guessed, enumerated, or leaked)
3. Standard HTTP client like curl or a browser
4. No Uber account or credentials required due to the bypass

## Defense

Defensive measures and detection strategies:

- Implement proper authentication and authorization checks on all endpoints, verifying user ownership of resources
- Use session-based or token-based auth for sensitive operations; avoid direct object references like UUIDs without validation
- Log all invoice download requests with UUID and user IP; monitor for anomalous access patterns (e.g., multiple UUIDs from one IP)
- Rate-limit requests to download endpoints and implement CAPTCHA for suspicious activity

## Objectives

1. Gain unauthorized access to another user's invoice data
2. Exfiltrate sensitive financial information for reconnaissance or extortion
3. Validate the presence of broken access control in the target system

## Instructions

### Step 1: Identify Target UUID

**Context**: Obtain a valid invoice UUID to target. This could be from previous interactions, error messages, or brute-forcing patterns (e.g., sequential UUIDs).

No specific command needed; manually note the UUID format (typically a 32-character hex string).

### Step 2: Request Invoice Download

**Context**: Use an HTTP GET request to the invoice download endpoint, substituting the UUID without any auth headers. This bypasses controls and retrieves the file.

**Command** ([[commands/curl-uuid-invoice-download]]):
```bash
curl -X GET "https://uber.com/api/invoice/download/{UUID}" -o stolen_invoice.pdf --header "User-Agent: Mozilla/5.0"
```

> This command sends a GET request to the endpoint, replacing `{UUID}` with the target value, and saves the response as a PDF. Expected output is the binary file content if successful (HTTP 200). If the UUID is invalid, expect 404; valid ones return the invoice without checks.

### Step 3: Verify Downloaded Content

**Context**: Open the downloaded file to confirm it contains unauthorized data, such as another user's billing details.

Use a PDF viewer or `file` command:
```bash
file stolen_invoice.pdf
```

> Confirms it's a PDF; inspect contents for sensitive info like names, amounts, and trip details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-uuid-invoice-download]]

## Tools Used


## Tags

- [[broken-access-control]]
- [[idor]]
- [[uuid-bypass]]
