---
id: 1e8dfbbe-bca8-4c0a-bd82-d31d87798853
name: GraphQL-Edge-Node-Data-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.821292+00:00'
updated_at: '2023-04-10T20:22:23.622904+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Exploit]]'
  - '[[tags/GraphQL-Injection]]'
  - '[[tags/Data-Extraction]]'
commands:
  - '[[commands/curl-send-graphql-query]]'
platforms:
  - Web
tools: []
validated: true
---

# GraphQL-Edge-Node-Data-Extraction

## Summary

This procedure exploits vulnerabilities in GraphQL APIs, such as insufficient authorization or injection flaws, to extract sensitive data using the edges and nodes structure inherent to GraphQL queries. By crafting targeted queries, an attacker can traverse the data graph to retrieve information like user details, team data, or other connected entities that may not be intended for public access, enabling data exfiltration from databases or linked services.

## Description

GraphQL APIs allow flexible querying of data, but misconfigurations like missing authentication checks on resolvers or lack of query depth limits can expose entire schemas. This technique involves injecting or modifying the 'query' parameter to leverage edges (connections between objects) and nodes (individual data objects) for traversal and extraction. For example, querying a 'teams' object might reveal internal IDs, descriptions, and states that lead to further pivoting. This is particularly effective against APIs without rate limiting or introspection disabled, and it maps to exploiting public-facing web applications for unauthorized data collection. The target environment is typically a web application with a GraphQL endpoint (e.g., /graphql), accessible over HTTP/HTTPS.

## Requirements

1. Network access to the target GraphQL endpoint (e.g., unauthenticated or low-privilege access).
2. Tools like curl for sending HTTP requests or a proxy like Burp Suite for interception and modification.
3. Knowledge of the API schema, obtainable via introspection queries if enabled.
4. A wordlist or understanding of potential object types (e.g., 'teams', 'users') from reconnaissance.

## Defense

- Implement proper authentication and authorization on all GraphQL resolvers to restrict data access based on user roles.
- Disable schema introspection in production and limit query complexity/depth to prevent broad traversals.
- Use web application firewalls (WAFs) to detect anomalous GraphQL queries, such as those with nested edges/nodes or injection patterns.
- Monitor API logs for unusual query patterns, high data volumes, or access to sensitive fields.

## Objectives

1. Identify and confirm a vulnerable GraphQL endpoint capable of processing custom queries.
2. Craft and execute queries using edges and nodes to extract sensitive data structures.
3. Validate the extracted data for usefulness in further attacks, such as identifying internal resources or credentials.
4. Achieve unauthorized data collection without triggering alerts.

## Instructions

### Step 1: Identify the GraphQL Endpoint

**Context**: Begin by confirming the presence of a GraphQL API, often at paths like /graphql or /api/graphql. Use reconnaissance to probe for it, ensuring the endpoint accepts POST requests with JSON payloads.

Send an introspection query to explore the schema if allowed.

**Command** ([[commands/curl-send-graphql-query]]):
```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "query { __schema { types { name } } }"}' $_TARGET_URL
```

> This command sends a basic introspection query to list available types. If introspection is disabled, proceed with guessed object names like 'teams' or 'users' based on common patterns.

### Step 2: Explore Schema and Identify Traversable Objects

**Context**: Once the endpoint is confirmed, query for specific objects to understand the data graph. Look for fields like 'edges' and 'node' which indicate paginated or connected data sets.

Use the command to test a simple query on a suspected object.

**Command** ([[commands/curl-send-graphql-query]]):
```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "query { teams { totalCount } }"}' $_TARGET_URL
```

> Expected response includes total count if the object exists. If errors occur, iterate on object names. This step verifies traversability before deeper extraction.

### Step 3: Extract Data Using Edges and Nodes

**Context**: Craft a query that uses 'edges' to iterate over connections and 'node' to access object details. This allows pulling sensitive fields like IDs, handles, or states that could reveal internal structures.

Embed the [[codes/graphql-teams-edge-node-query]] payload in the request.

**Command** ([[commands/curl-send-graphql-query]]):
```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "query { teams { total_count, edges { node { id, _id, about, handle, state } } } }"}' $_TARGET_URL
```

> This executes the extraction query. If successful, it returns an array of team objects via edges/node. Pipe output to jq for parsing: | jq '.data.teams.edges[].node' to isolate data. If the query fails due to auth, attempt with stolen tokens or bypasses.

### Step 4: Validate and Iterate Extraction

**Context**: Review the output for sensitive info and chain queries if cursors or pagination exist in edges. For example, use 'after' parameter in edges for deeper traversal.

Repeat the command with modifications based on initial results.

**Command** ([[commands/curl-send-graphql-query]]):
```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "query { teams(first: 10, after: \"$_CURSOR\") { edges { node { id, about } } } }"}' $_TARGET_URL
```

> Success is indicated by new data batches. If no more edges, the extraction is complete. Save outputs to files for analysis, e.g., > extracted_teams.json.
