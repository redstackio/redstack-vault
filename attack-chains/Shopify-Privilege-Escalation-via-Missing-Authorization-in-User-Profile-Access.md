---
tags:
  - broken-access-control
  - privilege-escalation
  - authorization-bypass
  - shopify
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Direct-Access-to-Shopify-Owner-Profile]]'
step_count: 1
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.679Z'
description: >-
  A single-step attack exploiting broken access control in Shopify to allow a
  full-access administrator to unauthorizedly view the account owner's sensitive
  user profile information by directly requesting the profile URL.
skill_level: beginner
impact_level: high
id: 8ec1a44b-a9d7-4588-a599-9159473e46b4
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Shopify Privilege Escalation via Missing Authorization in User Profile Access

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access as Admin] --> B[Privilege Escalation]
    B --> C[Access Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses browser or basic HTTP client)

### Target Environment

- Shopify admin platform (Web)
- Required services/ports: HTTPS (443)
- Network access requirements: Valid admin session

### Initial Access Requirements

- Valid full-access administrator credentials (not account owner)
- Network position: Authenticated session on Shopify admin dashboard
- Prior access needed: Logged in as full-access admin

## Detailed Attack Procedures

### Step 1: Unauthorized Profile Access
procedure: [[procedures/Direct-Access-to-Shopify-Owner-Profile]]

**Objective**: Bypass authorization checks to view the account owner's sensitive user profile information, achieving privilege escalation from full-access admin to owner-level data access.

**Instructions**: Log in to the Shopify admin dashboard as a full-access administrator. Identify the account owner's user ID (often visible in team management or via enumeration). Directly request the profile URL, such as `https://admin.shopify.com/store/[store-name]/users/[owner-user-id]/profile`, using a browser or HTTP client. No additional tools are required beyond an authenticated session.

Use [[commands/curl-shopify-profile-access]] to simulate the direct request if testing via command line:

```bash
curl -H "Cookie: [your-admin-session-cookie]" "https://admin.shopify.com/store/[store-name]/users/[owner-user-id]/profile"
```

**Expected Output**: The response contains the account owner's user profile data, including sensitive information like email, phone, or other personal details that should be restricted.

**Success Indicators**:
- Profile page loads without error or redirect
- Sensitive owner data (e.g., contact info) is visible in the response
- No authorization denial (e.g., 403 Forbidden)

## Attack Chain Summary

### Key Achievements

1. Successful bypass of owner-specific authorization checks
2. Unauthorized exposure of sensitive account owner profile information
3. Demonstration of privilege escalation within Shopify's admin roles

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
