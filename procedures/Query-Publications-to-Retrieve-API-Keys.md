---
tags:
  - api-key-exposure
  - information-disclosure
  - graphql
  - shopify
type: procedure
tools:
  - '[[tools/GraphiQL]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/graphql-query-publications-api-keys]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Cloud Instance Metadata API]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:53.068Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ef3088fa-c194-40c4-b188-ab1bdba6aab4
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
  - '[[Data from Information Repositories]]'
---
# Query-Publications-to-Retrieve-API-Keys

## Summary

This procedure queries publications in Shopify's GraphQL API to disclose app API keys without 'Products' permissions, enabling potential further abuse of exposed credentials.

## Description

The publications query exposes names, IDs, future publishing flags, and nested app API keys due to inadequate checks. This is a critical disclosure as API keys can grant app-level access. Targeted at QueryRoot, it affects stores using sales channels or apps.

## Requirements

1. GraphiQL access with 'Apps' permissions
2. Store with publications or sales channel apps installed
3. Ability to parse nested GraphQL fields

## Defense

Defensive measures and detection strategies:

- Mask or restrict API key exposure in GraphQL responses
- Require 'Products' scope validation for publication queries
- Rotate API keys and monitor for anomalous usage post-exposure

## Objectives

1. Extract app API keys from publications
2. Confirm permission bypass for sensitive credential access
3. Enable credential-based follow-on attacks

## Instructions

### Step 1: Build Publications Query

**Context**: Include app nesting to reach apiKey field.

**Instructions**: Set first:100 for broad coverage.

### Step 2: Run Query

**Context**: Execute to retrieve keys, validating exposure.

**Command** ([[commands/graphql-query-publications-api-keys]]):

```graphql
query {
  publications(first: 100) {
    edges {
      node {
        name
        id
        supportsFuturePublishing
        app {
          apiKey
        }
      }
    }
  }
}
```

> Expected output: Array of publications with apiKey strings visible, indicating successful leak.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Cloud Instance Metadata API]] Unsecured Credentials: Cloud Instance Metadata API (adapted for API keys)
- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-query-publications-api-keys]]

## Tools Used

- [[tools/GraphiQL]]

## Tags

- [[api-key-exposure]]
- [[graphql]]
- [[publications]]
