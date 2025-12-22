---
tags:
  - authorization-bypass
  - idor
  - broken-access-control
  - helium-console
  - device-management
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Accounts-and-Invite-Read-Only-User]]'
  - '[[procedures/Extract-Organization-ID-via-Delete-Request-Interception]]'
  - '[[procedures/Tamper-Device-Name-Update-Request-with-Org-ID]]'
  - '[[procedures/Verify-Device-Name-Modification-in-Admin-Account]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.400Z'
description: >-
  Multi-stage attack exploiting broken access control in Helium console to
  enable read-only users to update device names in admin organizations via IDOR
  and request tampering.
skill_level: intermediate
impact_level: medium
id: 5e5639ab-647d-4a84-9786-8410bd3dbe13
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Authorization Bypass in Helium Console Allowing Read-Only Users to Modify Admin Device Names

Multi-stage attack chain demonstrating a complete workflow to bypass authorization in the Helium console, allowing a read-only invited user to modify device names in an admin's organization through Insecure Direct Object Reference (IDOR) and HTTP request tampering.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Accounts and Invite Read-Only User] --> B[Extract Organization ID]
    B --> C[Tamper Device Update Request]
    C --> D[Verify Modification in Admin Account]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Helium Console web platform
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to console.helium.com

### Initial Access Requirements

- Ability to register new accounts on Helium console
- Admin account (Account A) with organization creation privileges
- Read-only invited user (Account B)

## Detailed Attack Procedures

### Step 1: Setup Accounts and Invite Read-Only User
procedure: [[procedures/Setup-Accounts-and-Invite-Read-Only-User]]

**Objective**: Establish the admin-victim (A) and attacker (B) accounts, granting B read-only access to A's organization to set up the authorization bypass scenario.

**Instructions**: Register two separate accounts on console.helium.com. From Account A, create an organization and invite Account B with read-only permissions.

**Expected Output**: Invitation accepted; B can view but not modify A's organization.

**Success Indicators**:
- Account B receives and accepts read-only invite
- B can browse A's devices but cannot perform write actions

### Step 2: Extract Organization ID via Delete Request Interception
procedure: [[procedures/Extract-Organization-ID-via-Delete-Request-Interception]]

**Objective**: Use a proxy to intercept a failed delete request from B's session to obtain the target organization's ID, which will be used for unauthorized updates.

**Instructions**: Log in as B, attempt to delete the organization from A's invite, and intercept the request using Burp Suite to capture the organization ID from the request body or parameters.

**Expected Output**: Organization ID (e.g., a UUID like "org_123abc") extracted from the intercepted HTTP DELETE request.

**Success Indicators**:
- Delete attempt fails due to read-only permissions
- Organization ID successfully captured in proxy logs

### Step 3: Tamper Device Name Update Request with Org ID
procedure: [[procedures/Tamper-Device-Name-Update-Request-with-Org-ID]]

**Objective**: From B's account, add a device, intercept its name update request, inject the extracted organization ID, and forward the modified request to alter a device name in A's organization.

**Instructions**: In B's session, add a new device and initiate a name update. Intercept the POST/PUT request in Burp Suite, insert the organization ID into the request body (e.g., as "organization_id": "org_123abc"), and forward it.

**Expected Output**: Server accepts the tampered request; device name updates without permission errors.

**Success Indicators**:
- Modified request forwarded successfully
- No immediate server rejection of the update

### Step 4: Verify Device Name Modification in Admin Account
procedure: [[procedures/Verify-Device-Name-Modification-in-Admin-Account]]

**Objective**: Confirm the unauthorized change by checking the admin account's view of the organization.

**Instructions**: Log in to Account A and navigate to the organization's device list to observe the altered device name.

**Expected Output**: Device name in A's view matches the tampered value set from B.

**Success Indicators**:
- Altered name visible in admin dashboard
- Confirmation of bypass: read-only user effected a write operation

## Attack Chain Summary

### Key Achievements

1. Established controlled accounts to simulate admin-victim and read-only attacker scenarios
2. Extracted sensitive organization ID through intercepted failed actions
3. Bypassed authorization to perform unauthorized device name modifications via IDOR
4. Verified impact, demonstrating potential for confusion or tampering in device management

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Defense Evasion]] Defense Evasion

---
*Last updated: 2023-10-01T00:00:00Z*
