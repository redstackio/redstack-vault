---
data: >-
  curl -X POST 'https://hackerone.com/graphql?' -H 'Content-Type:
  application/json' -H 'X-Auth-Token: [TOKEN]' -H 'Cookie: [COOKIES]' -d
  '{"query":"query
  User_programs_settings_page($first_0:Int!,$first_3:Int!,$size_1:ProfilePictureSizes!,$size_2:ProfilePictureSizes!)
  {me {id,...Fb}} fragment F0 on Team {...}
  ...","variables":{"first_0":500,"first_3":25,"size_1":"small","size_2":"medium"}}'
tags:
  - graphql
  - query
  - teams
type: command
output: >-
  JSON response with user ID, username, memberships (total count, edges), and
  team policy subscriptions
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.386Z'
id: ad3ab20e-1dd0-4d06-b46b-56deb6ed5f31
verified: false
validated: true
submitted: true
---
# graphql-user-programs-query

## Command

```bash
curl -X POST 'https://hackerone.com/graphql?' -H 'Content-Type: application/json' -H 'X-Auth-Token: [TOKEN]' -H 'Cookie: [COOKIES]' -d '{"query":"query User_programs_settings_page($first_0:Int!,$first_3:Int!,$size_1:ProfilePictureSizes!,$size_2:ProfilePictureSizes!) {me {id,...Fb}} fragment F0 on Team {...} ...","variables":{"first_0":500,"first_3":25,"size_1":"small","size_2":"medium"}}'
```

## Description

GraphQL query to fetch user programs, team memberships, and policy subscriptions, exposing organizational ties.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| first_0 | Number of memberships | Yes |
| first_3 | Number of subscriptions | Yes |
| size_1 | Profile pic size for teams | Yes |
| size_2 | Profile pic size for policies | Yes |

## Examples

### Basic Usage

```bash
curl ... -d '{"variables":{"first_0":100,...}}'
```

## Expected Output

JSON response with user ID, username, memberships (total count, edges), and team policy subscriptions

## Related

- [[commands/graphql-sessions-query]]
- [[procedures/Execute-Sessions-Data-Retrieval]]
