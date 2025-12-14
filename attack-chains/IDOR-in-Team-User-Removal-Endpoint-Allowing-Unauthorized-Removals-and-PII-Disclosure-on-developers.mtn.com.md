---
tags:
  - idor
  - information-disclosure
  - web-vulnerability
  - brute-force
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Test-Accounts-and-Invite-Users]]'
  - '[[procedures/Intercept-and-Modify-Removal-Request-with-Burp-Suite]]'
  - '[[procedures/Exploit-IDOR-for-Unauthorized-User-Removal]]'
  - '[[procedures/Brute-Force-Mass-User-Removals-with-Burp-Intruder]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:36.557Z'
description: >-
  Multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in the
  team user removal endpoint to remove any user from any team and disclose PII
  via brute-force on 4-digit IDs.
skill_level: intermediate
impact_level: high
id: fd5c8219-ec80-4230-890c-f76aef50e959
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# IDOR in Team User Removal Endpoint Allowing Unauthorized Removals and PII Disclosure on developers.mtn.com

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in the team user removal endpoint on developers.mtn.com, combined with information disclosure, allowing any authenticated user to disrupt team structures and expose PII.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~12-20 hours for full brute-force |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Setup and Invites] --> B[Intercept Legitimate Request]
    B --> C[Modify for Unauthorized Removal]
    C --> D[Brute-Force Mass Disruption]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform: developers.mtn.com
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to the target site

### Initial Access Requirements

- Authenticated user account on developers.mtn.com
- Ability to create multiple test accounts
- No prior privileged access needed; any authenticated user suffices

## Detailed Attack Procedures

### Step 1: Account Setup and Invites
procedure: [[procedures/Create-Test-Accounts-and-Invite-Users]]

**Objective**: Establish test accounts and team relationships to prepare for intercepting a legitimate removal request.

**Instructions**: Create three test accounts (A, B, C) with assigned user_ids (1111, 1112, 1113) and team_ids (0001, 0002, 0003). Log in to Account A and invite B to Team A. Then log in to Account B and invite C to Team B.

**Expected Output**: Users B and C added to respective teams, ready for removal testing.

**Success Indicators**:
- Invitation emails or confirmations received
- Team memberships visible in the dashboard

### Step 2: Intercept Legitimate Removal Request
procedure: [[procedures/Intercept-and-Modify-Removal-Request-with-Burp-Suite]]

**Objective**: Capture a valid team user removal request to understand the endpoint parameters.

**Instructions**: Configure [[tools/Burp-Suite]] as a proxy. Log in to Account A and attempt to remove B from Team A while intercepting the HTTP request. Forward the intercepted request to the Repeater tab for analysis.

**Expected Output**: Captured POST request to the removal endpoint showing user_id and team_id parameters.

**Success Indicators**:
- Request intercepted successfully
- Parameters like user_id=1112 and team_id=0001 visible

### Step 3: Exploit IDOR for Unauthorized Removal
procedure: [[procedures/Exploit-IDOR-for-Unauthorized-User-Removal]]

**Objective**: Modify the request to target unauthorized team and user, demonstrating IDOR and PII disclosure.

**Instructions**: In Burp Repeater, change team_id to 0002 (Team B) and user_id to 1113 (User C). Send the modified request. Observe the response and any email notifications.

**Expected Output**: User C removed from Team B; response discloses username and team name PII.

**Success Indicators**:
- Removal successful without authorization
- PII (e.g., "User C removed from Team B") in response
- Email notification sent to User C

### Step 4: Brute-Force Mass Removals
procedure: [[procedures/Brute-Force-Mass-User-Removals-with-Burp-Intruder]]

**Objective**: Scale the exploit to disrupt all teams by brute-forcing 4-digit IDs.

**Instructions**: From a captured request, send to Burp Intruder. Configure payload positions for user_id and team_id (0000-9999). Run the attack to test all combinations.

**Expected Output**: Successful removals for valid ID pairs; estimated 12-20 hours to complete 10,000 x 10,000 requests.

**Success Indicators**:
- Multiple successful responses indicating removals
- Team disruptions confirmed via site or notifications

## Attack Chain Summary

### Key Achievements

1. Unauthorized removal of users from teams via IDOR
2. Disclosure of PII including usernames and team names
3. Potential for complete team disruption through brute-force

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
