---
tags:
  - graphql
  - information-disclosure
  - api
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-team-mini-profile-query]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b766dd7b-473a-4a54-866d-eee1d3d1736c
created_at: '2025-12-14T17:26:00.199Z'
updated_at: '2025-12-14T17:26:00.199Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
---
# Query GraphQL Team Profile for vpn_suspended

## Summary

This procedure sends a crafted GraphQL query to HackerOne's /graphql endpoint to retrieve the team profile of an external program, including the sensitive vpn_suspended field, which is exposed without proper authorization checks.

## Description

The vulnerability stems from the vpn_suspended field on the Team object being accessible via GraphQL without model-level authorization. This allows any unauthenticated user to query team details for known handles and observe the vpn_suspended value. In the context of HackerOne, this field indicates VPN status, which is enabled only for programs with private features. The procedure targets external programs and uses a specific query fragment to include the field alongside benign team attributes like name and profile picture.

## Requirements

1. Network access to https://hackerone.com/graphql
2. Known team handle (e.g., from public HackerOne directories)
3. HTTP client like curl for POST requests

## Defense

Defensive measures and detection strategies:

- Implement GraphQL schema authorization at the field level to restrict access to sensitive fields like vpn_suspended
- Monitor GraphQL queries for patterns including vpn_suspended or team handles
- Use rate limiting on /graphql endpoint to prevent enumeration

## Objectives

1. Retrieve unauthorized team information including vpn_suspended status
2. Confirm exposure of the field for inference of program features
3. Validate the lack of authentication checks in the API

## Instructions

### Step 1: Craft and Send GraphQL Query

**Context**: Prepare the GraphQL query to fetch the team mini-profile, ensuring the vpn_suspended field is included in the fragment. Replace the handle with a target external program's handle.

**Command** ([[commands/graphql-team-mini-profile-query]]):
```bash
curl -X POST 'https://hackerone.com/graphql' \
  -H 'Content-Type: application/json' \
  -d '{"query":"query Team_mini_profile($handle_0:String!,$size_1:ProfilePictureSizes!) {team(handle:$handle_0) {id,...F0}} fragment F0 on Team {id,name,about,_profile_picturePkPpF:profile_picture(size:$size_1),offers_swag,offers_bounties,vpn_enabled,vpn_suspended,base_bounty}","variables":{"handle_0":"example-handle","size_1":"small"}}'
```

> This command sends a POST request with the JSON payload containing the query and variables. The response will include the team's vpn_suspended value if the field is exposed.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-team-mini-profile-query]]

## Tools Used


## Tags

- graphql
- information-disclosure
- api
