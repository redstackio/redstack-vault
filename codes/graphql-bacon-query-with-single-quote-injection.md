---
type: code
language: graphql
verified: true
platforms:
  - Web
tags:
  - graphql
  - sql-injection
  - payload
validated: true
---

# graphql-bacon-query-with-single-quote-injection

## Code

```graphql
{ 
    bacon(id: "1'") { 
        id, 
        type, 
        price
    }
}
```

## Description

This GraphQL query payload injects a single quote into the 'id' parameter to test for SQL injection in the backend resolver. It attempts to fetch 'bacon' entity data while breaking the SQL string literal, potentially causing errors or allowing further exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `id: "1'"` | Injected ID with trailing single quote to escape SQL context | `1'` |

## Usage

POST this payload to the GraphQL endpoint using curl or a client like Postman. Use in penetration testing to identify injectable fields; chain with UNION SELECT for data exfiltration if successful.

## Detection

- Monitor GraphQL logs for queries with unescaped single quotes or SQL keywords.
- WAF rules matching ' OR 1=1' patterns or error responses containing SQL syntax issues.
- Database query logs showing concatenated user input.

## Related

- [[procedures/GraphQL-SQL-Injection-Exploitation]]
