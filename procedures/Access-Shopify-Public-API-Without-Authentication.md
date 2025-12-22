---
tags:
  - auth-bypass
  - pii-disclosure
  - shopify
  - api
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-api-request]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9f2a4a60-d86b-4da2-92e6-04731d574c40
created_at: '2025-12-14T17:28:45.029Z'
updated_at: '2025-12-14T17:28:45.029Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Shopify-Public-API-Without-Authentication

## Summary

This procedure exploits a lack of authentication on Shopify's public API endpoint to retrieve store staff members' first and last names, enabling unauthorized PII disclosure.

## Description

In vulnerable Shopify instances, a public API endpoint exposes sensitive staff information without requiring authentication tokens or credentials. An attacker can send a simple HTTP GET request to this endpoint using any store's domain, resulting in the leakage of personally identifiable information (PII) such as first and last names of store administrators and staff. This vulnerability was reported in 2015 and highlights risks in e-commerce platforms where API endpoints are not properly secured. The procedure assumes access to the internet and knowledge of the target store's myshopify.com domain; no prior credentials or network position is needed. Expected outcomes include receiving a JSON payload with staff details, which could be used for social engineering or further reconnaissance.

## Requirements

1. Target Shopify store domain (e.g., example.myshopify.com)
2. HTTP client like curl for making requests
3. Basic understanding of REST APIs

## Defense

Defensive measures and detection strategies:

- Implement proper authentication (e.g., API keys or OAuth) on all endpoints handling sensitive data
- Use rate limiting and IP whitelisting for public APIs
- Monitor API logs for anomalous unauthenticated access patterns
- Conduct regular API security audits and penetration testing

## Objectives

1. Gain unauthorized access to staff PII via the API
2. Collect names for potential phishing or reconnaissance
3. Validate the presence of the authentication bypass vulnerability

## Instructions

### Step 1: Prepare the Target Endpoint

**Context**: Identify the vulnerable public API endpoint for the target Shopify store. The endpoint typically follows a pattern like /api/staff on the store's domain.

No command required; note the full URL: https://target.myshopify.com/api/staff

### Step 2: Send Unauthenticated Request

**Context**: Execute an HTTP GET request without any authentication headers to retrieve the staff data. This step confirms the vulnerability by returning PII if unprotected.

**Command** ([[commands/curl-api-request]]):
```bash
curl -X GET "https://target.myshopify.com/api/staff" -H "Content-Type: application/json" -s
```

> This command sends a silent GET request to the API endpoint. The -s flag suppresses progress output for cleaner results. Expected output is a JSON array like: {"staff": [{"first_name": "John", "last_name": "Doe"}, ...]}. If the endpoint requires auth, it will return 401 or 403; success indicates the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-request]]

## Tools Used


## Tags

- auth-bypass
- pii-disclosure
- shopify
- api
