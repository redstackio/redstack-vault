---
id: ac-uuid-001
tags:
  - broken-access-control
  - privilege-escalation
  - shopify
  - graphql
  - pos-staff
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enable-POS-Staff-Feature-via-GraphQL-Response-Modification]]'
  - '[[procedures/Create-POS-Staff-Member-in-Restricted-Environment]]'
  - '[[procedures/Delete-POS-Staff-as-Low-Privilege-User]]'
step_count: 3
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:20.168Z'
description: >-
  A multi-stage attack exploiting broken access controls in Shopify to bypass a
  beta flag and enable low-privilege staff to delete POS staff accounts.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
---
# Unauthorized POS Staff Deletion via Beta Flag Bypass in Shopify

Multi-stage attack chain demonstrating a complete attack workflow exploiting broken access controls in Shopify's POS staff management.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enable POS Feature] --> B[Create POS Staff]
    B --> C[Delete POS Staff]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Shopify Plus Partner Sandbox environment
- Web platform with GraphQL API
- POS staff features disabled by default

### Initial Access Requirements

- Authenticated admin session in Shopify admin panel
- Low-privilege staff account for deletion phase
- Network access to /admin and /graphql-proxy/admin endpoints

## Detailed Attack Procedures

### Step 1: Enable POS Staff Feature
procedure: [[procedures/Enable-POS-Staff-Feature-via-GraphQL-Response-Modification]]

**Objective**: Bypass the client-side beta flag to enable POS staff management in a restricted sandbox environment.

**Instructions**: Access the Shopify POS app from an admin session, intercept the GraphQL Overview query using Burp Suite, and modify the response to flip the staffPermissionsBetaFlag to true. Refresh the page to access the management area.

**Expected Output**: UI updates to show 'Manage POS staff' option.

**Success Indicators**:
- GraphQL response modified successfully
- POS staff management UI becomes visible

### Step 2: Create POS Staff Member
procedure: [[procedures/Create-POS-Staff-Member-in-Restricted-Environment]]

**Objective**: Add a new POS staff account now that the feature is enabled, setting up the target for unauthorized deletion.

**Instructions**: Navigate to the 'Manage POS staff' section, enter details such as first name, last name, email, and a generated PIN, then save the new staff member. Verify visibility in account settings.

**Expected Output**: New POS staff member listed in /admin/settings/account.

**Success Indicators**:
- POS staff added without errors
- Staff appears in account settings below regular staff

### Step 3: Delete POS Staff as Low-Privilege User
procedure: [[procedures/Delete-POS-Staff-as-Low-Privilege-User]]

**Objective**: Demonstrate broken access controls by deleting the POS staff using a staff account with no permissions.

**Instructions**: Log in as a low-privilege staff member, navigate to /admin/settings/account, locate the POS staff section, and click delete. The action succeeds without authorization checks.

**Expected Output**: POS staff account deleted successfully.

**Success Indicators**:
- Deletion completes without permission errors
- POS staff no longer visible in settings

## Attack Chain Summary

### Key Achievements

1. Bypassed beta flag restriction via client-side response tampering
2. Created POS staff in a disabled feature environment
3. Achieved unauthorized deletion causing operational inconvenience

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
