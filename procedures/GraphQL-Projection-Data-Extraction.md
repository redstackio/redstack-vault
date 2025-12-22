---
id: 1e77f444-4e90-4509-a393-ab5ebbc5aa47
name: GraphQL-Projection-Data-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.849465+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation-of-Public-Facing-Application|T1190 - Exploitation
    of Public-Facing Application]]
sub_techniques: []
tags:
  - '[[tags/Exploit]]'
  - '[[tags/GraphQL-Injection]]'
  - '[[tags/Data-Extraction]]'
  - '[[tags/Projection-Manipulation]]'
commands:
  - '[[commands/graphql-curl-post-injection-query]]'
platforms:
  - Web
tools: []
validated: true
---

# GraphQL-Projection-Data-Extraction

## Summary

GraphQL Projection Data Extraction involves manipulating the projection fields in a GraphQL query to bypass access controls and extract sensitive data, such as personal identifiable information (PII) like social security numbers (SSNs) from related entities. This procedure targets vulnerable GraphQL endpoints that fail to properly validate or sanitize the 'options' parameter, allowing attackers to inject MongoDB-like projection syntax to include unauthorized fields in the response.

## Description

In GraphQL APIs, queries specify which fields to return via projections. If the backend uses a database like MongoDB and passes user-supplied 'options' directly to the query without sanitization, attackers can inject projection operators (e.g., {"field": 1} to include or 0 to exclude) to force the inclusion of sensitive nested data. This technique exploits the flexibility of GraphQL's schema introspection and query structure to perform unauthorized data retrieval. It is commonly used in reconnaissance or collection phases against web applications with exposed GraphQL endpoints, such as healthcare or user management systems. Success depends on the endpoint allowing introspection and lacking field-level authorization. Expected outcomes include JSON responses containing unauthorized PII, which can be exfiltrated for further attacks like identity theft or privilege escalation.

## Requirements

1. Network access to the target GraphQL endpoint (e.g., HTTP/HTTPS reachable).
2. Knowledge of the GraphQL schema, particularly entity relationships (e.g., doctors linked to patients) via introspection queries.
3. A tool like curl for sending HTTP POST requests with JSON payloads.
4. Basic understanding of GraphQL syntax and MongoDB projection operators.

## Defense

- Implement strict input validation and sanitization on all query parameters, especially 'options' fields, to reject or escape projection-like syntax (e.g., using libraries like graphql-middleware).
- Enforce field-level authorization using resolvers that check user permissions for each requested field, preventing over-fetching of nested data.
- Monitor GraphQL endpoints for anomalous queries, such as unusual projection patterns or high-volume data requests, using tools like GraphQL Armor or API gateways with rate limiting.
- Disable schema introspection in production and use query whitelisting to restrict allowed fields.

## Objectives

1. Identify and exploit a vulnerable GraphQL endpoint to bypass query restrictions.
2. Extract sensitive nested data, such as SSNs from related entities.
3. Collect PII for further analysis or lateral movement without triggering access controls.

## Instructions

### Step 1: Verify GraphQL Endpoint Accessibility

**Context**: Confirm the target endpoint supports GraphQL by sending an introspection query. This step ensures the API is live and reveals the schema for crafting the injection.

**Command** ([[commands/graphql-introspection-query]]):
```bash
curl -X POST -H "Content-Type: application/json" --data '{"query": "query { __schema { types { name } } }"}' http://target.example.com/graphql
```

> This command sends a basic introspection query to list available types (e.g., Doctor, Patient). If successful, it returns a JSON schema outline, confirming the endpoint's structure and potential for projection manipulation. Look for types with nested relationships like doctors.patients.

### Step 2: Craft Malicious Projection Payload

**Context**: Prepare the injection payload using MongoDB projection syntax in the 'options' field to force inclusion of sensitive nested data. This exploits unsanitized backend query construction.

**Code** ([[codes/graphql-projection-injection-payload]]):

> Use the provided JSON payload to specify inclusion of unauthorized fields like patients.ssn. The payload manipulates the query to return doctors' details plus their patients' SSNs, bypassing any default exclusions.

### Step 3: Execute Injection Query

**Context**: Send the crafted query to the endpoint via HTTP POST. This step performs the actual data extraction by injecting the projection to include restricted fields.

**Command** ([[commands/graphql-curl-post-injection-query]]):
```bash
curl -X POST -H "Content-Type: application/json" --data '{"query": "{doctors(options: \"{\\\"patients.ssn\\\" :1}\"){firstName lastName id patients{ssn}}}"}' $_TARGET_ENDPOINT
```

> Replace $_TARGET_ENDPOINT with the GraphQL URL (e.g., http://target.example.com/graphql). The command injects the projection {"patients.ssn": 1} to include SSNs in the response. If vulnerable, the backend passes this directly to the database query, returning sensitive data.

### Step 4: Analyze and Verify Extracted Data

**Context**: Parse the response to confirm successful extraction of unauthorized fields. This validates the bypass and prepares data for exfiltration.

> Review the JSON output for fields like patients.ssn. If present, the injection succeeded. Decision point: If no sensitive data appears, try variations like excluding other fields (e.g., {"patients": 0, "patients.ssn": 1}) or target different nested entities. Save output to a file for offline analysis: curl ... > extracted_data.json.
