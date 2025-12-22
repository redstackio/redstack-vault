---
id: acme-gitlab-mr-bypass-001
tags:
  - gitlab
  - api
  - access-control
  - bypass
  - merge-request
  - unauthorized-access
type: attack_chain
tools:
  - '[[tools/Postman]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Private-Project-and-Invite-Developer]]'
  - '[[procedures/Create-Branch-and-Changes-as-Developer]]'
  - '[[procedures/Create-and-Assign-Merge-Request]]'
  - '[[procedures/Demote-User-to-Guest-Role]]'
  - '[[procedures/Generate-Personal-Access-Token]]'
  - '[[procedures/Query-Merge-Request-Data-via-API]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:11.105Z'
description: >-
  Demonstrates improper access control in GitLab API allowing demoted Guest
  users to access confidential Merge Request data via personal access tokens if
  previously assigned, bypassing web UI restrictions.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# GitLab API Access Control Bypass via Demoted User Merge Request Access

Multi-stage attack chain demonstrating improper access control in GitLab's API, where a user demoted from Developer to Guest can still access assigned Merge Request data via API endpoints using a personal access token, despite web UI restrictions. This exposes confidential project information in private repositories.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Project and User] --> B[Create Branch and MR] --> C[Demote User Role]
    C --> D[Generate Access Token] --> E[Query API for MR Data]
    E --> F[Access Confidential Info]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#f39c12
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Postman]]

### Target Environment

- GitLab instance (self-hosted or SaaS)
- Private project visibility
- Admin access to project settings
- Developer and Guest role capabilities

### Initial Access Requirements

- Valid GitLab account with admin privileges for setup
- Target user account for demotion and token generation
- Network access to GitLab UI and API (typically HTTPS on port 443)

## Detailed Attack Procedures

### Step 1: Create Private Project and Invite Developer

procedure: [[procedures/Create-Private-Project-and-Invite-Developer]]

**Objective**: Establish a private project and grant initial Developer access to the target user.

**Instructions**: Use the GitLab UI to create a new private project, then invite the target user as a Developer via project members settings.

**Expected Output**: Project created with user added as Developer; confirmation in project members list.

**Success Indicators**:
- Private project visibility confirmed
- User role shows as Developer

### Step 2: Create Branch and Changes as Developer

procedure: [[procedures/Create-Branch-and-Changes-as-Developer]]

**Objective**: Simulate development activity by creating a branch and making changes from the Developer account.

**Instructions**: Log in as the Developer user, create a new branch named 'test', and add or modify a file (e.g., create a new README.md).

**Expected Output**: New branch 'test' with committed changes visible in the repository.

**Success Indicators**:
- Branch created and pushed
- Changes committed to 'test' branch

### Step 3: Create and Assign Merge Request

procedure: [[procedures/Create-and-Assign-Merge-Request]]

**Objective**: Generate a Merge Request from the new branch and assign it to the Developer user to establish API access linkage.

**Instructions**: From the admin account, create an MR with source branch 'test' and target 'master', then assign it to the Developer user in the MR creation UI.

**Expected Output**: MR created with ID (e.g., 1) and assignee set to the Developer user.

**Success Indicators**:
- MR visible in project list
- Assignee confirmed as Developer user

### Step 4: Demote User to Guest Role

procedure: [[procedures/Demote-User-to-Guest-Role]]

**Objective**: Revoke Developer permissions by demoting the user to Guest, which should restrict access per web UI rules.

**Instructions**: From the admin account, navigate to project members settings and change the user's role from Developer to Guest.

**Expected Output**: User role updated to Guest; web UI access to MR restricted.

**Success Indicators**:
- Role change confirmed in members list
- Web UI shows no MR access for Guest user

### Step 5: Generate Personal Access Token

procedure: [[procedures/Generate-Personal-Access-Token]]

**Objective**: Create a personal access token from the demoted user's account with sufficient scopes for API access.

**Instructions**: Log in as the Guest user, go to user settings > Access Tokens, and generate a token selecting all scopes (e.g., api, read_api, write_api).

**Expected Output**: Token generated and copied; valid for API authentication.

**Success Indicators**:
- Token created successfully
- Token authentication tested (e.g., via simple API call)

### Step 6: Query Merge Request Data via API

procedure: [[procedures/Query-Merge-Request-Data-via-API]]

**Objective**: Exploit the API bypass to access confidential MR details using the token, confirming unauthorized exposure.

**Instructions**: Use [[tools/Postman]] or equivalent to send GET requests to endpoints like /api/v4/projects/[project_id]/merge_requests/[MR_id] with the token in the Authorization header. Test additional endpoints for participants, commits, changes, pipelines, approvals, and POST to /todo.

**Expected Output**: Full MR details returned, including title, description, commits, and ability to create TODOs, despite Guest role.

**Success Indicators**:
- API responses contain sensitive MR data
- Web UI access denied for comparison

## Attack Chain Summary

### Key Achievements

1. Bypassed role-based access controls in GitLab API post-demotion
2. Exposed confidential MR elements like changes, pipelines, and approvals
3. Demonstrated potential for information disclosure in private projects

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
