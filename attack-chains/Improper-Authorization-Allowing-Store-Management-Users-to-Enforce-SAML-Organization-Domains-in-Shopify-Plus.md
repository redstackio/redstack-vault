---
tags:
  - improper-authorization
  - graphql
  - shopify-plus
  - saml
  - auth-bypass
  - api-abuse
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
commands:
  - '[[commands/graphql-query-organization-domains]]'
  - '[[commands/graphql-enforce-saml-domains]]'
platforms:
  - Web
  - Shopify Plus
complexity: medium
procedures:
  - '[[procedures/Invite-Low-Privileged-User-with-Store-Management]]'
  - '[[procedures/Create-Organization-Domain-as-Admin]]'
  - '[[procedures/Login-as-Low-Privileged-User]]'
  - '[[procedures/Query-Organization-Domains-for-ID]]'
  - '[[procedures/Execute-enforceSamlOrganizationDomains-Mutation]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploitation for Privilege Escalation]]'
description: >-
  Multi-stage attack exploiting improper authorization in Shopify Plus GraphQL
  API, enabling low-privileged Store Management users to enforce SAML
  organization domains typically restricted to User Management permissions.
skill_level: intermediate
impact_level: medium
id: f583d8e4-daf7-49b6-be06-7d139afecbec
created_at: '2025-12-14T17:29:20.196Z'
updated_at: '2025-12-14T17:29:20.196Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Improper Authorization Allowing Store Management Users to Enforce SAML Organization Domains in Shopify Plus

## Overview

This attack chain demonstrates an improper authorization vulnerability in Shopify Plus, where users with only Store Management permissions can access and execute the `enforceSamlOrganizationDomains` GraphQL mutation, which is intended to be restricted to users with User Management permissions. The exploit begins with an organization admin inviting a low-privileged user, creating an organization domain, logging in as the low-privileged user, querying domain IDs via the GraphQL API, and finally enforcing SAML domains using those IDs. This could allow unauthorized modification of organization-wide authentication settings, though the impact is noted as limited in the original report.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Invite Low-Priv User] --> B[Create Org Domain]
    B --> C[Login as Low-Priv]
    C --> D[Query Domain IDs]
    D --> E[Enforce SAML Domains]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for authentication and navigation
- Intercepting proxy like Burp Suite for GraphQL requests

### Target Environment

- Shopify Plus organization account
- Access to admin dashboard at https://shopify.plus/:org_id
- GraphQL endpoint at /stores/api

### Initial Access Requirements

- Valid organization admin credentials for setup
- Network access to Shopify Plus domains
- No prior low-priv access needed; created during attack

## Detailed Attack Procedures

### Step 1: Invite Low-Privileged User
procedure: [[procedures/Invite-Low-Privileged-User-with-Store-Management]]

**Objective**: Create a user account with only Store Management permissions to simulate an unauthorized actor.

**Instructions**: As an organization admin, navigate to the user invitation page and invite a new user with Store Management access only.

**Expected Output**: Invitation email sent; user can register and access the store API.

**Success Indicators**:
- User invited successfully
- Low-priv user can log in to https://shopify.plus/:plus_org_id/stores/api

### Step 2: Create Organization Domain
procedure: [[procedures/Create-Organization-Domain-as-Admin]]

**Objective**: Set up an organization domain required for the SAML enforcement exploit.

**Instructions**: As the admin, visit the security settings and add a new domain to the organization.

**Expected Output**: Domain added to organization settings.

**Success Indicators**:
- Domain visible in organization security page
- Domain ID retrievable via GraphQL

### Step 3: Login as Low-Privileged User
procedure: [[procedures/Login-as-Low-Privileged-User]]

**Objective**: Authenticate as the Store Management user to gain access to the GraphQL endpoint with limited permissions.

**Instructions**: Use the invited user's credentials to log in to the Shopify Plus dashboard.

**Expected Output**: Successful login; session active for API calls.

**Success Indicators**:
- Access to store management features
- Ability to make GraphQL queries to /stores/api

### Step 4: Query Organization Domains
procedure: [[procedures/Query-Organization-Domains-for-ID]]

**Objective**: Retrieve the domain ID needed for the enforcement mutation using the low-priv account.

**Instructions**: Intercept a request to the GraphQL endpoint and execute a query to fetch organization domains. Use [[commands/graphql-query-organization-domains]]:

```bash
curl -X POST 'https://shopify.plus/34946971/stores/api' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"query":"query{organization{domains{id}}}"}'
```

**Expected Output**: JSON response with domain IDs, e.g., {"data":{"organization":{"domains":[{"id":"gid://..."}]}}.

**Success Indicators**:
- Domain ID extracted without errors
- No permission denied response

### Step 5: Execute SAML Enforcement
procedure: [[procedures/Execute-enforceSamlOrganizationDomains-Mutation]]

**Objective**: Use the low-priv account to enforce SAML domains, bypassing intended restrictions.

**Instructions**: Replace the domain ID in the mutation and POST to the GraphQL endpoint using [[commands/graphql-enforce-saml-domains]]:

```bash
curl -X POST 'https://shopify.plus/34946971/stores/api' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"query":"mutation { enforceSamlOrganizationDomains(domainIds:[\"gid://...\"]) { userErrors{message} } }"}'
```

**Expected Output**: JSON response showing successful enforcement or empty userErrors.

**Success Indicators**:
- Mutation executes without permission errors
- SAML domains enforced organization-wide

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to query sensitive organization data with low-priv account
2. Executed restricted GraphQL mutation for SAML configuration changes
3. Demonstrated potential for unauthorized auth setting modifications

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Lateral Movement]]

---
*Last updated: 2023-10-01*
