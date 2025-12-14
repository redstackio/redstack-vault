---
id: proc-graphql-identify-001
tags:
  - graphql
  - recon
  - api-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/graphql-introspect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:53.110Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-GraphQL-Endpoint-for-Profile-Management

## Summary

This procedure involves exploring the GraphQL API of a web application to identify endpoints and operations related to user profile image management, setting the stage for potential vulnerabilities like IDOR.

## Description

In the context of the LINE entry service, an authenticated user interacts with profile features to observe network traffic and perform GraphQL introspection. This reveals schema details for mutations handling profile images, such as uploading or deleting thumbnails. The target environment is a web-based GraphQL API at https://entry.line.me/graphql. Prerequisites include a valid login session. Expected outcomes include a list of relevant GraphQL types and mutations, enabling further exploitation.

## Requirements

1. Authenticated session to the target service (e.g., LINE entry account)
2. Access to browser developer tools or HTTP client like curl
3. Basic knowledge of GraphQL queries

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on GraphQL introspection queries
- Use schema stitching or partial introspection to hide sensitive operations
- Monitor for unusual API exploration patterns in logs

## Objectives

1. Discover GraphQL operations for profile image management
2. Identify parameter structures like image IDs
3. Prepare for targeted exploitation without alerting defenses

## Instructions

### Step 1: Inspect Network Traffic

**Context**: Log in to the application and interact with profile image features to capture API calls.

**Command** ([[commands/graphql-introspect]]):
```bash
curl -X POST https://entry.line.me/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query { __schema { types { name fields { name } } } }"}'
```

> This introspection query returns the GraphQL schema, highlighting types like UserProfile and fields such as profileImageId. Expected output: JSON with schema structure; look for delete or remove mutations.

### Step 2: Test Profile Operations

**Context**: Send a test query to confirm image management endpoints.

**Command** ([[commands/graphql-introspect]]):
```bash
curl -X POST https://entry.line.me/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query { me { profileImage { id } } }"}'
```

> Retrieves your own profile image ID for reference. Expected output: Your image details, confirming the endpoint's functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-introspect]]

## Tools Used


## Tags

- [[graphql]]
- [[recon]]
- [[api-discovery]]
