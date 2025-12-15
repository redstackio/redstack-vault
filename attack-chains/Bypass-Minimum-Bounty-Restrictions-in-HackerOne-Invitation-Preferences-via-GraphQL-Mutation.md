---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - graphql
  - client-side-bypass
  - parameter-tampering
  - hackerone
  - business-logic
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Setup-Burp-Proxy-for-Interception]]'
  - '[[procedures/Authenticate-HackerOne-Account]]'
  - '[[procedures/Navigate-to-Bounty-Preferences]]'
  - '[[procedures/Enable-Bounty-Only-Invitations]]'
  - '[[procedures/Intercept-and-Modify-GraphQL-Mutation]]'
  - '[[procedures/Verify-Min-Bounty-Update]]'
step_count: 12
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.516Z'
description: >-
  Client-side enforcement bypass in HackerOne's Bounty Preferences allowing
  arbitrary minimum bounty thresholds via intercepted GraphQL mutations,
  enabling selective private program invitations.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Minimum Bounty Restrictions in HackerOne Invitation Preferences via GraphQL Mutation

Multi-stage attack chain demonstrating a complete attack workflow exploiting a client-side enforcement flaw in HackerOne's Bounty Preferences feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 12 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Proxy and Authenticate] --> B[Configure Preferences UI]
    B --> C[Intercept GraphQL Request]
    C --> D[Modify and Replay Mutation]
    D --> E[Verify Update and Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#9b59b6
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- HackerOne application at https://hackerone.com
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid HackerOne hacker account credentials
- Network access to HackerOne (no VPN or proxy restrictions beyond Burp)
- Prior access: None, but authenticated session required

## Detailed Attack Procedures

### Step 1: Setup Interception Proxy
procedure: [[procedures/Setup-Burp-Proxy-for-Interception]]

**Objective**: Establish a proxy to intercept HTTP traffic from the browser to HackerOne.

**Instructions**: Launch Burp Suite and configure your browser to proxy through it on localhost:8080.

**Expected Output**: Proxy active, ready to capture requests.

**Success Indicators**:
- Burp dashboard shows no errors
- Browser traffic routes through proxy

### Step 2: Authenticate to HackerOne
procedure: [[procedures/Authenticate-HackerOne-Account]]

**Objective**: Log in as a hacker to access preferences.

**Instructions**: Navigate to https://hackerone.com and enter credentials.

**Expected Output**: Successful login, dashboard visible.

**Success Indicators**:
- Authenticated session established
- No login errors

### Step 3: Navigate to Preferences Page
procedure: [[procedures/Navigate-to-Bounty-Preferences]]

**Objective**: Reach the Bounty Preferences UI to trigger relevant requests.

**Instructions**: Go to https://hackerone.com/settings/preferences.

**Expected Output**: Preferences page loaded.

**Success Indicators**:
- Page renders with slider and options
- No 404 or auth errors

### Step 4: Enable Bounty-Only Invitations
procedure: [[procedures/Enable-Bounty-Only-Invitations]]

**Objective**: Activate the feature to expose the vulnerable slider.

**Instructions**: Toggle 'Only invite me for programs that award a Bounty' to on.

**Expected Output**: Option enabled, slider appears.

**Success Indicators**:
- UI confirms toggle
- Slider visible for min bounty adjustment

### Step 5: Intercept and Modify GraphQL Mutation
procedure: [[procedures/Intercept-and-Modify-GraphQL-Mutation]]

**Objective**: Capture the UpdateInvitationPreferencesMutation and tamper with min_bounty.

**Instructions**: Adjust the slider to trigger a request, intercept in Burp, edit JSON to set min_bounty to 7000, and forward.

**Expected Output**: Server responds with 200 OK and was_successful: true.

**Success Indicators**:
- Modified request sent successfully
- No validation errors from server

### Step 6: Verify the Update
procedure: [[procedures/Verify-Min-Bounty-Update]]

**Objective**: Confirm the arbitrary value is persisted and affects invitations.

**Instructions**: Query UserInvitationSettingsQuery via Burp or UI refresh to check min_bounty value.

**Expected Output**: Query returns min_bounty: 7000.0.

**Success Indicators**:
- Value exceeds UI limit (e.g., average bounty 600.625)
- Future invitations filtered accordingly

## Attack Chain Summary

### Key Achievements

1. Bypassed client-side slider limit on minimum critical bounty.
2. Updated preferences via unvalidated GraphQL mutation.
3. Enabled selective access to higher-paying private programs.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T12:00:00Z*
