---
tags:
  - graphql
  - information-disclosure
  - reconnaissance
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
id: eeb17cdf-a3d5-48d0-9b9f-878556ef0d65
created_at: '2025-12-14T17:26:00.193Z'
updated_at: '2025-12-14T17:26:00.193Z'
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
# Analyze vpn_suspended Status to Infer Private Programs

## Summary

This procedure analyzes the vpn_suspended field from a GraphQL response to infer whether an external HackerOne program hosts private programs, as a false value indicates VPN enablement, which is exclusive to private features and absent in sandboxed environments.

## Description

After querying the GraphQL API, the vpn_suspended field provides insight into program configuration. HackerOne's internal logic sets vpn_suspended to true by default but exposes it without checks during frontend testing. A false value reveals VPN usage, signaling private program hosting. This enables attackers to enumerate and target external programs with sensitive, private bug bounty setups. The procedure involves parsing the response and correlating the value across multiple queries for broader reconnaissance.

## Requirements

1. JSON response from a prior GraphQL team query
2. Tool like jq for parsing (optional, for automation)
3. Knowledge of HackerOne program types (external vs. sandboxed)

## Defense

Defensive measures and detection strategies:

- Remove or authorize sensitive fields like vpn_suspended in GraphQL resolvers
- Log and alert on queries targeting team objects with configuration fields
- Conduct regular API audits for over-exposed schema elements

## Objectives

1. Interpret vpn_suspended to detect private program indicators
2. Map external programs for further targeting
3. Highlight API misconfigurations for remediation

## Instructions

### Step 1: Parse and Evaluate Response

**Context**: Extract the vpn_suspended value from the GraphQL response and analyze it. False indicates potential private programs due to VPN enablement.

**Command** ([[commands/graphql-team-mini-profile-query]]):
```bash
curl -X POST 'https://hackerone.com/graphql' \
  -H 'Content-Type: application/json' \
  -d '{"query":"query Team_mini_profile($handle_0:String!,$size_1:ProfilePictureSizes!) {team(handle:$handle_0) {id,...F0}} fragment F0 on Team {id,name,about,_profile_picturePkPpF:profile_picture(size:$size_1),offers_swag,offers_bounties,vpn_enabled,vpn_suspended,base_bounty}","variables":{"handle_0":"example-handle","size_1":"small"}}' | jq '.data.team.vpn_suspended'
```

> If the output is false, the program likely hosts private features. Repeat for multiple handles to build a list of targets.

### Step 2: Correlate Across Programs

**Context**: Query additional handles and compare vpn_suspended values to identify patterns.

**Command** ([[commands/graphql-team-mini-profile-query]]):
```bash
# Repeat for different handles, e.g., handle_0: "another-handle"
```

> Aggregate results: false values flag private program hosts.

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
- reconnaissance
- inference
