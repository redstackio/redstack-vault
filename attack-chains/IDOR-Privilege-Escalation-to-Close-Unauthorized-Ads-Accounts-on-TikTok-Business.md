---
id: ac-tiktok-idor-priv-esc-1505567
tags:
  - idor
  - privilege-escalation
  - tiktok
  - web
  - ads
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Authenticate-and-Test-IDOR-on-TikTok-Parameters]]'
  - '[[procedures/Exploit-IDOR-to-Close-Unauthorized-Ads-Account]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:27.070Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in TikTok Business endpoints to allow Analyst users to escalate
  privileges and close other organizations' ads accounts.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# IDOR Privilege Escalation to Close Unauthorized Ads Accounts on TikTok Business

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in TikTok Business to escalate privileges from an Analyst role and disrupt other users' ads accounts.

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
    A[Authenticate as Analyst] --> B[Test IDOR Parameters]
    B --> C[Exploit to Close Account]
    C --> D[Disrupt Operations]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (Business.TikTok.com)
- Required services: Ads management endpoints
- Network access: Authenticated session to TikTok Business

### Initial Access Requirements

- Analyst-level credentials for TikTok Business
- Network position: Direct access to web interface
- Prior access: Valid login session

## Detailed Attack Procedures

### Step 1: Authenticate and Test IDOR
procedure: [[procedures/Authenticate-and-Test-IDOR-on-TikTok-Parameters]]

**Objective**: Gain authenticated access as an Analyst and test manipulation of org_id and account_id parameters to identify unauthorized resource access.

**Instructions**: Log in to Business.TikTok.com with Analyst credentials. Use [[tools/Burp-Suite]] to intercept requests and modify the org_id and account_id parameters in API calls to reference other organizations' resources. For example, capture a legitimate request and alter the parameters:

```bash
# Example using curl to simulate (replace with actual tokens)
curl -X POST 'https://business.tiktok.com/api/ads' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d 'org_id=TARGET_ORG_ID&account_id=TARGET_ACCOUNT_ID'
```

**Expected Output**: Successful response indicating access to unauthorized data or actions.

**Success Indicators**:
- Response returns data from another org/account
- No authorization error on modified parameters

### Step 2: Exploit IDOR for Privilege Escalation
procedure: [[procedures/Exploit-IDOR-to-Close-Unauthorized-Ads-Account]]

**Objective**: Use the identified IDOR to perform destructive actions, such as closing another user's ads account, leading to operational disruption.

**Instructions**: With the manipulated parameters confirmed, send a request to close the target ads account using the altered org_id and account_id. Intercept and modify via [[tools/Burp-Suite]] or simulate with curl:

```bash
# Example curl to close account (replace placeholders)
curl -X POST 'https://business.tiktok.com/api/ads/close' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d 'org_id=TARGET_ORG_ID&account_id=TARGET_ACCOUNT_ID&action=close'
```

**Expected Output**: Confirmation of account closure from the API response.

**Success Indicators**:
- API returns success for closure
- Target account status changes to closed in verification queries

## Attack Chain Summary

### Key Achievements

1. Successful authentication and parameter manipulation to bypass access controls
2. Privilege escalation from Analyst to perform admin-like actions on unauthorized accounts
3. Disruption of business operations by closing ads accounts

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
