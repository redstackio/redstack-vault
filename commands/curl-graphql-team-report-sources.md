---
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -d '{"query":"query {team(handle:\"$HANDLE\"){_id,report_sources}}"}'
tags:
  - graphql
  - api
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Web
  - Linux
  - macOS
  - Windows
id: d98b3ecf-b32b-4fc5-b20e-f4ff2d8e1284
created_at: '2025-12-14T17:30:47.341Z'
updated_at: '2025-12-14T17:30:47.341Z'
verified: false
validated: true
submitted: true
---
# curl-graphql-team-report-sources

## Command

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query":"query {team(handle:\"$HANDLE\"){_id,report_sources}}"}'
```

## Description

This command sends a GraphQL query via curl to HackerOne's /graphql endpoint, retrieving the _id and report_sources fields for a specified team handle. It exploits the lack of authorization to disclose program privacy status: empty array for non-private, ['HackerOne Platform'] for private. Use it during reconnaissance to identify private bug bounty programs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$HANDLE` | The team handle (e.g., 'example-team') to query; replace the placeholder in the JSON payload | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON data | Yes |
| `-d` | The data payload containing the GraphQL query | Yes |

## Examples

### Basic Usage

Query a non-private team:

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query":"query {team(handle:\"example-nonprivate\"){_id,report_sources}}"}'
```

### Advanced Usage

Query a private team and pipe to jq for parsing:

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query":"query {team(handle:\"example-private\"){_id,report_sources}}"}' | jq '.data.team.report_sources'
```

## Expected Output

For non-private teams: `{"data":{"team":{"_id":"team-id","report_sources":[]}}}`

For private teams: `{"data":{"team":{"_id":"team-id","report_sources":["HackerOne Platform"]}}}`

Successful execution returns HTTP 200 with the JSON structure; errors may include GraphQL syntax issues or invalid handles.

## Related

- [[procedures/Detect-Private-HackerOne-Programs-via-GraphQL]]
