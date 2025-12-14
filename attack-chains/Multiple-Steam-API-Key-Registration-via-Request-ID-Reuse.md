---
tags:
  - business-logic-flaw
  - api-key-abuse
  - steam-api
  - valve
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-Steam-API-Key-Registration]]'
  - '[[procedures/Confirm-Registration-via-Mobile-Authenticator]]'
  - '[[procedures/Reuse-Request-ID-for-Additional-Key-Registration]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.943Z'
description: >-
  Attack chain exploiting a business logic flaw in Steam's Web API key
  registration to obtain multiple API keys for the same account by reusing a
  confirmed request_id.
skill_level: intermediate
impact_level: low
id: 394f7071-68e4-4b8d-9c2b-23b6d68f06dd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Multiple Steam API Key Registration via Request ID Reuse

Multi-stage attack chain demonstrating exploitation of a business logic flaw in Valve's Steam Web API key registration process, allowing attackers to register multiple API keys for the same account by reusing a confirmed `request_id` without invalidation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Registration] --> B[Confirm via Authenticator]
    B --> C[Reuse request_id for Multiple Keys]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Steam account with mobile authenticator enabled
- Web browser or API client (e.g., curl)

### Target Environment

- Steam Web platform
- Access to Steam Web API registration endpoint
- No specific ports required (HTTPS/443)

### Initial Access Requirements

- Valid Steam account credentials
- Enabled mobile authenticator
- Network access to steamcommunity.com

## Detailed Attack Procedures

### Step 1: Initiate Registration
procedure: [[procedures/Initiate-Steam-API-Key-Registration]]

**Objective**: Start the API key registration process to generate a unique `request_id` that requires mobile confirmation.

**Instructions**: Log in to your Steam account via the web interface and navigate to the API key management section. Initiate the registration by submitting the required details, which generates a `request_id`.

**Expected Output**: A `request_id` is returned, prompting for mobile authenticator confirmation.

**Success Indicators**:
- `request_id` generated and displayed
- Confirmation prompt appears

### Step 2: Confirm via Authenticator
procedure: [[procedures/Confirm-Registration-via-Mobile-Authenticator]]

**Objective**: Complete the initial registration by confirming the `request_id` using the Steam mobile app, which issues the first API key.

**Instructions**: Open the Steam mobile app, review the confirmation request for the `request_id`, and approve it. This finalizes the first key issuance.

**Expected Output**: First API key is generated and visible in the account dashboard.

**Success Indicators**:
- Confirmation approved in mobile app
- Initial API key received

### Step 3: Reuse request_id for Additional Keys
procedure: [[procedures/Reuse-Request-ID-for-Additional-Key-Registration]]

**Objective**: Exploit the lack of `request_id` invalidation to resubmit the same `request_id` and obtain additional API keys.

**Instructions**: Using the same `request_id` from Step 1, resubmit the registration request to the API endpoint without regenerating a new ID. Repeat as needed to generate multiple keys.

**Expected Output**: Additional API keys are issued for the same account.

**Success Indicators**:
- Multiple API keys listed in the account
- No error on resubmission

## Attack Chain Summary

### Key Achievements

1. Generated initial `request_id` via registration initiation
2. Confirmed and obtained first API key through mobile authenticator
3. Successfully reused `request_id` to register extra keys, bypassing one-key-per-account limit

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2024-01-01T00:00:00Z*
