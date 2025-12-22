---
type: procedure
description: >-
  Enumerate GraphQL schema types and fields using introspection queries to
  discover application structure.
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.876432+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Active-Scanning|T1595 - Active Scanning]]'
  - >-
    [[techniques/Gather-Victim-Host-Information|T1592 - Gather Victim Host
    Information]]
sub_techniques: []
tags:
  - graphql
  - introspection
  - enumeration
  - discovery
  - web
  - injection
commands:
  - '[[commands/curl-send-graphql-type-query]]'
platforms:
  - Web
tools: []
validated: true
---

# GraphQL-Type-Enumeration

## Summary

This procedure uses GraphQL introspection queries to enumerate the structure of specific types in a GraphQL API, revealing fields, types, and nested structures. This technique exploits misconfigured endpoints that allow schema introspection, aiding attackers in mapping the API for further reconnaissance or identifying injection points and sensitive data exposures.

## Description

GraphQL APIs provide introspection capabilities through meta-fields like __type and __schema, allowing clients to query the API's own structure. In vulnerable applications where introspection is not disabled, attackers can send targeted queries to retrieve details about object types (e.g., User, Query), including field names, types (scalar, object, list), and kind (INPUT_OBJECT, ENUM). This procedure focuses on querying a single type's definition, which can be chained to enumerate the full schema. It is typically used during the reconnaissance phase against web applications with exposed GraphQL endpoints, such as /graphql, to understand data models and potential attack vectors like field injections or unauthorized queries.

## Requirements

1. Network access to the target GraphQL endpoint (e.g., HTTP/HTTPS access to https://target.com/graphql).
2. A tool capable of sending HTTP POST requests with JSON payloads, such as curl (available on most Unix-like systems).
3. Basic knowledge of GraphQL query syntax and the target type name (e.g., "User" obtained from prior enumeration or error messages).
4. Optional: Proxy tools like Burp Suite for intercepting and modifying requests in a controlled environment.

## Defense

- Disable introspection in production by configuring the GraphQL server (e.g., set introspection: false in Apollo Server or use middleware to block __type/__schema queries).
- Implement authentication and authorization on the GraphQL endpoint to restrict access to authenticated users.
- Apply rate limiting and monitor query logs for patterns involving __type, __schema, or nested type queries.
- Use schema stitching or partial schemas to hide sensitive types and fields from introspection.

## Objectives

1. Retrieve detailed definitions of specific GraphQL types, including fields and their type kinds.
2. Map the API's data structure to identify potential vulnerabilities like over-fetching or injection points.
3. Gather intelligence on the application's backend models for targeted follow-up attacks, such as GraphQL injection or batching attacks.

## Instructions

### Step 1: Prepare the Introspection Query

**Context**: Craft the GraphQL query to target a specific type. This step uses a predefined query snippet that requests the type's name, fields, and type details. Replace the type name (e.g., "User") with the target type based on prior knowledge or error leaks.

**Code** ([[codes/GraphQL-Type-Introspection-Query]]):

```javascript
{__type (name: "User") {name fields{name type{name kind ofType{name kind}}}}}
```

> This query leverages GraphQL's built-in __type field to introspect the specified type. The nested fields retrieve field names and type information, including handling for lists (LIST kind) or non-null types (NON_NULL kind) via ofType. Expected result is a JSON object under "data" with the type structure if successful; errors indicate disabled introspection or invalid type name.

### Step 2: Send the Query to the Endpoint

**Context**: Transmit the prepared query as a JSON payload via HTTP POST to the GraphQL endpoint. This step verifies access and retrieves the schema details. Use placeholders for the endpoint URL and type name to customize.

**Command** ([[commands/curl-send-graphql-type-query]]):

```bash
curl -X POST -H "Content-Type: application/json" --data '{"query": "{__type (name: \"$_TYPE_NAME\") {name fields{name type{name kind ofType{name kind}}}}"}' $_ENDPOINT
```

> Execute this command to send the introspection query. If the endpoint requires authentication, add headers like -H "Authorization: Bearer $_TOKEN". Success is indicated by a 200 OK response with JSON data; failures may return 400 Bad Request or empty data if introspection is blocked. Parse the output to review fields like id: Int or email: String for insights into the data model.
