---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - authorization-bypass
  - impersonation
  - twitter-ads
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Assign-Ad-Manager-Role-to-User]]'
  - '[[procedures/Switch-to-Target-Ads-Dashboard]]'
  - '[[procedures/Compose-Promoted-Tweet-in-Campaign]]'
  - '[[procedures/Intercept-and-Modify-Tweet-Request]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.741Z'
description: >-
  Multi-stage attack exploiting role-based access control flaw in Twitter's Ads
  & Analytics to allow Ad Managers to post regular tweets on behalf of account
  owners by manipulating HTTP parameters.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Authorization Bypass in Twitter Ads for Unauthorized Account Tweeting

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in Twitter's (now X) Ads & Analytics feature, allowing users with Ad Manager roles to post regular tweets on behalf of account owners by bypassing the 'nullcast_flag' parameter restriction.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Assign Ad Manager Role] --> B[Switch to Target Dashboard]
    B --> C[Compose Promoted Tweet]
    C --> D[Intercept and Modify Request]
    D --> E[Unauthorized Tweet Posted]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Twitter Ads & Analytics service
- Access to Twitter accounts with administrative privileges

### Initial Access Requirements

- Valid Twitter account with ability to manage ads
- Target account credentials or shared access
- Network access to https://ads.twitter.com

## Detailed Attack Procedures

### Step 1: Assign Ad Manager Role
procedure: [[procedures/Assign-Ad-Manager-Role-to-User]]

**Objective**: Grant a user the Ad Manager role on the target account to enable creation of promoted tweets.

**Instructions**: Navigate to the account users management page and add the user with the appropriate permission.

**Expected Output**: User added successfully with 'Allow user to create new Promoted-only Tweets' enabled.

**Success Indicators**:
- Confirmation message on user addition
- User listed in account users with Ad Manager role

### Step 2: Switch to Target Dashboard
procedure: [[procedures/Switch-to-Target-Ads-Dashboard]]

**Objective**: Access the target account's ads dashboard using the assigned user's credentials.

**Instructions**: From the assigned user's account, use the switch accounts feature to select the target.

**Expected Output**: Dashboard loads for the target account.

**Success Indicators**:
- Successful account switch
- Ads dashboard visible for target account

### Step 3: Compose Promoted Tweet
procedure: [[procedures/Compose-Promoted-Tweet-in-Campaign]]

**Objective**: Initiate the creation of a promoted tweet within a campaign, triggering the vulnerable HTTP request.

**Instructions**: In the dashboard, create a new promoted tweet, which generates a POST request with nullcast_flag=1.

**Expected Output**: Tweet composition interface active; request intercepted if using proxy.

**Success Indicators**:
- Tweet box opens
- HTTP request visible in Burp Suite

### Step 4: Intercept and Modify Request
procedure: [[procedures/Intercept-and-Modify-Tweet-Request]]

**Objective**: Remove the nullcast_flag parameter to convert the promoted tweet request into a regular tweet post.

**Instructions**: Use Burp Repeater to edit and resend the request without the parameter.

**Expected Output**: Tweet posted to the owner's public timeline.

**Success Indicators**:
- Tweet appears on target account's timeline
- No errors in request response

## Attack Chain Summary

### Key Achievements

1. Bypassed role restrictions to post unauthorized content
2. Enabled impersonation via legitimate but abused account roles
3. Demonstrated failure in server-side parameter validation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---
*Last updated: 2023-10-01T12:00:00Z*
