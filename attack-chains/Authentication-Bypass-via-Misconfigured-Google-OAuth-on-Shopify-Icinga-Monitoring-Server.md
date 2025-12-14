---
id: ac-uuid-001
tags:
  - oauth
  - auth-bypass
  - google
  - icinga
  - misconfiguration
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Bypass-Google-OAuth-Domain-Validation-on-Icinga-Server]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.856Z'
description: >-
  A multi-stage attack chain exploiting a misconfiguration in Google OAuth on
  Shopify's Icinga monitoring server, allowing unauthorized access with any
  Google account due to missing 'hd' parameter validation.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authentication Bypass via Misconfigured Google OAuth on Shopify Icinga Monitoring Server

Multi-stage attack chain demonstrating a complete attack workflow exploiting OAuth misconfiguration for unauthorized access to internal monitoring infrastructure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Authentication Attempt] --> B[Access Granted to Monitoring Server]
    B --> C[Exposure of Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Web-based Icinga monitoring server with Google OAuth integration
- No specific ports required beyond standard HTTPS (443)
- Network access to the public-facing login endpoint

### Initial Access Requirements

- A valid Google account (any domain, not restricted to shopify.com)
- No prior credentials or network position needed; attack is external

## Detailed Attack Procedures

### Step 1: Attempt Authentication with Non-Shopify Google Account
procedure: [[procedures/Bypass-Google-OAuth-Domain-Validation-on-Icinga-Server]]

**Objective**: Exploit the lack of 'hd' parameter validation to authenticate using an arbitrary Google account.

**Instructions**: Navigate to the Icinga server's login page, which uses Google OAuth. Initiate the OAuth flow by clicking the 'Sign in with Google' button. When redirected to Google's authentication page, use a personal or non-Shopify Google account (e.g., a Gmail account). Complete the login without entering any Shopify-specific credentials.

**Expected Output**: Successful redirection back to the Icinga dashboard, indicating authentication succeeded.

**Success Indicators**:
- Login prompt accepts the non-Shopify account without error
- Access to the Icinga interface is granted

### Step 2: Access Internal Monitoring Features
procedure: [[procedures/Bypass-Google-OAuth-Domain-Validation-on-Icinga-Server]]

**Objective**: Gain unauthorized entry to sensitive monitoring data and features on the Icinga server.

**Instructions**: Once authenticated, explore the Icinga dashboard. Attempt to view host statuses, service checks, and any internal infrastructure metrics. No additional commands are needed; interaction occurs via the web interface.

**Expected Output**: Visibility into internal monitoring data, such as server statuses and alerts, which should be restricted to Shopify employees.

**Success Indicators**:
- Dashboard loads without access denial
- Sensitive data (e.g., infrastructure monitoring logs) is visible

## Attack Chain Summary

### Key Achievements

1. Bypassed domain restrictions in Google OAuth using the 'hd' parameter omission
2. Achieved unauthorized access to Shopify's internal Icinga monitoring server
3. Demonstrated potential for exposure of sensitive infrastructure monitoring data to external attackers

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T12:00:00Z*
