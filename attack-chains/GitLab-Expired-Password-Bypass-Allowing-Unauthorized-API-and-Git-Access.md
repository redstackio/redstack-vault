---
tags:
  - gitlab
  - access-control
  - auth-bypass
  - api
  - token
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-GitLab-User-and-Private-Project]]'
  - '[[procedures/Generate-Personal-Access-Token]]'
  - '[[procedures/Expire-User-Password-as-Admin]]'
  - '[[procedures/Exploit-API-Access-with-Expired-Token]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:32:29.260Z'
description: >-
  Attack chain exploiting improper access control in GitLab where expired
  passwords do not invalidate personal access tokens, enabling unauthorized
  access to private projects via REST API, GraphQL, and Git endpoints.
skill_level: intermediate
impact_level: medium
id: 0ef7b607-ffa4-41db-adbc-2202bfe40dd2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---
# GitLab Expired Password Bypass Allowing Unauthorized API and Git Access

Multi-stage attack chain demonstrating improper access control in GitLab versions around 14.1.0, where users with expired passwords retain full access to REST API, GraphQL API, and Git HTTP endpoints via personal access tokens or OAuth tokens. This bypasses password expiration security, allowing unauthorized actions on private projects such as pulling/pushing code and API queries. The root cause is a flawed patch in the User model's password expiration logic that reintroduces access for non-LDAP users.

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
    A[Setup User and Project] --> B[Generate Token]
    B --> C[Expire Password]
    C --> D[Exploit Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Self-hosted GitLab instance (e.g., version 14.1.0)
- Administrator access for password expiration
- Network access to GitLab web interface and API endpoints

### Initial Access Requirements

- Valid user credentials for initial setup
- Admin credentials to modify user accounts
- No prior compromise needed; assumes legitimate access for testing

## Detailed Attack Procedures

### Step 1: Setup User and Private Project
procedure: [[procedures/Setup-GitLab-User-and-Private-Project]]

**Objective**: Create a test user and a private project to serve as the target for unauthorized access demonstration.

**Instructions**: Register a new user account, log in, and create a private project while noting its ID for later API calls.

**Expected Output**: Successful user login and private project creation with visible project ID in the URL.

**Success Indicators**:
- User 'user01' account active and logged in
- Private project created at https://gitlab.domain.com/projects/new#blank_project with recorded ID

### Step 2: Generate Personal Access Token
procedure: [[procedures/Generate-Personal-Access-Token]]

**Objective**: Obtain a personal access token for the user to use in API requests post-password expiration.

**Instructions**: Navigate to the user's profile settings and create a token with appropriate scopes (e.g., api, read_repository).

**Expected Output**: Token generated and copied for use in subsequent steps.

**Success Indicators**:
- Token visible in user profile at https://gitlab.domain.com/-/profile/personal_access_tokens
- Token valid for API authentication

### Step 3: Expire User Password as Admin
procedure: [[procedures/Expire-User-Password-as-Admin]]

**Objective**: Simulate password expiration by modifying the user account as an administrator, locking out UI login but not tokens.

**Instructions**: Log in as admin, edit the user account, and set the password to expire by changing it, which updates 'password expired at' to current time.

**Expected Output**: User login fails with old password; new password prompts for update but is left incomplete to maintain expired state.

**Success Indicators**:
- Admin edit at https://gitlab.domain.com/admin/users/user01/edit completes
- User UI login blocked due to expiration

### Step 4: Exploit API Access with Expired Token
procedure: [[procedures/Exploit-API-Access-with-Expired-Token]]

**Objective**: Demonstrate unauthorized access to private project resources using the still-valid token.

**Instructions**: Use the token to query the private project API endpoint, confirming access despite expiration.

Execute [[commands/curl-gitlab-api-access]]:

```bash
curl --request GET --url https://gitlab.domain.com/api/v4/projects/:ID --header 'Authorization: Bearer <TOKEN>'
```

Replace :ID with the project ID and <TOKEN> with the generated token.

**Expected Output**: JSON response with private project details, including name, visibility, and permissions.

**Success Indicators**:
- API returns project data without authentication errors
- Confirms token bypasses password expiration

## Attack Chain Summary

### Key Achievements

1. Bypassed password expiration to retain API and Git access
2. Accessed private project resources unauthorized via tokens
3. Highlighted flaw in GitLab's User model password check logic

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[External Remote Services]] External Remote Services

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---

*Last updated: 2023-10-01T00:00:00Z*
