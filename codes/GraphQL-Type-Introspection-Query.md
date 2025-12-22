---
type: code
language: javascript
verified: true
created_at: '2023-04-06T03:55:58.870876+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - graphql
  - introspection
  - query
validated: true
---

# GraphQL-Type-Introspection-Query

## Code

```javascript
{__type (name: "User") {name fields{name type{name kind ofType{name kind}}}}}
```

## Description

This GraphQL query snippet performs introspection on a specific type (e.g., User) to retrieve its name, fields, and detailed type information. It exposes the schema structure, including whether types are scalars, objects, lists, or non-null, which is useful for mapping API capabilities and finding exploitable fields.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| name | The GraphQL type to query (replace "User" with target type like Query or Mutation) | "User" |

## Usage

Embed this query in a JSON payload for a POST request to a GraphQL endpoint, e.g., {"query": "...query here..."}. Use in tools like curl, Postman, or GraphQL clients during reconnaissance to enumerate schema without authentication if allowed. Chain with full __schema queries for complete API mapping.

## Detection

- Web application logs showing queries with __type or nested type fields.
- WAF rules blocking introspection keywords like __type, __schema.
- Anomalous API traffic patterns with high query complexity or meta-field access.

## Related

- [[procedures/GraphQL-Type-Enumeration]]
- [[commands/curl-send-graphql-type-query]]
