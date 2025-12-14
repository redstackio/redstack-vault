---
data: >-
  curl -X POST 'https://hackerone.com/graphql?' -H 'Content-Type:
  application/json' -H 'X-Auth-Token: [TOKEN]' -H 'Cookie: [COOKIES]' -d
  '{"query":"query Sessions_page($first_0:Int!) {me {id,...F1}} fragment F0 on
  UserSession {id} fragment F1 on User {_sessionssvoGn:sessions(first:$first_0)
  {total_count,pageInfo {hasNextPage,hasPreviousPage},edges {node
  {id,ip_address,user_agent,abbreviated_user_agent,country
  {name,flag,id},session_last_used_at,deactivated_at,device_type,current,...F0},cursor}},id}","variables":{"first_0":10}}'
tags:
  - graphql
  - query
  - sessions
type: command
output: >-
  JSON response with user ID, session details including IP addresses, user
  agents, countries, last used times, and pagination info
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.389Z'
id: 8dcaa560-9eaa-4bb1-9599-d2519058052b
verified: false
validated: true
submitted: true
---
# graphql-sessions-query

## Command

```bash
curl -X POST 'https://hackerone.com/graphql?' -H 'Content-Type: application/json' -H 'X-Auth-Token: [TOKEN]' -H 'Cookie: [COOKIES]' -d '{"query":"query Sessions_page($first_0:Int!) {me {id,...F1}} fragment F0 on UserSession {id} fragment F1 on User {_sessionssvoGn:sessions(first:$first_0) {total_count,pageInfo {hasNextPage,hasPreviousPage},edges {node {id,ip_address,user_agent,abbreviated_user_agent,country {name,flag,id},session_last_used_at,deactivated_at,device_type,current,...F0},cursor}},id}","variables":{"first_0":10}}'
```

## Description

Sends a GraphQL query to retrieve session history from a user's account, useful for exfiltrating login details in access bypass scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| first_0 | Number of sessions to fetch | Yes |
| X-Auth-Token | Authentication token | Yes |
| Cookie | Session cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://hackerone.com/graphql?' -H 'Content-Type: application/json' -H 'X-Auth-Token: abc123' -H 'Cookie: session=def456' -d '{"query":"...","variables":{"first_0":10}}'
```

### Advanced Usage

Increase fetch limit:

```bash
... -d '{"variables":{"first_0":50}}'
```

## Expected Output

JSON response with user ID, session details including IP addresses, user agents, countries, last used times, and pagination info

## Related

- [[commands/graphql-user-programs-query]]
- [[procedures/Execute-Sessions-Data-Retrieval]]
