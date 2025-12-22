---
tags:
  - gitlab
  - graphql
  - access-control
  - type-confusion
  - repository-deletion
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/GraphiQL-Explorer]]'
tactics:
  - '[[Impact]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/destroy-snippet-mutation-diffnote]]'
  - '[[commands/destroy-snippet-mutation-project]]'
  - '[[commands/gitlab-env-info]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-GitLab-Users-and-Project]]'
  - '[[procedures/Create-Merge-Request-and-DiffNote]]'
  - '[[procedures/Extract-DiffNote-ID-with-Burp-Suite]]'
  - '[[procedures/Execute-DestroySnippet-Mutation]]'
  - '[[procedures/Verify-Repository-Deletion]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:25:53.163Z'
description: >-
  Attack chain exploiting insufficient type checking in GitLab's GraphQL
  destroySnippet mutation, allowing maintainers to delete project repositories
  using DiffNote global IDs.
skill_level: intermediate
impact_level: high
id: f5052ce4-fe4f-4ca3-b3de-83b7485ceaaa
validated: true
mitre_tactics:
  - '[[Impact]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
---
# GitLab Maintainer Repository Deletion via GraphQL Type Confusion

Multi-stage attack chain demonstrating exploitation of improper access control in GitLab's GraphQL API, where maintainers can delete entire project repositories by abusing the destroySnippet mutation with DiffNote global IDs due to missing type validation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Users and Project] --> B[Create Merge Request and DiffNote]
    B --> C[Extract DiffNote ID]
    C --> D[Execute GraphQL Mutation]
    D --> E[Verify Deletion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/GraphiQL-Explorer]]

### Target Environment

- GitLab instance (e.g., version 12.10.0-ee)
- Required services: Redis, Git, Sidekiq, PostgreSQL
- Tech stack: Ruby on Rails, GraphQL, PostgreSQL
- Network access: Authenticated access as maintainer

### Initial Access Requirements

- Two GitLab accounts: Owner (User A) and Maintainer (User B)
- Maintainer role on the target project
- Access to GraphiQL explorer (/api/graphql/explorer)

## Detailed Attack Procedures

### Step 1: Setup Users and Project
procedure: [[procedures/Setup-GitLab-Users-and-Project]]

**Objective**: Establish test environment with owner and maintainer roles, create project and branches to prepare for merge request.

**Instructions**: Register two users, create a project, assign maintainer role, and set up branches with differing file content.

**Expected Output**: Project ready with branches (e.g., main and feature) containing a file with different content.

**Success Indicators**:
- User B has maintainer permissions confirmed
- Branches created and visible in project

### Step 2: Create Merge Request and DiffNote
procedure: [[procedures/Create-Merge-Request-and-DiffNote]]

**Objective**: Generate a merge request to expose diff view and create a DiffNote for ID extraction.

**Instructions**: Create merge request between branches, then add a comment on a diff line to generate DiffNote.

**Expected Output**: Merge request active with DiffNote created.

**Success Indicators**:
- Merge request visible in project
- DiffNote comment appears in the MR discussion

### Step 3: Extract DiffNote ID with Burp Suite
procedure: [[procedures/Extract-DiffNote-ID-with-Burp-Suite]]

**Objective**: Delete a DiffNote to capture its global ID via intercepted request, then create a new one for the next incremental ID.

**Instructions**: Use Burp Suite to proxy and extract ID (e.g., gid://gitlab/DiffNote/116) during deletion, recreate DiffNote for ID 117 or 118.

**Expected Output**: Global ID of DiffNote obtained.

**Success Indicators**:
- ID extracted from HTTP request (e.g., in Burp's proxy history)
- New DiffNote created successfully

### Step 4: Execute DestroySnippet Mutation
procedure: [[procedures/Execute-DestroySnippet-Mutation]]

**Objective**: Use the DiffNote global ID in the destroySnippet GraphQL mutation to trigger repository deletion.

**Instructions**: In GraphiQL explorer, run the mutation with the extracted ID using [[commands/destroy-snippet-mutation-diffnote]]:

```graphql
mutation test { destroySnippet(input: {id: "gid://gitlab/DiffNote/118"}) { errors } }
```

**Expected Output**: Mutation succeeds with no errors; repository deleted.

**Success Indicators**:
- No errors in GraphQL response
- Project repository inaccessible

### Step 5: Verify Repository Deletion
procedure: [[procedures/Verify-Repository-Deletion]]

**Objective**: Confirm the impact of deletion, including 404 errors and project lingering in user list.

**Instructions**: Attempt to access or create repository in the project; run [[commands/gitlab-env-info]] for environment confirmation if needed.

**Expected Output**: Project page 404s on repository actions, but project still listed.

**Success Indicators**:
- 404 error on repository creation
- Project visible in dashboard but inaccessible

## Attack Chain Summary

### Key Achievements

1. Bypassed snippet-only deletion to target project repository
2. Exploited type confusion in authorized_find! without object validation
3. Achieved unauthorized data destruction as a maintainer

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Data Destruction]]

### MITRE ATT&CK Tactics

- [[Impact]]
- [[Privilege Escalation]]

---

*Last updated: 2023-10-01T00:00:00Z*
