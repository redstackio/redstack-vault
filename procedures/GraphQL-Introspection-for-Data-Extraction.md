---
id: 7902e15b-408c-4c57-bf78-f24228753816
name: GraphQL-Introspection-for-Data-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.793832+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Exploit]]'
  - '[[tags/Extract data]]'
  - '[[tags/GraphQL Injection]]'
commands:
  - '[[commands/curl-graphql-query]]'
platforms:
  - Web
tools: []
validated: true
---

# GraphQL-Introspection-for-Data-Extraction

## Summary

This procedure demonstrates how to exploit GraphQL endpoints vulnerable to introspection queries to extract the schema and sensitive data from a target application. By crafting queries that leverage GraphQL's built-in introspection capabilities, attackers can discover available types, fields, and then query for unauthorized data such as user information or internal resources, often bypassing standard access controls.

## Description

GraphQL APIs are designed for flexible querying, but many implementations fail to disable introspection, allowing attackers to query the schema metadata (__schema, __type) to map the entire data structure. Once the schema is understood, targeted queries can extract sensitive data like user profiles, emails, or database contents. This technique is particularly effective against public-facing web applications with insufficient input validation or query complexity limits. The attack assumes the endpoint accepts unauthenticated queries and does not enforce depth or cost limits. Successful execution can lead to full data exfiltration, enabling further attacks like identity theft or targeted phishing.

## Requirements

1. Network access to the GraphQL endpoint (e.g., https://target.com/graphql).
2. Basic knowledge of GraphQL syntax for crafting queries.
3. Tools like curl for sending HTTP requests; optionally, a proxy like Burp Suite for interception and modification.
4. The target GraphQL server must have introspection enabled (common in development or misconfigured production environments).

## Defense

- Disable introspection in production by setting query introspection to false in the GraphQL server configuration (e.g., Apollo Server's introspection: false).
- Implement query depth and complexity limits to prevent excessive data extraction.
- Use authentication and authorization checks on all queries, validating user permissions for requested fields.
- Monitor GraphQL logs for introspection queries (__schema, __type) and anomalous large data responses.
- Employ web application firewalls (WAFs) to detect and block suspicious GraphQL payloads.

## Objectives

1. Discover the GraphQL schema to identify extractable data types and fields.
2. Craft and execute queries to pull sensitive information without authentication.
3. Exfiltrate data for further analysis or malicious use, such as reconnaissance or fraud.

## Instructions

### Step 1: Identify the GraphQL Endpoint

**Context**: Confirm the presence of a GraphQL endpoint by sending a basic introspection query. This step verifies accessibility and introspection support.

**Command** ([[commands/curl-graphql-query]]):
```bash
curl -X POST https://target.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{__schema { types { name } } }"}'
```

> This command sends a minimal introspection query to list available types. If introspection is disabled, the server may return an error or empty response. Expected output includes a JSON array of type names, indicating success.

### Step 2: Extract Full Schema via Introspection

**Context**: Use a comprehensive introspection query to map all types, fields, and relationships. This reveals the data model, allowing identification of sensitive fields like 'users { id, email, password }'.

**Command** ([[commands/curl-graphql-query]]):
```bash
curl -X POST https://target.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{__schema { queryType { name } mutationType { name } types { name description fields { name type { name } } } } }"}'
```

> This expands on the basic query to fetch detailed schema information. Parse the JSON response to understand the query structure. If the endpoint uses GET, adapt to URL parameters, but POST is standard for complex queries.

### Step 3: Query for Sensitive Data

**Context**: Based on the schema, craft a targeted query to extract data. For example, if 'User' type with 'email' and 'role' fields is discovered, query all users to dump credentials or admin details.

**Command** ([[commands/curl-graphql-query]]):
```bash
curl -X POST https://target.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{users { id email role sensitiveField } }"}'
```

> Replace 'users', 'email', etc., with actual schema fields. This step accomplishes data exfiltration. Expected output is a JSON object with the requested data array. If pagination exists, iterate with 'first: 100' or similar arguments. Verify no rate limiting blocks repeated queries.
