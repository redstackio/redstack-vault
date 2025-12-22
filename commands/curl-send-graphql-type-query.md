---
type: command
executor: bash
data: >-
  curl -X POST -H "Content-Type: application/json" --data '{"query": "{__type
  (name: \"$_TYPE_NAME\") {name fields{name type{name kind ofType{name
  kind}}}}"}' $_ENDPOINT
output: null
created_at: '2023-04-06T03:55:58.870942+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows (with curl)
tags:
  - graphql
  - introspection
  - curl
  - web
verified: true
validated: true
---

# curl-send-graphql-type-query

## Command

```bash
curl -X POST -H "Content-Type: application/json" --data '{"query": "{__type (name: \"$_TYPE_NAME\") {name fields{name type{name kind ofType{name kind}}}}"}' $_ENDPOINT
```

## Description

This command sends a GraphQL introspection query via curl to enumerate the fields and types of a specified GraphQL object type. It is used to probe the schema structure of a web API during reconnaissance, helping identify data models and potential vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ENDPOINT | The full URL of the GraphQL endpoint (e.g., https://target.com/graphql) | Yes |
| $_TYPE_NAME | The name of the GraphQL type to introspect (e.g., User, Query) | Yes |
| -X POST | Specifies HTTP POST method | Built-in |
| -H "Content-Type: application/json" | Sets the request header for JSON payload | Built-in |
| --data | The JSON payload containing the query | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" --data '{"query": "{__type (name: \"User\") {name fields{name type{name kind ofType{name kind}}}}"}' https://target.com/graphql
```

### Advanced Usage (with Authentication)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $_TOKEN" --data '{"query": "{__type (name: \"User\") {name fields{name type{name kind ofType{name kind}}}}"}' https://target.com/graphql
```

## Expected Output

Successful execution returns a JSON response with the type's structure:

```json
{
  "data": {
    "__type": {
      "name": "User",
      "fields": [
        {
          "name": "id",
          "type": {
            "name": "ID",
            "kind": "SCALAR"
          }
        },
        {
          "name": "email",
          "type": {
            "name": "String",
            "kind": "SCALAR"
          }
        }
      ]
    }
  }
}
```

If introspection is disabled, expect an error like {"errors": [{"message": "Introspection has been disabled"}]}.

## Related

- [[procedures/GraphQL-Type-Enumeration]]
- [[tools/cURL]] (base tool)
