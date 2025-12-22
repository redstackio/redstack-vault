---
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:29.949Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6f77a89a-5291-4f86-8298-100c57594fec
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify Vulnerable CSRF Endpoint in Email Settings

## Summary

This procedure involves reconnaissance to identify API endpoints in web applications, specifically those handling sensitive actions like email notification changes, that lack proper CSRF protection. In the context of Instacart, it targets the email settings API to find unprotected POST endpoints.

## Description

Cross-Site Request Forgery (CSRF) vulnerabilities occur when a web application accepts state-changing requests without validating the origin or including anti-CSRF tokens. This procedure focuses on analyzing network requests during legitimate interactions with the email settings page to pinpoint endpoints like https://www.instacart.com/api/v2/email_settings/{id}/disable?resource_token=, which accept POST requests without token validation. The target environment is a web-based e-commerce platform where users manage account preferences. Prerequisites include access to the application's frontend and tools for inspecting HTTP traffic. Expected outcomes include confirmation of the vulnerability, enabling subsequent exploitation steps.

## Requirements

1. Access to the target web application (e.g., Instacart)
2. Browser with developer tools enabled for network inspection
3. Basic knowledge of HTTP requests and API structures

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing endpoints
- Enforce same-origin policy and validate request origins
- Monitor for anomalous POST requests from external domains

## Objectives

1. Locate unprotected API endpoints for email preferences
2. Verify lack of CSRF protection through request testing
3. Document endpoint details for exploitation

## Instructions

### Step 1: Inspect Legitimate Requests

**Context**: Navigate to the email settings page in the target application and perform actions like disabling notifications to capture the API calls.

Open browser developer tools (F12) and monitor the Network tab while interacting with email settings.

> Look for POST requests to endpoints containing '/email_settings/' or similar paths. Note parameters like 'resource_token' and absence of CSRF headers.

### Step 2: Test for CSRF Protection

**Context**: Attempt to replicate the request from an external context to confirm vulnerability.

Use a tool like curl or Postman to send a POST request to the identified endpoint without CSRF tokens.

```bash
curl -X POST "https://www.instacart.com/api/v2/email_settings/76/disable?resource_token=example_token" -d "{}"
```

> If the request succeeds without authentication or token errors, the endpoint is vulnerable to CSRF.

### Step 3: Document Findings

**Context**: Record the endpoint URL, method, and parameters for use in proof-of-concept development.

Save details including the full URL and any required query parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
