---
id: ac-csrf-shopify-pinterest-oauth
tags:
  - csrf
  - oauth
  - shopify
  - pinterest
  - web-vulnerability
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
  - '[[procedures/Identify-Missing-CSRF-in-OAuth-Callback]]'
  - '[[procedures/Forge-CSRF-Request-to-Attach-Pinterest-Account]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.285Z'
description: >-
  Attack chain exploiting CSRF vulnerability in Shopify's Pinterest OAuth
  callback to attach an attacker's Pinterest account to a victim's Shopify
  profile without authorization.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CSRF in Shopify Pinterest OAuth Callback for Unauthorized Account Attachment

Multi-stage attack chain demonstrating a complete attack workflow exploiting the absence of a state parameter in Shopify's Pinterest OAuth callback, allowing unauthorized attachment of an attacker's Pinterest account to a victim's profile.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerability] --> B[Forge and Execute CSRF]
    B --> C[Attach Account and Monitor]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser Developer Tools
- Optional: [[Burp Suite]] for request interception

### Target Environment

- Web platform
- Shopify app environment with Pinterest integration
- Access to victim's session (e.g., via phishing or shared link)

### Initial Access Requirements

- Victim must be authenticated to Shopify
- Attacker needs victim's Shopify session cookie
- Network access to https://pinterest-commerce.shopifyapps.com

## Detailed Attack Procedures

### Step 1: Identify Missing CSRF Protection
procedure: [[procedures/Identify-Missing-CSRF-in-OAuth-Callback]]

**Objective**: Inspect the OAuth callback endpoint to confirm the absence of state parameter or CSRF token validation, enabling the attack.

**Instructions**: Use browser developer tools to inspect the OAuth flow. Navigate to the Pinterest attachment page in Shopify and monitor the network tab for the callback request to /auth/pinterest/callback?code=.... Verify no state parameter is sent or validated.

**Expected Output**: Callback URL like https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=AUTH_CODE without ?state= or token checks.

**Success Indicators**:
- No state parameter in request
- Endpoint accepts code without additional validation

### Step 2: Forge CSRF Request to Attach Account
procedure: [[procedures/Forge-CSRF-Request-to-Attach-Pinterest-Account]]

**Objective**: Craft and deliver a forged request to attach the attacker's Pinterest account using the victim's session, allowing unauthorized monitoring.

**Instructions**: First, obtain the victim's Shopify session cookie. Then, create an HTML page with a hidden form or auto-submitting iframe targeting the callback endpoint. Use the code from a legitimate OAuth initiation but forge it from the attacker's Pinterest account. Deliver via phishing email or malicious site.

Example forged request using curl for testing (replace COOKIES and CODE):

```bash
curl -X GET "https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=AUTH_CODE" -H "Cookie: shopify_session=VICTIM_COOKIE"
```

**Expected Output**: Successful attachment confirmation, with attacker's Pinterest linked to victim's profile.

**Success Indicators**:
- Pinterest account attached without user interaction
- Attacker can monitor victim's Pinterest-synced activities via Shopify

## Attack Chain Summary

### Key Achievements

1. Confirmed CSRF vulnerability in OAuth callback
2. Forged request to hijack account attachment
3. Enabled unauthorized monitoring of victim activities

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
