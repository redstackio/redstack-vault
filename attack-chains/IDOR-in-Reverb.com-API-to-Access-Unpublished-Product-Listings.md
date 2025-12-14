---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - idor
  - api
  - web
  - unauthorized-access
  - product-listing
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Authenticate-to-Reverb-com-Sandbox]]'
  - '[[procedures/Create-Test-Product-Listing]]'
  - '[[procedures/Intercept-and-Analyze-API-Requests-with-Burp-Suite]]'
  - '[[procedures/Exploit-IDOR-by-Manipulating-Listing-ID]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:29.120Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the Reverb.com sandbox API to retrieve sensitive details of
  unpublished product listings without authorization.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# IDOR in Reverb.com API to Access Unpublished Product Listings

Multi-stage attack chain demonstrating a complete workflow to exploit an Insecure Direct Object Reference (IDOR) in the Reverb.com sandbox API, allowing unauthorized retrieval of unpublished product listing details.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Authenticate] --> B[Discovery: Create Listing]
    B --> C[Recon: Intercept API]
    C --> D[Exploitation: Modify ID]
    D --> E[Objective: Retrieve Unpublished Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (sandbox.reverb.com)
- Required services: API endpoints over HTTPS
- Network access: Direct internet access to Reverb.com

### Initial Access Requirements

- Valid user credentials for Reverb.com sandbox (test account)
- Network position: Standard user browser session
- Prior access: None, but authentication required

## Detailed Attack Procedures

### Step 1: Authenticate to Platform

procedure: [[procedures/Authenticate-to-Reverb-com-Sandbox]]

**Objective**: Gain authenticated access to the Reverb.com sandbox to enable listing creation and API interactions.

**Instructions**: Navigate to sandbox.reverb.com and log in with test user credentials to establish a session.

**Expected Output**: Successful login redirect to the dashboard, with session cookies set for API calls.

**Success Indicators**:
- Dashboard accessible
- User profile visible

### Step 2: Create Test Listing

procedure: [[procedures/Create-Test-Product-Listing]]

**Objective**: Generate a product listing to observe the API endpoint behavior and capture the legitimate request format.

**Instructions**: Use the web interface to create a new unpublished product listing, triggering the API call to /api/listings/{own_id}/product_bundle.

**Expected Output**: Listing created with a unique ID, and JSON response containing product details.

**Success Indicators**:
- Listing ID obtained (e.g., via network inspection)
- API response returns expected JSON structure

### Step 3: Intercept API Requests

procedure: [[procedures/Intercept-and-Analyze-API-Requests-with-Burp-Suite]]

**Objective**: Monitor and capture the API request during listing creation to identify the vulnerable endpoint.

**Instructions**: Configure [[tools/Burp-Suite]] as a proxy, perform the listing creation, and inspect the traffic for the /api/listings/{id}/product_bundle request.

**Expected Output**: Captured GET request with listing ID parameter visible in Burp Suite.

**Success Indicators**:
- Proxy intercepts the request successfully
- Endpoint URL and parameters logged

### Step 4: Exploit IDOR

procedure: [[procedures/Exploit-IDOR-by-Manipulating-Listing-ID]]

**Objective**: Modify the listing ID in the API request to access an unauthorized unpublished product.

**Instructions**: In Burp Suite, edit the intercepted request by replacing the {own_id} with a target unlisted ID (e.g., 65905), then forward the request to retrieve the JSON data.

**Expected Output**: API returns detailed JSON of the unpublished listing, including product details, photos, prices, descriptions, and seller info.

**Success Indicators**:
- Unauthorized JSON data retrieved
- No error or redirect; full details exposed

## Attack Chain Summary

### Key Achievements

1. Bypassed web interface controls to access private API data
2. Retrieved sensitive unpublished listing information without ownership
3. Demonstrated potential for privacy violations and exposure of seller details

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T12:00:00Z*
