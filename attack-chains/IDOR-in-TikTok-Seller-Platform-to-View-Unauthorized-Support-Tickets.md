---
tags:
  - idor
  - web
  - tiktok
  - support-tickets
  - access-control
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-to-Access-Unauthorized-Support-Tickets]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:35.206Z'
description: >-
  An authenticated attacker exploits an Insecure Direct Object Reference (IDOR)
  vulnerability in TikTok's seller platform to access and view support tickets
  belonging to other users by manipulating user-specific identifiers.
skill_level: intermediate
impact_level: medium
id: 3b7af2f7-74b0-4b04-95b8-eae40d8d7255
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# IDOR in TikTok Seller Platform to View Unauthorized Support Tickets

Multi-stage attack chain demonstrating a complete attack workflow targeting an IDOR vulnerability in TikTok's seller platform, allowing authenticated users to access other users' sensitive support ticket information.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Authentication] --> B[Exploit IDOR]
    B --> C[Access Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Target OS/Platform: Web application (TikTok Seller Platform)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to seller.tiktok.com or equivalent endpoint

### Initial Access Requirements

- Credential requirements: Valid authenticated account on TikTok Seller Platform
- Network position: External attacker with valid session
- Prior access needed: Successful login to the platform

## Detailed Attack Procedures

### Step 1: Authenticate and Exploit IDOR
procedure: [[procedures/Exploit-IDOR-to-Access-Unauthorized-Support-Tickets]]

**Objective**: Gain access to the seller platform and manipulate request parameters to view support tickets of other users, exposing sensitive information.

**Instructions**: First, log in to the TikTok Seller Platform using valid credentials. Then, navigate to the support tickets section and intercept the request using Burp Suite to identify the user-specific identifier (e.g., ticket ID or user ID). Modify the identifier to target another user's ticket and forward the request.

**Expected Output**: The response contains details of another user's support ticket, including potentially sensitive information like personal data or transaction details.

**Success Indicators**:
- Unauthorized support ticket loads without errors
- Sensitive data from another user is visible in the response

## Attack Chain Summary

### Key Achievements

1. Successful authentication to the seller platform
2. Manipulation of object references to bypass authorization
3. Exposure of other users' support ticket information

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
