---
tags:
  - sso-bypass
  - zendesk
  - graphql
  - email-verification-bypass
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/graphql-zendesk-token-query]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Register-Unverified-Email-on-Trint]]'
  - '[[procedures/Intercept-GraphQL-Request-with-Burp-Suite]]'
  - '[[procedures/Execute-GraphQL-Query-for-Zendesk-Token]]'
  - '[[procedures/Craft-Zendesk-SSO-URL]]'
  - '[[procedures/Access-Internal-Zendesk-Tickets]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack exploiting lack of email verification in Trint to bypass
  Zendesk SSO and access internal tickets
skill_level: intermediate
impact_level: high
id: c766114f-66c0-4969-8fb4-f933f4dfa115
created_at: '2025-12-13T09:01:26.375Z'
updated_at: '2025-12-13T09:01:26.375Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# SSO Bypass via Unverified Email Registration in Trint Leading to Zendesk Access

Multi-stage attack chain demonstrating how to exploit the lack of email verification in Trint's registration process to obtain a Zendesk JWT token and bypass SSO, ultimately accessing internal ticket information.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Register Email] --> B[Intercept Request]
    B --> C[Query Token]
    C --> D[Craft URL]
    D --> E[Access Tickets]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#2ecc71
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Required services: Trint API, Zendesk
- Network access requirements: Public internet access to app.trint.com and graphql2.trint.com

### Initial Access Requirements

- No prior credentials needed
- Ability to register on app.trint.com
- Network position: External attacker

## Detailed Attack Procedures

### Step 1: Register Unverified Email
procedure: [[procedures/Register-Unverified-Email-on-Trint]]

**Objective**: Create an account using an organization domain email without verification to gain initial access.

**Instructions**: Navigate to app.trint.com and complete the registration process using an email like support+1@trint.com. No email verification is required, allowing claim of the organization's domain.

**Expected Output**: Successful account registration and login to app.trint.com.

**Success Indicators**:
- Account created
- Access to Trint dashboard

### Step 2: Intercept GraphQL Request
procedure: [[procedures/Intercept-GraphQL-Request-with-Burp-Suite]]

**Objective**: Use Burp Suite to capture and identify the GraphQL request for token retrieval.

**Instructions**: Configure Burp Suite as a proxy, browse the Trint application, and review the request history to find the POST request to https://graphql2.trint.com/.

**Expected Output**: Identified GraphQL POST request in Burp history.

**Success Indicators**:
- GraphQL endpoint captured
- Request details available for replication

### Step 3: Execute GraphQL Query for Zendesk Token
procedure: [[procedures/Execute-GraphQL-Query-for-Zendesk-Token]]

**Objective**: Send a GraphQL query to retrieve the Zendesk JWT token using the registered account's authorization.

**Instructions**: Use [[commands/graphql-zendesk-token-query]] to send the POST request:

```bash
curl -X POST https://graphql2.trint.com/ \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2FwcC50cmludC5jb20vdXNlcklkIjoiNWRjOTUwZWEzOGFhMjI3MmExNzAyMzFkIiwiaHR0cHM6Ly9hcHAudHJpbnQuY29tL2lzTmV3VXNlciI6dHJ1ZSwiaHR0cHM6Ly9zY2hlbWEudHJpbnQuY29tL2F1dGhqdGkiOiI0ZmMwMjUyZS03NTFiLTQwNjctOWU0MC00OGQ4MWMzMjRiMjIiLCJpc3MiOiJodHRwczovL3RyaW50LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZGM5NTBlYTM4YWEyMjcyYTE3MDIzMWQiLCJhdWQiOiJ0cmludC1hcGlzIiwiaWF0IjoxNTczNDc0NTQyLCJleHAiOjE1NzYwNjY1NDIsImF6cCI6ImljaDRoeVZZUEtLZ2VFb1RoNmZXUFhjNmZydmVUY1RxIiwiZ3R5IjoicGFzc3dvcmQifQ.JyIc6PZyjidptrvaFT6MykOr0BopUi1F7fZWTvbeKeU' \
  -H 'Content-Type: application/json' \
  -d '{"operationName":null,"variables":{"status":"PENDING"},"query":"query zendeskToken {\n zendeskToken\n }\n"}'
```

**Expected Output**: JSON response with zendeskToken JWT.

**Success Indicators**:
- Valid JWT token received
- No authentication errors

### Step 4: Craft Zendesk SSO URL
procedure: [[procedures/Craft-Zendesk-SSO-URL]]

**Objective**: Construct a login URL using the obtained JWT to bypass SSO.

**Instructions**: Append the JWT to the URL: https://trintsupport.zendesk.com/access/jwt?jwt=<JWT_TOKEN> and access it in a browser.

**Expected Output**: Successful login to Zendesk as an organization member.

**Success Indicators**:
- SSO bypass confirmed
- Access to Zendesk dashboard

### Step 5: Access Internal Zendesk Tickets
procedure: [[procedures/Access-Internal-Zendesk-Tickets]]

**Objective**: Navigate to organization tickets to leak internal information.

**Instructions**: After login, visit https://support.trint.com/hc/en-us/requests/organization to view and read ticket details.

**Expected Output**: List of internal ticket requests and their contents.

**Success Indicators**:
- Tickets visible
- Sensitive information accessible

## Attack Chain Summary

### Key Achievements

1. Bypassed email verification for domain registration
2. Obtained valid Zendesk JWT via GraphQL
3. Gained unauthorized access to internal Zendesk resources

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

*Last updated: 2023-10-01*
