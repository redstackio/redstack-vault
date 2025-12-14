---
tags:
  - open-redirect
  - oauth
  - phishing
  - shopify
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Shopify-App-with-Custom-Redirect]]'
  - '[[procedures/Test-Shopify-OAuth-with-Valid-Scope]]'
  - '[[procedures/Trigger-Shopify-OAuth-Open-Redirect]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:35.515Z'
description: >-
  Multi-stage attack exploiting an open redirection vulnerability in Shopify's
  OAuth authorization flow to enable phishing by bypassing redirect URI
  validation with an invalid scope.
skill_level: intermediate
impact_level: high
id: 40fbe316-dc4b-47ed-ba4b-30fcb5d322fe
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Shopify OAuth Open Redirection for Phishing Attacks

Multi-stage attack chain demonstrating exploitation of an open redirection in Shopify's OAuth flow, allowing attackers to redirect users to arbitrary phishing sites by using an invalid scope to bypass redirect URI hostname validation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious App] --> B[Test Valid Scope Behavior]
    B --> C[Trigger Open Redirect with Invalid Scope]
    C --> D[Phishing Page Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-visit-url]] for accessing endpoints

### Target Environment

- Shopify store (e.g., admin panel accessible)
- Required services/ports: HTTPS on port 443
- Network access requirements: Internet access to myshopify.com

### Initial Access Requirements

- Shopify developer account to create apps
- No prior credentials on target store needed
- Network position: External attacker

## Detailed Attack Procedures

### Step 1: Create Malicious App
procedure: [[procedures/Create-Shopify-App-with-Custom-Redirect]]

**Objective**: Register a test app on Shopify with a malicious redirect URI pointing to an external phishing site to set up the redirection target.

**Instructions**: Use Shopify's app creation interface to register the app, specifying a client ID and a redirect URI to an attacker-controlled domain like Facebook for testing.

**Expected Output**: App registered with client_id=616ce3efcd495007438000ad958a6629 and redirect_uri=http://www.facebook.com/abc/.

**Success Indicators**:
- App creation confirmation from Shopify
- Client ID generated and verifiable

### Step 2: Test Valid Scope Behavior
procedure: [[procedures/Test-Shopify-OAuth-with-Valid-Scope]]

**Objective**: Verify normal OAuth flow behavior with a valid scope to confirm the redirect URI validation is enforced under standard conditions.

**Instructions**: Construct and visit the OAuth authorize URL using a valid scope like read_customers, observing that the redirect does not occur to the external URI due to validation.

Use [[commands/curl-visit-url]] to simulate:

```bash
curl "https://prans.myshopify.com/admin/oauth/authorize?client_id=616ce3efcd495007438000ad958a6629&scope=read_customers&redirect_uri=http://www.facebook.com/abc/"
```

**Expected Output**: No redirection to external site; error or standard Shopify response due to invalid redirect URI hostname.

**Success Indicators**:
- Validation error for redirect URI
- No unauthorized redirect observed

### Step 3: Trigger Open Redirect
procedure: [[procedures/Trigger-Shopify-OAuth-Open-Redirect]]

**Objective**: Exploit the vulnerability by using an invalid scope to bypass redirect URI validation, forcing a redirect to the attacker-controlled phishing site.

**Instructions**: Modify the OAuth URL to use an invalid scope like 'a', then visit it to trigger the open redirect.

Use [[commands/curl-visit-url]] to test:

```bash
curl -L "https://prans.myshopify.com/admin/oauth/authorize?client_id=616ce3efcd495007438000ad958a6629&scope=a&redirect_uri=https://www.facebook.com/abc" -o redirect_output.html
```

**Expected Output**: Redirect to https://www.facebook.com/abc with query parameters including error=invalid_scope, hmac, shop, signature, and timestamp.

**Success Indicators**:
- Successful redirect to external URI
- Phishing page loads with Shopify-mimicking content

## Attack Chain Summary

### Key Achievements

1. Bypassed OAuth redirect validation using invalid scope
2. Enabled redirection to arbitrary external sites for phishing
3. Demonstrated potential for credential theft via fake app authorization

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
