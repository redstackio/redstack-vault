---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.763308+00:00'
updated_at: '2023-04-10T20:22:23.218748+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/Active Scanning|T1595.002 - Vulnerability Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Exploit]]'
  - '[[tags/GraphQL-Injection]]'
  - '[[tags/Identify-Injection-Point]]'
commands:
  - '[[commands/graphql-empty-query]]'
  - '[[commands/graphql-schema-introspection-query]]'
  - '[[commands/graphql-invalid-query-test]]'
platforms:
  - Web
tools: []
validated: true
---

# Identify-GraphQL-Injection-Points

## Summary

This procedure outlines how to identify potential GraphQL injection points in an application's API by sending crafted queries to common endpoints like /graphql and /graphiql. By testing with empty, schema introspection, and invalid queries, you can detect if the API exposes sensitive schema information, returns detailed error messages, or processes malformed inputs insecurely, indicating vulnerability to injection attacks.

## Description

GraphQL APIs can be vulnerable to injection attacks if they do not properly validate or sanitize inputs, allowing attackers to manipulate queries to extract schema details, bypass authentication, or cause denial of service. This procedure focuses on reconnaissance to identify such points by leveraging GraphQL's introspection capabilities and error handling behaviors. It targets public-facing GraphQL endpoints and assumes HTTP access. Successful identification helps in further exploitation or securing the API. The technique involves sending GET or POST requests with query parameters or bodies to probe responses for leakage of internal data structures or error details that reveal injection feasibility.

## Requirements

1. Network access to the target GraphQL API endpoint (e.g., https://target.com/graphql).
2. Basic knowledge of GraphQL syntax and HTTP request methods (GET/POST).
3. Tools like curl or a browser for sending requests; optionally, a proxy like Burp Suite for interception.
4. Target URL and any known authentication tokens if the endpoint requires them.

## Defense

- Implement strict input validation and sanitization for all GraphQL queries to prevent payload injection.
- Disable introspection queries in production environments to hide schema details.
- Use query whitelisting or depth limiting to restrict complex or malformed queries.
- Monitor API logs for anomalous query patterns, such as introspection attempts or invalid syntax, and implement rate limiting.
- Enable detailed error logging without exposing sensitive information in responses.

## Objectives

1. Probe GraphQL endpoints to confirm their presence and accessibility.
2. Test for schema introspection to reveal API structure and potential injection vectors.
3. Analyze error responses from invalid queries to detect verbose error handling that aids attackers.
4. Determine overall vulnerability to GraphQL injection based on response behaviors.

## Instructions

### Step 1: Probe GraphQL Endpoint with Empty Query

**Context**: Send an empty query to the /graphql endpoint to verify if it processes requests and returns a standard error or empty response, indicating the endpoint is active and potentially vulnerable to injection if it doesn't reject malformed inputs outright.

**Command** ([[commands/graphql-empty-query]]):
```bash
curl -X GET "$_TARGET_URL/graphql?query={}" -H "Content-Type: application/json"
```

> This command appends an empty query parameter to the URL. Replace $_TARGET_URL with the base API URL (e.g., https://example.com). The expected response should be a JSON error indicating invalid syntax, but if it processes without rejection, it may confirm basic injection feasibility. Look for any schema hints in errors.

### Step 2: Perform Schema Introspection Query

**Context**: Attempt to introspect the GraphQL schema to extract type information, which can reveal database structures or sensitive fields if introspection is enabled, a common injection entry point.

**Command** ([[commands/graphql-schema-introspection-query]]):
```bash
curl -X GET "$_TARGET_URL/graphql?query={__schema{types{name}}}" -H "Content-Type: application/json"
```

> This sends a schema introspection query. A successful response will list object types, confirming introspection is allowed and exposing potential injection targets. If blocked, the API may still be vulnerable via other means; note any error details for further probing.

### Step 3: Test with Invalid Query for Error Analysis

**Context**: Submit an intentionally invalid query to observe error messages. Verbose errors can leak stack traces, field names, or implementation details that facilitate crafting effective injection payloads.

**Command** ([[commands/graphql-invalid-query-test]]):
```bash
curl -X GET "$_TARGET_URL/graphql?query={thisdefinitelydoesnotexist}" -H "Content-Type: application/json"
```

> This tests error handling with a non-existent field. Successful output includes detailed errors (e.g., 'Unknown field') that might reveal internal info. If errors are sanitized, the API is better protected; otherwise, use this to refine injection attempts.

### Step 4: Test GraphiQL Interface if Accessible

**Context**: If a /graphiql endpoint exists (often for development), probe it similarly to identify if it's exposed in production, providing an interactive injection testing ground.

**Instructions**: Repeat Steps 1-3 but append to /graphiql instead of /graphql. For example, use the empty query command with "$_TARGET_URL/graphiql?query={}". Check browser access or curl for responses. Success is indicated by any processing of the query, as GraphiQL should not be public-facing.

### Step 5: Analyze Responses for Vulnerability Indicators

**Context**: Review all responses for signs of injection vulnerability, such as schema exposure, detailed errors, or unexpected data returns.

**Instructions**: Compare outputs: Introspection success means high risk; verbose errors suggest injection potential. If no leaks, the API may use protections like persisted queries or validators. Document findings for escalation in an attack chain.
