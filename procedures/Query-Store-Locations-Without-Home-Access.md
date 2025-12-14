---
tags:
  - information-disclosure
  - graphql
  - shopify
type: procedure
tools:
  - '[[tools/GraphiQL]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:53.074Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9f8e68d4-65e1-46e4-8254-7e8b346409da
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Data from Information Repositories]]'
---
# Query-Store-Locations-Without-Home-Access

## Summary

This procedure exploits the lack of permission checks on the 'locations' query in Shopify's GraphQL Admin API, allowing retrieval of store addresses and details with only 'Apps' permissions.

## Description

Shopify documentation requires 'home' or location-specific scopes for accessing store locations, but the API fails to enforce this, leading to disclosure of business-sensitive addresses to unauthorized users. This occurs via the QueryRoot endpoint and can reveal physical store locations, impacting privacy and operational security. The procedure assumes prior API access via GraphiQL and focuses on executing the vulnerable query.

## Requirements

1. Active GraphQL Admin API session with 'Apps' permissions
2. GraphiQL app installed and accessible
3. Target Shopify store with multiple locations configured

## Defense

Defensive measures and detection strategies:

- Implement runtime permission validation for all GraphQL fields
- Log and alert on location queries from non-home scoped sessions
- Restrict GraphiQL app access to high-privilege users only

## Objectives

1. Retrieve unauthorized store location data
2. Confirm bypass of 'home' scope requirement
3. Expose business addresses for potential reconnaissance

## Instructions

### Step 1: Prepare Location Query

**Context**: The 'locations' query traverses edges to access node details like addresses.

**Instructions**: In GraphiQL, construct a query targeting the locations field with a limit to avoid overload.

### Step 2: Execute Query

**Context**: Run the query to fetch location data, expecting success despite missing permissions.

**Command** ([[Custom GraphQL Query]]):

```graphql
query {
  locations(first: 10) {
    edges {
      node {
        id
        name
        address {
          address1
          address2
          city
          province
          country
          zip
        }
      }
    }
  }
}
```

> This query retrieves up to 10 locations with full address details. Expected output is a JSON response with location nodes populated, no 'access denied' errors.

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

- Custom GraphQL query for locations

## Tools Used

- [[tools/GraphiQL]]

## Tags

- [[information-disclosure]]
- [[graphql]]
- [[locations]]
