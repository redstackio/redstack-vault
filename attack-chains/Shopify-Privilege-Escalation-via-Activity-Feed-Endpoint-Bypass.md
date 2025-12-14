---
id: ac-uuid-1234
tags:
  - broken-access-control
  - privilege-escalation
  - information-disclosure
  - shopify
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Test-Users-in-Shopify]]'
  - '[[procedures/Access-Activity-Feed-as-Admin]]'
  - '[[procedures/Attempt-Access-as-Limited-User]]'
  - '[[procedures/Observe-Paginated-Endpoint]]'
  - '[[procedures/Bypass-Access-via-Paginated-Endpoint]]'
step_count: 5
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:52.140Z'
description: >-
  Demonstrates improper access control in Shopify admin allowing limited users
  to bypass permissions and access sensitive activity feed data.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
---
# Shopify Privilege Escalation via Activity Feed Endpoint Bypass

Multi-stage attack chain demonstrating improper access control in Shopify's admin panel, where users with limited 'Overviews' permissions can bypass restrictions to access the full Activity Feed, normally restricted to 'Home' permission holders. This leads to privilege escalation and unauthorized disclosure of sensitive shop events.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Test Users] --> B[Admin Access Activity]
    B --> C[Limited User Blocked]
    C --> D[Observe Endpoint]
    D --> E[Bypass via Paginated Feed]
    E --> F[View Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)
- Access to a Shopify test shop

### Target Environment

- Shopify admin panel
- Authenticated sessions

### Initial Access Requirements

- Shopify account owner credentials
- Ability to create limited access users

## Detailed Attack Procedures

### Step 1: Create Test Users
procedure: [[procedures/Create-Test-Users-in-Shopify]]

**Objective**: Set up admin and limited users to test permissions.

**Instructions**: Log in as shop owner and create users with specific roles.

**Expected Output**: Two users created: full admin (X) and limited (Y with Overviews only).

**Success Indicators**:
- User X has full permissions
- User Y restricted to Sales Channels Overviews

### Step 2: Access Activity Feed as Admin
procedure: [[procedures/Access-Activity-Feed-as-Admin]]

**Objective**: Verify normal admin access to activity feed.

**Instructions**: Log in as User X and navigate to the activity page.

**Expected Output**: Full activity feed visible at /admin/activity.

**Success Indicators**:
- Activities load without errors
- Pagination options available

### Step 3: Attempt Access as Limited User
procedure: [[procedures/Attempt-Access-as-Limited-User]]

**Objective**: Confirm limited user is blocked from main activity page.

**Instructions**: Log in as User Y and try to access /admin/activity.

**Expected Output**: Access denied due to insufficient permissions.

**Success Indicators**:
- Error message or redirect for insufficient perms

### Step 4: Observe Paginated Endpoint
procedure: [[procedures/Observe-Paginated-Endpoint]]

**Objective**: Identify the backend endpoint used for loading more activities.

**Instructions**: As admin, interact with pagination to capture the endpoint URL.

**Expected Output**: Endpoint /admin/dashboard/activity_feed with parameters noted.

**Success Indicators**:
- Endpoint URL and params (activity_pages, activity_filter) identified

### Step 5: Bypass Access via Paginated Endpoint
procedure: [[procedures/Bypass-Access-via-Paginated-Endpoint]]

**Objective**: Exploit the endpoint to gain unauthorized access as limited user.

**Instructions**: As User Y, directly access the paginated endpoint.

**Expected Output**: Full activity feed data returned, disclosing sensitive events.

**Success Indicators**:
- Limited user views all shop activities
- No permission checks enforced

## Attack Chain Summary

### Key Achievements

1. Demonstrated permission bypass in Shopify admin
2. Achieved privilege escalation for limited users
3. Exposed sensitive shop owner activities

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
