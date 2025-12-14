---
tags:
  - broken-access-control
  - taxjar
  - stripe
  - unauthorized-linking
  - account-disclosure
type: attack_chain
tools: []
tactics:
  - '[[Lateral Movement]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Taxjar-Access-Control-Bypass]]'
step_count: 1
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:44.376Z'
description: >-
  Exploit broken access controls in Stripe's Taxjar integration to allow member
  users to link unauthorized external carts and disclose linked account
  information via a simple GET request bypass.
skill_level: beginner
impact_level: low
id: b13f5213-17d8-4fbd-997e-a675ff870cef
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Broken Access Control in Taxjar Integration for Unauthorized Account Linking

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access with Member Account] --> B[Exploit Access Control Bypass]
    B --> C[Link Unauthorized Accounts or Disclose Info]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- Web platform
- Taxjar service integrated with Stripe
- External services: Shopify, Xero, QuickBooks, Squarespace, Etsy, eBay
- No specific ports required (standard HTTPS)
- Network access to Taxjar's authentication endpoints

### Initial Access Requirements

- Valid member-level credentials for a Taxjar account
- Authenticity token (bypassed by setting to 0)
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Exploit Access Control to Link or View Accounts
procedure: [[procedures/Exploit-Taxjar-Access-Control-Bypass]]

**Objective**: Bypass permission restrictions to link new external carts or view information about existing linked accounts using a member account.

**Instructions**: Authenticate as a member user in the Taxjar dashboard. Then, send a GET request to the /auth/[CARTS-NAME] endpoint, replacing [CARTS-NAME] with the target integration (e.g., shopify, xero). Include the authenticity_token parameter set to 0 to bypass controls. Use [[commands/curl-get-taxjar-auth-bypass]] for this:

```bash
curl -X GET "https://taxjar.com/auth/shopify?authenticity_token=0" -H "Cookie: session=your_session_cookie" -H "User-Agent: Mozilla/5.0"
```

Replace 'shopify' with other carts like 'xero', 'quickbooks', etc. Include necessary session cookies from your authenticated browser session.

**Expected Output**: Successful response indicating account linking initiation or disclosure of linked account details, such as account IDs or status, without admin permissions.

**Success Indicators**:
- Response code 200 with linking form or account info
- Ability to proceed with unauthorized integration setup
- No permission error messages

## Attack Chain Summary

### Key Achievements

1. Bypassed member-level restrictions to link external carts like Shopify or Xero
2. Disclosed information about activated linked accounts
3. Potential for unauthorized data exposure from linked services

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Lateral Movement]]

---
*Last updated: 2023-10-01T00:00:00Z*
