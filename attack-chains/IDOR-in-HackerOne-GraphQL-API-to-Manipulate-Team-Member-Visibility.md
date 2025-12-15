---
tags:
  - idor
  - graphql
  - authorization-bypass
  - web
  - hackerone
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
  - '[[Impact]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Login-and-Capture-GraphQL-Visibility-Request]]'
  - '[[procedures/Decode-and-Obtain-Target-Team-Member-ID]]'
  - '[[procedures/Modify-GraphQL-Request-for-IDOR-Exploitation]]'
step_count: 4
techniques:
  - '[[Account Discovery]]'
  - '[[Data Manipulation]]'
description: >-
  Authenticated users exploit an Insecure Direct Object Reference in HackerOne's
  GraphQL API to unauthorizedly change other team members' profile visibility
  settings, revealing or concealing team affiliations.
skill_level: intermediate
impact_level: medium
id: c7dfbd12-9122-436d-89de-a6e97a99933c
created_at: '2025-12-14T17:25:33.503Z'
updated_at: '2025-12-14T17:25:33.503Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Data Manipulation]]'
---
# IDOR in HackerOne GraphQL API to Manipulate Team Member Visibility

## Overview

This attack chain exploits an Insecure Direct Object Reference (IDOR) vulnerability in HackerOne's GraphQL API, specifically the Update_team_member_visibility_mutation. An authenticated team member can capture their own visibility update request, decode the base64-encoded team_member_id, replace it with another team member's ID obtained from a public endpoint, and forward the modified request to change the victim's profile visibility (Revealed or Concealed) without authorization. This mismatches intended backend behavior (manager-only access) with frontend UI controls, allowing unauthorized manipulation of team affiliations and privacy settings. The vulnerability was reported as a duplicate but highlights API authorization gaps.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login and Capture Request] --> B[Decode and Obtain IDs]
    B --> C[Modify Request]
    C --> D[Exploit Visibility Change]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform with GraphQL API (HackerOne instance)
- Required services/ports: HTTPS on port 443
- Network access requirements: Authenticated access to HackerOne

### Initial Access Requirements

- Valid HackerOne account with team membership
- Network position: Direct internet access
- Prior access needed: None beyond authentication

## Detailed Attack Procedures

### Step 1: Login and Capture GraphQL Visibility Request
procedure: [[procedures/Login-and-Capture-GraphQL-Visibility-Request]]

**Objective**: Authenticate and intercept the GraphQL mutation request triggered by changing personal team visibility to understand the request structure.

**Instructions**: Log in to HackerOne, navigate to team settings, and use Burp Suite to capture the POST request sent to /graphql when toggling visibility.

**Expected Output**: Intercepted request body containing the Update_team_member_visibility_mutation with base64-encoded team_member_id in variables.input_0.

**Success Indicators**:
- Request captured successfully
- team_member_id parameter visible in the request

### Step 2: Decode and Obtain Target Team Member IDs
procedure: [[procedures/Decode-and-Obtain-Target-Team-Member-ID]]

**Objective**: Extract the numeric ID from the captured request and retrieve victim IDs from the public team members endpoint.

**Instructions**: Base64-decode the team_member_id (e.g., 'Z2lkOi8vaGFja2Vyb25lL1RlYW1NZW1iZXIvNDM3OTQ=' to 'gid://hackerone/TeamMember/43794'). Then access the public JSON endpoint like https://hackerone.com/parrot_sec/team_members.json to list team_member_ids.

**Expected Output**: Decoded Global ID format and a JSON array of victim team_member_ids.

**Success Indicators**:
- Own ID decoded correctly
- Victim IDs retrieved from public endpoint

### Step 3: Modify GraphQL Request for IDOR Exploitation
procedure: [[procedures/Modify-GraphQL-Request-for-IDOR-Exploitation]]

**Objective**: Alter the request to target a victim's team_member_id and change their visibility setting.

**Instructions**: In Burp Suite, replace the team_member_id with the victim's (e.g., 'gid://hackerone/TeamMember/<victim_id>'), set 'concealed' to true/false, add 'clientMutationId' if needed, and forward the POST to /graphql.

**Expected Output**: Successful GraphQL response indicating the mutation applied, with the victim's visibility updated.

**Success Indicators**:
- Response status 200 with no errors
- Victim's profile visibility changed upon verification

## Attack Chain Summary

### Key Achievements

1. Captured and understood the GraphQL mutation for visibility updates
2. Bypassed authorization via IDOR to target other team members
3. Unauthorizedly modified team visibility, impacting privacy and affiliations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]
- [[Data Manipulation]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
