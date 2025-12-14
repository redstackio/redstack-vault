---
id: cmd-graphql-introspect
data: >-
  curl -X POST https://www.on-running.com/en-in/graphql -H "Content-Type:
  application/json" -d '{"query": "query IntrospectionQuery { __schema
  {queryType { name },mutationType { name },subscriptionType { name },types
  {...FullType},directives {name,description,args
  {...InputValue},onOperation,onFragment,onField}}\nfragment FullType on __Type
  {kind,name,description,fields(includeDeprecated: true) {name,description,args
  {...InputValue},type {...TypeRef},isDeprecated,deprecationReason},inputFields
  {...InputValue},interfaces {...TypeRef},enumValues(includeDeprecated: true)
  {name,description,isDeprecated,deprecationReason},possibleTypes
  {...TypeRef}}\nfragment InputValue on __InputValue {name,description,type {
  ...TypeRef },defaultValue}\nfragment TypeRef on __Type {kind,name,ofType
  {kind,name,ofType {kind,name,ofType {kind,name}}}}"}'
tags:
  - graphql
  - introspection
  - recon
type: command
output: >-
  JSON response with __schema object containing types, queries, mutations,
  fields, and directives.
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.557Z'
verified: false
validated: true
submitted: true
---
# graphql-introspection-query

## Command

```bash
curl -X POST https://www.on-running.com/en-in/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query IntrospectionQuery { __schema {queryType { name },mutationType { name },subscriptionType { name },types {...FullType},directives {name,description,args {...InputValue},onOperation,onFragment,onField}}\nfragment FullType on __Type {kind,name,description,fields(includeDeprecated: true) {name,description,args {...InputValue},type {...TypeRef},isDeprecated,deprecationReason},inputFields {...InputValue},interfaces {...TypeRef},enumValues(includeDeprecated: true) {name,description,isDeprecated,deprecationReason},possibleTypes {...TypeRef}}\nfragment InputValue on __InputValue {name,description,type { ...TypeRef },defaultValue}\nfragment TypeRef on __Type {kind,name,ofType {kind,name,ofType {kind,name,ofType {kind,name}}}}"}'
```

## Description

This command sends a standard GraphQL introspection query to fetch the entire schema, revealing types, fields, queries, mutations, and directives for API reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method for GraphQL queries | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type for request body | Yes |
| `-d '{...}'` | JSON payload with the introspection query string | Yes |
| URL | Target GraphQL endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -d '{"query": "query IntrospectionQuery { __schema { ... } }"}'
```

### Advanced Usage

Add authentication header if required:

```bash
curl -X POST https://target.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token" \
  -d '{...query...}'
```

## Expected Output

A JSON object with data.__schema containing queryType, mutationType, types array (with FullType details like fields and args), and directives. Errors if introspection is disabled.

## Related

- [[commands/graphql-user-exists-enumeration]]
- [[procedures/Exploit-GraphQL-Introspection-for-Schema-Leakage]]
